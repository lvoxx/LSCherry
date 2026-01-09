import bpy
from ..utils import ShaderNode


class ShaderNodeHsrAddColorFromColormap(ShaderNode):
    bl_label = "HSR: Add Color From Colormap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Original_Color_socket = nt.interface.new_socket(
                name="Original Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Original_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 0.0
        Factor_socket.min_value = 0.0
        Factor_socket.max_value = 1.0
        Factor_socket.subtype = "FACTOR"
            Bright_Mask_socket = nt.interface.new_socket(
                name="Bright Mask",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Bright_Mask_socket.default_value = 0.0
        Bright_Mask_socket.min_value = 0.0
        Bright_Mask_socket.max_value = 1.0
        Bright_Mask_socket.subtype = "FACTOR"
            Bright_Color_socket = nt.interface.new_socket(
                name="Bright Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Bright_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-224.9178466796875, -52.68484878540039)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-11.48541259765625, 149.56277465820312)
        # Create links
        nt.links.new(Group_Input.outputs["Original Color"], Group.inputs["Original Color"])
        nt.links.new(Group_Input.outputs["Bright Mask"], Group.inputs["Bright Mask"])
        nt.links.new(Group_Input.outputs["Bright Color"], Group.inputs["Bright Color"])
        nt.links.new(Group.outputs["Color"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Factor"], Group.inputs["Factor"])