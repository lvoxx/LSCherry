import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Moles(ShaderNode):
    bl_label = "SST1: Moles"
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
        
        Red_Color_socket.default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 75.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 1000.0999755859375
        Scale_socket.subtype = "NONE"
            Threadhold_socket = nt.interface.new_socket(
                name="Threadhold",
                in_out="INPUT",
                socket_type="NodeSocketInt"
            )
        
        Threadhold_socket.default_value = 0
        Threadhold_socket.min_value = 0
        Threadhold_socket.max_value = 1000
        Threadhold_socket.subtype = "NONE"
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (838.1542358398438, 75.11792755126953)
        Voronoi_Texture = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture.location = (-787.4796752929688, 299.2722473144531)
        Voronoi_Texture.inputs["W"].default_value = 0.0
        Voronoi_Texture.inputs["Detail"].default_value = 0.0
        Voronoi_Texture.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture.inputs["Randomness"].default_value = 1.0
        Voronoi_Texture_001 = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture_001.location = (-792.2933959960938, 670.41943359375)
        Voronoi_Texture_001.inputs["W"].default_value = 0.0
        Voronoi_Texture_001.inputs["Detail"].default_value = 0.0
        Voronoi_Texture_001.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture_001.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture_001.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture_001.inputs["Randomness"].default_value = 1.0
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (-613.2284545898438, 609.3649291992188)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-967.4796752929688, 259.2722473144531)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.7999999523162842, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Scale"].default_value = (1.5, 1.0, 1.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-271.3526611328125, 397.8365783691406)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mapping_001 = nt.nodes.new("ShaderNodeMapping")
        Mapping_001.location = (-972.2932739257812, 630.41943359375)
        Mapping_001.vector_type = "POINT"
        Mapping_001.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Scale"].default_value = (1.2000000476837158, 1.8000000715255737, 1.2000000476837158)
        Mapping_002 = nt.nodes.new("ShaderNodeMapping")
        Mapping_002.location = (-958.6446533203125, 751.018798828125)
        Mapping_002.vector_type = "POINT"
        Mapping_002.inputs["Location"].default_value = (0.09999999403953552, 0.0, 0.0)
        Mapping_002.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_002.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (-453.0848693847656, 1043.5096435546875)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Detail"].default_value = 2.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (-587.3325805664062, 272.9144287109375)
        ColorRamp.color_ramp.color_mode = "RGB"
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (561.3139038085938, 11.55462646484375)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1490.2750244140625, 234.89669799804688)
        Invert = nt.nodes.new("ShaderNodeInvert")
        Invert.location = (-24.335580825805664, 139.37413024902344)
        Invert.inputs["Fac"].default_value = 1.0
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (294.0952453613281, 221.1226043701172)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        ColorRamp_002 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_002.location = (-210.730224609375, 999.4328002929688)
        ColorRamp_002.color_ramp.color_mode = "RGB"
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (90.96469116210938, 643.0156860351562)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-670.0914306640625, 760.6842651367188)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (278.703125, -152.36697387695312)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (481.33123779296875, 759.0723266601562)
        # Create links
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Builder"])
        nt.links.new(Group_Input.outputs["Scale"], Voronoi_Texture_001.inputs["Scale"])
        nt.links.new(Group_Input.outputs["Scale"], Voronoi_Texture.inputs["Scale"])
        nt.links.new(Voronoi_Texture.outputs["Distance"], ColorRamp.inputs["Fac"])
        nt.links.new(Mapping.outputs["Vector"], Voronoi_Texture.inputs["Vector"])
        nt.links.new(Voronoi_Texture_001.outputs["Distance"], ColorRamp_001.inputs["Fac"])
        nt.links.new(Mapping_001.outputs["Vector"], Voronoi_Texture_001.inputs["Vector"])
        nt.links.new(ColorRamp.outputs["Color"], Mix.inputs["B"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix.inputs["A"])
        nt.links.new(ColorRamp.outputs["Color"], Mix.inputs["B"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["A"])
        nt.links.new(Mapping_002.outputs["Vector"], Noise_Texture.inputs["Vector"])
        nt.links.new(Noise_Texture.outputs["Color"], ColorRamp_002.inputs["Fac"])
        nt.links.new(Invert.outputs["Color"], Mix_002.inputs["B"])
        nt.links.new(ColorRamp_002.outputs["Color"], Math.inputs["Value"])
        nt.links.new(Mix.outputs["Result"], Invert.inputs["Color"])
        nt.links.new(Mix_002.outputs["Result"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Threadhold"], Math.inputs["Value"])
        nt.links.new(Group_Input_002.outputs["Builder"], Mix_001.inputs["A"])
        nt.links.new(Group_Input_002.outputs["Red Color"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_001.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_002.inputs["Vector"])
        nt.links.new(Group_Input_001.outputs["Threadhold"], Noise_Texture.inputs["Scale"])
        nt.links.new(ColorRamp_002.outputs["Color"], Mix_002.inputs["Factor"])