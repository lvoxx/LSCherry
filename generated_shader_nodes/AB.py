import bpy
from ..utils import ShaderNode


class ShaderNodeAB(ShaderNode):
    bl_label = "A >= B"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Boolean_socket = nt.interface.new_socket(
                name="Boolean",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Boolean_socket.default_value = 0.0
        Boolean_socket.min_value = -3.4028234663852886e+38
        Boolean_socket.max_value = 3.4028234663852886e+38
        Boolean_socket.subtype = "NONE"

        # Input sockets
            A_socket = nt.interface.new_socket(
                name="A",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        A_socket.default_value = 0.5
        A_socket.min_value = -10000.0
        A_socket.max_value = 10000.0
        A_socket.subtype = "NONE"
            B_socket = nt.interface.new_socket(
                name="B",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        B_socket.default_value = 0.5
        B_socket.min_value = -10000.0
        B_socket.max_value = 10000.0
        B_socket.subtype = "NONE"

        # Create nodes
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (0.0, 0.0)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-260.1634216308594, -58.99203109741211)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (5.0423126220703125, 149.66824340820312)
        # Create links
        nt.links.new(Group_Input.outputs["A"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["B"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Boolean"])