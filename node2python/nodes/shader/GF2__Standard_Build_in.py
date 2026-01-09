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


class ShaderNodeGF2__Standard_Build_in(ShaderNode):
    bl_idname = 'ShaderNodeGF2__Standard_Build_in'
    bl_label = "GF2: Standard Build-in"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Diffuse Texture"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Alpha"].default_value = 1.0
        self.inputs["Spec Texture"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Normal Texture"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Anisotropic"].default_value = 0.0
        self.inputs["AO"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GF2: Standard Build-in'

        # Create output sockets
        nt.interface.new_socket('Diffuse Texture', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Alpha', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Specular Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Specular Tint', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Metal Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Blend Metal Ramp', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Diffuse Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Spec Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Normal Texture', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Anisotropic', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('AO', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-141.62542724609375, 75.1331787109375)
        Separate_Color.name = "Separate Color"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (89.5264663696289, 7.390474319458008)
        Map_Range.name = "Map Range"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (577.2362060546875, -222.5399169921875)
        Group.name = "Group"

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (577.2362060546875, -159.46548461914062)
        Group_001.name = "Group.001"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (791.058837890625, -99.7928695678711)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (377.9173583984375, -124.38348388671875)
        Math.label = "1 - X"
        Math.name = "Math"
        Math.operation = 'SUBTRACT'

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (-146.75616455078125, -113.14131164550781)
        Group_002.name = "Group.002"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (575.6005249023438, 264.1119689941406)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (151.82542419433594, -78.43937683105469)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (368.2861022949219, 9.572591781616211)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Hue_Saturation_Value_001 = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value_001.location = (1044.7650146484375, -160.9136962890625)
        Hue_Saturation_Value_001.name = "Hue/Saturation/Value.001"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (1096.2611083984375, 67.11038208007812)
        Math_001.name = "Math.001"
        Math_001.operation = 'DIVIDE'

        # Create internal links
        nt.links.new(Separate_Color.outputs[1], Map_Range.inputs[0])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[2], Separate_Color.inputs[0])
        nt.links.new(Group_001.outputs[0], Mix.inputs[6])
        nt.links.new(Group.outputs[1], Mix.inputs[7])
        nt.links.new(Map_Range.outputs[0], Math.inputs[1])
        nt.links.new(Math.outputs[0], Group.inputs[1])
        nt.links.new(GroupInput.outputs[4], Mix.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[5])
        nt.links.new(GroupInput.outputs[3], Group_002.inputs[0])
        nt.links.new(Group_002.outputs[0], Group.inputs[5])
        nt.links.new(Group_002.outputs[0], GroupOutput.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[6])
        nt.links.new(Hue_Saturation_Value.outputs[0], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[5], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], GroupOutput.inputs[1])
        nt.links.new(Map_Range.outputs[0], GroupOutput.inputs[6])
        nt.links.new(Math_001.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Separate_Color.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[5], Mix_002.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_002.inputs[7])
        nt.links.new(Mix_002.outputs[2], Hue_Saturation_Value.inputs[4])
        nt.links.new(Mix_001.outputs[2], Hue_Saturation_Value_001.inputs[4])
        nt.links.new(Hue_Saturation_Value_001.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Separate_Color.outputs[0], Math_001.inputs[0])

        # Set default values
        Map_Range.inputs[1].default_value = 0.20000000298023224
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Group.inputs[0].default_value = True
        Group.inputs[2].default_value = 4.010000228881836
        Group.inputs[3].default_value = 1.0
        Group.inputs[4].default_value = 0.10000000149011612
        Group_001.inputs[0].default_value = 0.8999999761581421
        Group_001.inputs[1].default_value = 0.9399999976158142
        Group_001.inputs[2].default_value = 0.9800000190734863
        Group_001.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_001.inputs[4].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        Group_001.inputs[5].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        Group_001.inputs[6].default_value = (1.0, 1.0, 1.0, 1.0)
        Group_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[0].default_value = 1.0
        Math.inputs[2].default_value = 0.5
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[1].default_value = 0.5
        Hue_Saturation_Value.inputs[2].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Hue_Saturation_Value_001.inputs[0].default_value = 0.5
        Hue_Saturation_Value_001.inputs[1].default_value = 0.20000000298023224
        Hue_Saturation_Value_001.inputs[2].default_value = 1.5
        Hue_Saturation_Value_001.inputs[3].default_value = 1.0
        Math_001.inputs[1].default_value = 10.0
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
