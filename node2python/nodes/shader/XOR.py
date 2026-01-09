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


class ShaderNodeXOR(ShaderNode):
    bl_idname = 'ShaderNodeXOR'
    bl_label = "XOR"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["A"].default_value = 0.0
        self.inputs["B"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'XOR'

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

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (360.69439697265625, -64.64056396484375)
        Group_012.name = "Group.012"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (360.0, 180.0)
        Group_011.name = "Group.011"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (180.0, 40.0)
        Group_010.name = "Group.010"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (560.0, 120.0)
        Group_013.name = "Group.013"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group_011.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group_012.inputs[1])
        nt.links.new(GroupInput.outputs[0], Group_010.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group_010.inputs[1])
        nt.links.new(Group_010.outputs[0], Group_011.inputs[1])
        nt.links.new(Group_010.outputs[0], Group_012.inputs[0])
        nt.links.new(Group_011.outputs[0], Group_013.inputs[0])
        nt.links.new(Group_012.outputs[0], Group_013.inputs[1])
        nt.links.new(Group_013.outputs[0], GroupOutput.inputs[0])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
