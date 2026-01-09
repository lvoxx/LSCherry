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


class ShaderNodeMake_Toon(ShaderNode):
    bl_idname = 'ShaderNodeMake_Toon'
    bl_label = "Make Toon"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base Color"].default_value = (1.0, 0.0, 0.0, 1.0)
        self.inputs["Shadow Color"].default_value = (0.177734375, 0.0, 0.0, 1.0)
        self.inputs["SSS Color"].default_value = (0.7484369277954102, 0.1325332671403885, 0.0, 1.0)
        self.inputs["Rim Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Back Color"].default_value = (0.0, 0.04392065852880478, 0.42326757311820984, 1.0)
        self.inputs["Rim Strength"].default_value = 0.5
        self.inputs["Rim Size"].default_value = 0.30000001192092896
        self.inputs["Rim Smooth"].default_value = 0.5
        self.inputs["Specular Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Specular Tint"].default_value = 0.0
        self.inputs["Roughness"].default_value = 0.10000000149011612
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Emission"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Emission Strength"].default_value = 1.0
        self.inputs["Alpha"].default_value = 1.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Disable Toon Style"].default_value = False
        self.inputs["Toon Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Disable SSS Style"].default_value = False
        self.inputs["SSS Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Disable Back Style"].default_value = False
        self.inputs["Back Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Enable Custom Ramp"].default_value = False
        self.inputs["Custom Ramp"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Blend With Custom Ramp"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Make Toon'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('To AgrX', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Alpha', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Diffuse Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Post Diffuse Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('SSS Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Rim Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Back Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Light Sources Mask', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shadow Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.177734375, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('SSS Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.7484369277954102, 0.1325332671403885, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Rim Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Back Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.04392065852880478, 0.42326757311820984, 1.0)
        input_socket = nt.interface.new_socket('Rim Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Rim Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Rim Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Specular Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Specular Tint', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Emission', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Disable Toon Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Toon Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Disable SSS Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('SSS Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Disable Back Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Back Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Enable Custom Ramp', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Custom Ramp', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Blend With Custom Ramp', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (114.47570037841797, 173.71424865722656)
        Group_004.name = "Group.004"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-148.395263671875, -7.279314994812012)
        Group.name = "Group"

        # Create internal links
        nt.links.new(Group.outputs[0], Group_004.inputs[0])
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[1])
        nt.links.new(GroupInput.outputs[2], Group.inputs[2])
        nt.links.new(GroupInput.outputs[3], Group.inputs[3])
        nt.links.new(GroupInput.outputs[4], Group.inputs[4])
        nt.links.new(GroupInput.outputs[10], Group.inputs[10])
        nt.links.new(GroupInput.outputs[22], Group.inputs[21])
        nt.links.new(GroupInput.outputs[23], Group.inputs[22])
        nt.links.new(Group.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Group.outputs[2], GroupOutput.inputs[5])
        nt.links.new(Group.outputs[3], GroupOutput.inputs[6])
        nt.links.new(Group.outputs[4], GroupOutput.inputs[7])
        nt.links.new(Group.outputs[5], GroupOutput.inputs[8])
        nt.links.new(GroupInput.outputs[12], Group.inputs[12])
        nt.links.new(GroupInput.outputs[13], Group.inputs[13])
        nt.links.new(GroupInput.outputs[11], Group.inputs[11])
        nt.links.new(Group.outputs[1], GroupOutput.inputs[4])
        nt.links.new(Group.outputs[6], GroupOutput.inputs[9])
        nt.links.new(GroupInput.outputs[15], Group.inputs[14])
        nt.links.new(GroupInput.outputs[24], Group.inputs[23])
        nt.links.new(GroupInput.outputs[8], Group.inputs[8])
        nt.links.new(GroupInput.outputs[9], Group.inputs[9])
        nt.links.new(GroupInput.outputs[14], Group_004.inputs[1])
        nt.links.new(Group_004.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_004.outputs[1], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[14], GroupOutput.inputs[3])
        nt.links.new(GroupInput.outputs[17], Group.inputs[16])
        nt.links.new(GroupInput.outputs[19], Group.inputs[18])
        nt.links.new(GroupInput.outputs[21], Group.inputs[20])
        nt.links.new(GroupInput.outputs[5], Group.inputs[5])
        nt.links.new(GroupInput.outputs[6], Group.inputs[6])
        nt.links.new(GroupInput.outputs[7], Group.inputs[7])
        nt.links.new(GroupInput.outputs[16], Group.inputs[15])
        nt.links.new(GroupInput.outputs[18], Group.inputs[17])
        nt.links.new(GroupInput.outputs[20], Group.inputs[19])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
