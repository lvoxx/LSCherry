import bpy
from ..utils import ShaderNode


class ShaderNodeNamedProperties(ShaderNode):
    bl_label = "Named Properties"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Main_Light_Vector_socket = nt.interface.new_socket(
                name="Main Light Vector",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Main_Light_Vector_socket.default_value = (0.0, 0.0, 0.0)
        Main_Light_Vector_socket.subtype = "NONE"
            Back_Light_Vector_socket = nt.interface.new_socket(
                name="Back Light Vector",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Back_Light_Vector_socket.default_value = (0.0, 0.0, 0.0)
        Back_Light_Vector_socket.subtype = "NONE"
            Fx_socket = nt.interface.new_socket(
                name="Fx",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Fx_socket.default_value = (0.0, 0.0, 0.0)
        Fx_socket.subtype = "NONE"
            Fy_socket = nt.interface.new_socket(
                name="Fy",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Fy_socket.default_value = (0.0, 0.0, 0.0)
        Fy_socket.subtype = "NONE"
            Toon_Normal_socket = nt.interface.new_socket(
                name="Toon Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Toon_Normal_socket.default_value = (0.0, 0.0, 0.0)
        Toon_Normal_socket.subtype = "NONE"

        # Input sockets

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-200.0, 0.0)
        Attribute_001 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_001.location = (0.0, -123.15982055664062)
        Attribute_002 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_002.location = (0.0, 22.36132049560547)
        Attribute_003 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_003.location = (0.0, -13.008338928222656)
        Attribute_004 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_004.location = (0.0, -49.85173797607422)
        Attribute_005 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_005.location = (0.0, -85.90742492675781)
        # Create links
        nt.links.new(Attribute_002.outputs["Vector"], Group_Output.inputs["Main Light Vector"])
        nt.links.new(Attribute_003.outputs["Vector"], Group_Output.inputs["Back Light Vector"])
        nt.links.new(Attribute_004.outputs["Vector"], Group_Output.inputs["Fx"])
        nt.links.new(Attribute_005.outputs["Vector"], Group_Output.inputs["Fy"])
        nt.links.new(Attribute_001.outputs["Vector"], Group_Output.inputs["Toon Normal"])