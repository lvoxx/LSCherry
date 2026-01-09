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


class ShaderNodeAdd_Outline(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Outline'
    bl_label = "Add Outline"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Outline Color"].default_value = (0.012772791087627411, 0.012772791087627411, 0.012772791087627411, 1.0)
        self.inputs["Alpha"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Outline'

        # Create output sockets
        nt.interface.new_socket('Outline', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Outline Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.012772791087627411, 0.012772791087627411, 0.012772791087627411, 1.0)
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (8.618843078613281, 0.0)
        Emission.name = "Emission"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (220.51385498046875, 64.11897277832031)
        Mix_Shader.name = "Mix Shader"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (8.618843078613281, 84.397216796875)
        Transparent_BSDF.name = "Transparent BSDF"

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (8.618843078613281, 151.6417694091797)
        Geometry.name = "Geometry"

        Mix_Shader_001 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_001.location = (571.7650146484375, 64.11897277832031)
        Mix_Shader_001.name = "Mix Shader.001"

        Transparent_BSDF_001 = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF_001.location = (220.51385498046875, -81.97634887695312)
        Transparent_BSDF_001.name = "Transparent BSDF.001"

        Light_Path = nt.nodes.new('ShaderNodeLightPath')
        Light_Path.location = (220.51385498046875, 138.98599243164062)
        Light_Path.name = "Light Path"

        Mix_Shader_002 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_002.location = (752.0, 64.11897277832031)
        Mix_Shader_002.name = "Mix Shader.002"

        Transparent_BSDF_002 = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF_002.location = (564.6485595703125, -81.97634887695312)
        Transparent_BSDF_002.name = "Transparent BSDF.002"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Emission.inputs[0])
        nt.links.new(Mix_Shader_002.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Geometry.outputs[6], Mix_Shader.inputs[0])
        nt.links.new(Transparent_BSDF_001.outputs[0], Mix_Shader_001.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], Mix_Shader_001.inputs[2])
        nt.links.new(Light_Path.outputs[0], Mix_Shader_001.inputs[0])
        nt.links.new(Emission.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Transparent_BSDF_002.outputs[0], Mix_Shader_002.inputs[1])
        nt.links.new(Mix_Shader_001.outputs[0], Mix_Shader_002.inputs[2])
        nt.links.new(GroupInput.outputs[1], Mix_Shader_002.inputs[0])

        # Set default values
        Emission.inputs[1].default_value = 1.0
        Emission.inputs[2].default_value = 0.0
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0
        Transparent_BSDF_001.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF_001.inputs[1].default_value = 0.0
        Transparent_BSDF_002.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF_002.inputs[1].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
