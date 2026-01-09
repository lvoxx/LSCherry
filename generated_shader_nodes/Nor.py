import bpy
from ..utils import ShaderNode


class ShaderNodeNor(ShaderNode):
    bl_label = "NOR"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            NOR_socket = nt.interface.new_socket(
                name="NOR",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        NOR_socket.default_value = 0.0
        NOR_socket.min_value = 0.0
        NOR_socket.max_value = 1.0
        NOR_socket.subtype = "NONE"

        # Input sockets
            A_socket = nt.interface.new_socket(
                name="A",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        A_socket.default_value = 0.0
        A_socket.min_value = 0.0
        A_socket.max_value = 1.0
        A_socket.subtype = "FACTOR"
            B_socket = nt.interface.new_socket(
                name="B",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        B_socket.default_value = 0.0
        B_socket.min_value = 0.0
        B_socket.max_value = 1.0
        B_socket.subtype = "FACTOR"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-320.0, -40.0)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (-120.0, 0.0)
        Group_007 = nt.nodes.new("ShaderNodeGroup")
        Group_007.location = (80.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (280.0, 0.0)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (53.691986083984375, 108.37329864501953)
        # Create links
        nt.links.new(Group_Input.outputs["A"], Group_003.inputs["A"])
        nt.links.new(Group_Input.outputs["B"], Group_003.inputs["B"])
        nt.links.new(Group_003.outputs["O"], Group_007.inputs["A"])
        nt.links.new(Group_007.outputs["O"], Group_Output.inputs["NOR"])