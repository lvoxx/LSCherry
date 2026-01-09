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


class ShaderNodeSimple_Pantyhose_Type_2(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Pantyhose_Type_2'
    bl_label = "Simple Pantyhose Type 2"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Enable Dot"].default_value = False
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Color"].default_value = (0.685835599899292, 0.685835599899292, 0.685835599899292, 1.0)
        self.inputs["Highlight Color"].default_value = (1.0, 0.6242283582687378, 0.5513602495193481, 1.0)
        self.inputs["Size"].default_value = 8.0
        self.inputs["Roughness"].default_value = 0.20000000298023224

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Pantyhose Type 2'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Pattern', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Enable Dot', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.685835599899292, 0.685835599899292, 0.685835599899292, 1.0)
        input_socket = nt.interface.new_socket('Highlight Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.6242283582687378, 0.5513602495193481, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 8.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.20000000298023224

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

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (0.0, 0.0)
        Group_003.name = "Group.003"

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Group_003.inputs[2])
        nt.links.new(GroupInput.outputs[2], Group_003.inputs[3])
        nt.links.new(GroupInput.outputs[3], Group_003.inputs[4])
        nt.links.new(GroupInput.outputs[4], Group_003.inputs[5])
        nt.links.new(GroupInput.outputs[5], Group_003.inputs[6])
        nt.links.new(Group_003.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_003.outputs[1], GroupOutput.inputs[1])
        nt.links.new(Group_003.outputs[2], GroupOutput.inputs[2])
        nt.links.new(GroupInput.outputs[0], Group_003.inputs[1])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
