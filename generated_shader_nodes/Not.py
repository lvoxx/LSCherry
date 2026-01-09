import bpy
from ..utils import ShaderNode


class ShaderNodeNot(ShaderNode):
    bl_label = "NOT"
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
        O_socket.max_value = 0.0
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

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (200.0, -0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-180.0, 0.0)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (0.0, 0.0)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (34.57511901855469, 159.30897521972656)
        # Create links
        nt.links.new(Group_001.outputs["O"], Group_Output.inputs["O"])
        nt.links.new(Group_Input.outputs["A"], Group_001.inputs["A"])
        nt.links.new(Group_Input.outputs["A"], Group_001.inputs["B"])