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


class ShaderNodeBack_Style(ShaderNode):
    bl_idname = 'ShaderNodeBack_Style'
    bl_label = "Back Style"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Disable Back Style"].default_value = False
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Fresnel (Required)"].default_value = 0.0
        self.inputs["Back Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Size"].default_value = 0.8999999761581421
        self.inputs["Smooth"].default_value = 1.0
        self.inputs["Soft Shading Fac"].default_value = 0.75
        self.inputs["Mix With Fresnel"].default_value = 0.800000011920929

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Back Style'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Back Style', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Disable Back Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Fresnel (Required)', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Back Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8999999761581421
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Soft Shading Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.75
        input_socket = nt.interface.new_socket('Mix With Fresnel', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.800000011920929

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

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (-1055.1097412109375, -163.498291015625)
        Frame_007.label = "Args Extract"
        Frame_007.name = "Frame.007"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (261.44140625, 547.5108642578125)
        Frame_002.label = "Mix With Fresnel"
        Frame_002.name = "Frame.002"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (512.2535400390625, 547.5108642578125)
        Frame_003.label = "Soft Shading Fac"
        Frame_003.name = "Frame.003"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (752.91552734375, 547.5108642578125)
        Frame_005.label = "Smooth"
        Frame_005.name = "Frame.005"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (1008.0479736328125, 547.5108642578125)
        Frame_006.label = "Size"
        Frame_006.name = "Frame.006"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (1240.947021484375, 24.751373291015625)
        Frame.label = "Args Compress"
        Frame.name = "Frame"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (349.61798095703125, 140.68194580078125)
        Group.name = "Group"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (836.2164306640625, 485.64886474609375)
        Reroute_027.name = "Reroute.027"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (566.2532958984375, 244.51991271972656)
        Reroute_002.name = "Reroute.002"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (566.2532958984375, 537.213623046875)
        Reroute_001.name = "Reroute.001"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (890.453369140625, 537.213623046875)
        Reroute_029.name = "Reroute.029"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (309.05218505859375, 264.3453674316406)
        Reroute_032.name = "Reroute.032"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (309.05218505859375, 50.98263931274414)
        Reroute_031.name = "Reroute.031"

        Group_015 = nt.nodes.new('ShaderNodeGroup')
        Group_015.location = (349.61798095703125, 355.18438720703125)
        Group_015.name = "Group.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (241.40000915527344, 155.45950317382812)
        Reroute_016.name = "Reroute.016"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (241.40000915527344, 485.64886474609375)
        Reroute_026.name = "Reroute.026"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (238.33975219726562, 76.2190933227539)
        Reroute_020.name = "Reroute.020"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (238.33975219726562, 96.8551025390625)
        Reroute_019.name = "Reroute.019"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (238.33975219726562, 136.61932373046875)
        Reroute_017.name = "Reroute.017"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-572.9722290039062, 155.45950317382812)
        Reroute_005.name = "Reroute.005"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-320.38726806640625, 136.61932373046875)
        Reroute_008.name = "Reroute.008"

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (24.9521484375, -12.63818359375)
        Group_003.name = "Group.003"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (22.22052001953125, -12.63818359375)
        Group_004.name = "Group.004"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (182.83912658691406, 76.2190933227539)
        Reroute_014.name = "Reroute.014"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-82.33319091796875, 96.8551025390625)
        Reroute_011.name = "Reroute.011"

        Group_006 = nt.nodes.new('ShaderNodeGroup')
        Group_006.location = (28.4024658203125, -12.63818359375)
        Group_006.name = "Group.006"

        Group_007 = nt.nodes.new('ShaderNodeGroup')
        Group_007.location = (17.2528076171875, -12.63818359375)
        Group_007.name = "Group.007"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (1224.246337890625, 145.81634521484375)
        Reroute_018.name = "Reroute.018"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (627.0657958984375, 362.00244140625)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (958.4904174804688, 288.48321533203125)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (1224.246337890625, 384.50555419921875)
        Reroute_010.name = "Reroute.010"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (1261.41552734375, 362.0920104980469)
        Reroute_035.name = "Reroute.035"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (1261.41552734375, 319.8714294433594)
        Reroute_033.name = "Reroute.033"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (1261.41552734375, 100.033203125)
        Reroute_034.name = "Reroute.034"

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (1402.4820556640625, 306.7259826660156)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MIX'

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (1224.246337890625, 251.80245971679688)
        Reroute_009.name = "Reroute.009"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (1593.9512939453125, 251.80245971679688)
        Reroute_036.name = "Reroute.036"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (1593.9512939453125, 342.06756591796875)
        Reroute_037.name = "Reroute.037"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (1657.6627197265625, 458.8431701660156)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (1402.4820556640625, 549.53955078125)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (28.959716796875, 735.97998046875)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (971.7767333984375, 477.3105163574219)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (182.8392333984375, 313.812255859375)
        Reroute_013.name = "Reroute.013"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (733.7225952148438, 477.3105163574219)
        Reroute_007.name = "Reroute.007"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (481.13763427734375, 477.3105163574219)
        Reroute_006.name = "Reroute.006"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (836.2164306640625, 125.64111328125)
        Reroute_028.name = "Reroute.028"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (890.453369140625, 171.819580078125)
        Reroute_030.name = "Reroute.030"

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (-184.13900756835938, -22.2276611328125)
        Group_008.name = "Group.008"

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (-184.13900756835938, -133.83966064453125)
        Group_009.name = "Group.009"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (-184.1390380859375, -379.6467590332031)
        Group_012.name = "Group.012"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (-184.1390380859375, -264.3142395019531)
        Group_011.name = "Group.011"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (458.80810546875, -183.4082794189453)
        Combine_XYZ.name = "Combine XYZ"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (46.2967529296875, 4.879142761230469)
        Group_014.name = "Group.014"

        Group_018 = nt.nodes.new('ShaderNodeGroup')
        Group_018.location = (46.2967529296875, -227.87857055664062)
        Group_018.name = "Group.018"

        Separate_XYZ = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ.location = (39.97125244140625, 515.7647094726562)
        Separate_XYZ.name = "Separate XYZ"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (220.1097412109375, 481.1959533691406)
        Reroute_015.name = "Reroute.015"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (220.1097412109375, 606.8242797851562)
        Reroute_021.name = "Reroute.021"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (709.3273315429688, 606.8242797851562)
        Reroute_022.name = "Reroute.022"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (1984.662353515625, 537.213623046875)
        Reroute_038.name = "Reroute.038"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (2143.3310546875, 200.2785186767578)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (1984.662353515625, 63.26121139526367)
        Reroute_039.name = "Reroute.039"

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (2234.62109375, 444.61395263671875)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MIX'

        # Create internal links
        nt.links.new(GroupInput.outputs[6], Group.inputs[4])
        nt.links.new(GroupInput.outputs[5], Group.inputs[2])
        nt.links.new(GroupInput.outputs[4], Group.inputs[1])
        nt.links.new(Mix_006.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Group.inputs[0])
        nt.links.new(Group.outputs[0], Mix_001.inputs[2])
        nt.links.new(Group_015.outputs[0], Mix_001.inputs[3])
        nt.links.new(GroupInput.outputs[3], Math.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_017.inputs[0])
        nt.links.new(GroupInput.outputs[7], Mix_003.inputs[2])
        nt.links.new(Reroute_026.outputs[0], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Mix_003.inputs[3])
        nt.links.new(Reroute_029.outputs[0], Reroute_030.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_029.inputs[0])
        nt.links.new(Reroute_030.outputs[0], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_031.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Reroute_032.inputs[0])
        nt.links.new(Reroute_032.outputs[0], Group_015.inputs[0])
        nt.links.new(Group_003.outputs[0], Group_004.inputs[0])
        nt.links.new(Group_006.outputs[0], Group_007.inputs[0])
        nt.links.new(Group_003.outputs[1], Reroute_006.inputs[0])
        nt.links.new(Group_004.outputs[1], Reroute_007.inputs[0])
        nt.links.new(Group_006.outputs[1], Reroute_012.inputs[0])
        nt.links.new(Group_007.outputs[1], Reroute_013.inputs[0])
        nt.links.new(GroupInput.outputs[4], Group_008.inputs[0])
        nt.links.new(GroupInput.outputs[5], Group_009.inputs[0])
        nt.links.new(GroupInput.outputs[6], Group_011.inputs[0])
        nt.links.new(GroupInput.outputs[7], Group_012.inputs[0])
        nt.links.new(Group_008.outputs[0], Group_014.inputs[1])
        nt.links.new(Group_009.outputs[0], Group_014.inputs[2])
        nt.links.new(Group_012.outputs[0], Group_018.inputs[2])
        nt.links.new(Reroute_017.outputs[0], Group_015.inputs[4])
        nt.links.new(Reroute_014.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Group_015.inputs[1])
        nt.links.new(Reroute_016.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Group_015.inputs[2])
        nt.links.new(Mix_003.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Mix_004.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Mix_005.inputs[0])
        nt.links.new(Mix_001.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Mix_005.inputs[7])
        nt.links.new(Reroute_033.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Mix_004.inputs[6])
        nt.links.new(Reroute_009.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Mix.inputs[0])
        nt.links.new(Mix_005.outputs[2], Mix.inputs[2])
        nt.links.new(Mix_004.outputs[2], Mix.inputs[3])
        nt.links.new(Group_011.outputs[0], Group_018.inputs[1])
        nt.links.new(Group_014.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(Group_018.outputs[0], Combine_XYZ.inputs[1])
        nt.links.new(Mix_002.outputs[1], GroupOutput.inputs[1])
        nt.links.new(Math.outputs[0], Reroute_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Separate_XYZ.inputs[0])
        nt.links.new(Separate_XYZ.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Separate_XYZ.outputs[1], Group_003.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Group_006.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Reroute_038.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mix_002.inputs[4])
        nt.links.new(GroupInput.outputs[3], Mix_002.inputs[5])
        nt.links.new(Reroute_038.outputs[0], Reroute_039.inputs[0])
        nt.links.new(Reroute_039.outputs[0], Mix_002.inputs[0])
        nt.links.new(Mix.outputs[0], Mix_006.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix_006.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_006.inputs[3])

        # Set default values
        Group.inputs[3].default_value = 1.0
        Group_015.inputs[3].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Combine_XYZ.inputs[2].default_value = 0.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_006.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
