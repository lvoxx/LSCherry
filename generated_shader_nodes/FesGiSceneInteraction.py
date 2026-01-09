import bpy
from ..utils import ShaderNode


class ShaderNodeFesGiSceneInteraction(ShaderNode):
    bl_label = "FES_GI: Scene Interaction"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            Emission_socket = nt.interface.new_socket(
                name="Emission",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            NormalMap_socket = nt.interface.new_socket(
                name="NormalMap",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        NormalMap_socket.default_value = (0.5, 0.5, 1.0, 1.0)
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.5
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Metallic_socket = nt.interface.new_socket(
                name="Metallic",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metallic_socket.default_value = 0.0
        Metallic_socket.min_value = 0.0
        Metallic_socket.max_value = 1.0
        Metallic_socket.subtype = "FACTOR"
            Specular_socket = nt.interface.new_socket(
                name="Specular",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Specular_socket.default_value = 0.0
        Specular_socket.min_value = 0.0
        Specular_socket.max_value = 1.0
        Specular_socket.subtype = "FACTOR"

        # Create nodes
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (101.38098907470703, -271.2422790527344)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-465.604736328125, 605.0078125)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-579.748779296875, 952.8850708007812)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (450.2518615722656, -478.066162109375)
        Frame_006 = nt.nodes.new("NodeFrame")
        Frame_006.location = (91.34136962890625, -282.8273620605469)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (46.763427734375, 42.5770263671875)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (126.33084106445312, -236.13287353515625)
        Frame_007 = nt.nodes.new("NodeFrame")
        Frame_007.location = (54.069244384765625, 40.13958740234375)
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (79.74908447265625, 89.97789001464844)
        Diffuse_BSDF = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF.location = (-119.14013671875, 62.84724044799805)
        Diffuse_BSDF.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF.inputs["Weight"].default_value = 0.0
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (238.96055603027344, 123.51708984375)
        ColorRamp.color_ramp.color_mode = "RGB"
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (453.2306213378906, 215.9006805419922)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "ADD"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-269.32891845703125, 137.32728576660156)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = 0.6666663289070129
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.4782622754573822, 0.47619470953941345, 0.7479339241981506, 1.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1181.9190673828125, -82.55907440185547)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Hue_Saturation_Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue_Saturation_Value.location = (704.4492797851562, -98.35372161865234)
        Hue_Saturation_Value.inputs["Hue"].default_value = 0.5
        Hue_Saturation_Value.inputs["Saturation"].default_value = 4.0
        Hue_Saturation_Value.inputs["Value"].default_value = 1.0
        Hue_Saturation_Value.inputs["Fac"].default_value = 1.0
        RGB_Curves_002 = nt.nodes.new("ShaderNodeRGBCurve")
        RGB_Curves_002.location = (-218.51947021484375, 48.40130615234375)
        RGB_Curves_002.inputs["Fac"].default_value = 1.0
        Layer_Weight_002 = nt.nodes.new("ShaderNodeLayerWeight")
        Layer_Weight_002.location = (-383.14251708984375, 14.54913330078125)
        Layer_Weight_002.inputs["Blend"].default_value = 0.5
        Layer_Weight_002.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Shader_to_RGB_001 = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB_001.location = (-32.14910888671875, -51.34002685546875)
        Diffuse_BSDF_001 = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF_001.location = (-325.3837890625, -16.66668701171875)
        Diffuse_BSDF_001.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF_001.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF_001.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF_001.inputs["Weight"].default_value = 0.0
        RGB_Curves_001 = nt.nodes.new("ShaderNodeRGBCurve")
        RGB_Curves_001.location = (-218.51947021484375, 48.40130615234375)
        RGB_Curves_001.inputs["Fac"].default_value = 1.0
        Layer_Weight_001 = nt.nodes.new("ShaderNodeLayerWeight")
        Layer_Weight_001.location = (-383.14251708984375, 14.54913330078125)
        Layer_Weight_001.inputs["Blend"].default_value = 0.5
        Layer_Weight_001.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        ColorRamp_002 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_002.location = (110.77627563476562, 31.057647705078125)
        ColorRamp_002.color_ramp.color_mode = "RGB"
        ColorRamp_003 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_003.location = (57.312713623046875, 2.509857177734375)
        ColorRamp_003.color_ramp.color_mode = "RGB"
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (2252.60205078125, 43.44681930541992)
        Mix_Shader.inputs["Fac"].default_value = 0.10000000149011612
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (1553.8638916015625, -95.7667236328125)
        Emission.inputs["Strength"].default_value = 1.0
        Emission.inputs["Weight"].default_value = 0.0
        ColorRamp_008 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_008.location = (184.7190399169922, 25.6153564453125)
        ColorRamp_008.color_ramp.color_mode = "RGB"
        Diffuse_BSDF_002 = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF_002.location = (-325.3837890625, -16.66668701171875)
        Diffuse_BSDF_002.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF_002.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF_002.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF_002.inputs["Weight"].default_value = 0.0
        Shader_to_RGB_002 = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB_002.location = (-76.42486572265625, -50.740997314453125)
        ColorRamp_009 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_009.location = (141.92010498046875, 28.53045654296875)
        ColorRamp_009.color_ramp.color_mode = "RGB"
        Normal_Map = nt.nodes.new("ShaderNodeNormalMap")
        Normal_Map.location = (1414.9747314453125, -730.3173828125)
        Normal_Map.inputs["Strength"].default_value = 1.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-589.8997192382812, -618.329345703125)
        Principled_BSDF = nt.nodes.new("ShaderNodeBsdfPrincipled")
        Principled_BSDF.location = (1741.7601318359375, -242.10362243652344)
        Principled_BSDF.inputs["IOR"].default_value = 1.4500000476837158
        Principled_BSDF.inputs["Alpha"].default_value = 1.0
        Principled_BSDF.inputs["Weight"].default_value = 0.0
        Principled_BSDF.inputs["Diffuse Roughness"].default_value = 0.0
        Principled_BSDF.inputs["Subsurface Weight"].default_value = 0.0
        Principled_BSDF.inputs["Subsurface Radius"].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
        Principled_BSDF.inputs["Subsurface Scale"].default_value = 0.05000000074505806
        Principled_BSDF.inputs["Subsurface IOR"].default_value = 1.399999976158142
        Principled_BSDF.inputs["Subsurface Anisotropy"].default_value = 0.0
        Principled_BSDF.inputs["Specular IOR Level"].default_value = 0.0
        Principled_BSDF.inputs["Specular Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs["Anisotropic"].default_value = 0.0
        Principled_BSDF.inputs["Anisotropic Rotation"].default_value = 0.0
        Principled_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs["Transmission Weight"].default_value = 0.0
        Principled_BSDF.inputs["Coat Weight"].default_value = 0.0
        Principled_BSDF.inputs["Coat Roughness"].default_value = 0.029999999329447746
        Principled_BSDF.inputs["Coat IOR"].default_value = 1.5
        Principled_BSDF.inputs["Coat Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs["Coat Normal"].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs["Sheen Weight"].default_value = 0.0
        Principled_BSDF.inputs["Sheen Roughness"].default_value = 0.5
        Principled_BSDF.inputs["Sheen Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        Principled_BSDF.inputs["Emission Strength"].default_value = 1.0
        Principled_BSDF.inputs["Thin Film Thickness"].default_value = 0.0
        Principled_BSDF.inputs["Thin Film IOR"].default_value = 1.3300000429153442
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (2637.043212890625, 216.8212432861328)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (742.1223754882812, 407.61859130859375)
        # Create links
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Base Color"], Mix_001.inputs["B"])
        nt.links.new(Diffuse_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Shader_to_RGB.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["A"])
        nt.links.new(Group_Input.outputs["Base Color"], Mix.inputs["A"])
        nt.links.new(Diffuse_BSDF_001.outputs["BSDF"], Shader_to_RGB_001.inputs["Shader"])
        nt.links.new(Layer_Weight_001.outputs["Fresnel"], RGB_Curves_001.inputs["Color"])
        nt.links.new(RGB_Curves_001.outputs["Color"], ColorRamp_002.inputs["Fac"])
        nt.links.new(Shader_to_RGB_001.outputs["Color"], ColorRamp_008.inputs["Fac"])
        nt.links.new(Diffuse_BSDF_002.outputs["BSDF"], Shader_to_RGB_002.inputs["Shader"])
        nt.links.new(Layer_Weight_002.outputs["Fresnel"], RGB_Curves_002.inputs["Color"])
        nt.links.new(RGB_Curves_002.outputs["Color"], ColorRamp_003.inputs["Fac"])
        nt.links.new(Shader_to_RGB_002.outputs["Color"], ColorRamp_009.inputs["Fac"])
        nt.links.new(Hue_Saturation_Value.outputs["Color"], Mix_002.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Hue_Saturation_Value.inputs["Color"])
        nt.links.new(Mix_001.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Mix_002.outputs["Result"], Emission.inputs["Color"])
        nt.links.new(Emission.outputs["Emission"], Mix_Shader.inputs["Shader"])
        nt.links.new(Principled_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Base Color"], Principled_BSDF.inputs["Base Color"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Emission"])
        nt.links.new(Group_Input.outputs["NormalMap"], Normal_Map.inputs["Color"])
        nt.links.new(Group_Input.outputs["Roughness"], Principled_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Metallic"], Principled_BSDF.inputs["Metallic"])
        nt.links.new(ColorRamp_008.outputs["Color"], Mix_001.inputs["Factor"])
        nt.links.new(ColorRamp_009.outputs["Color"], Mix_002.inputs["Factor"])
        nt.links.new(Normal_Map.outputs["Normal"], Principled_BSDF.inputs["Normal"])