import bpy
from ..utils import ShaderNode


class ShaderNodeHi3BuildBodyPackage(ShaderNode):
    bl_label = "HI3: Build Body Package"
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
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (29.35137939453125, 197.34471130371094)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-292.2634582519531, -122.03985595703125)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-292.2634582519531, 361.5968933105469)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (54.47758483886719, -122.03985595703125)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (29.35137939453125, 361.5968933105469)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (469.66668701171875, 286.6356506347656)
        Group_009.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (-163.25311279296875, 176.67845153808594)
        Group_012.inputs["Lighmap Alpha"].default_value = 0.0
        Group_012.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs["Range 1"].default_value = 0.10000000149011612
        Group_012.inputs["Range 2"].default_value = 0.30000001192092896
        Group_012.inputs["Range 3"].default_value = 0.44999998807907104
        Group_012.inputs["Range 4"].default_value = 0.6200000047683716
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (119.60452270507812, 337.15423583984375)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (119.60452270507812, 140.53842163085938)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-359.80499267578125, 385.0780334472656)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (749.6708374023438, 548.0823364257812)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (703.9854125976562, 459.8439025878906)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (786.8346557617188, 249.42929077148438)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (699.9108276367188, -69.5866470336914)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (786.8346557617188, -50.58142852783203)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (749.6708374023438, -95.37936401367188)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (703.9854125976562, -30.21869659423828)
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (243.6751708984375, -346.0987243652344)
        Group_014.inputs["Mix 1"].default_value = 0.5800000429153442
        Group_014.inputs["Mix 2"].default_value = 0.800000011920929
        Group_014.inputs["Mix 3"].default_value = 0.949999988079071
        Group_014.inputs["Lv 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_014.inputs["Lv 2"].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        Group_014.inputs["Lv 3"].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        Group_014.inputs["Lv 4"].default_value = (1.0, 1.0, 1.0, 1.0)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (915.252685546875, -383.3872375488281)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (915.252685546875, -141.6001434326172)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (851.361328125, -118.61495208740234)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (-183.88922119140625, -274.15557861328125)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (-359.80499267578125, -386.8644104003906)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-292.2634582519531, 88.91595458984375)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (80.90692901611328, 360.7911376953125)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (509.58935546875, 494.6773376464844)
        Group_008.inputs["Factor"].default_value = 0.0
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (80.90692901611328, -331.902587890625)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (851.361328125, -312.82415771484375)
        Reroute_024 = nt.nodes.new("NodeReroute")
        Reroute_024.location = (945.45361328125, -312.82415771484375)
        Reroute_025 = nt.nodes.new("NodeReroute")
        Reroute_025.location = (945.45361328125, -161.94097900390625)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (993.4732666015625, -331.902587890625)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (993.4732666015625, -184.88821411132812)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-543.9733276367188, 442.4372253417969)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (469.66668701171875, -33.64481735229492)
        Group_011.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (214.99557495117188, -96.81194305419922)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-584.1752319335938, 116.87246704101562)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (493.3109130859375, 586.2869873046875)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (232.54052734375, 504.83636474609375)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (207.02908325195312, 191.7263641357422)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1019.322021484375, 3.594024658203125)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-34.701202392578125, 656.6986083984375)
        # Create links
        nt.links.new(Group_Input.outputs["Body Texture"], Group_008.inputs["Original Color"])
        nt.links.new(Group_Input.outputs["Lighmap  Alpha Texture"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Group_009.inputs["Lighmap Alpha"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Group_011.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input.outputs["Lightmap Texture"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_007.inputs["Input"])
        nt.links.new(Group_013.outputs["Metal"], Reroute_008.inputs["Input"])
        nt.links.new(Group_013.outputs["Shadow"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Group_Input_003.outputs["Map 1"], Group_009.inputs["Map 1"])
        nt.links.new(Group_Input_003.outputs["Map 2"], Group_009.inputs["Map 2"])
        nt.links.new(Group_Input_003.outputs["Map 3"], Group_009.inputs["Map 3"])
        nt.links.new(Group_Input_003.outputs["Map 4"], Group_009.inputs["Map 4"])
        nt.links.new(Group_Input_003.outputs["Range 1"], Group_009.inputs["Range 1"])
        nt.links.new(Group_Input_003.outputs["Range 2"], Group_009.inputs["Range 2"])
        nt.links.new(Group_Input_003.outputs["Range 3"], Group_009.inputs["Range 3"])
        nt.links.new(Group_012.outputs["Color Map"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_012.outputs["Output"], Group_008.inputs["Shadow Color"])
        nt.links.new(Reroute_019.outputs["Output"], Group_Output.inputs["SSS Color"])
        nt.links.new(Group_Input_004.outputs["Map 1"], Group_011.inputs["Map 1"])
        nt.links.new(Group_Input_004.outputs["Map 2"], Group_011.inputs["Map 2"])
        nt.links.new(Group_Input_004.outputs["Map 3"], Group_011.inputs["Map 3"])
        nt.links.new(Group_Input_004.outputs["Map 4"], Group_011.inputs["Map 4"])
        nt.links.new(Group_Input_004.outputs["Range 1"], Group_011.inputs["Range 1"])
        nt.links.new(Group_Input_004.outputs["Range 2"], Group_011.inputs["Range 2"])
        nt.links.new(Group_Input_004.outputs["Range 3"], Group_011.inputs["Range 3"])
        nt.links.new(Group_Input_005.outputs["Body Alpha"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Reroute_014.outputs["Output"], Group_Output.inputs["Body Alpha"])
        nt.links.new(Group_008.outputs["Color"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Group_Output.inputs["Base Color"])
        nt.links.new(Group_009.outputs["Color Map"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Group_Output.inputs["Shadow Color"])
        nt.links.new(Group_011.outputs["Color Map"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Group_Output.inputs["Enable Custom Ramp"])
        nt.links.new(Group_014.outputs["Custom Ramp"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_022.outputs["Output"], Group_Output.inputs["Custom Ramp"])
        nt.links.new(Reroute_007.outputs["Output"], Group_013.inputs["Lightmap"])
        nt.links.new(Reroute_010.outputs["Output"], Group_008.inputs["Shadow Mask"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_024.inputs["Input"])
        nt.links.new(Reroute_024.outputs["Output"], Reroute_025.inputs["Input"])
        nt.links.new(Reroute_025.outputs["Output"], Group_Output.inputs["Metal Mask"])
        nt.links.new(Reroute_023.outputs["Output"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Group_Output.inputs["Shadow Mask"])
        nt.links.new(Group_Input_004.outputs["Map 5"], Group_011.inputs["Map 5"])
        nt.links.new(Group_Input_004.outputs["Range 4"], Group_011.inputs["Range 4"])
        nt.links.new(Group_Input_003.outputs["Map 5"], Group_009.inputs["Map 5"])
        nt.links.new(Group_Input_003.outputs["Range 4"], Group_009.inputs["Range 4"])