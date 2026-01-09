import bpy
from ..utils import ShaderNode


class ShaderNodeLimitColorValue(ShaderNode):
    bl_label = "Limit Color Value"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Limited_Color_socket = nt.interface.new_socket(
                name="Limited Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Limited_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Target_Color_socket = nt.interface.new_socket(
                name="Target Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Target_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Limit_Color_socket = nt.interface.new_socket(
                name="Limit Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Limit_Color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Limit_Value_socket = nt.interface.new_socket(
                name="Limit Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Limit_Value_socket.default_value = 0.8899999856948853
        Limit_Value_socket.min_value = 0.0
        Limit_Value_socket.max_value = 1.0
        Limit_Value_socket.subtype = "PERCENTAGE"

        # Create nodes
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (207.2974395751953, 66.01544189453125)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (402.84014892578125, 28.847089767456055)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-816.1978149414062, -131.56199645996094)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (46.77466583251953, -126.66946411132812)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-161.3773956298828, -64.03618621826172)
        Math_001.operation = "GREATER_THAN"
        Math_001.inputs["Value"].default_value = 0.5
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-355.7034912109375, -133.75070190429688)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Separate_Color_001 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color_001.location = (-544.141845703125, -102.017822265625)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-544.141845703125, 107.83062744140625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-156.24740600585938, 248.858642578125)
        # Create links
        nt.links.new(Separate_Color.outputs["Green"], Combine_Color.inputs["Green"])
        nt.links.new(Separate_Color.outputs["Red"], Combine_Color.inputs["Red"])
        nt.links.new(Group_Input.outputs["Target Color"], Separate_Color.inputs["Color"])
        nt.links.new(Combine_Color.outputs["Color"], Group_Output.inputs["Limited Color"])
        nt.links.new(Group_Input.outputs["Limit Value"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Limit Color"], Separate_Color_001.inputs["Color"])
        nt.links.new(Separate_Color_001.outputs["Blue"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["B"])
        nt.links.new(Separate_Color.outputs["Blue"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Combine_Color.inputs["Blue"])