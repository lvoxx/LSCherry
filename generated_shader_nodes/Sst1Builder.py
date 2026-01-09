import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Builder(ShaderNode):
    bl_label = "SST1: Builder"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Input sockets
            Skin_Color_socket = nt.interface.new_socket(
                name="Skin Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Skin_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-200.0, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (1.278045654296875, 119.17662811279297)
        # Create links
        nt.links.new(Group_Input.outputs["Skin Color"], Group_Output.inputs["Builder"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])