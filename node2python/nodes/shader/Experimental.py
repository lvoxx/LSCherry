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


class ShaderNodeExperimental(ShaderNode):
    bl_idname = 'ShaderNodeExperimental'
    bl_label = "Experimental"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Experimental'

        # Create output sockets
        nt.interface.new_socket('Unstable', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('DO NOT USE FOR PRODUCTION', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        nt.interface.new_socket('Unstable', in_out='INPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('DO NOT USE FOR PRODUCTION', in_out='INPUT', socket_type='NodeSocketShader')

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

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (11.932327270507812, -13.32492446899414)
        Frame.label = "⚠️ **Experimental**: This package is still in development. "
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (18.357421875, -90.05806732177734)
        Frame_001.label = "Features may change or be removed without notice."
        Frame_001.name = "Frame.001"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], GroupOutput.inputs[1])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
