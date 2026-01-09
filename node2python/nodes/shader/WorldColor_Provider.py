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


class ShaderNodeWorldColor_Provider(ShaderNode):
    bl_idname = 'ShaderNodeWorldColor_Provider'
    bl_label = "WorldColor Provider"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Saturation"].default_value = 1.2000000476837158
        self.inputs["Value"].default_value = 1.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'WorldColor Provider'

        # Create output sockets
        nt.interface.new_socket('WorldColor', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Saturation', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.2000000476837158
        input_socket = nt.interface.new_socket('Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.5

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

        Diffuse_BSDF = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF.location = (84.53228759765625, 63.373985290527344)
        Diffuse_BSDF.name = "Diffuse BSDF"

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (284.64068603515625, 54.18236541748047)
        Shader_to_RGB.name = "Shader to RGB"

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (478.91204833984375, 176.95895385742188)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        # Create internal links
        nt.links.new(Diffuse_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Hue_Saturation_Value.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Shader_to_RGB.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(GroupInput.outputs[0], Hue_Saturation_Value.inputs[1])
        nt.links.new(GroupInput.outputs[1], Hue_Saturation_Value.inputs[2])

        # Set default values
        Diffuse_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Diffuse_BSDF.inputs[1].default_value = 0.0
        Diffuse_BSDF.inputs[2].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF.inputs[3].default_value = 0.0
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[3].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
