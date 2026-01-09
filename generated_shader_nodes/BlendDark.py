import bpy
from ..utils import ShaderNode


class ShaderNodeBlendDark(ShaderNode):
    bl_label = "Blend Dark"
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
            Mix_Multiply_And_Blend_socket = nt.interface.new_socket(
                name="Mix Multiply And Blend",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_Multiply_And_Blend_socket.default_value = 1.0
        Mix_Multiply_And_Blend_socket.min_value = 0.0
        Mix_Multiply_And_Blend_socket.max_value = 1.0
        Mix_Multiply_And_Blend_socket.subtype = "FACTOR"
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
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (812.5900268554688, -40.394775390625)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-58.180564880371094, 417.8006286621094)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = 1.0
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-668.17138671875, 476.02691650390625)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (523.4609375, 476.02691650390625)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (523.4609375, 28.1114501953125)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-788.0956420898438, -271.0006408691406)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (592.9998779296875, 180.3450927734375)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (373.0000305175781, -43.70854187011719)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-668.17138671875, 60.91716766357422)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1110.9573974609375, 115.31524658203125)
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (152.62855529785156, -288.7783203125)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-542.53515625, -93.56166076660156)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-542.53515625, -291.0170593261719)
        Math_003.operation = "ADD"
        Math_003.inputs["Value"].default_value = 0.5
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (-542.53515625, -452.8582763671875)
        Math_004.operation = "ADD"
        Math_004.inputs["Value"].default_value = 0.5
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-885.9739990234375, 77.80416870117188)
        Separate_Color_001 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color_001.location = (-788.0956420898438, -455.009521484375)
        Math_006 = nt.nodes.new("ShaderNodeMath")
        Math_006.location = (-92.74543762207031, -93.56166076660156)
        Math_006.operation = "MODULO"
        Math_006.inputs["Value"].default_value = 255.0
        Math_006.inputs["Value"].default_value = 0.5
        Math_007 = nt.nodes.new("ShaderNodeMath")
        Math_007.location = (-85.99999237060547, -281.081298828125)
        Math_007.operation = "MODULO"
        Math_007.inputs["Value"].default_value = 255.0
        Math_007.inputs["Value"].default_value = 0.5
        Math_008 = nt.nodes.new("ShaderNodeMath")
        Math_008.location = (-86.00000762939453, -447.4449157714844)
        Math_008.operation = "MODULO"
        Math_008.inputs["Value"].default_value = 255.0
        Math_008.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-306.30902099609375, -93.56166076660156)
        Math_001.operation = "DIVIDE"
        Math_001.inputs["Value"].default_value = 2.0
        Math_001.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-306.30902099609375, -291.0170593261719)
        Math_002.operation = "DIVIDE"
        Math_002.inputs["Value"].default_value = 2.0
        Math_002.inputs["Value"].default_value = 0.5
        Math_005 = nt.nodes.new("ShaderNodeMath")
        Math_005.location = (-306.30902099609375, -452.8582763671875)
        Math_005.operation = "DIVIDE"
        Math_005.inputs["Value"].default_value = 2.0
        Math_005.inputs["Value"].default_value = 0.5
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-180.15850830078125, 598.89111328125)
        # Create links
        nt.links.new(Group_Input.outputs["Base Color"], Separate_Color.inputs["Color"])
        nt.links.new(Group_Input.outputs["Blend Color"], Separate_Color_001.inputs["Color"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Blended Color"])
        nt.links.new(Separate_Color.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Green"], Math_003.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Green"], Math_003.inputs["Value"])
        nt.links.new(Group_Input.outputs["Blend Color"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Base Color"], Mix_001.inputs["A"])
        nt.links.new(Mix_003.outputs["Result"], Mix_002.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Group_Input.outputs["Mix Multiply And Blend"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_004.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Blue"], Math_004.inputs["Value"])
        nt.links.new(Math_004.outputs["Value"], Math_005.inputs["Value"])
        nt.links.new(Group_Input.outputs["Factor"], Reroute_004.inputs["Input"])
        nt.links.new(Group_Input.outputs["Base Color"], Mix_003.inputs["A"])
        nt.links.new(Combine_Color.outputs["Color"], Mix_003.inputs["B"])
        nt.links.new(Reroute_004.outputs["Output"], Mix_003.inputs["Factor"])
        nt.links.new(Math_006.outputs["Value"], Combine_Color.inputs["Red"])
        nt.links.new(Math_007.outputs["Value"], Combine_Color.inputs["Green"])
        nt.links.new(Math_008.outputs["Value"], Combine_Color.inputs["Blue"])
        nt.links.new(Math_001.outputs["Value"], Math_006.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Math_007.inputs["Value"])
        nt.links.new(Math_005.outputs["Value"], Math_008.inputs["Value"])