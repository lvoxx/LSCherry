import bpy
from ..utils import ShaderNode


class ShaderNodeColorSelector(ShaderNode):
    bl_label = "Color Selector"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Selected_Color_socket = nt.interface.new_socket(
                name="Selected Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Selected_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Case_Number_socket = nt.interface.new_socket(
                name="Case Number",
                in_out="INPUT",
                socket_type="NodeSocketInt"
            )
        
        Case_Number_socket.default_value = 1
        Case_Number_socket.min_value = 1
        Case_Number_socket.max_value = 10
        Case_Number_socket.subtype = "NONE"
            Color_1_socket = nt.interface.new_socket(
                name="Color 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_1_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_2_socket = nt.interface.new_socket(
                name="Color 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_2_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_3_socket = nt.interface.new_socket(
                name="Color 3",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_3_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_4_socket = nt.interface.new_socket(
                name="Color 4",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_4_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_5_socket = nt.interface.new_socket(
                name="Color 5",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_5_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_6_socket = nt.interface.new_socket(
                name="Color 6",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_6_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_7_socket = nt.interface.new_socket(
                name="Color 7",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_7_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_8_socket = nt.interface.new_socket(
                name="Color 8",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_8_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_9_socket = nt.interface.new_socket(
                name="Color 9",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_9_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_10_socket = nt.interface.new_socket(
                name="Color 10",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_10_socket.default_value = (0.0, 0.0, 0.0, 1.0)

        # Create nodes
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-481.2478942871094, -153.72579956054688)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (-743.9290771484375, -400.3948974609375)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (-1177.1661376953125, -829.6622924804688)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_006 = nt.nodes.new("ShaderNodeMix")
        Mix_006.location = (-1683.350341796875, -1194.5777587890625)
        Mix_006.data_type = "RGBA"
        Mix_006.blend_type = "MIX"
        Mix_006.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs["A"].default_value = 0.0
        Mix_006.inputs["B"].default_value = 0.0
        Mix_006.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (-952.0189208984375, -621.5968627929688)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (-1405.95263671875, -1012.6511840820312)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MIX"
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math_005 = nt.nodes.new("ShaderNodeMath")
        Math_005.location = (-1871.8441162109375, -975.42578125)
        Math_005.operation = "GREATER_THAN"
        Math_005.inputs["Value"].default_value = 6.099999904632568
        Math_005.inputs["Value"].default_value = 0.5
        Math_006 = nt.nodes.new("ShaderNodeMath")
        Math_006.location = (-2148.79443359375, -1110.295654296875)
        Math_006.operation = "GREATER_THAN"
        Math_006.inputs["Value"].default_value = 7.099999904632568
        Math_006.inputs["Value"].default_value = 0.5
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (-1674.364013671875, -812.9003295898438)
        Math_004.operation = "GREATER_THAN"
        Math_004.inputs["Value"].default_value = 5.099999904632568
        Math_004.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-1489.7413330078125, -655.294189453125)
        Math_003.operation = "GREATER_THAN"
        Math_003.inputs["Value"].default_value = 4.099999904632568
        Math_003.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-1346.8056640625, -449.7989807128906)
        Math_002.operation = "GREATER_THAN"
        Math_002.inputs["Value"].default_value = 3.0999999046325684
        Math_002.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-1209.071533203125, -264.5382385253906)
        Math_001.operation = "GREATER_THAN"
        Math_001.inputs["Value"].default_value = 2.0999999046325684
        Math_001.inputs["Value"].default_value = 0.5
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-1194.1641845703125, -35.95575714111328)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 1.100000023841858
        Math.inputs["Value"].default_value = 0.5
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-260.5355529785156, 144.94393920898438)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (277.49163818359375, 75.7210922241211)
        Math_007 = nt.nodes.new("ShaderNodeMath")
        Math_007.location = (-2465.22705078125, -1235.902099609375)
        Math_007.operation = "GREATER_THAN"
        Math_007.inputs["Value"].default_value = 8.100000381469727
        Math_007.inputs["Value"].default_value = 0.5
        Mix_007 = nt.nodes.new("ShaderNodeMix")
        Mix_007.location = (-1982.593017578125, -1387.9356689453125)
        Mix_007.data_type = "RGBA"
        Mix_007.blend_type = "MIX"
        Mix_007.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs["A"].default_value = 0.0
        Mix_007.inputs["B"].default_value = 0.0
        Mix_007.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-3322.276611328125, -1201.4033203125)
        Math_008 = nt.nodes.new("ShaderNodeMath")
        Math_008.location = (-2671.56005859375, -1450.7152099609375)
        Math_008.operation = "GREATER_THAN"
        Math_008.inputs["Value"].default_value = 9.100000381469727
        Math_008.inputs["Value"].default_value = 0.5
        Mix_008 = nt.nodes.new("ShaderNodeMix")
        Mix_008.location = (-2188.926025390625, -1602.748779296875)
        Mix_008.data_type = "RGBA"
        Mix_008.blend_type = "MIX"
        Mix_008.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_008.inputs["A"].default_value = 0.0
        Mix_008.inputs["B"].default_value = 0.0
        Mix_008.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math_009 = nt.nodes.new("ShaderNodeMath")
        Math_009.location = (-2922.989501953125, -1574.5716552734375)
        Math_009.operation = "GREATER_THAN"
        Math_009.inputs["Value"].default_value = 10.100000381469727
        Math_009.inputs["Value"].default_value = 0.5
        Mix_009 = nt.nodes.new("ShaderNodeMix")
        Mix_009.location = (-2433.908447265625, -1810.46630859375)
        Mix_009.data_type = "RGBA"
        Mix_009.blend_type = "MIX"
        Mix_009.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_009.inputs["A"].default_value = 0.0
        Mix_009.inputs["B"].default_value = 0.0
        Mix_009.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-3325.571044921875, -1028.12158203125)
        # Create links
        nt.links.new(Group_Input.outputs["Color 1"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Color 2"], Mix_001.inputs["A"])
        nt.links.new(Mix_001.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Color 3"], Mix_002.inputs["A"])
        nt.links.new(Mix_002.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Mix_003.outputs["Result"], Mix_002.inputs["B"])
        nt.links.new(Mix_004.outputs["Result"], Mix_003.inputs["B"])
        nt.links.new(Mix_005.outputs["Result"], Mix_004.inputs["B"])
        nt.links.new(Group_Input.outputs["Color 4"], Mix_003.inputs["A"])
        nt.links.new(Group_Input.outputs["Color 5"], Mix_004.inputs["A"])
        nt.links.new(Group_Input.outputs["Color 6"], Mix_005.inputs["A"])
        nt.links.new(Group_Input.outputs["Color 7"], Mix_006.inputs["A"])
        nt.links.new(Group_Input.outputs["Color 8"], Mix_007.inputs["A"])
        nt.links.new(Mix_007.outputs["Result"], Mix_006.inputs["B"])
        nt.links.new(Group_Input.outputs["Case Number"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_002.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Mix_002.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_003.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Mix_003.inputs["Factor"])
        nt.links.new(Mix_006.outputs["Result"], Mix_005.inputs["B"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_007.inputs["Value"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_006.inputs["Value"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_005.inputs["Value"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_004.inputs["Value"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Selected Color"])
        nt.links.new(Math_004.outputs["Value"], Mix_004.inputs["Factor"])
        nt.links.new(Math_005.outputs["Value"], Mix_005.inputs["Factor"])
        nt.links.new(Math_006.outputs["Value"], Mix_006.inputs["Factor"])
        nt.links.new(Math_007.outputs["Value"], Mix_007.inputs["Factor"])
        nt.links.new(Math_008.outputs["Value"], Mix_008.inputs["Factor"])
        nt.links.new(Mix_008.outputs["Result"], Mix_007.inputs["B"])
        nt.links.new(Group_Input.outputs["Color 9"], Mix_008.inputs["A"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_008.inputs["Value"])
        nt.links.new(Math_009.outputs["Value"], Mix_009.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Case Number"], Math_009.inputs["Value"])
        nt.links.new(Group_Input.outputs["Color 10"], Mix_009.inputs["A"])
        nt.links.new(Mix_009.outputs["Result"], Mix_008.inputs["B"])