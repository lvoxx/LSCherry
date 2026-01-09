import bpy
from ..utils import ShaderNode


class ShaderNodeNand(ShaderNode):
    bl_label = "NAND"
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
        Group_Input.location = (-560.0, 60.0)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-380.0, 60.0)
        Math_002.operation = "CEIL"
        Math_002.inputs["Value"].default_value = 7.0
        Math_002.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-380.0, -80.0)
        Math_003.operation = "CEIL"
        Math_003.inputs["Value"].default_value = 7.0
        Math_003.inputs["Value"].default_value = 0.5
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (-200.0, 60.0)
        Math_004.operation = "ADD"
        Math_004.inputs["Value"].default_value = 0.5
        Math_006 = nt.nodes.new("ShaderNodeMath")
        Math_006.location = (-20.0, 60.0)
        Math_006.operation = "LESS_THAN"
        Math_006.inputs["Value"].default_value = 2.0
        Math_006.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (160.0, 60.0)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (-171.618896484375, 246.07894897460938)
        # Create links
        nt.links.new(Math_002.outputs["Value"], Math_004.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Math_004.inputs["Value"])
        nt.links.new(Group_Input.outputs["A"], Math_002.inputs["Value"])
        nt.links.new(Group_Input.outputs["B"], Math_003.inputs["Value"])
        nt.links.new(Math_004.outputs["Value"], Math_006.inputs["Value"])
        nt.links.new(Math_006.outputs["Value"], Group_Output.inputs["O"])