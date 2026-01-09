import bpy
from ..utils import ShaderNode


class ShaderNodeSst1SkinBump(ShaderNode):
    bl_label = "SST1: Skin Bump"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Input sockets
            Pores_(require)_socket = nt.interface.new_socket(
                name="Pores (require)",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Pores_(require)_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Goose_Bumps_socket = nt.interface.new_socket(
                name="Goose Bumps",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Goose_Bumps_socket.default_value = 0.0
        Goose_Bumps_socket.min_value = 0.0
        Goose_Bumps_socket.max_value = 1.0
        Goose_Bumps_socket.subtype = "FACTOR"
            Details_socket = nt.interface.new_socket(
                name="Details",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Details_socket.default_value = 0.30000001192092896
        Details_socket.min_value = 0.0
        Details_socket.max_value = 1.0
        Details_socket.subtype = "FACTOR"
            Skin_Scale_socket = nt.interface.new_socket(
                name="Skin Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Skin_Scale_socket.default_value = 9.0
        Skin_Scale_socket.min_value = 0.0
        Skin_Scale_socket.max_value = 1000.0
        Skin_Scale_socket.subtype = "NONE"
            Noise_Scale_socket = nt.interface.new_socket(
                name="Noise Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Noise_Scale_socket.default_value = 50.0
        Noise_Scale_socket.min_value = 0.0
        Noise_Scale_socket.max_value = 1000.0
        Noise_Scale_socket.subtype = "NONE"
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        ColorRamp_005 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_005.location = (68.5015869140625, -249.48028564453125)
        ColorRamp_005.color_ramp.color_mode = "RGB"
        ColorRamp_006 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_006.location = (69.91107177734375, 4.5892333984375)
        ColorRamp_006.color_ramp.color_mode = "RGB"
        ColorRamp_004 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_004.location = (89.59808349609375, 248.72756958007812)
        ColorRamp_004.color_ramp.color_mode = "RGB"
        Mix_007 = nt.nodes.new("ShaderNodeMix")
        Mix_007.location = (427.24053955078125, 78.65878295898438)
        Mix_007.data_type = "RGBA"
        Mix_007.blend_type = "MULTIPLY"
        Mix_007.inputs["Factor"].default_value = 1.0
        Mix_007.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs["A"].default_value = 0.0
        Mix_007.inputs["B"].default_value = 0.0
        Mix_007.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-393.5880126953125, 408.3785705566406)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (786.3019409179688, 180.87889099121094)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MULTIPLY"
        Mix_005.inputs["Factor"].default_value = 1.0
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (768.5088500976562, 444.6479187011719)
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (128.5283966064453, 530.4926147460938)
        ColorRamp.color_ramp.color_mode = "RGB"
        Noise_Texture_002 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_002.location = (-139.1096649169922, 530.7962036132812)
        Noise_Texture_002.inputs["W"].default_value = 0.0
        Noise_Texture_002.inputs["Detail"].default_value = 2.0
        Noise_Texture_002.inputs["Roughness"].default_value = 0.5
        Noise_Texture_002.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_002.inputs["Offset"].default_value = 0.0
        Noise_Texture_002.inputs["Gain"].default_value = 1.0
        Noise_Texture_002.inputs["Distortion"].default_value = 0.0
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (-141.70558166503906, 239.77838134765625)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Scale"].default_value = 600.0
        Noise_Texture.inputs["Detail"].default_value = 2.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        Mapping_001 = nt.nodes.new("ShaderNodeMapping")
        Mapping_001.location = (-547.6753540039062, 37.490234375)
        Mapping_001.vector_type = "POINT"
        Mapping_001.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Voronoi_Texture = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture.location = (-135.90493774414062, -51.195247650146484)
        Voronoi_Texture.inputs["W"].default_value = 0.0
        Voronoi_Texture.inputs["Scale"].default_value = 550.0
        Voronoi_Texture.inputs["Detail"].default_value = 0.0
        Voronoi_Texture.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture.inputs["Randomness"].default_value = 1.0
        Noise_Texture_001 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_001.location = (-140.345947265625, -326.91839599609375)
        Noise_Texture_001.inputs["W"].default_value = 0.0
        Noise_Texture_001.inputs["Scale"].default_value = 500.0
        Noise_Texture_001.inputs["Detail"].default_value = 2.0
        Noise_Texture_001.inputs["Roughness"].default_value = 0.5
        Noise_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_001.inputs["Offset"].default_value = 0.0
        Noise_Texture_001.inputs["Gain"].default_value = 1.0
        Noise_Texture_001.inputs["Distortion"].default_value = 0.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1034.840576171875, -195.56600952148438)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1640.5115966796875, 363.211181640625)
        Mix_006 = nt.nodes.new("ShaderNodeMix")
        Mix_006.location = (1016.4611206054688, 398.5201110839844)
        Mix_006.data_type = "RGBA"
        Mix_006.blend_type = "MIX"
        Mix_006.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs["A"].default_value = 0.0
        Mix_006.inputs["B"].default_value = 0.0
        Mix_006.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Bump = nt.nodes.new("ShaderNodeBump")
        Bump.location = (1216.7667236328125, 404.4734802246094)
        Bump.inputs["Strength"].default_value = 0.125
        Bump.inputs["Distance"].default_value = 1.0
        Bump.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Bump_001 = nt.nodes.new("ShaderNodeBump")
        Bump_001.location = (1390.9560546875, 406.4095153808594)
        Bump_001.inputs["Strength"].default_value = 0.15000000596046448
        Bump_001.inputs["Distance"].default_value = 1.0
        Invert = nt.nodes.new("ShaderNodeInvert")
        Invert.location = (1203.473388671875, 225.90773010253906)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (1018.8739013671875, 145.30740356445312)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-782.0856323242188, -209.17237854003906)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (190.92507934570312, 628.4528198242188)
        # Create links
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping_001.inputs["Scale"])
        nt.links.new(Noise_Texture.outputs["Color"], ColorRamp_004.inputs["Fac"])
        nt.links.new(Voronoi_Texture.outputs["Distance"], ColorRamp_006.inputs["Fac"])
        nt.links.new(Mapping_001.outputs["Vector"], Noise_Texture_001.inputs["Vector"])
        nt.links.new(Noise_Texture_001.outputs["Color"], ColorRamp_005.inputs["Fac"])
        nt.links.new(ColorRamp_006.outputs["Color"], Mix_007.inputs["B"])
        nt.links.new(ColorRamp_005.outputs["Color"], Mix_007.inputs["A"])
        nt.links.new(Mix_007.outputs["Result"], Mix_005.inputs["A"])
        nt.links.new(ColorRamp_004.outputs["Color"], Mix_005.inputs["B"])
        nt.links.new(Mapping_001.outputs["Vector"], Noise_Texture.inputs["Vector"])
        nt.links.new(Mapping_001.outputs["Vector"], Voronoi_Texture.inputs["Vector"])
        nt.links.new(Mapping_001.outputs["Vector"], Noise_Texture_002.inputs["Vector"])
        nt.links.new(Mix_005.outputs["Result"], Mix_006.inputs["A"])
        nt.links.new(ColorRamp.outputs["Color"], Mix_006.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Noise Scale"], Noise_Texture_002.inputs["Scale"])
        nt.links.new(Group_Input_002.outputs["Details"], Mix_006.inputs["Factor"])
        nt.links.new(Noise_Texture_002.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(Mix_006.outputs["Result"], Bump.inputs["Height"])
        nt.links.new(Bump_001.outputs["Normal"], Group_Output.inputs["Normal"])
        nt.links.new(Invert.outputs["Color"], Bump_001.inputs["Height"])
        nt.links.new(Bump.outputs["Normal"], Bump_001.inputs["Normal"])
        nt.links.new(Group_Input_003.outputs["Pores (require)"], Invert.inputs["Color"])
        nt.links.new(Group_Input_003.outputs["Goose Bumps"], Invert.inputs["Fac"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_001.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Skin Scale"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input.outputs["Skin Scale"], Combine_XYZ.inputs["Y"])
        nt.links.new(Group_Input.outputs["Skin Scale"], Combine_XYZ.inputs["Z"])