import bpy
from ..utils import ShaderNode


class ShaderNodeXnor(ShaderNode):
    bl_label = "XNOR"
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
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-20.0, 20.0)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (160.0, 20.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (360.0, 20.0)
        Group_020 = nt.nodes.new("ShaderNodeGroup")
        Group_020.location = (-20.0, -140.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-320.0, -100.0)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (75.40475463867188, 171.4458770751953)
        # Create links
        nt.links.new(Group_001.outputs["O"], Group_Output.inputs["O"])
        nt.links.new(Group_Input.outputs["A"], Group.inputs["A"])
        nt.links.new(Group_Input.outputs["B"], Group.inputs["B"])
        nt.links.new(Group.outputs["NOR"], Group_001.inputs["A"])
        nt.links.new(Group_020.outputs["O"], Group_001.inputs["B"])
        nt.links.new(Group_Input.outputs["A"], Group_020.inputs["A"])
        nt.links.new(Group_Input.outputs["B"], Group_020.inputs["B"])