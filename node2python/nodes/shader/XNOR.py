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


class ShaderNodeXNOR(ShaderNode):
    bl_idname = 'ShaderNodeXNOR'
    bl_label = "XNOR"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["A"].default_value = 0.0
        self.inputs["B"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'XNOR'

        # Create output sockets
        nt.interface.new_socket('O', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('A', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('B', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0

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

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-20.0, 20.0)
        Group.name = "Group"

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (160.0, 20.0)
        Group_001.name = "Group.001"

        Group_020 = nt.nodes.new('ShaderNodeGroup')
        Group_020.location = (-20.0, -140.0)
        Group_020.name = "Group.020"

        # Create internal links
        nt.links.new(Group_001.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[1])
        nt.links.new(Group.outputs[0], Group_001.inputs[0])
        nt.links.new(Group_020.outputs[0], Group_001.inputs[1])
        nt.links.new(GroupInput.outputs[0], Group_020.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group_020.inputs[1])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
