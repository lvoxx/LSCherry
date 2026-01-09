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


class ShaderNodeInit_Nose_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeInit_Nose_Ramp'
    bl_label = "Init Nose Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Min Dot Value"].default_value = 0.0
        self.inputs["Max  Dot Value"].default_value = 1.0
        self.inputs["Default UV"].default_value = 1.0
        self.inputs["Flip UV"].default_value = -1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Init Nose Ramp'

        # Create output sockets
        nt.interface.new_socket('Face Value', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Face Vector', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        nt.interface.new_socket('Deprecated', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Min Dot Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Max  Dot Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Default UV', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Flip UV', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = -1.0

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

        Group_006 = nt.nodes.new('ShaderNodeGroup')
        Group_006.location = (0.0, 0.0)
        Group_006.name = "Group.006"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (-57.394195556640625, 135.42788696289062)
        Frame_003.label = "Changed to \"Nose Ramp Builder\""
        Frame_003.name = "Frame.003"

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Group_006.inputs[1])
        nt.links.new(GroupInput.outputs[2], Group_006.inputs[2])
        nt.links.new(GroupInput.outputs[3], Group_006.inputs[3])
        nt.links.new(GroupInput.outputs[4], Group_006.inputs[4])
        nt.links.new(GroupInput.outputs[5], Group_006.inputs[5])
        nt.links.new(Group_006.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_006.outputs[1], GroupOutput.inputs[1])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
