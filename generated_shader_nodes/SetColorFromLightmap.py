import bpy
from ..utils import ShaderNode


class ShaderNodeSetColorFromLightmap(ShaderNode):
    bl_label = "Set Color From LightMap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Color_Map_socket = nt.interface.new_socket(
                name="Color Map",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_Map_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Lighmap_Alpha_socket = nt.interface.new_socket(
                name="Lighmap Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Lighmap_Alpha_socket.default_value = 0.0
        Lighmap_Alpha_socket.min_value = 0.0
        Lighmap_Alpha_socket.max_value = 1.0
        Lighmap_Alpha_socket.subtype = "NONE"
            Map_0_socket = nt.interface.new_socket(
                name="Map 0",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_0_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_1_socket = nt.interface.new_socket(
                name="Map 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_1_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            Map_2_socket = nt.interface.new_socket(
                name="Map 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_2_socket.default_value = (0.5, 0.5, 0.5, 1.0)
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
        
        Range_1_socket.default_value = 0.125
        Range_1_socket.min_value = 0.0
        Range_1_socket.max_value = 1.0
        Range_1_socket.subtype = "FACTOR"
            Range_2_socket = nt.interface.new_socket(
                name="Range 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_2_socket.default_value = 0.25
        Range_2_socket.min_value = 0.0
        Range_2_socket.max_value = 1.0
        Range_2_socket.subtype = "FACTOR"
            Range_3_socket = nt.interface.new_socket(
                name="Range 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_3_socket.default_value = 0.375
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
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (30.667633056640625, -667.5250244140625)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (299.2472229003906, -667.5250244140625)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (543.0482177734375, -667.5250244140625)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (770.0927124023438, -667.5250244140625)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (1094.8883056640625, -667.5250244140625)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (-199.6328887939453, -298.7019348144531)
        Frame_007 = nt.nodes.new("NodeFrame")
        Frame_007.location = (-293.37939453125, 607.97216796875)
        Frame_006 = nt.nodes.new("NodeFrame")
        Frame_006.location = (-288.67315673828125, 11.44439697265625)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (-242.65359497070312, 285.47021484375)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (-495.1866149902344, -717.140625)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (-505.9344177246094, -737.4423828125)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (86.0718994140625, -49.6156005859375)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (-520.2648315429688, -760.7019653320312)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (92.6072998046875, -69.9173583984375)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (-534.59521484375, -784.58642578125)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (-552.5081787109375, -805.5131225585938)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (88.6785888671875, -93.17694091796875)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-495.1866149902344, -191.36065673828125)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (-505.9344177246094, -211.66244506835938)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (-520.2648315429688, -233.15846252441406)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (-534.59521484375, -257.04290771484375)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (855.5302124023438, 312.8330078125)
        Reroute_024 = nt.nodes.new("NodeReroute")
        Reroute_024.location = (85.4375, -117.0614013671875)
        Reroute_028 = nt.nodes.new("NodeReroute")
        Reroute_028.location = (832.6552124023438, 334.69036865234375)
        Reroute_045 = nt.nodes.new("NodeReroute")
        Reroute_045.location = (737.8606567382812, 361.5754699707031)
        Reroute_027 = nt.nodes.new("NodeReroute")
        Reroute_027.location = (832.6552124023438, 188.00936889648438)
        Reroute_047 = nt.nodes.new("NodeReroute")
        Reroute_047.location = (514.1026000976562, 60.175350189208984)
        Reroute_041 = nt.nodes.new("NodeReroute")
        Reroute_041.location = (610.5150146484375, 36.48591232299805)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (631.726806640625, 14.40898609161377)
        Reroute_044 = nt.nodes.new("NodeReroute")
        Reroute_044.location = (738.1204223632812, 430.5069885253906)
        Reroute_046 = nt.nodes.new("NodeReroute")
        Reroute_046.location = (514.1026000976562, 116.64396667480469)
        Reroute_048 = nt.nodes.new("NodeReroute")
        Reroute_048.location = (313.4267578125, -155.08016967773438)
        Reroute_040 = nt.nodes.new("NodeReroute")
        Reroute_040.location = (610.5150146484375, -96.34208679199219)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (391.8545227050781, -271.4598388671875)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (359.75311279296875, -249.5117645263672)
        Reroute_049 = nt.nodes.new("NodeReroute")
        Reroute_049.location = (313.4267578125, -225.42100524902344)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (359.75311279296875, -333.16766357421875)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (116.73953247070312, -504.5400085449219)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (438.9729919433594, -62.5921630859375)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-361.1925048828125, -251.5056610107422)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (906.6698608398438, 522.9893188476562)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (-552.5081787109375, -279.733154296875)
        Reroute_025 = nt.nodes.new("NodeReroute")
        Reroute_025.location = (102.971435546875, -137.98809814453125)
        Reroute_029 = nt.nodes.new("NodeReroute")
        Reroute_029.location = (1197.8597412109375, 520.4842529296875)
        Reroute_031 = nt.nodes.new("NodeReroute")
        Reroute_031.location = (1152.9039306640625, 542.9382934570312)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (1242.59228515625, 729.4307250976562)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_030 = nt.nodes.new("NodeReroute")
        Reroute_030.location = (1152.9039306640625, 486.0926513671875)
        Reroute_043 = nt.nodes.new("NodeReroute")
        Reroute_043.location = (1079.2274169921875, 567.0616455078125)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (180.7213134765625, -296.008544921875)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1429.9124755859375, 725.6527709960938)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (661.3955078125, 222.58270263671875)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_002 = nt.nodes.new("ShaderNodeGroup")
        Group_002.location = (25.710861206054688, -89.328369140625)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (133.28594970703125, -162.08978271484375)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-361.1925048828125, -168.4062042236328)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (84.99075317382812, -125.42955017089844)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (-165.55682373046875, 681.7037963867188)
        Reroute_033 = nt.nodes.new("NodeReroute")
        Reroute_033.location = (-286.8544921875, -208.77713012695312)
        Reroute_034 = nt.nodes.new("NodeReroute")
        Reroute_034.location = (-286.8544921875, -500.4668884277344)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-361.1925048828125, -475.3236389160156)
        Reroute_036 = nt.nodes.new("NodeReroute")
        Reroute_036.location = (-322.4431457519531, -229.9558868408203)
        Reroute_037 = nt.nodes.new("NodeReroute")
        Reroute_037.location = (-322.4431457519531, 70.39837646484375)
        Reroute_032 = nt.nodes.new("NodeReroute")
        Reroute_032.location = (-286.8544921875, -300.2310485839844)
        Reroute_035 = nt.nodes.new("NodeReroute")
        Reroute_035.location = (-322.4431457519531, -324.2978820800781)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-361.1925048828125, 23.253538131713867)
        Reroute_039 = nt.nodes.new("NodeReroute")
        Reroute_039.location = (-391.4541931152344, 44.2531623840332)
        Reroute_050 = nt.nodes.new("NodeReroute")
        Reroute_050.location = (-391.4541931152344, 355.63629150390625)
        Reroute_038 = nt.nodes.new("NodeReroute")
        Reroute_038.location = (-391.4541931152344, -346.1920166015625)
        Reroute_051 = nt.nodes.new("NodeReroute")
        Reroute_051.location = (-434.6198425292969, -367.7909240722656)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (-361.1925048828125, 594.4157104492188)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-361.1925048828125, 311.29632568359375)
        Reroute_052 = nt.nodes.new("NodeReroute")
        Reroute_052.location = (-434.6198425292969, 336.6661071777344)
        Reroute_053 = nt.nodes.new("NodeReroute")
        Reroute_053.location = (-434.6198425292969, 570.7300415039062)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (125.93382263183594, -129.94737243652344)
        Reroute_042 = nt.nodes.new("NodeReroute")
        Reroute_042.location = (1079.2274169921875, 627.8395385742188)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-173.1974334716797, -557.7557983398438)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-791.37451171875, -135.48171997070312)
        Frame_009 = nt.nodes.new("NodeFrame")
        Frame_009.location = (-872.7659912109375, 26.563953399658203)
        # Create links
        nt.links.new(Group_Input.outputs["Lighmap Alpha"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Group_Input.outputs["Map 1"], Reroute_006.inputs["Input"])
        nt.links.new(Group_Input.outputs["Map 2"], Reroute_007.inputs["Input"])
        nt.links.new(Group_Input.outputs["Map 3"], Reroute_008.inputs["Input"])
        nt.links.new(Group_Input.outputs["Map 4"], Reroute_009.inputs["Input"])
        nt.links.new(Group_Input.outputs["Map 5"], Reroute_010.inputs["Input"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Color Map"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Mix_004.inputs["B"])
        nt.links.new(Reroute_012.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Mix_003.inputs["B"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Mix_002.inputs["B"])
        nt.links.new(Mix_004.outputs["Result"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_022.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_023.outputs["Output"], Mix_003.inputs["A"])
        nt.links.new(Reroute_014.outputs["Output"], Reroute_024.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_025.inputs["Input"])
        nt.links.new(Reroute_024.outputs["Output"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Mix_001.inputs["B"])
        nt.links.new(Mix_002.outputs["Result"], Reroute_027.inputs["Input"])
        nt.links.new(Reroute_027.outputs["Output"], Reroute_028.inputs["Input"])
        nt.links.new(Reroute_028.outputs["Output"], Mix_001.inputs["A"])
        nt.links.new(Reroute_025.outputs["Output"], Reroute_029.inputs["Input"])
        nt.links.new(Reroute_029.outputs["Output"], Mix.inputs["B"])
        nt.links.new(Reroute_030.outputs["Output"], Reroute_031.inputs["Input"])
        nt.links.new(Reroute_031.outputs["Output"], Mix.inputs["A"])
        nt.links.new(Mix_003.outputs["Result"], Reroute_040.inputs["Input"])
        nt.links.new(Reroute_040.outputs["Output"], Reroute_041.inputs["Input"])
        nt.links.new(Reroute_041.outputs["Output"], Mix_002.inputs["A"])
        nt.links.new(Reroute_042.outputs["Output"], Reroute_043.inputs["Input"])
        nt.links.new(Reroute_043.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Reroute_044.outputs["Output"], Reroute_045.inputs["Input"])
        nt.links.new(Reroute_045.outputs["Output"], Mix_001.inputs["Factor"])
        nt.links.new(Reroute_046.outputs["Output"], Reroute_047.inputs["Input"])
        nt.links.new(Reroute_047.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Reroute_048.outputs["Output"], Reroute_049.inputs["Input"])
        nt.links.new(Reroute_049.outputs["Output"], Mix_003.inputs["Factor"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Mix_001.outputs["Result"], Reroute_030.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Group_002.inputs["A"])
        nt.links.new(Group_002.outputs["Boolean"], Mix_004.inputs["Factor"])
        nt.links.new(Reroute_003.outputs["Output"], Group_003.inputs["A"])
        nt.links.new(Group_003.outputs["Boolean"], Reroute_042.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Group.inputs["Input"])
        nt.links.new(Group.outputs["Boolean"], Reroute_044.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Group_001.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Group_004.inputs["Input"])
        nt.links.new(Group_004.outputs["Boolean"], Reroute_048.inputs["Input"])
        nt.links.new(Group_001.outputs["Boolean"], Reroute_046.inputs["Input"])
        nt.links.new(Group_Input.outputs["Range 1"], Reroute_032.inputs["Input"])
        nt.links.new(Reroute_032.outputs["Output"], Reroute_033.inputs["Input"])
        nt.links.new(Reroute_033.outputs["Output"], Group_004.inputs["A"])
        nt.links.new(Reroute_032.outputs["Output"], Reroute_034.inputs["Input"])
        nt.links.new(Reroute_034.outputs["Output"], Group_002.inputs["B"])
        nt.links.new(Group_Input.outputs["Range 2"], Reroute_035.inputs["Input"])
        nt.links.new(Reroute_035.outputs["Output"], Reroute_036.inputs["Input"])
        nt.links.new(Reroute_036.outputs["Output"], Group_004.inputs["B"])
        nt.links.new(Reroute_036.outputs["Output"], Reroute_037.inputs["Input"])
        nt.links.new(Reroute_037.outputs["Output"], Group_001.inputs["A"])
        nt.links.new(Group_Input.outputs["Range 3"], Reroute_038.inputs["Input"])
        nt.links.new(Reroute_038.outputs["Output"], Reroute_039.inputs["Input"])
        nt.links.new(Reroute_039.outputs["Output"], Group_001.inputs["B"])
        nt.links.new(Reroute_039.outputs["Output"], Reroute_050.inputs["Input"])
        nt.links.new(Reroute_050.outputs["Output"], Group.inputs["A"])
        nt.links.new(Group_Input.outputs["Range 4"], Reroute_051.inputs["Input"])
        nt.links.new(Reroute_051.outputs["Output"], Reroute_052.inputs["Input"])
        nt.links.new(Reroute_052.outputs["Output"], Group.inputs["B"])
        nt.links.new(Reroute_052.outputs["Output"], Reroute_053.inputs["Input"])
        nt.links.new(Reroute_053.outputs["Output"], Group_003.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Map 0"], Mix_004.inputs["A"])