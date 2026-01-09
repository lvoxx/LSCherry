import bpy
from ..utils import ShaderNode


class ShaderNodeHi3AddShadowFromLightmap(ShaderNode):
    bl_label = "HI3: Add Shadow From Lightmap"
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
            Shadow_socket = nt.interface.new_socket(
                name="Shadow",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_socket.default_value = 0.0
        Shadow_socket.min_value = 0.0
        Shadow_socket.max_value = 1.0
        Shadow_socket.subtype = "FACTOR"
            Shadow_Color_socket = nt.interface.new_socket(
                name="Shadow Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Shadow_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-200.0, -50.743080139160156)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-41.55853271484375, 126.92027282714844)
        # Create links
        nt.links.new(Group_Input.outputs["Original Color"], Group.inputs["Original Color"])
        nt.links.new(Group_Input.outputs["Shadow"], Group.inputs["Shadow Mask"])
        nt.links.new(Group_Input.outputs["Shadow Color"], Group.inputs["Shadow Color"])
        nt.links.new(Group.outputs["Color"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Factor"], Group.inputs["Factor"])