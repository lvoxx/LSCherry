import bpy
from ..utils import ShaderNode


class ShaderNodeBackStyle(ShaderNode):
    bl_label = "Back Style"
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
            Back_Style_socket = nt.interface.new_socket(
                name="Back Style",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Back_Style_socket.default_value = (0.0, 0.0, 0.0)
        Back_Style_socket.subtype = "XYZ"

        # Input sockets
            Disable_Back_Style_socket = nt.interface.new_socket(
                name="Disable Back Style",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Disable_Back_Style_socket.default_value = False
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
            Back_Style_socket = nt.interface.new_socket(
                name="Back Style",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Back_Style_socket.default_value = (0.0, 0.0, 0.0)
        Back_Style_socket.subtype = "XYZ"
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 0.8999999761581421
        Size_socket.min_value = 0.0
        Size_socket.max_value = 1.0
        Size_socket.subtype = "FACTOR"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 1.0
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "FACTOR"
            Soft_Shading_Fac_socket = nt.interface.new_socket(
                name="Soft Shading Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Soft_Shading_Fac_socket.default_value = 0.75
        Soft_Shading_Fac_socket.min_value = 0.0
        Soft_Shading_Fac_socket.max_value = 1.0
        Soft_Shading_Fac_socket.subtype = "FACTOR"
            Mix_With_Fresnel_socket = nt.interface.new_socket(
                name="Mix With Fresnel",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_With_Fresnel_socket.default_value = 0.800000011920929
        Mix_With_Fresnel_socket.min_value = 0.0
        Mix_With_Fresnel_socket.max_value = 1.0
        Mix_With_Fresnel_socket.subtype = "FACTOR"

        # Create nodes
        Frame_007 = nt.nodes.new("NodeFrame")
        Frame_007.location = (-1055.1097412109375, -163.498291015625)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (261.44140625, 547.5108642578125)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (512.2535400390625, 547.5108642578125)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (752.91552734375, 547.5108642578125)
        Frame_006 = nt.nodes.new("NodeFrame")
        Frame_006.location = (1008.0479736328125, 547.5108642578125)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (1240.947021484375, 24.751373291015625)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (349.61798095703125, 140.68194580078125)
        Group.inputs["White Level"].default_value = 1.0
        Reroute_027 = nt.nodes.new("NodeReroute")
        Reroute_027.location = (836.2164306640625, 485.64886474609375)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (566.2532958984375, 244.51991271972656)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (566.2532958984375, 537.213623046875)
        Reroute_029 = nt.nodes.new("NodeReroute")
        Reroute_029.location = (890.453369140625, 537.213623046875)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-62.53218078613281, 18.86733055114746)
        Reroute_032 = nt.nodes.new("NodeReroute")
        Reroute_032.location = (309.05218505859375, 264.3453674316406)
        Reroute_031 = nt.nodes.new("NodeReroute")
        Reroute_031.location = (309.05218505859375, 50.98263931274414)
        Group_015 = nt.nodes.new("ShaderNodeGroup")
        Group_015.location = (349.61798095703125, 355.18438720703125)
        Group_015.inputs["White Level"].default_value = 1.0
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (241.40000915527344, 155.45950317382812)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (241.40000915527344, 485.64886474609375)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (238.33975219726562, 76.2190933227539)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (238.33975219726562, 96.8551025390625)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (238.33975219726562, 136.61932373046875)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-572.9722290039062, 155.45950317382812)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (-320.38726806640625, 136.61932373046875)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (24.9521484375, -12.63818359375)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (22.22052001953125, -12.63818359375)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (182.83912658691406, 76.2190933227539)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (-82.33319091796875, 96.8551025390625)
        Group_006 = nt.nodes.new("ShaderNodeGroup")
        Group_006.location = (28.4024658203125, -12.63818359375)
        Group_007 = nt.nodes.new("ShaderNodeGroup")
        Group_007.location = (17.2528076171875, -12.63818359375)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (1224.246337890625, 145.81634521484375)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (627.0657958984375, 362.00244140625)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (958.4904174804688, 288.48321533203125)
        Mix_003.data_type = "FLOAT"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (1224.246337890625, 384.50555419921875)
        Reroute_035 = nt.nodes.new("NodeReroute")
        Reroute_035.location = (1261.41552734375, 362.0920104980469)
        Reroute_033 = nt.nodes.new("NodeReroute")
        Reroute_033.location = (1261.41552734375, 319.8714294433594)
        Reroute_034 = nt.nodes.new("NodeReroute")
        Reroute_034.location = (1261.41552734375, 100.033203125)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (1402.4820556640625, 306.7259826660156)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MIX"
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (1224.246337890625, 251.80245971679688)
        Reroute_036 = nt.nodes.new("NodeReroute")
        Reroute_036.location = (1593.9512939453125, 251.80245971679688)
        Reroute_037 = nt.nodes.new("NodeReroute")
        Reroute_037.location = (1593.9512939453125, 342.06756591796875)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (1657.6627197265625, 458.8431701660156)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (1402.4820556640625, 549.53955078125)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (2750.89453125, 278.29669189453125)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (651.08935546875, 140.51177978515625)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (28.959716796875, 735.97998046875)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-207.8680419921875, 534.953125)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (971.7767333984375, 477.3105163574219)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (182.8392333984375, 313.812255859375)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (733.7225952148438, 477.3105163574219)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (481.13763427734375, 477.3105163574219)
        Reroute_028 = nt.nodes.new("NodeReroute")
        Reroute_028.location = (836.2164306640625, 125.64111328125)
        Reroute_030 = nt.nodes.new("NodeReroute")
        Reroute_030.location = (890.453369140625, 171.819580078125)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (-184.13900756835938, -22.2276611328125)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (-184.13900756835938, -133.83966064453125)
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (-184.1390380859375, -379.6467590332031)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (-184.1390380859375, -264.3142395019531)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (458.80810546875, -183.4082794189453)
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (46.2967529296875, 4.879142761230469)
        Group_018 = nt.nodes.new("ShaderNodeGroup")
        Group_018.location = (46.2967529296875, -227.87857055664062)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-439.33465576171875, -187.82388305664062)
        Separate_XYZ = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ.location = (39.97125244140625, 515.7647094726562)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (220.1097412109375, 481.1959533691406)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (220.1097412109375, 606.8242797851562)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (709.3273315429688, 606.8242797851562)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-985.916015625, 737.2328491210938)
        Reroute_038 = nt.nodes.new("NodeReroute")
        Reroute_038.location = (1984.662353515625, 537.213623046875)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (2143.3310546875, 200.2785186767578)
        Mix_002.data_type = "VECTOR"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (1921.23095703125, -193.61178588867188)
        Reroute_039 = nt.nodes.new("NodeReroute")
        Reroute_039.location = (1984.662353515625, 63.26121139526367)
        Mix_006 = nt.nodes.new("ShaderNodeMix")
        Mix_006.location = (2234.62109375, 444.61395263671875)
        Mix_006.data_type = "FLOAT"
        Mix_006.blend_type = "MIX"
        Mix_006.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_006.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (2234.62109375, 526.736572265625)
        # Create links
        nt.links.new(Group_Input.outputs["Soft Shading Fac"], Group.inputs["Soft Shading Fac"])
        nt.links.new(Group_Input.outputs["Smooth"], Group.inputs["Smooth"])
        nt.links.new(Group_Input.outputs["Size"], Group.inputs["Size"])
        nt.links.new(Mix_006.outputs["Result"], Group_Output.inputs["Shading"])
        nt.links.new(Reroute_031.outputs["Output"], Group.inputs["Shading"])
        nt.links.new(Group.outputs["Shading"], Mix_001.inputs["A"])
        nt.links.new(Group_015.outputs["Shading"], Mix_001.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Back Style"], Math.inputs["Value"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Mix_001.inputs["Factor"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_012.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_017.inputs["Input"])
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
        nt.links.new(Group_003.outputs["Compressed"], Group_004.inputs["Compressed"])
        nt.links.new(Group_006.outputs["Compressed"], Group_007.inputs["Compressed"])
        nt.links.new(Group_003.outputs["Extracted"], Reroute_006.inputs["Input"])
        nt.links.new(Group_004.outputs["Extracted"], Reroute_007.inputs["Input"])
        nt.links.new(Group_006.outputs["Extracted"], Reroute_012.inputs["Input"])
        nt.links.new(Group_007.outputs["Extracted"], Reroute_013.inputs["Input"])
        nt.links.new(Group_Input_002.outputs["Size"], Group_008.inputs["Number"])
        nt.links.new(Group_Input_002.outputs["Smooth"], Group_009.inputs["Number"])
        nt.links.new(Group_Input_002.outputs["Soft Shading Fac"], Group_011.inputs["Number"])
        nt.links.new(Group_Input_002.outputs["Mix With Fresnel"], Group_012.inputs["Number"])
        nt.links.new(Group_008.outputs["Sequence"], Group_014.inputs["Sequence 1"])
        nt.links.new(Group_009.outputs["Sequence"], Group_014.inputs["Sequence 2"])
        nt.links.new(Group_012.outputs["Sequence"], Group_018.inputs["Sequence 2"])
        nt.links.new(Reroute_017.outputs["Output"], Group_015.inputs["Soft Shading Fac"])
        nt.links.new(Reroute_014.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Group_015.inputs["Size"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Group_015.inputs["Smooth"])
        nt.links.new(Mix_003.outputs["Result"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Mix_004.inputs["Factor"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Mix_005.inputs["Factor"])
        nt.links.new(Mix_001.outputs["Result"], Reroute_033.inputs["Input"])
        nt.links.new(Reroute_033.outputs["Output"], Reroute_034.inputs["Input"])
        nt.links.new(Reroute_034.outputs["Output"], Mix_005.inputs["B"])
        nt.links.new(Reroute_033.outputs["Output"], Reroute_035.inputs["Input"])
        nt.links.new(Reroute_035.outputs["Output"], Mix_004.inputs["A"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_036.inputs["Input"])
        nt.links.new(Reroute_036.outputs["Output"], Reroute_037.inputs["Input"])
        nt.links.new(Reroute_037.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Mix_005.outputs["Result"], Mix.inputs["A"])
        nt.links.new(Mix_004.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Group_011.outputs["Sequence"], Group_018.inputs["Sequence 1"])
        nt.links.new(Group_014.outputs["Compressed"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_018.outputs["Compressed"], Combine_XYZ.inputs["Y"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Back Style"])
        nt.links.new(Math.outputs["Value"], Reroute_001.inputs["Input"])
        nt.links.new(Group_Input_001.outputs["Back Style"], Separate_XYZ.inputs["Vector"])
        nt.links.new(Separate_XYZ.outputs["X"], Reroute_015.inputs["Input"])
        nt.links.new(Separate_XYZ.outputs["Y"], Group_003.inputs["Compressed"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_022.outputs["Output"], Group_006.inputs["Compressed"])
        nt.links.new(Reroute_029.outputs["Output"], Reroute_038.inputs["Input"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mix_002.inputs["A"])
        nt.links.new(Group_Input_004.outputs["Back Style"], Mix_002.inputs["B"])
        nt.links.new(Reroute_038.outputs["Output"], Reroute_039.inputs["Input"])
        nt.links.new(Reroute_039.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Mix.outputs["Result"], Mix_006.inputs["A"])
        nt.links.new(Group_Input_005.outputs["Disable Back Style"], Mix_006.inputs["Factor"])
        nt.links.new(Group_Input_005.outputs["Shading"], Mix_006.inputs["B"])