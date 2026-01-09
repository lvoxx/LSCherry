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


class ShaderNodeBuild_Stacked_Toon(ShaderNode):
    bl_idname = 'ShaderNodeBuild_Stacked_Toon'
    bl_label = "Build Stacked Toon"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Stack"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Alpha"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Build Stacked Toon'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('To AgX', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Stack', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
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

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-141.0716552734375, -43.58099365234375)
        Group_013.name = "Group.013"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (-141.0716552734375, 43.5809326171875)
        Transparent_BSDF.name = "Transparent BSDF"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (141.0716552734375, -21.1348876953125)
        Mix_Shader.name = "Mix Shader"

        Mix_Shader_001 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_001.location = (141.0716552734375, -143.97640991210938)
        Mix_Shader_001.name = "Mix Shader.001"

        # Create internal links
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Group_013.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(GroupInput.outputs[0], Group_013.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_Shader.inputs[0])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_013.outputs[1], Mix_Shader_001.inputs[2])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader_001.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_Shader_001.inputs[0])
        nt.links.new(Mix_Shader_001.outputs[0], GroupOutput.inputs[1])

        # Set default values
        Group_013.inputs[1].default_value = 1.0
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
