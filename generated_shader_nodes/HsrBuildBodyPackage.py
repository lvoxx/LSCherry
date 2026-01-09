import bpy
from ..utils import ShaderNode


class ShaderNodeHsrBuildBodyPackage(ShaderNode):
    bl_label = "HSR: Build Body Package"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            Shadow_Color_socket = nt.interface.new_socket(
                name="Shadow Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Shadow_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            SSS_Color_socket = nt.interface.new_socket(
                name="SSS Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        SSS_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            Body_Alpha_socket = nt.interface.new_socket(
                name="Body Alpha",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Body_Alpha_socket.default_value = 0.0
        Body_Alpha_socket.min_value = -3.4028234663852886e+38
        Body_Alpha_socket.max_value = 3.4028234663852886e+38
        Body_Alpha_socket.subtype = "NONE"
            Enable_Custom_Ramp_socket = nt.interface.new_socket(
                name="Enable Custom Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Enable_Custom_Ramp_socket.default_value = 0.0
        Enable_Custom_Ramp_socket.min_value = -3.4028234663852886e+38
        Enable_Custom_Ramp_socket.max_value = 3.4028234663852886e+38
        Enable_Custom_Ramp_socket.subtype = "NONE"
            Custom_Ramp_socket = nt.interface.new_socket(
                name="Custom Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Custom_Ramp_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Metal_Mask_socket = nt.interface.new_socket(
                name="Metal Mask",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metal_Mask_socket.default_value = 0.0
        Metal_Mask_socket.min_value = -3.4028234663852886e+38
        Metal_Mask_socket.max_value = 3.4028234663852886e+38
        Metal_Mask_socket.subtype = "NONE"
            Shadow_Mask_socket = nt.interface.new_socket(
                name="Shadow Mask",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Mask_socket.default_value = 0.0
        Shadow_Mask_socket.min_value = -3.4028234663852886e+38
        Shadow_Mask_socket.max_value = 3.4028234663852886e+38
        Shadow_Mask_socket.subtype = "NONE"

        # Input sockets
            Body_Texture_socket = nt.interface.new_socket(
                name="Body Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Body_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Body_Alpha_socket = nt.interface.new_socket(
                name="Body Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Body_Alpha_socket.default_value = 0.0
        Body_Alpha_socket.min_value = -3.4028234663852886e+38
        Body_Alpha_socket.max_value = 3.4028234663852886e+38
        Body_Alpha_socket.subtype = "NONE"
            Lightmap_Texture_socket = nt.interface.new_socket(
                name="Lightmap Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Lighmap__Alpha_Texture_socket = nt.interface.new_socket(
                name="Lighmap  Alpha Texture",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Lighmap__Alpha_Texture_socket.default_value = 0.0
        Lighmap__Alpha_Texture_socket.min_value = 0.0
        Lighmap__Alpha_Texture_socket.max_value = 1.0
        Lighmap__Alpha_Texture_socket.subtype = "NONE"
            --_Fake_Shadow_--_socket = nt.interface.new_socket(
                name="-- Fake Shadow --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Fac_socket = nt.interface.new_socket(
                name="Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fac_socket.default_value = 0.0
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Map_1_socket = nt.interface.new_socket(
                name="Map 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_1_socket.default_value = (0.8518279790878296, 0.8518394231796265, 0.8518364429473877, 1.0)
            Map_2_socket = nt.interface.new_socket(
                name="Map 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_2_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
            Map_3_socket = nt.interface.new_socket(
                name="Map 3",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_3_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
            Map_4_socket = nt.interface.new_socket(
                name="Map 4",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_4_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
            Map_5_socket = nt.interface.new_socket(
                name="Map 5",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_5_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
            Range_1_socket = nt.interface.new_socket(
                name="Range 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_1_socket.default_value = 0.10000000149011612
        Range_1_socket.min_value = 0.0
        Range_1_socket.max_value = 1.0
        Range_1_socket.subtype = "FACTOR"
            Range_2_socket = nt.interface.new_socket(
                name="Range 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_2_socket.default_value = 0.30000001192092896
        Range_2_socket.min_value = 0.0
        Range_2_socket.max_value = 1.0
        Range_2_socket.subtype = "FACTOR"
            Range_3_socket = nt.interface.new_socket(
                name="Range 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_3_socket.default_value = 0.44999998807907104
        Range_3_socket.min_value = 0.0
        Range_3_socket.max_value = 1.0
        Range_3_socket.subtype = "FACTOR"
            Range_4_socket = nt.interface.new_socket(
                name="Range 4",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_4_socket.default_value = 0.6200000047683716
        Range_4_socket.min_value = 0.0
        Range_4_socket.max_value = 1.0
        Range_4_socket.subtype = "FACTOR"
            ---_Shadow_---_socket = nt.interface.new_socket(
                name="--- Shadow ---",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Map_1_socket = nt.interface.new_socket(
                name="Map 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_1_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_2_socket = nt.interface.new_socket(
                name="Map 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_2_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_3_socket = nt.interface.new_socket(
                name="Map 3",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_3_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_4_socket = nt.interface.new_socket(
                name="Map 4",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_4_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_5_socket = nt.interface.new_socket(
                name="Map 5",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_5_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Range_1_socket = nt.interface.new_socket(
                name="Range 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_1_socket.default_value = 0.10000000149011612
        Range_1_socket.min_value = 0.0
        Range_1_socket.max_value = 1.0
        Range_1_socket.subtype = "FACTOR"
            Range_2_socket = nt.interface.new_socket(
                name="Range 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_2_socket.default_value = 0.30000001192092896
        Range_2_socket.min_value = 0.0
        Range_2_socket.max_value = 1.0
        Range_2_socket.subtype = "FACTOR"
            Range_3_socket = nt.interface.new_socket(
                name="Range 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_3_socket.default_value = 0.44999998807907104
        Range_3_socket.min_value = 0.0
        Range_3_socket.max_value = 1.0
        Range_3_socket.subtype = "FACTOR"
            Range_4_socket = nt.interface.new_socket(
                name="Range 4",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_4_socket.default_value = 0.6200000047683716
        Range_4_socket.min_value = 0.0
        Range_4_socket.max_value = 1.0
        Range_4_socket.subtype = "FACTOR"
            ---_SSS_---_socket = nt.interface.new_socket(
                name="--- SSS ---",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Map_1_socket = nt.interface.new_socket(
                name="Map 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_1_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_2_socket = nt.interface.new_socket(
                name="Map 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_2_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_3_socket = nt.interface.new_socket(
                name="Map 3",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_3_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_4_socket = nt.interface.new_socket(
                name="Map 4",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_4_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_5_socket = nt.interface.new_socket(
                name="Map 5",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_5_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Range_1_socket = nt.interface.new_socket(
                name="Range 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_1_socket.default_value = 0.10000000149011612
        Range_1_socket.min_value = 0.0
        Range_1_socket.max_value = 1.0
        Range_1_socket.subtype = "FACTOR"
            Range_2_socket = nt.interface.new_socket(
                name="Range 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_2_socket.default_value = 0.30000001192092896
        Range_2_socket.min_value = 0.0
        Range_2_socket.max_value = 1.0
        Range_2_socket.subtype = "FACTOR"
            Range_3_socket = nt.interface.new_socket(
                name="Range 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_3_socket.default_value = 0.44999998807907104
        Range_3_socket.min_value = 0.0
        Range_3_socket.max_value = 1.0
        Range_3_socket.subtype = "FACTOR"
            Range_4_socket = nt.interface.new_socket(
                name="Range 4",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_4_socket.default_value = 0.6200000047683716
        Range_4_socket.min_value = 0.0
        Range_4_socket.max_value = 1.0
        Range_4_socket.subtype = "FACTOR"

        # Create nodes
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (469.66668701171875, 54.39471435546875)
        Group_009.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (1187.905029296875, 794.9137573242188)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (784.7681884765625, -75.69245147705078)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (786.8346557617188, -52.32594299316406)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (1187.905029296875, -29.346439361572266)
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (964.995361328125, -110.56251525878906)
        Group_014.inputs["Mix 1"].default_value = 0.5800000429153442
        Group_014.inputs["Mix 2"].default_value = 0.800000011920929
        Group_014.inputs["Mix 3"].default_value = 0.949999988079071
        Group_014.inputs["Lv 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_014.inputs["Lv 2"].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        Group_014.inputs["Lv 3"].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        Group_014.inputs["Lv 4"].default_value = (1.0, 1.0, 1.0, 1.0)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (1205.2579345703125, -118.61495971679688)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (-153.73291015625, -594.967529296875)
        Reroute_024 = nt.nodes.new("NodeReroute")
        Reroute_024.location = (1205.2579345703125, -653.2064819335938)
        Reroute_025 = nt.nodes.new("NodeReroute")
        Reroute_025.location = (1205.2579345703125, -161.94097900390625)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (1167.956787109375, -631.6388549804688)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (1167.956787109375, -184.88821411132812)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (447.07623291015625, 705.8348388671875)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (469.66668701171875, -265.8857421875)
        Group_011.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (219.76475524902344, -450.00592041015625)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (884.257080078125, 27.014625549316406)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (219.76475524902344, -145.8258819580078)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1256.731689453125, 3.594024658203125)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-351.971435546875, -689.62158203125)
        Group_Input_006 = nt.nodes.new("NodeGroupInput")
        Group_Input_006.location = (-122.02725982666016, 20.770904541015625)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (469.66668701171875, 378.1245422363281)
        Group_010.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Input_007 = nt.nodes.new("NodeGroupInput")
        Group_Input_007.location = (219.76475524902344, 180.7880096435547)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (829.9855346679688, 641.1907348632812)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (992.2984008789062, 830.6312255859375)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_027 = nt.nodes.new("NodeReroute")
        Reroute_027.location = (738.54150390625, -631.6388549804688)
        Reroute_028 = nt.nodes.new("NodeReroute")
        Reroute_028.location = (738.54150390625, 480.8481750488281)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (165.00869750976562, 532.0931396484375)
        # Create links
        nt.links.new(Group_Input_003.outputs["Map 1"], Group_009.inputs["Map 1"])
        nt.links.new(Group_Input_003.outputs["Map 2"], Group_009.inputs["Map 2"])
        nt.links.new(Group_Input_003.outputs["Map 3"], Group_009.inputs["Map 3"])
        nt.links.new(Group_Input_003.outputs["Map 4"], Group_009.inputs["Map 4"])
        nt.links.new(Group_Input_003.outputs["Range 1"], Group_009.inputs["Range 1"])
        nt.links.new(Group_Input_003.outputs["Range 2"], Group_009.inputs["Range 2"])
        nt.links.new(Group_Input_003.outputs["Range 3"], Group_009.inputs["Range 3"])
        nt.links.new(Reroute_019.outputs["Output"], Group_Output.inputs["SSS Color"])
        nt.links.new(Group_Input_004.outputs["Map 1"], Group_011.inputs["Map 1"])
        nt.links.new(Group_Input_004.outputs["Map 2"], Group_011.inputs["Map 2"])
        nt.links.new(Group_Input_004.outputs["Map 3"], Group_011.inputs["Map 3"])
        nt.links.new(Group_Input_004.outputs["Map 4"], Group_011.inputs["Map 4"])
        nt.links.new(Group_Input_004.outputs["Range 1"], Group_011.inputs["Range 1"])
        nt.links.new(Group_Input_004.outputs["Range 2"], Group_011.inputs["Range 2"])
        nt.links.new(Group_Input_004.outputs["Range 3"], Group_011.inputs["Range 3"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Group_Output.inputs["Base Color"])
        nt.links.new(Reroute_018.outputs["Output"], Group_Output.inputs["Shadow Color"])
        nt.links.new(Group_011.outputs["Color Map"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Group_Output.inputs["Enable Custom Ramp"])
        nt.links.new(Reroute_024.outputs["Output"], Reroute_025.inputs["Input"])
        nt.links.new(Reroute_025.outputs["Output"], Group_Output.inputs["Metal Mask"])
        nt.links.new(Reroute_023.outputs["Output"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Group_Output.inputs["Shadow Mask"])
        nt.links.new(Group_Input_004.outputs["Map 5"], Group_011.inputs["Map 5"])
        nt.links.new(Group_Input_004.outputs["Range 4"], Group_011.inputs["Range 4"])
        nt.links.new(Group_Input_003.outputs["Map 5"], Group_009.inputs["Map 5"])
        nt.links.new(Group_Input_003.outputs["Range 4"], Group_009.inputs["Range 4"])
        nt.links.new(Mix_001.outputs["Result"], Reroute_015.inputs["Input"])
        nt.links.new(Group_014.outputs["Custom Ramp"], Group_Output.inputs["Custom Ramp"])
        nt.links.new(Group_Input_002.outputs["Lightmap Texture"], Group_013.inputs["Lightmap"])
        nt.links.new(Group_Input_006.outputs["Lighmap  Alpha Texture"], Group_009.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input_006.outputs["Lighmap  Alpha Texture"], Group_011.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input_007.outputs["Map 1"], Group_010.inputs["Map 1"])
        nt.links.new(Group_Input_007.outputs["Map 2"], Group_010.inputs["Map 2"])
        nt.links.new(Group_Input_007.outputs["Map 3"], Group_010.inputs["Map 3"])
        nt.links.new(Group_Input_007.outputs["Map 4"], Group_010.inputs["Map 4"])
        nt.links.new(Group_Input_007.outputs["Map 5"], Group_010.inputs["Map 5"])
        nt.links.new(Group_Input_006.outputs["Lighmap  Alpha Texture"], Group_010.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input_007.outputs["Range 1"], Group_010.inputs["Range 1"])
        nt.links.new(Group_Input_007.outputs["Range 2"], Group_010.inputs["Range 2"])
        nt.links.new(Group_Input_007.outputs["Range 3"], Group_010.inputs["Range 3"])
        nt.links.new(Group_Input_007.outputs["Range 4"], Group_010.inputs["Range 4"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Body Texture"], Mix_001.inputs["A"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input_005.outputs["Body Alpha"], Group_Output.inputs["Body Alpha"])
        nt.links.new(Group_010.outputs["Color Map"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Body Texture"], Mix.inputs["A"])
        nt.links.new(Reroute_027.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_025.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Group_013.outputs["Metal"], Reroute_024.inputs["Input"])
        nt.links.new(Group_009.outputs["Color Map"], Reroute_018.inputs["Input"])
        nt.links.new(Group_013.outputs["Shadow"], Reroute_027.inputs["Input"])
        nt.links.new(Reroute_027.outputs["Output"], Reroute_028.inputs["Input"])
        nt.links.new(Reroute_028.outputs["Output"], Mix.inputs["Factor"])