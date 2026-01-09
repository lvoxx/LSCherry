import bpy
from ..utils import ShaderNode


class ShaderNodeHsrBuildHairPackage(ShaderNode):
    bl_label = "HSR: Build Hair Package"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            Shadow_Mask_socket = nt.interface.new_socket(
                name="Shadow Mask",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Mask_socket.default_value = 0.0
        Shadow_Mask_socket.min_value = -3.4028234663852886e+38
        Shadow_Mask_socket.max_value = 3.4028234663852886e+38
        Shadow_Mask_socket.subtype = "NONE"
            Highlight_Mask_socket = nt.interface.new_socket(
                name="Highlight Mask",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Highlight_Mask_socket.default_value = 0.0
        Highlight_Mask_socket.min_value = -3.4028234663852886e+38
        Highlight_Mask_socket.max_value = 3.4028234663852886e+38
        Highlight_Mask_socket.subtype = "NONE"
            Hair_Ramp_UV_socket = nt.interface.new_socket(
                name="Hair Ramp UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Hair_Ramp_UV_socket.default_value = (0.0, 0.0, 0.0)
        Hair_Ramp_UV_socket.subtype = "NONE"

        # Input sockets
            Hair_Texture_socket = nt.interface.new_socket(
                name="Hair Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Hair_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Lightmap_Texture_socket = nt.interface.new_socket(
                name="Lightmap Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Shadow_Factor_socket = nt.interface.new_socket(
                name="Shadow Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Factor_socket.default_value = 0.0
        Shadow_Factor_socket.min_value = 0.0
        Shadow_Factor_socket.max_value = 1.0
        Shadow_Factor_socket.subtype = "NONE"
            Shadow_Color_socket = nt.interface.new_socket(
                name="Shadow Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Shadow_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Toon_socket.default_value = 0.0
        Toon_socket.min_value = 0.0
        Toon_socket.max_value = 1.0
        Toon_socket.subtype = "NONE"
            Shadow_Factor_socket = nt.interface.new_socket(
                name="Shadow Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Factor_socket.default_value = 1.0
        Shadow_Factor_socket.min_value = 0.0
        Shadow_Factor_socket.max_value = 1.0
        Shadow_Factor_socket.subtype = "FACTOR"
            Ramp_Size_socket = nt.interface.new_socket(
                name="Ramp Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Ramp_Size_socket.default_value = 0.949999988079071
        Ramp_Size_socket.min_value = 0.0
        Ramp_Size_socket.max_value = 1.0
        Ramp_Size_socket.subtype = "FACTOR"
            Value_Enhance_socket = nt.interface.new_socket(
                name="Value Enhance",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Value_Enhance_socket.default_value = 0.10000000149011612
        Value_Enhance_socket.min_value = 0.0
        Value_Enhance_socket.max_value = 1.0
        Value_Enhance_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (624.552001953125, -15.024467468261719)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (47.569889068603516, -189.241455078125)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-586.1533203125, -45.20416259765625)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (-356.17462158203125, -143.7783660888672)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (358.57220458984375, 181.16868591308594)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (152.6489715576172, 263.60748291015625)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (-83.16200256347656, -41.765098571777344)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-314.6316223144531, 181.09207153320312)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap Texture"], Group_009.inputs["Lightmap"])
        nt.links.new(Group_009.outputs["Highlight"], Group_Output.inputs["Highlight Mask"])
        nt.links.new(Group_009.outputs["Shadow"], Group_Output.inputs["Shadow Mask"])
        nt.links.new(Group_Input.outputs["Toon"], Group_010.inputs["Toon"])
        nt.links.new(Group_Input.outputs["Shadow Factor"], Group_010.inputs["Shadow Factor"])
        nt.links.new(Group_009.outputs["Shadow"], Group_010.inputs["Shadow Mask"])
        nt.links.new(Group_Input.outputs["Ramp Size"], Group_010.inputs["Ramp Size"])
        nt.links.new(Group_010.outputs["UV"], Group_Output.inputs["Hair Ramp UV"])
        nt.links.new(Group_Input.outputs["Value Enhance"], Group_010.inputs["Value Enhance"])
        nt.links.new(Group_Input.outputs["Hair Texture"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Shadow Factor"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Hair Texture"], Mix_001.inputs["A"])
        nt.links.new(Invert_Color.outputs["Color"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Shadow Color"], Mix_001.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Base Color"])
        nt.links.new(Group_009.outputs["Shadow"], Invert_Color.inputs["Color"])