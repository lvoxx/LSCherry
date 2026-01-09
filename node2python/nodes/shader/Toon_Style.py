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


class ShaderNodeToon_Style(ShaderNode):
    bl_idname = 'ShaderNodeToon_Style'
    bl_label = "Toon Style"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Disable Toon Style"].default_value = False
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Fresnel (Required)"].default_value = 0.0
        self.inputs["Toon Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Size"].default_value = 1.0
        self.inputs["Smooth"].default_value = 0.10000000149011612
        self.inputs["Soft Shading Fac"].default_value = 0.0
        self.inputs["Mix With Fresnel"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Toon Style'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Toon Style', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Disable Toon Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Fresnel (Required)', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Toon Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Soft Shading Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Mix With Fresnel', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (-1337.984375, -163.49826049804688)
        Frame_007.label = "Args Extract"
        Frame_007.name = "Frame.007"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (1260.05908203125, 547.5108642578125)
        Frame_006.label = "Size"
        Frame_006.name = "Frame.006"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (1004.9266357421875, 547.5108642578125)
        Frame_005.label = "Smooth"
        Frame_005.name = "Frame.005"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (768.98974609375, 547.5108642578125)
        Frame_004.label = "Soft Shading Fac"
        Frame_004.name = "Frame.004"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (539.2431030273438, 547.5108642578125)
        Frame_003.label = "Mix With Fresnel"
        Frame_003.name = "Frame.003"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (348.564697265625, -180.18630981445312)
        Frame.label = "Args Compress"
        Frame.name = "Frame"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (627.0657958984375, 362.00244140625)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (1166.7294921875, 365.2580261230469)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (836.2164306640625, 485.64886474609375)
        Reroute_027.name = "Reroute.027"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (566.2532958984375, 252.51161193847656)
        Reroute_002.name = "Reroute.002"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (566.2532958984375, 697.967041015625)
        Reroute_001.name = "Reroute.001"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (890.453369140625, 249.08660888671875)
        Reroute_030.name = "Reroute.030"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (890.453369140625, 697.967041015625)
        Reroute_029.name = "Reroute.029"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (309.05218505859375, 264.3453674316406)
        Reroute_032.name = "Reroute.032"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (309.05218505859375, 50.98263931274414)
        Reroute_031.name = "Reroute.031"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (958.4904174804688, 358.4822998046875)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (836.2164306640625, 200.6311492919922)
        Reroute_028.name = "Reroute.028"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (171.59561157226562, 96.8551025390625)
        Reroute_011.name = "Reroute.011"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-112.65252685546875, 117.58712768554688)
        Reroute_009.name = "Reroute.009"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-357.1219177246094, 136.61932373046875)
        Reroute_008.name = "Reroute.008"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-607.7640991210938, 155.45950317382812)
        Reroute_005.name = "Reroute.005"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (171.59561157226562, 313.1551208496094)
        Reroute_013.name = "Reroute.013"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (249.08609008789062, 96.8551025390625)
        Reroute_019.name = "Reroute.019"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (249.08609008789062, 136.61932373046875)
        Reroute_017.name = "Reroute.017"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (249.08609008789062, 155.45950317382812)
        Reroute_016.name = "Reroute.016"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (249.08609008789062, 117.58712768554688)
        Reroute_018.name = "Reroute.018"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (249.08609008789062, 485.64886474609375)
        Reroute_026.name = "Reroute.026"

        Group_006 = nt.nodes.new('ShaderNodeGroup')
        Group_006.location = (28.4024658203125, -12.63818359375)
        Group_006.name = "Group.006"

        Group_007 = nt.nodes.new('ShaderNodeGroup')
        Group_007.location = (17.2528076171875, -12.63818359375)
        Group_007.name = "Group.007"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (989.721923828125, 669.6449584960938)
        Reroute_040.name = "Reroute.040"

        Reroute_041 = nt.nodes.new('NodeReroute')
        Reroute_041.location = (989.721923828125, 503.22674560546875)
        Reroute_041.name = "Reroute.041"

        Group_005 = nt.nodes.new('ShaderNodeGroup')
        Group_005.location = (22.16192626953125, -12.63818359375)
        Group_005.name = "Group.005"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (-4.76904296875, -12.63818359375)
        Group_004.name = "Group.004"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (730.2202758789062, 476.65338134765625)
        Reroute_007.name = "Reroute.007"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (980.8624267578125, 476.65338134765625)
        Reroute_010.name = "Reroute.010"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (1225.331787109375, 476.65338134765625)
        Reroute_012.name = "Reroute.012"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (247.80078125, 896.2862548828125)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Separate_XYZ = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ.location = (187.884765625, 621.6536865234375)
        Separate_XYZ.name = "Separate XYZ"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (370.94921875, 586.433349609375)
        Reroute_035.name = "Reroute.035"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (370.94921875, 669.6449584960938)
        Reroute_037.name = "Reroute.037"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (648.1437377929688, 861.46533203125)
        Reroute.name = "Reroute"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (472.6180419921875, 562.8353271484375)
        Reroute_038.name = "Reroute.038"

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (472.6180419921875, 422.9320068359375)
        Reroute_039.name = "Reroute.039"

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (-184.13900756835938, -22.2276611328125)
        Group_008.name = "Group.008"

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (-184.13900756835938, -133.83966064453125)
        Group_009.name = "Group.009"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (-184.1390380859375, -248.64447021484375)
        Group_011.name = "Group.011"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (-184.1390380859375, -364.0426940917969)
        Group_012.name = "Group.012"

        Group_016 = nt.nodes.new('ShaderNodeGroup')
        Group_016.location = (16.025146484375, -219.2871551513672)
        Group_016.name = "Group.016"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (16.025146484375, 4.00971794128418)
        Group_014.name = "Group.014"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (250.9688720703125, -170.16883850097656)
        Combine_XYZ.name = "Combine XYZ"

        Group_015 = nt.nodes.new('ShaderNodeGroup')
        Group_015.location = (349.61798095703125, 355.18438720703125)
        Group_015.name = "Group.015"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (349.61798095703125, 140.68194580078125)
        Group.name = "Group"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1475.7452392578125, 73.4469985961914)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (1367.421142578125, 697.967041015625)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (1367.4210205078125, -65.09404754638672)
        Reroute_004.name = "Reroute.004"

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (1562.58837890625, 365.2580261230469)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (1386.27197265625, -8.412811279296875)
        Reroute_020.name = "Reroute.020"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (1386.27197265625, 209.67552185058594)
        Reroute_021.name = "Reroute.021"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (1386.27197265625, 328.5213928222656)
        Reroute_022.name = "Reroute.022"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (1386.27197265625, 232.95460510253906)
        Reroute_023.name = "Reroute.023"

        # Create internal links
        nt.links.new(GroupInput.outputs[6], Group.inputs[4])
        nt.links.new(GroupInput.outputs[5], Group.inputs[2])
        nt.links.new(GroupInput.outputs[4], Group.inputs[1])
        nt.links.new(Mix_004.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Group.inputs[0])
        nt.links.new(Group.outputs[0], Mix_001.inputs[2])
        nt.links.new(Group_015.outputs[0], Mix_001.inputs[3])
        nt.links.new(GroupInput.outputs[3], Math.inputs[0])
        nt.links.new(Math.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_018.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[3])
        nt.links.new(Mix_001.outputs[0], Mix.inputs[2])
        nt.links.new(Mix_003.outputs[0], Mix.inputs[0])
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
        nt.links.new(Group_004.outputs[0], Group_005.inputs[0])
        nt.links.new(Group_006.outputs[0], Group_007.inputs[0])
        nt.links.new(Group_004.outputs[1], Reroute_007.inputs[0])
        nt.links.new(Group_005.outputs[1], Reroute_010.inputs[0])
        nt.links.new(Group_006.outputs[1], Reroute_012.inputs[0])
        nt.links.new(Group_007.outputs[1], Reroute_013.inputs[0])
        nt.links.new(GroupInput.outputs[4], Group_008.inputs[0])
        nt.links.new(GroupInput.outputs[5], Group_009.inputs[0])
        nt.links.new(GroupInput.outputs[6], Group_011.inputs[0])
        nt.links.new(GroupInput.outputs[7], Group_012.inputs[0])
        nt.links.new(Group_008.outputs[0], Group_014.inputs[1])
        nt.links.new(Group_009.outputs[0], Group_014.inputs[2])
        nt.links.new(Reroute_017.outputs[0], Group_015.inputs[4])
        nt.links.new(Reroute_016.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Group_016.outputs[0], Combine_XYZ.inputs[1])
        nt.links.new(Group_014.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(Mix_002.outputs[1], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[3], Separate_XYZ.inputs[0])
        nt.links.new(Separate_XYZ.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_038.outputs[0], Reroute_039.inputs[0])
        nt.links.new(Reroute_039.outputs[0], Group_004.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Reroute_040.inputs[0])
        nt.links.new(Reroute_040.outputs[0], Reroute_041.inputs[0])
        nt.links.new(Reroute_041.outputs[0], Group_006.inputs[0])
        nt.links.new(Group_011.outputs[0], Group_016.inputs[1])
        nt.links.new(Group_012.outputs[0], Group_016.inputs[2])
        nt.links.new(Reroute_007.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Group_015.inputs[1])
        nt.links.new(Reroute_018.outputs[0], Group_015.inputs[2])
        nt.links.new(Separate_XYZ.outputs[1], Reroute_038.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mix_002.inputs[4])
        nt.links.new(Reroute_003.outputs[0], Reroute_004.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix_002.inputs[5])
        nt.links.new(Reroute_004.outputs[0], Mix_002.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Reroute_003.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Mix_004.inputs[3])
        nt.links.new(Mix.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Mix_004.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix_004.inputs[0])

        # Set default values
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Combine_XYZ.inputs[2].default_value = 0.0
        Group_015.inputs[3].default_value = 1.0
        Group.inputs[3].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
