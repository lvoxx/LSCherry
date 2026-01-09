import bpy
from ..utils import ShaderNode


class ShaderNodeAnd(ShaderNode):
    bl_label = "AND"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            O_socket = nt.interface.new_socket(
                name="O",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        O_socket.default_value = 0.0
        O_socket.min_value = 0.0
        O_socket.max_value = 1.0
        O_socket.subtype = "NONE"

        # Input sockets
            A_socket = nt.interface.new_socket(
                name="A",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        A_socket.default_value = 0.0
        A_socket.min_value = 0.0
        A_socket.max_value = 1.0
        A_socket.subtype = "NONE"
            B_socket = nt.interface.new_socket(
                name="B",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        B_socket.default_value = 0.0
        B_socket.min_value = 0.0
        B_socket.max_value = 1.0
        B_socket.subtype = "NONE"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-151.23851013183594, -15.037093162536621)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (83.06617736816406, 34.27818298339844)
        Math.operation = "COMPARE"
        Math.inputs["Value"].default_value = 0.0
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (460.0, 0.0)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (100.36026000976562, 155.38441467285156)
        # Create links
        nt.links.new(Group_Input.outputs["A"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["B"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["O"])