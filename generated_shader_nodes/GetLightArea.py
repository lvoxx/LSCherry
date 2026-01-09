import bpy
from ..utils import ShaderNode


class ShaderNodeGetLightArea(ShaderNode):
    bl_label = "Get Light Area"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Fixed_Shading_socket = nt.interface.new_socket(
                name="Fixed Shading",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fixed_Shading_socket.default_value = 0.0
        Fixed_Shading_socket.min_value = -3.4028234663852886e+38
        Fixed_Shading_socket.max_value = 3.4028234663852886e+38
        Fixed_Shading_socket.subtype = "NONE"

        # Input sockets
            Mask_socket = nt.interface.new_socket(
                name="Mask",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mask_socket.default_value = 0.5
        Mask_socket.min_value = 0.0
        Mask_socket.max_value = 1.0
        Mask_socket.subtype = "FACTOR"
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 0.0
        Shading_socket.min_value = -3.4028234663852886e+38
        Shading_socket.max_value = 3.4028234663852886e+38
        Shading_socket.subtype = "NONE"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-298.2978820800781, -130.1934356689453)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (0.0, 0.0)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-76.47296142578125, 159.6187286376953)
        # Create links
        nt.links.new(Group_Input.outputs["Mask"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Shading"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Fixed Shading"])