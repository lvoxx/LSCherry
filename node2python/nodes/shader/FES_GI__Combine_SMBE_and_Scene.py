import bpy
import sys
from pathlib import Path

# Import utils (handle both relative and absolute imports)
try:
    from ..utils import ShaderNode
except ImportError:
    # Fallback for direct execution
    import importlib.util
    utils_path = Path(__file__).parent.parent / 'utils.py'
    spec = importlib.util.spec_from_file_location('utils', utils_path)
    utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utils)
    ShaderNode = utils.ShaderNode


class ShaderNodeFES_GI__Combine_SMBE_and_Scene(ShaderNode):
    bl_idname = 'ShaderNodeFES_GI__Combine_SMBE_and_Scene'
    bl_label = "FES_GI: Combine SMBE and Scene"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lightmap"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        self.inputs["Emission Strength"].default_value = 85.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'FES_GI: Combine SMBE and Scene'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        nt.interface.new_socket('SMBE', in_out='INPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('Scene', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Lightmap', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 85.0

        # Build node tree
        self.rebuildNodetree(None)

    def rebuildNodetree(self, context):
        if context is not None:
            if self.node_tree.users > 1:
                self.duplicate()

        nt = self.node_tree

        # Clear existing nodes
        for node in list(nt.nodes):
            nt.nodes.remove(node)

        # Create group input/output
        GroupInput = nt.nodes.new('NodeGroupInput')
        GroupInput.location = (-400, 0)
        GroupOutput = nt.nodes.new('NodeGroupOutput')
        GroupOutput.location = (400, 0)

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (-232.69863891601562, -94.54873657226562)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (84.0018310546875, 16.318572998046875)
        Emission.name = "Emission"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (-223.17481994628906, 85.97417449951172)
        Mix_Shader.name = "Mix Shader"

        Add_Shader = nt.nodes.new('ShaderNodeAddShader')
        Add_Shader.location = (258.75457763671875, 139.43801879882812)
        Add_Shader.name = "Add Shader"

        # Create internal links
        nt.links.new(GroupInput.outputs[2], Hue_Saturation_Value.inputs[4])
        nt.links.new(GroupInput.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_Shader.inputs[2])
        nt.links.new(Hue_Saturation_Value.outputs[0], Emission.inputs[0])
        nt.links.new(GroupInput.outputs[3], Emission.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], Add_Shader.inputs[0])
        nt.links.new(Emission.outputs[0], Add_Shader.inputs[1])
        nt.links.new(Add_Shader.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Hue_Saturation_Value.inputs[0].default_value = 0.5199999809265137
        Hue_Saturation_Value.inputs[1].default_value = 1.0
        Hue_Saturation_Value.inputs[2].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Emission.inputs[2].default_value = 0.0
        Mix_Shader.inputs[0].default_value = 0.15800000727176666

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
