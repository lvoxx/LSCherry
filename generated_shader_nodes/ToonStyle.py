import bpy
from ..utils import ShaderNode


class ShaderNodeToonStyle(ShaderNode):
    bl_label = "Toon Style"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 0.0
        Shading_socket.min_value = 0.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"
            Toon_Style_socket = nt.interface.new_socket(
                name="Toon Style",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Toon_Style_socket.default_value = (0.0, 0.0, 0.0)
        Toon_Style_socket.subtype = "XYZ"

        # Input sockets
            Disable_Toon_Style_socket = nt.interface.new_socket(
                name="Disable Toon Style",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Disable_Toon_Style_socket.default_value = False
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = -1.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"
            Fresnel_(Required)_socket = nt.interface.new_socket(
                name="Fresnel (Required)",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fresnel_(Required)_socket.default_value = 0.0
        Fresnel_(Required)_socket.min_value = -1.0
        Fresnel_(Required)_socket.max_value = 1.0
        Fresnel_(Required)_socket.subtype = "NONE"
            Toon_Style_socket = nt.interface.new_socket(
                name="Toon Style",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Toon_Style_socket.default_value = (0.0, 0.0, 0.0)
        Toon_Style_socket.subtype = "XYZ"
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 1.0
        Size_socket.min_value = 0.0
        Size_socket.max_value = 1.0
        Size_socket.subtype = "FACTOR"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 0.10000000149011612
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "FACTOR"
            Soft_Shading_Fac_socket = nt.interface.new_socket(
                name="Soft Shading Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Soft_Shading_Fac_socket.default_value = 0.0
        Soft_Shading_Fac_socket.min_value = 0.0
        Soft_Shading_Fac_socket.max_value = 1.0
        Soft_Shading_Fac_socket.subtype = "FACTOR"
            Mix_With_Fresnel_socket = nt.interface.new_socket(
                name="Mix With Fresnel",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_With_Fresnel_socket.default_value = 0.0
        Mix_With_Fresnel_socket.min_value = 0.0
        Mix_With_Fresnel_socket.max_value = 1.0
        Mix_With_Fresnel_socket.subtype = "FACTOR"

        # Create nodes
        Frame_007 = nt.nodes.new("NodeFrame")
        Frame_007.location = (-1337.984375, -163.49826049804688)
        Frame_006 = nt.nodes.new("NodeFrame")
        Frame_006.location = (1260.05908203125, 547.5108642578125)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (1004.9266357421875, 547.5108642578125)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (768.98974609375, 547.5108642578125)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (539.2431030273438, 547.5108642578125)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (348.564697265625, -180.18630981445312)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (627.0657958984375, 362.00244140625)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (1166.7294921875, 365.2580261230469)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_027 = nt.nodes.new("NodeReroute")
        Reroute_027.location = (836.2164306640625, 485.64886474609375)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (566.2532958984375, 252.51161193847656)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (566.2532958984375, 697.967041015625)
        Reroute_030 = nt.nodes.new("NodeReroute")
        Reroute_030.location = (890.453369140625, 249.08660888671875)
        Reroute_029 = nt.nodes.new("NodeReroute")
        Reroute_029.location = (890.453369140625, 697.967041015625)
        Reroute_032 = nt.nodes.new("NodeReroute")
        Reroute_032.location = (309.05218505859375, 264.3453674316406)
        Reroute_031 = nt.nodes.new("NodeReroute")
        Reroute_031.location = (309.05218505859375, 50.98263931274414)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (958.4904174804688, 358.4822998046875)
        Mix_003.data_type = "FLOAT"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_028 = nt.nodes.new("NodeReroute")
        Reroute_028.location = (836.2164306640625, 200.6311492919922)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (171.59561157226562, 96.8551025390625)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (-112.65252685546875, 117.58712768554688)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (-357.1219177246094, 136.61932373046875)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-607.7640991210938, 155.45950317382812)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (171.59561157226562, 313.1551208496094)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (249.08609008789062, 96.8551025390625)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (249.08609008789062, 136.61932373046875)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (249.08609008789062, 155.45950317382812)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (249.08609008789062, 117.58712768554688)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (249.08609008789062, 485.64886474609375)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-62.53218078613281, 18.86733055114746)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (682.6304931640625, 159.24392700195312)
        Group_006 = nt.nodes.new("ShaderNodeGroup")
        Group_006.location = (28.4024658203125, -12.63818359375)
        Group_007 = nt.nodes.new("ShaderNodeGroup")
        Group_007.location = (17.2528076171875, -12.63818359375)
        Reroute_040 = nt.nodes.new("NodeReroute")
        Reroute_040.location = (989.721923828125, 669.6449584960938)
        Reroute_041 = nt.nodes.new("NodeReroute")
        Reroute_041.location = (989.721923828125, 503.22674560546875)
        Group_005 = nt.nodes.new("ShaderNodeGroup")
        Group_005.location = (22.16192626953125, -12.63818359375)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (-4.76904296875, -12.63818359375)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (730.2202758789062, 476.65338134765625)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (980.8624267578125, 476.65338134765625)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (1225.331787109375, 476.65338134765625)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (247.80078125, 896.2862548828125)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-68.3975830078125, 645.47119140625)
        Separate_XYZ = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ.location = (187.884765625, 621.6536865234375)
        Reroute_035 = nt.nodes.new("NodeReroute")
        Reroute_035.location = (370.94921875, 586.433349609375)
        Reroute_037 = nt.nodes.new("NodeReroute")
        Reroute_037.location = (370.94921875, 669.6449584960938)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (648.1437377929688, 861.46533203125)
        Reroute_038 = nt.nodes.new("NodeReroute")
        Reroute_038.location = (472.6180419921875, 562.8353271484375)
        Reroute_039 = nt.nodes.new("NodeReroute")
        Reroute_039.location = (472.6180419921875, 422.9320068359375)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (-184.13900756835938, -22.2276611328125)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (-184.13900756835938, -133.83966064453125)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (-184.1390380859375, -248.64447021484375)
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (-184.1390380859375, -364.0426940917969)
        Group_016 = nt.nodes.new("ShaderNodeGroup")
        Group_016.location = (16.025146484375, -219.2871551513672)
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (16.025146484375, 4.00971794128418)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (250.9688720703125, -170.16883850097656)
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-430.780517578125, -200.1904754638672)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1995.8916015625, 131.5595703125)
        Group_015 = nt.nodes.new("ShaderNodeGroup")
        Group_015.location = (349.61798095703125, 355.18438720703125)
        Group_015.inputs["White Level"].default_value = 1.0
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (349.61798095703125, 140.68194580078125)
        Group.inputs["White Level"].default_value = 1.0
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-837.493896484375, 935.5900268554688)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1475.7452392578125, 73.4469985961914)
        Mix_002.data_type = "VECTOR"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (1367.421142578125, 697.967041015625)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (1367.4210205078125, -65.09404754638672)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (1237.939453125, -209.27749633789062)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (1562.58837890625, 365.2580261230469)
        Mix_004.data_type = "FLOAT"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (1386.27197265625, -8.412811279296875)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (1386.27197265625, 209.67552185058594)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (1386.27197265625, 328.5213928222656)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (1386.27197265625, 232.95460510253906)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (1564.072021484375, 428.61309814453125)
        # Create links
        nt.links.new(Group_Input.outputs["Soft Shading Fac"], Group.inputs["Soft Shading Fac"])
        nt.links.new(Group_Input.outputs["Smooth"], Group.inputs["Smooth"])
        nt.links.new(Group_Input.outputs["Size"], Group.inputs["Size"])
        nt.links.new(Mix_004.outputs["Result"], Group_Output.inputs["Shading"])
        nt.links.new(Reroute_031.outputs["Output"], Group.inputs["Shading"])
        nt.links.new(Group.outputs["Shading"], Mix_001.inputs["A"])
        nt.links.new(Group_015.outputs["Shading"], Mix_001.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Toon Style"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Mix_001.inputs["Factor"])
        nt.links.new(Reroute_005.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Group_Input_003.outputs["Fresnel (Required)"], Mix.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Mix.inputs["A"])
        nt.links.new(Mix_003.outputs["Result"], Mix.inputs["Factor"])
        nt.links.new(Group_Input_003.outputs["Mix With Fresnel"], Mix_003.inputs["A"])
        nt.links.new(Reroute_026.outputs["Output"], Reroute_027.inputs["Input"])
        nt.links.new(Reroute_027.outputs["Output"], Reroute_028.inputs["Input"])
        nt.links.new(Reroute_028.outputs["Output"], Mix_003.inputs["B"])
        nt.links.new(Reroute_029.outputs["Output"], Reroute_030.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_029.inputs["Input"])
        nt.links.new(Reroute_030.outputs["Output"], Mix_003.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Shading"], Reroute_031.inputs["Input"])
        nt.links.new(Reroute_031.outputs["Output"], Reroute_032.inputs["Input"])
        nt.links.new(Reroute_032.outputs["Output"], Group_015.inputs["Shading"])
        nt.links.new(Group_004.outputs["Compressed"], Group_005.inputs["Compressed"])
        nt.links.new(Group_006.outputs["Compressed"], Group_007.inputs["Compressed"])
        nt.links.new(Group_004.outputs["Extracted"], Reroute_007.inputs["Input"])
        nt.links.new(Group_005.outputs["Extracted"], Reroute_010.inputs["Input"])
        nt.links.new(Group_006.outputs["Extracted"], Reroute_012.inputs["Input"])
        nt.links.new(Group_007.outputs["Extracted"], Reroute_013.inputs["Input"])
        nt.links.new(Group_Input_002.outputs["Size"], Group_008.inputs["Number"])
        nt.links.new(Group_Input_002.outputs["Smooth"], Group_009.inputs["Number"])
        nt.links.new(Group_Input_002.outputs["Soft Shading Fac"], Group_011.inputs["Number"])
        nt.links.new(Group_Input_002.outputs["Mix With Fresnel"], Group_012.inputs["Number"])
        nt.links.new(Group_008.outputs["Sequence"], Group_014.inputs["Sequence 1"])
        nt.links.new(Group_009.outputs["Sequence"], Group_014.inputs["Sequence 2"])
        nt.links.new(Reroute_017.outputs["Output"], Group_015.inputs["Soft Shading Fac"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_019.inputs["Input"])
        nt.links.new(Group_016.outputs["Compressed"], Combine_XYZ.inputs["Y"])
        nt.links.new(Group_014.outputs["Compressed"], Combine_XYZ.inputs["X"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Toon Style"])
        nt.links.new(Group_Input_001.outputs["Toon Style"], Separate_XYZ.inputs["Vector"])
        nt.links.new(Separate_XYZ.outputs["X"], Reroute_035.inputs["Input"])
        nt.links.new(Reroute_035.outputs["Output"], Reroute_037.inputs["Input"])
        nt.links.new(Reroute_038.outputs["Output"], Reroute_039.inputs["Input"])
        nt.links.new(Reroute_039.outputs["Output"], Group_004.inputs["Compressed"])
        nt.links.new(Reroute_037.outputs["Output"], Reroute_040.inputs["Input"])
        nt.links.new(Reroute_040.outputs["Output"], Reroute_041.inputs["Input"])
        nt.links.new(Reroute_041.outputs["Output"], Group_006.inputs["Compressed"])
        nt.links.new(Group_011.outputs["Sequence"], Group_016.inputs["Sequence 1"])
        nt.links.new(Group_012.outputs["Sequence"], Group_016.inputs["Sequence 2"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_012.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Group_015.inputs["Size"])
        nt.links.new(Reroute_018.outputs["Output"], Group_015.inputs["Smooth"])
        nt.links.new(Separate_XYZ.outputs["Y"], Reroute_038.inputs["Input"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mix_002.inputs["A"])
        nt.links.new(Reroute_003.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Group_Input_004.outputs["Toon Style"], Mix_002.inputs["B"])
        nt.links.new(Reroute_004.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Reroute_029.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Group_Input.outputs["Shading"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Mix_004.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_022.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_023.outputs["Output"], Mix_004.inputs["A"])
        nt.links.new(Group_Input_005.outputs["Disable Toon Style"], Mix_004.inputs["Factor"])