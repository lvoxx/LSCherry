import bpy
from ..utils import ShaderNode


class ShaderNodeXor(ShaderNode):
    bl_label = "XOR"
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
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (360.69439697265625, -64.64056396484375)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (360.0, 180.0)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (180.0, 40.0)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (560.0, 120.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (740.0, 120.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-60.0, 0.0)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (394.69000244140625, 306.4065856933594)
        # Create links
        nt.links.new(Group_Input.outputs["A"], Group_011.inputs["A"])
        nt.links.new(Group_Input.outputs["B"], Group_012.inputs["B"])
        nt.links.new(Group_Input.outputs["A"], Group_010.inputs["A"])
        nt.links.new(Group_Input.outputs["B"], Group_010.inputs["B"])
        nt.links.new(Group_010.outputs["O"], Group_011.inputs["B"])
        nt.links.new(Group_010.outputs["O"], Group_012.inputs["A"])
        nt.links.new(Group_011.outputs["O"], Group_013.inputs["A"])
        nt.links.new(Group_012.outputs["O"], Group_013.inputs["B"])
        nt.links.new(Group_013.outputs["O"], Group_Output.inputs["O"])