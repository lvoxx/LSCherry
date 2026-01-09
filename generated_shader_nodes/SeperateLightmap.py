import bpy
from ..utils import ShaderNode


class ShaderNodeSeperateLightmap(ShaderNode):
    bl_label = "Seperate Lightmap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Metal_socket = nt.interface.new_socket(
                name="Metal",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metal_socket.default_value = 0.0
        Metal_socket.min_value = -3.4028234663852886e+38
        Metal_socket.max_value = 3.4028234663852886e+38
        Metal_socket.subtype = "NONE"
            Diffuse_socket = nt.interface.new_socket(
                name="Diffuse",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Diffuse_socket.default_value = 0.0
        Diffuse_socket.min_value = -3.4028234663852886e+38
        Diffuse_socket.max_value = 3.4028234663852886e+38
        Diffuse_socket.subtype = "NONE"
            Highlight_socket = nt.interface.new_socket(
                name="Highlight",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Highlight_socket.default_value = 0.0
        Highlight_socket.min_value = -3.4028234663852886e+38
        Highlight_socket.max_value = 3.4028234663852886e+38
        Highlight_socket.subtype = "NONE"

        # Input sockets
            Lightmap_socket = nt.interface.new_socket(
                name="Lightmap",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-237.17576599121094, -110.4205322265625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (2.6214752197265625, 126.10626983642578)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Separate_Color.inputs["Color"])
        nt.links.new(Separate_Color.outputs["Red"], Group_Output.inputs["Metal"])
        nt.links.new(Separate_Color.outputs["Green"], Group_Output.inputs["Diffuse"])
        nt.links.new(Separate_Color.outputs["Blue"], Group_Output.inputs["Highlight"])