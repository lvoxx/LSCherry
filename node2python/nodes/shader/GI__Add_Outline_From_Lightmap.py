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


class ShaderNodeGI__Add_Outline_From_Lightmap(ShaderNode):
    bl_idname = 'ShaderNodeGI__Add_Outline_From_Lightmap'
    bl_label = "GI: Add Outline From Lightmap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lighmap Alpha"].default_value = 0.0
        self.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Range 1"].default_value = 0.10000000149011612
        self.inputs["Range 2"].default_value = 0.30000001192092896
        self.inputs["Range 3"].default_value = 0.44999998807907104

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GI: Add Outline From Lightmap'

        # Create output sockets
        nt.interface.new_socket('Outline', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Lighmap Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Map 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Range 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Range 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Range 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.44999998807907104

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
        Group.location = (139.360107421875, 146.60858154296875)
        Group.name = "Group"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[2])
        nt.links.new(GroupInput.outputs[2], Group.inputs[3])
        nt.links.new(GroupInput.outputs[3], Group.inputs[4])
        nt.links.new(GroupInput.outputs[4], Group.inputs[5])
        nt.links.new(GroupInput.outputs[5], Group.inputs[7])
        nt.links.new(GroupInput.outputs[6], Group.inputs[8])
        nt.links.new(GroupInput.outputs[7], Group.inputs[9])
        nt.links.new(Group.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[7], Group.inputs[10])
        nt.links.new(GroupInput.outputs[4], Group.inputs[6])

        # Set default values
        Group.inputs[1].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
