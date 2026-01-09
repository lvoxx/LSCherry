import bpy
from ..utils import ShaderNode


class ShaderNodeGiBuildHairPackage(ShaderNode):
    bl_label = "GI: Build Hair Package"
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
            Emission_socket = nt.interface.new_socket(
                name="Emission",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Emission_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Emission_Strength_socket = nt.interface.new_socket(
                name="Emission Strength",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Emission_Strength_socket.default_value = 0.0
        Emission_Strength_socket.min_value = -3.4028234663852886e+38
        Emission_Strength_socket.max_value = 3.4028234663852886e+38
        Emission_Strength_socket.subtype = "NONE"
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
            Metal_Mask_socket = nt.interface.new_socket(
                name="Metal Mask",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metal_Mask_socket.default_value = 0.0
        Metal_Mask_socket.min_value = -3.4028234663852886e+38
        Metal_Mask_socket.max_value = 3.4028234663852886e+38
        Metal_Mask_socket.subtype = "NONE"
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
            Hair_Alpha_socket = nt.interface.new_socket(
                name="Hair Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Hair_Alpha_socket.default_value = 0.0
        Hair_Alpha_socket.min_value = -3.4028234663852886e+38
        Hair_Alpha_socket.max_value = 3.4028234663852886e+38
        Hair_Alpha_socket.subtype = "NONE"
            Lightmap_Texture_socket = nt.interface.new_socket(
                name="Lightmap Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Lightmap_Alpha_socket = nt.interface.new_socket(
                name="Lightmap Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Lightmap_Alpha_socket.default_value = 0.0
        Lightmap_Alpha_socket.min_value = -3.4028234663852886e+38
        Lightmap_Alpha_socket.max_value = 3.4028234663852886e+38
        Lightmap_Alpha_socket.subtype = "NONE"
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
            Emission_Strength_socket = nt.interface.new_socket(
                name="Emission Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Emission_Strength_socket.default_value = 1.0
        Emission_Strength_socket.min_value = 0.0
        Emission_Strength_socket.max_value = 10000.0
        Emission_Strength_socket.subtype = "NONE"
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
        Group_Output.location = (349.03948974609375, 81.58348083496094)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (89.72325134277344, 191.2218017578125)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (47.569889068603516, -189.241455078125)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-586.1533203125, -45.20416259765625)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (-354.9768371582031, -116.06968688964844)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-58.22869873046875, 310.39947509765625)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (37.0870475769043, -48.61395263671875)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        # Create links
        nt.links.new(Group_008.outputs["Color"], Group_Output.inputs["Base Color"])
        nt.links.new(Group_Input.outputs["Hair Texture"], Group_008.inputs["Original Color"])
        nt.links.new(Group_Input.outputs["Shadow Factor"], Group_008.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Lightmap Texture"], Group_009.inputs["Lightmap"])
        nt.links.new(Group_Input.outputs["Shadow Color"], Group_008.inputs["Shadow Color"])
        nt.links.new(Group_009.outputs["Highlight"], Group_Output.inputs["Highlight Mask"])
        nt.links.new(Group_009.outputs["Shadow"], Group_008.inputs["Shadow Mask"])
        nt.links.new(Group_009.outputs["Shadow"], Group_Output.inputs["Shadow Mask"])
        nt.links.new(Group_Input.outputs["Toon"], Group_010.inputs["Toon"])
        nt.links.new(Group_009.outputs["Shadow"], Group_010.inputs["Shadow Mask"])
        nt.links.new(Group_010.outputs["Cold-UV1"], Group_Output.inputs["Hair Ramp UV"])
        nt.links.new(Group_Input.outputs["Shadow Factor"], Group_010.inputs["Shadow Factor"])
        nt.links.new(Group_009.outputs["Metal"], Group_Output.inputs["Metal Mask"])
        nt.links.new(Group_Input.outputs["Hair Alpha"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Emission Strength"])
        nt.links.new(Group_Input.outputs["Hair Texture"], Group_Output.inputs["Emission"])
        nt.links.new(Group_Input.outputs["Emission Strength"], Math.inputs["Value"])