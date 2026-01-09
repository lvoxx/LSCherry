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


class ShaderNodeDisable_All_Shader(ShaderNode):
    bl_idname = 'ShaderNodeDisable_All_Shader'
    bl_label = "Disable All Shader"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Disable All Shader'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        nt.interface.new_socket('Shader', in_out='INPUT', socket_type='NodeSocketShader')

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

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (115.50872802734375, 53.576416015625)
        Mix_Shader.name = "Mix Shader"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (-115.50869750976562, -53.576416015625)
        Transparent_BSDF.name = "Transparent BSDF"

        # Create internal links
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(GroupInput.outputs[1], Mix_Shader.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_Shader.inputs[0])

        # Set default values
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
