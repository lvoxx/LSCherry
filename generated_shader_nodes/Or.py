import bpy
from ..utils import ShaderNode


class ShaderNodeOr(ShaderNode):
    bl_label = "OR"
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
        Group_Input.location = (-360.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (295.75408935546875, 57.18584060668945)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (91.49552154541016, 61.736228942871094)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (-100.0, 80.0)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (-97.16517639160156, -62.70294189453125)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (-29.307601928710938, 215.10145568847656)
        # Create links
        nt.links.new(Group_Input.outputs["A"], Group_003.inputs["B"])
        nt.links.new(Group_008.outputs["O"], Group_Output.inputs["O"])
        nt.links.new(Group_Input.outputs["B"], Group_004.inputs["B"])
        nt.links.new(Group_Input.outputs["B"], Group_004.inputs["A"])
        nt.links.new(Group_004.outputs["O"], Group_008.inputs["B"])
        nt.links.new(Group_003.outputs["O"], Group_008.inputs["A"])
        nt.links.new(Group_Input.outputs["A"], Group_003.inputs["A"])