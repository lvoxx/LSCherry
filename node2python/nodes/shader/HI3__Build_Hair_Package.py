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


class ShaderNodeHI3__Build_Hair_Package(ShaderNode):
    bl_idname = 'ShaderNodeHI3__Build_Hair_Package'
    bl_label = "HI3: Build Hair Package"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Hair Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Lightmap Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Hair Mask Texture"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Shadow Factor"].default_value = 0.0
        self.inputs["Shadow Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Toon"].default_value = 0.0
        self.inputs["Shadow Factor"].default_value = 1.0
        self.inputs["Ramp Size"].default_value = 0.949999988079071
        self.inputs["Value Enhance"].default_value = 0.10000000149011612

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HI3: Build Hair Package'

        # Create output sockets
        nt.interface.new_socket('Base Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Shadow Mask', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Highlight Mask', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Hair Ramp UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Hair Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Lightmap Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Hair Mask Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shadow Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Toon', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Ramp Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.949999988079071
        input_socket = nt.interface.new_socket('Value Enhance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612

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

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (89.72325134277344, 191.2218017578125)
        Group_008.name = "Group.008"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (169.68411254882812, -336.4360046386719)
        Group_010.name = "Group.010"

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (-356.17462158203125, -143.7783660888672)
        Group_009.name = "Group.009"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (38.178409576416016, -130.77976989746094)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        RGB_to_BW = nt.nodes.new('ShaderNodeRGBToBW')
        RGB_to_BW.location = (-402.6463317871094, -322.1174621582031)
        RGB_to_BW.name = "RGB to BW"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-216.64598083496094, -380.8717041015625)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        # Create internal links
        nt.links.new(Group_008.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group_009.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[2])
        nt.links.new(Group_009.outputs[0], Group_008.inputs[2])
        nt.links.new(Group_009.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Group_009.outputs[0], Group_010.inputs[2])
        nt.links.new(Group_010.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Group_009.outputs[1], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[4], Group_008.inputs[3])
        nt.links.new(GroupInput.outputs[3], Group_008.inputs[1])
        nt.links.new(GroupInput.outputs[5], Group_010.inputs[1])
        nt.links.new(GroupInput.outputs[6], Group_010.inputs[0])
        nt.links.new(GroupInput.outputs[7], Group_010.inputs[3])
        nt.links.new(GroupInput.outputs[8], Group_010.inputs[4])
        nt.links.new(GroupInput.outputs[2], RGB_to_BW.inputs[0])
        nt.links.new(GroupInput.outputs[0], Group_008.inputs[0])
        nt.links.new(RGB_to_BW.outputs[0], Math.inputs[0])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(RGB_to_BW.outputs[0], Mix.inputs[7])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
