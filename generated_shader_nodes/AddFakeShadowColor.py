import bpy
from ..utils import ShaderNode


class ShaderNodeAddFakeShadowColor(ShaderNode):
    bl_label = "Add Fake Shadow Color"
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
            Shadow_Mask_socket = nt.interface.new_socket(
                name="Shadow Mask",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Mask_socket.default_value = 0.0
        Shadow_Mask_socket.min_value = 0.0
        Shadow_Mask_socket.max_value = 1.0
        Shadow_Mask_socket.subtype = "FACTOR"
            Shadow_Color_socket = nt.interface.new_socket(
                name="Shadow Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Shadow_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (342.3965148925781, 68.57737731933594)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (93.79545593261719, 60.5994873046875)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-158.3504638671875, 77.71369934082031)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-169.3253936767578, -214.0353546142578)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (1.0, 1.0, 1.0, 1.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-694.8594970703125, -47.18974685668945)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (-418.74639892578125, -93.11418151855469)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-405.02935791015625, 195.96018981933594)
        # Create links
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Color"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Original Color"], Mix_001.inputs["A"])
        nt.links.new(Group_Input.outputs["Shadow Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Factor"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Shadow Mask"], Invert_Color.inputs["Color"])
        nt.links.new(Invert_Color.outputs["Color"], Math.inputs["Value"])
        nt.links.new(Invert_Color.outputs["Color"], Mix.inputs["Factor"])