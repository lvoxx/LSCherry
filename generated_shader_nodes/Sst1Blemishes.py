import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Blemishes(ShaderNode):
    bl_label = "SST1: Blemishes"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Input sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Red_Color_socket = nt.interface.new_socket(
                name="Red Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Red_Color_socket.default_value = (0.8999999761581421, 0.19262465834617615, 0.13571682572364807, 1.0)
            Blue_Color_socket = nt.interface.new_socket(
                name="Blue Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Blue_Color_socket.default_value = (0.3672824203968048, 0.24802467226982117, 0.8999999761581421, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 1.100000023841858
        Size_socket.min_value = 0.0
        Size_socket.max_value = 100.0
        Size_socket.subtype = "NONE"
            Strength_socket = nt.interface.new_socket(
                name="Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Strength_socket.default_value = 1.0
        Strength_socket.min_value = 0.0
        Strength_socket.max_value = 100.0
        Strength_socket.subtype = "NONE"
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        Mapping_001 = nt.nodes.new("ShaderNodeMapping")
        Mapping_001.location = (-217.18475341796875, 358.1181640625)
        Mapping_001.vector_type = "POINT"
        Mapping_001.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
        Noise_Texture_001 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_001.location = (14.221753120422363, 505.1114501953125)
        Noise_Texture_001.inputs["W"].default_value = 0.0
        Noise_Texture_001.inputs["Scale"].default_value = 50.0
        Noise_Texture_001.inputs["Detail"].default_value = 2.0
        Noise_Texture_001.inputs["Roughness"].default_value = 0.5
        Noise_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_001.inputs["Offset"].default_value = 0.0
        Noise_Texture_001.inputs["Gain"].default_value = 1.0
        Noise_Texture_001.inputs["Distortion"].default_value = 0.0
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (206.98255920410156, 215.9663543701172)
        ColorRamp.color_ramp.color_mode = "RGB"
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (26.512100219726562, 182.0371551513672)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Detail"].default_value = 2.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-216.86880493164062, 275.5738525390625)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Scale"].default_value = (500.0, 500.0, 500.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (590.14599609375, 243.8597412109375)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0, 1.0)
        ColorRamp_002 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_002.location = (208.282958984375, 955.2742309570312)
        ColorRamp_002.color_ramp.color_mode = "RGB"
        Noise_Texture_002 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_002.location = (27.81256103515625, 921.3450317382812)
        Noise_Texture_002.inputs["W"].default_value = 0.0
        Noise_Texture_002.inputs["Detail"].default_value = 2.0
        Noise_Texture_002.inputs["Roughness"].default_value = 0.5
        Noise_Texture_002.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_002.inputs["Offset"].default_value = 0.0
        Noise_Texture_002.inputs["Gain"].default_value = 1.0
        Noise_Texture_002.inputs["Distortion"].default_value = 0.0
        Mapping_002 = nt.nodes.new("ShaderNodeMapping")
        Mapping_002.location = (-216.5802764892578, 439.599365234375)
        Mapping_002.vector_type = "POINT"
        Mapping_002.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping_002.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_002.inputs["Scale"].default_value = (450.0, 450.0, 450.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-612.101318359375, 453.23260498046875)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (596.834228515625, 889.9492797851562)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MULTIPLY"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1637.5155029296875, 411.2171630859375)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1402.8897705078125, 375.63250732421875)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "OVERLAY"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (1148.755126953125, 109.32256317138672)
        Mix.data_type = "RGBA"
        Mix.blend_type = "OVERLAY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (930.453369140625, 200.7408447265625)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (760.275390625, 78.90968322753906)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (648.5368041992188, 588.137939453125)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (818.7147827148438, 709.9691162109375)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 0.5
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (217.14248657226562, 501.28955078125)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (1013.916259765625, 885.3092041015625)
        # Create links
        nt.links.new(Group_Input.outputs["Size"], Noise_Texture.inputs["Scale"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Builder"])
        nt.links.new(Noise_Texture.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture.inputs["Vector"])
        nt.links.new(ColorRamp.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Noise_Texture_001.outputs["Color"], ColorRamp_001.inputs["Fac"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix_001.inputs["Factor"])
        nt.links.new(Mapping_001.outputs["Vector"], Noise_Texture_001.inputs["Vector"])
        nt.links.new(ColorRamp.outputs["Color"], Mix_001.inputs["A"])
        nt.links.new(Mix_001.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Group_Input_001.outputs["Strength"], Math.inputs["Value"])
        nt.links.new(Noise_Texture_002.outputs["Color"], ColorRamp_002.inputs["Fac"])
        nt.links.new(Mapping_002.outputs["Vector"], Noise_Texture_002.inputs["Vector"])
        nt.links.new(ColorRamp_002.outputs["Color"], Mix_003.inputs["A"])
        nt.links.new(Group_Input.outputs["Size"], Noise_Texture_002.inputs["Scale"])
        nt.links.new(Mix.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Group_Input_003.outputs["Strength"], Math_001.inputs["Value"])
        nt.links.new(Mix_003.outputs["Result"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Mix_002.inputs["Factor"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix_003.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Builder"], Mix.inputs["A"])
        nt.links.new(Group_Input_001.outputs["Red Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_001.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_002.inputs["Vector"])
        nt.links.new(Group_Input_001.outputs["Blue Color"], Mix_002.inputs["B"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])