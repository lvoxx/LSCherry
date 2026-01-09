import bpy
from ..utils import ShaderNode


class ShaderNodeSimplePantyhoseType2(ShaderNode):
    bl_label = "Simple Pantyhose Type 2"
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
        
        Color_socket.default_value = (0.8055135011672974, 0.8055135011672974, 0.8055135011672974, 1.0)
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Pattern_socket.default_value = 0.0
        Pattern_socket.min_value = -3.4028234663852886e+38
        Pattern_socket.max_value = 3.4028234663852886e+38
        Pattern_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Input sockets
            Enable_Dot_socket = nt.interface.new_socket(
                name="Enable Dot",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Enable_Dot_socket.default_value = False
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.685835599899292, 0.685835599899292, 0.685835599899292, 1.0)
            Highlight_Color_socket = nt.interface.new_socket(
                name="Highlight Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Highlight_Color_socket.default_value = (1.0, 0.6242283582687378, 0.5513602495193481, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 8.0
        Size_socket.min_value = 1.0
        Size_socket.max_value = 100.0
        Size_socket.subtype = "NONE"
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.20000000298023224
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-245.48587036132812, -95.02903747558594)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-30.669525146484375, 115.61321258544922)
        # Create links
        nt.links.new(Group_Input.outputs["UV"], Group_003.inputs["UV"])
        nt.links.new(Group_Input.outputs["Color"], Group_003.inputs["Base Color"])
        nt.links.new(Group_Input.outputs["Highlight Color"], Group_003.inputs["Highlight Color"])
        nt.links.new(Group_Input.outputs["Size"], Group_003.inputs["Size"])
        nt.links.new(Group_Input.outputs["Roughness"], Group_003.inputs["Roughness"])
        nt.links.new(Group_003.outputs["Color"], Group_Output.inputs["Color"])
        nt.links.new(Group_003.outputs["Pattern"], Group_Output.inputs["Pattern"])
        nt.links.new(Group_003.outputs["Normal"], Group_Output.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Enable Dot"], Group_003.inputs["Enable Dot"])