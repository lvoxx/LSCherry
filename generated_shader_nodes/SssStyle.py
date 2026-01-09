import bpy
from ..utils import ShaderNode


class ShaderNodeSssStyle(ShaderNode):
    bl_label = "SSS Style"
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
        Shading_socket.min_value = -1.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"
            SSS_Style_socket = nt.interface.new_socket(
                name="SSS Style",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        SSS_Style_socket.default_value = (0.0, 0.0, 0.0)
        SSS_Style_socket.subtype = "XYZ"

        # Input sockets
            Disable_SSS_Style_socket = nt.interface.new_socket(
                name="Disable SSS Style",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Disable_SSS_Style_socket.default_value = False
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = -1.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"
            Toon_Style_(If_only_using_Toon_Style)_socket = nt.interface.new_socket(
                name="Toon Style (If only using Toon Style)",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Toon_Style_(If_only_using_Toon_Style)_socket.default_value = (0.0, 0.0, 0.0)
        Toon_Style_(If_only_using_Toon_Style)_socket.subtype = "XYZ"
            SSS_Style_socket = nt.interface.new_socket(
                name="SSS Style",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        SSS_Style_socket.default_value = (0.0, 0.0, 0.0)
        SSS_Style_socket.subtype = "XYZ"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 0.15000000596046448
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "FACTOR"
            SSS_Intensity_socket = nt.interface.new_socket(
                name="SSS Intensity",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        SSS_Intensity_socket.default_value = 5.0
        SSS_Intensity_socket.min_value = 0.0
        SSS_Intensity_socket.max_value = 15.0
        SSS_Intensity_socket.subtype = "FACTOR"

        # Create nodes
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (1238.00341796875, 67.6219711303711)
        Frame_007 = nt.nodes.new("NodeFrame")
        Frame_007.location = (-688.0994873046875, -163.498291015625)
        Frame_009 = nt.nodes.new("NodeFrame")
        Frame_009.location = (140.0347900390625, 877.7711791992188)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (760.5214233398438, 296.70355224609375)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (956.4403076171875, 238.19834899902344)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (956.4403076171875, 122.7415542602539)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (1284.5455322265625, 327.1082458496094)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (999.6919555664062, 304.1543273925781)
        Math_001.operation = "GREATER_THAN"
        Math_001.inputs["Value"].default_value = 0.10000000149011612
        Math_001.inputs["Value"].default_value = 0.5
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (1400.8521728515625, 458.9847412109375)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1188.1192626953125, 283.9954528808594)
        Mix_002.data_type = "FLOAT"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (1662.4051513671875, 291.8478088378906)
        Mix_003.data_type = "FLOAT"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (509.2532958984375, 244.51991271972656)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (1611.4578857421875, 174.94662475585938)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (619.2569580078125, 74.0623779296875)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (1582.530029296875, 74.0623779296875)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (1900.7923583984375, 412.13568115234375)
        Math_002.operation = "MULTIPLY"
        Math_002.inputs["Value"].default_value = 0.5
        Reroute_031 = nt.nodes.new("NodeReroute")
        Reroute_031.location = (252.05218505859375, 50.98263931274414)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (2740.99853515625, 200.47607421875)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (1611.4578857421875, 879.4537353515625)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (619.2569580078125, -85.91157531738281)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (570.0657958984375, 362.00244140625)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (509.2532958984375, 879.4537353515625)
        Reroute_032 = nt.nodes.new("NodeReroute")
        Reroute_032.location = (252.05218505859375, 264.3453674316406)
        Reroute_033 = nt.nodes.new("NodeReroute")
        Reroute_033.location = (215.50836181640625, 651.8941040039062)
        Reroute_034 = nt.nodes.new("NodeReroute")
        Reroute_034.location = (215.50836181640625, 27.916229248046875)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (1412.3397216796875, 159.64431762695312)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (201.7791748046875, -114.72412109375)
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (4.858154296875, -144.12692260742188)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (-62.09632110595703, -85.91157531738281)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (-26.080875396728516, 222.7157440185547)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-9.130905151367188, 65.3867416381836)
        Group_002 = nt.nodes.new("ShaderNodeGroup")
        Group_002.location = (308.06121826171875, 353.60882568359375)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (674.46728515625, 938.2427978515625)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (629.43798828125, 690.698486328125)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (674.46728515625, 733.836181640625)
        Separate_XYZ = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ.location = (428.36224365234375, 592.2326049804688)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (660.0187377929688, 555.3638916015625)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (626.003173828125, 534.9234619140625)
        Group_017 = nt.nodes.new("ShaderNodeGroup")
        Group_017.location = (46.729736328125, -19.95025634765625)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-208.1873779296875, 1078.2200927734375)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-208.1873779296875, 911.917236328125)
        Math_003.operation = "GREATER_THAN"
        Math_003.inputs["Value"].default_value = 0.0
        Math_003.inputs["Value"].default_value = 0.5
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (-36.7691650390625, 938.2427978515625)
        Separate_XYZ_001 = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ_001.location = (-207.4635009765625, 737.2314453125)
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (-22.391357421875, 846.4981079101562)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (-404.0948486328125, 965.1768798828125)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-600.830078125, 632.415283203125)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (-370.2911376953125, 598.7947998046875)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (-370.2911376953125, 798.3321533203125)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (-404.0948486328125, 490.6129455566406)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-404.0948486328125, 576.2481689453125)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (308.06121826171875, 140.9680633544922)
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (428.22021484375, 869.1403198242188)
        Math_004.operation = "SUBTRACT"
        Math_004.inputs["Value"].default_value = 0.10000000149011612
        Math_004.inputs["Value"].default_value = 0.5
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (629.44873046875, 833.9447021484375)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (718.3782958984375, 850.16357421875)
        Mix_004.data_type = "FLOAT"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.8999999761581421
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-879.8428955078125, 1067.5665283203125)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (2253.012939453125, 184.26473999023438)
        Mix_005.data_type = "VECTOR"
        Mix_005.blend_type = "MIX"
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_005.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (2093.28125, 879.4537353515625)
        Reroute_024 = nt.nodes.new("NodeReroute")
        Reroute_024.location = (2093.28125, 48.293128967285156)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (1919.03759765625, -55.01121139526367)
        Mix_006 = nt.nodes.new("ShaderNodeMix")
        Mix_006.location = (2212.6728515625, 409.2442321777344)
        Mix_006.data_type = "FLOAT"
        Mix_006.blend_type = "MIX"
        Mix_006.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_006.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (2212.36767578125, 486.1951904296875)
        # Create links
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Mix_001.inputs["Factor"])
        nt.links.new(Reroute_012.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Group_Input.outputs["Shading"], Reroute_031.inputs["Input"])
        nt.links.new(Reroute_031.outputs["Output"], Reroute_032.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Mix_001.outputs["Result"], Invert_Color.inputs["Color"])
        nt.links.new(Reroute_003.outputs["Output"], Math_001.inputs["Value"])
        nt.links.new(Invert_Color.outputs["Color"], Reroute_003.inputs["Input"])
        nt.links.new(Math_001.outputs["Value"], Mix_002.inputs["Factor"])
        nt.links.new(Reroute_003.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Mix_002.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Reroute_005.inputs["Input"])
        nt.links.new(Mix_002.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Reroute_005.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Mix.outputs["Result"], Math_002.inputs["Value"])
        nt.links.new(Group_Input_003.outputs["SSS Intensity"], Mix_003.inputs["A"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_007.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Mix_003.inputs["Factor"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Mix_003.inputs["B"])
        nt.links.new(Mix_006.outputs["Result"], Group_Output.inputs["Shading"])
        nt.links.new(Group_Input.outputs["Smooth"], Group_001.inputs["Smooth"])
        nt.links.new(Reroute_031.outputs["Output"], Group_001.inputs["Shading"])
        nt.links.new(Group_001.outputs["Shading"], Mix_001.inputs["A"])
        nt.links.new(Reroute_032.outputs["Output"], Group_002.inputs["Shading"])
        nt.links.new(Group_002.outputs["Shading"], Mix_001.inputs["B"])
        nt.links.new(Mix_003.outputs["Result"], Math_002.inputs["Value"])
        nt.links.new(Mix_005.outputs["Result"], Group_Output.inputs["SSS Style"])
        nt.links.new(Separate_XYZ_001.outputs["X"], Group_012.inputs["Compressed"])
        nt.links.new(Group_012.outputs["Compressed"], Group_017.inputs["Compressed"])
        nt.links.new(Math_004.outputs["Value"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Mix_004.inputs["Factor"])
        nt.links.new(Reroute_020.outputs["Output"], Mix_004.inputs["B"])
        nt.links.new(Mix_004.outputs["Result"], Reroute_033.inputs["Input"])
        nt.links.new(Reroute_033.outputs["Output"], Reroute_034.inputs["Input"])
        nt.links.new(Reroute_034.outputs["Output"], Group_001.inputs["Size"])
        nt.links.new(Reroute_034.outputs["Output"], Group_002.inputs["Size"])
        nt.links.new(Math.outputs["Value"], Reroute_001.inputs["Input"])
        nt.links.new(Math_003.outputs["Value"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Group_Input_002.outputs["Smooth"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input_002.outputs["SSS Intensity"], Combine_XYZ.inputs["Y"])
        nt.links.new(Separate_XYZ.outputs["Y"], Reroute_015.inputs["Input"])
        nt.links.new(Separate_XYZ.outputs["X"], Reroute_012.inputs["Input"])
        nt.links.new(Group_Input_001.outputs["SSS Style"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Separate_XYZ.inputs["Vector"])
        nt.links.new(Reroute.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Reroute_014.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Group_Input_001.outputs["Toon Style (If only using Toon Style)"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_022.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_023.outputs["Output"], Math_003.inputs["Value"])
        nt.links.new(Reroute_022.outputs["Output"], Separate_XYZ_001.inputs["Vector"])
        nt.links.new(Reroute_011.outputs["Output"], Group_002.inputs["Smooth"])
        nt.links.new(Group_017.outputs["Extracted"], Math_004.inputs["Value"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mix_005.inputs["A"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Reroute_024.inputs["Input"])
        nt.links.new(Reroute_024.outputs["Output"], Mix_005.inputs["Factor"])
        nt.links.new(Group_Input_004.outputs["SSS Style"], Mix_005.inputs["B"])
        nt.links.new(Math_002.outputs["Value"], Mix_006.inputs["A"])
        nt.links.new(Group_Input_005.outputs["Shading"], Mix_006.inputs["B"])
        nt.links.new(Group_Input_005.outputs["Disable SSS Style"], Mix_006.inputs["Factor"])