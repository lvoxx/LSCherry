import bpy
from ..utils import ShaderNode


class ShaderNodeHi3BuildHairPackage(ShaderNode):
    bl_label = "HI3: Build Hair Package"
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
            Hair_Mask_Texture_socket = nt.interface.new_socket(
                name="Hair Mask Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Hair_Mask_Texture_socket.default_value = (0.0, 0.0, 0.0, 1.0)
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
        Group_Output.location = (349.03948974609375, 81.58348083496094)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (89.72325134277344, 191.2218017578125)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (169.68411254882812, -336.4360046386719)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-693.0052490234375, -127.53965759277344)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (-356.17462158203125, -143.7783660888672)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (38.178409576416016, -130.77976989746094)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        RGB_to_BW = nt.nodes.new("ShaderNodeRGBToBW")
        RGB_to_BW.location = (-402.6463317871094, -322.1174621582031)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (87.36091613769531, 270.3291015625)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (173.00711059570312, -521.7962036132812)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-216.64598083496094, -380.8717041015625)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-338.0084533691406, 221.82000732421875)
        # Create links
        nt.links.new(Group_008.outputs["Color"], Group_Output.inputs["Base Color"])
        nt.links.new(Group_Input.outputs["Lightmap Texture"], Group_009.inputs["Lightmap"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Highlight Mask"])
        nt.links.new(Group_009.outputs["Shadow"], Group_008.inputs["Shadow Mask"])
        nt.links.new(Group_009.outputs["Shadow"], Group_Output.inputs["Shadow Mask"])
        nt.links.new(Group_009.outputs["Shadow"], Group_010.inputs["Shadow Mask"])
        nt.links.new(Group_010.outputs["UV"], Group_Output.inputs["Hair Ramp UV"])
        nt.links.new(Group_009.outputs["Highlight"], Mix.inputs["A"])
        nt.links.new(Group_Input_001.outputs["Shadow Color"], Group_008.inputs["Shadow Color"])
        nt.links.new(Group_Input_001.outputs["Shadow Factor"], Group_008.inputs["Factor"])
        nt.links.new(Group_Input_002.outputs["Toon"], Group_010.inputs["Toon"])
        nt.links.new(Group_Input_002.outputs["Shadow Factor"], Group_010.inputs["Shadow Factor"])
        nt.links.new(Group_Input_002.outputs["Ramp Size"], Group_010.inputs["Ramp Size"])
        nt.links.new(Group_Input_002.outputs["Value Enhance"], Group_010.inputs["Value Enhance"])
        nt.links.new(Group_Input.outputs["Hair Mask Texture"], RGB_to_BW.inputs["Color"])
        nt.links.new(Group_Input.outputs["Hair Texture"], Group_008.inputs["Original Color"])
        nt.links.new(RGB_to_BW.outputs["Val"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(RGB_to_BW.outputs["Val"], Mix.inputs["B"])