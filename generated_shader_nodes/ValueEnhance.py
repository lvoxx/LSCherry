import bpy
from ..utils import ShaderNode


class ShaderNodeValueEnhance(ShaderNode):
    bl_label = "Value Enhance"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Enhanced_Shading_socket = nt.interface.new_socket(
                name="Enhanced Shading",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Enhanced_Shading_socket.default_value = 0.0
        Enhanced_Shading_socket.min_value = -3.4028234663852886e+38
        Enhanced_Shading_socket.max_value = 3.4028234663852886e+38
        Enhanced_Shading_socket.subtype = "NONE"

        # Input sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = -10000.0
        Shading_socket.max_value = 10000.0
        Shading_socket.subtype = "NONE"
            Value_Enhance_socket = nt.interface.new_socket(
                name="Value Enhance",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Value_Enhance_socket.default_value = 0.10000000149011612
        Value_Enhance_socket.min_value = 0.0
        Value_Enhance_socket.max_value = 1.0
        Value_Enhance_socket.subtype = "FACTOR"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-379.063720703125, -32.596839904785156)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.00003051757812, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-64.39303588867188, -0.6713714599609375)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-116.10324096679688, 129.24578857421875)
        # Create links
        nt.links.new(Group_Input.outputs["Shading"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Value Enhance"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Enhanced Shading"])