import bpy
from ..utils import ShaderNode


class ShaderNodeInitNoseRamp(ShaderNode):
    bl_label = "Init Nose Ramp"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "NONE"
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
            Deprecated_socket = nt.interface.new_socket(
                name="Deprecated",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
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
        
        Default_UV_socket.default_value = 1.0
        Default_UV_socket.min_value = -1.0
        Default_UV_socket.max_value = 1.0
        Default_UV_socket.subtype = "NONE"
            Flip_UV_socket = nt.interface.new_socket(
                name="Flip UV",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Flip_UV_socket.default_value = -1.0
        Flip_UV_socket.min_value = -1.0
        Flip_UV_socket.max_value = 1.0
        Flip_UV_socket.subtype = "NONE"

        # Create nodes
        Group_006 = nt.nodes.new("ShaderNodeGroup")
        Group_006.location = (0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-337.40008544921875, -74.62030792236328)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-57.394195556640625, 135.42788696289062)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (-49.3419189453125, 229.49078369140625)
        # Create links
        nt.links.new(Group_Input.outputs["UV"], Group_006.inputs["UV"])
        nt.links.new(Group_Input.outputs["Min Dot Value"], Group_006.inputs["Min Dot Value"])
        nt.links.new(Group_Input.outputs["Max  Dot Value"], Group_006.inputs["Max  Dot Value"])
        nt.links.new(Group_Input.outputs["Default UV"], Group_006.inputs["Default UV"])
        nt.links.new(Group_Input.outputs["Flip UV"], Group_006.inputs["Flip UV"])
        nt.links.new(Group_006.outputs["Face Value"], Group_Output.inputs["Face Value"])
        nt.links.new(Group_006.outputs["Face Vector"], Group_Output.inputs["Face Vector"])