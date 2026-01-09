import bpy
from ..utils import ShaderNode


class ShaderNodeNoseRampBuilder(ShaderNode):
    bl_label = "Nose Ramp Builder"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Face_Value_socket = nt.interface.new_socket(
                name="Face Value",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Value_socket.default_value = 0.0
        Face_Value_socket.min_value = -3.4028234663852886e+38
        Face_Value_socket.max_value = 3.4028234663852886e+38
        Face_Value_socket.subtype = "NONE"
            Face_Vector_socket = nt.interface.new_socket(
                name="Face Vector",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Face_Vector_socket.default_value = (0.0, 0.0, 0.0)
        Face_Vector_socket.subtype = "NONE"

        # Input sockets
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"
            Min_Dot_Value_socket = nt.interface.new_socket(
                name="Min Dot Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Min_Dot_Value_socket.default_value = 0.0
        Min_Dot_Value_socket.min_value = -1.0
        Min_Dot_Value_socket.max_value = 1.0
        Min_Dot_Value_socket.subtype = "NONE"
            Max__Dot_Value_socket = nt.interface.new_socket(
                name="Max  Dot Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Max__Dot_Value_socket.default_value = 1.0
        Max__Dot_Value_socket.min_value = -1.0
        Max__Dot_Value_socket.max_value = 1.0
        Max__Dot_Value_socket.subtype = "NONE"
            Default_UV_socket = nt.interface.new_socket(
                name="Default UV",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Default_UV_socket.default_value = -1.0
        Default_UV_socket.min_value = -1.0
        Default_UV_socket.max_value = 1.0
        Default_UV_socket.subtype = "NONE"
            Flip_UV_socket = nt.interface.new_socket(
                name="Flip UV",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Flip_UV_socket.default_value = 1.0
        Flip_UV_socket.min_value = -1.0
        Flip_UV_socket.max_value = 1.0
        Flip_UV_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-200.0, 0.0)
        Group_007 = nt.nodes.new("ShaderNodeGroup")
        Group_007.location = (0.0, 0.0)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (2.401885986328125, 190.20518493652344)
        # Create links
        nt.links.new(Group_007.outputs["Face Value"], Group_Output.inputs["Face Value"])
        nt.links.new(Group_007.outputs["Face Vector"], Group_Output.inputs["Face Vector"])
        nt.links.new(Group_Input.outputs["UV"], Group_007.inputs["UV"])
        nt.links.new(Group_Input.outputs["Min Dot Value"], Group_007.inputs["Min Dot Value"])
        nt.links.new(Group_Input.outputs["Max  Dot Value"], Group_007.inputs["Max  Dot Value"])
        nt.links.new(Group_Input.outputs["Default UV"], Group_007.inputs["Default UV"])
        nt.links.new(Group_Input.outputs["Flip UV"], Group_007.inputs["Flip UV"])