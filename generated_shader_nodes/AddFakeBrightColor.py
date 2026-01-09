import bpy
from ..utils import ShaderNode


class ShaderNodeAddFakeBrightColor(ShaderNode):
    bl_label = "Add Fake Bright Color"
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
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (309.29541015625, 123.12516021728516)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-451.4675598144531, -47.18974685668945)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (105.35580444335938, 125.22613525390625)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-105.35580444335938, -125.22610473632812)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (1.0, 1.0, 1.0, 1.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-324.986328125, 128.2766876220703)
        # Create links
        nt.links.new(Group_Input.outputs["Bright Mask"], Mix.inputs["Factor"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Bright Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Factor"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Original Color"], Mix_001.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])