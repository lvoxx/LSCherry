import bpy
from ..utils import ShaderNode


class ShaderNodeBlendLight(ShaderNode):
    bl_label = "Blend Light"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Blended_Color_socket = nt.interface.new_socket(
                name="Blended Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Blended_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 1.0
        Factor_socket.min_value = 0.0
        Factor_socket.max_value = 1.0
        Factor_socket.subtype = "FACTOR"
            Mix_Add_And_Blend_socket = nt.interface.new_socket(
                name="Mix Add And Blend",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_Add_And_Blend_socket.default_value = 0.0
        Mix_Add_And_Blend_socket.min_value = 0.0
        Mix_Add_And_Blend_socket.max_value = 1.0
        Mix_Add_And_Blend_socket.subtype = "FACTOR"
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Blend_Color_socket = nt.interface.new_socket(
                name="Blend Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Blend_Color_socket.default_value = (0.0, 0.0, 0.0, 1.0)

        # Create nodes
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-58.180564880371094, 417.8006286621094)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "ADD"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-668.17138671875, 476.02691650390625)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-668.17138671875, 59.636253356933594)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-892.2695922851562, 115.31524658203125)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-568.0955200195312, -25.37151336669922)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (738.197509765625, 476.02691650390625)
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (587.3651123046875, -43.149192810058594)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1027.32666015625, -40.394775390625)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (807.7364501953125, 180.3450927734375)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (738.197509765625, 28.1114501953125)
        Separate_Color_001 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color_001.location = (-568.0955200195312, -209.38037109375)
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (-184.5499725341797, -188.0381622314453)
        Math_004.operation = "ADD"
        Math_004.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-184.5499725341797, -17.24056625366211)
        Math_003.operation = "ADD"
        Math_003.inputs["Value"].default_value = 0.5
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-184.5499725341797, 150.09715270996094)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Math_005 = nt.nodes.new("ShaderNodeMath")
        Math_005.location = (51.67621612548828, -188.0381622314453)
        Math_005.operation = "DIVIDE"
        Math_005.inputs["Value"].default_value = 2.0
        Math_005.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (51.67621612548828, -17.24056625366211)
        Math_002.operation = "DIVIDE"
        Math_002.inputs["Value"].default_value = 2.0
        Math_002.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (51.67621612548828, 150.09715270996094)
        Math_001.operation = "DIVIDE"
        Math_001.inputs["Value"].default_value = 2.0
        Math_001.inputs["Value"].default_value = 0.5
        Math_007 = nt.nodes.new("ShaderNodeMath")
        Math_007.location = (289.21795654296875, -17.24056625366211)
        Math_007.operation = "SUBTRACT"
        Math_007.inputs["Value"].default_value = 1.0
        Math_007.inputs["Value"].default_value = 0.5
        Math_006 = nt.nodes.new("ShaderNodeMath")
        Math_006.location = (289.21795654296875, 150.09715270996094)
        Math_006.operation = "SUBTRACT"
        Math_006.inputs["Value"].default_value = 1.0
        Math_006.inputs["Value"].default_value = 0.5
        Math_008 = nt.nodes.new("ShaderNodeMath")
        Math_008.location = (289.21795654296875, -188.0381622314453)
        Math_008.operation = "SUBTRACT"
        Math_008.inputs["Value"].default_value = 1.0
        Math_008.inputs["Value"].default_value = 0.5
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (6.462799072265625, 591.4071655273438)
        # Create links
        nt.links.new(Group_Input.outputs["Base Color"], Separate_Color.inputs["Color"])
        nt.links.new(Group_Input.outputs["Blend Color"], Separate_Color_001.inputs["Color"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Blended Color"])
        nt.links.new(Separate_Color.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Math_006.outputs["Value"], Combine_Color.inputs["Red"])
        nt.links.new(Separate_Color.outputs["Green"], Math_003.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Green"], Math_003.inputs["Value"])
        nt.links.new(Group_Input.outputs["Blend Color"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Base Color"], Mix_001.inputs["A"])
        nt.links.new(Combine_Color.outputs["Color"], Mix_002.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Group_Input.outputs["Mix Add And Blend"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Factor"], Mix_001.inputs["Factor"])
        nt.links.new(Math.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Math_007.outputs["Value"], Combine_Color.inputs["Green"])
        nt.links.new(Math_004.outputs["Value"], Math_005.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_004.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Blue"], Math_004.inputs["Value"])
        nt.links.new(Math_008.outputs["Value"], Combine_Color.inputs["Blue"])
        nt.links.new(Math_002.outputs["Value"], Math_007.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Math_006.inputs["Value"])
        nt.links.new(Math_005.outputs["Value"], Math_008.inputs["Value"])