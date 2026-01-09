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


class ShaderNodeNumber_To_Sequence(ShaderNode):
    bl_idname = 'ShaderNodeNumber_To_Sequence'
    bl_label = "Number To Sequence"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Number"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Number To Sequence'

        # Create output sockets
        nt.interface.new_socket('Sequence', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Number', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5

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

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (0.0, 0.0)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Math_001.inputs[1].default_value = 1000.0
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
