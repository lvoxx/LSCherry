import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Veins(ShaderNode):
    bl_label = "SST1: Veins"
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
            Blue_Color_socket = nt.interface.new_socket(
                name="Blue Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Blue_Color_socket.default_value = (0.35572776198387146, 0.082790806889534, 0.800000011920929, 1.0)
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 1.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 100.0
        Scale_socket.subtype = "NONE"
            Mask_Scale_socket = nt.interface.new_socket(
                name="Mask Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mask_Scale_socket.default_value = 7.0
        Mask_Scale_socket.min_value = 0.0
        Mask_Scale_socket.max_value = 100.0
        Mask_Scale_socket.subtype = "NONE"
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
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (-406.425537109375, 100.4263916015625)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Scale"].default_value = 38.599998474121094
        Noise_Texture.inputs["Detail"].default_value = 2.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-603.987060546875, 72.609130859375)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.09999999403953552, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Noise_Texture_001 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_001.location = (39.596435546875, 194.2781982421875)
        Noise_Texture_001.inputs["W"].default_value = 0.0
        Noise_Texture_001.inputs["Scale"].default_value = 50.0
        Noise_Texture_001.inputs["Detail"].default_value = 2.0
        Noise_Texture_001.inputs["Roughness"].default_value = 0.5
        Noise_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_001.inputs["Offset"].default_value = 0.0
        Noise_Texture_001.inputs["Gain"].default_value = 1.0
        Noise_Texture_001.inputs["Distortion"].default_value = 0.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1107.0045166015625, -133.71278381347656)
        ColorRamp_002 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_002.location = (271.8576965332031, 471.7603454589844)
        ColorRamp_002.color_ramp.color_mode = "RGB"
        Noise_Texture_002 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_002.location = (36.507564544677734, 497.9704895019531)
        Noise_Texture_002.inputs["W"].default_value = 0.0
        Noise_Texture_002.inputs["Detail"].default_value = 2.0
        Noise_Texture_002.inputs["Roughness"].default_value = 0.5
        Noise_Texture_002.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_002.inputs["Offset"].default_value = 0.0
        Noise_Texture_002.inputs["Gain"].default_value = 1.0
        Noise_Texture_002.inputs["Distortion"].default_value = 0.0
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (684.0132446289062, 170.9726104736328)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0, 1.0)
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (263.0909118652344, 188.2017364501953)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1557.9462890625, -37.04841613769531)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1782.6136474609375, -42.81689453125)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-394.78387451171875, 364.64447021484375)
        Voronoi_Texture = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture.location = (323.5619812011719, -326.6441345214844)
        Voronoi_Texture.inputs["W"].default_value = 0.0
        Voronoi_Texture.inputs["Scale"].default_value = 5.0
        Voronoi_Texture.inputs["Detail"].default_value = 0.0
        Voronoi_Texture.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture.inputs["Randomness"].default_value = 1.0
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (526.8511352539062, -304.5538635253906)
        ColorRamp.color_ramp.color_mode = "RGB"
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (907.9888305664062, 152.14817810058594)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0, 1.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (1314.5264892578125, 44.909603118896484)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-849.4810791015625, -206.96209716796875)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (1089.93603515625, -124.26397705078125)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (908.6856079101562, 328.4031677246094)
        # Create links
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Builder"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping.inputs["Scale"])
        nt.links.new(Voronoi_Texture.outputs["Distance"], ColorRamp.inputs["Fac"])
        nt.links.new(Noise_Texture.outputs["Color"], Voronoi_Texture.inputs["Vector"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture.inputs["Vector"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture_001.inputs["Vector"])
        nt.links.new(ColorRamp.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Mix_001.outputs["Result"], Mix.inputs["Factor"])
        nt.links.new(Noise_Texture_001.outputs["Color"], ColorRamp_001.inputs["Fac"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix_001.inputs["A"])
        nt.links.new(Noise_Texture_002.outputs["Color"], ColorRamp_002.inputs["Fac"])
        nt.links.new(ColorRamp_002.outputs["Color"], Mix_001.inputs["Factor"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture_002.inputs["Vector"])
        nt.links.new(Math.outputs["Value"], Mix_002.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Mask Scale"], Noise_Texture_002.inputs["Scale"])
        nt.links.new(Mix.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["Y"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["Z"])
        nt.links.new(Group_Input_003.outputs["Builder"], Mix_002.inputs["A"])
        nt.links.new(Group_Input_003.outputs["Blue Color"], Mix_002.inputs["B"])
        nt.links.new(Group_Input_003.outputs["Strength"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])