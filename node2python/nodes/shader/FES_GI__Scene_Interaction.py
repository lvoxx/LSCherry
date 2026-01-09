import bpy
import sys
from pathlib import Path

# Import utils (handle both relative and absolute imports)
try:
    from ..utils import ShaderNode
except ImportError:
    # Fallback for direct execution
    import importlib.util
    utils_path = Path(__file__).parent.parent / 'utils.py'
    spec = importlib.util.spec_from_file_location('utils', utils_path)
    utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utils)
    ShaderNode = utils.ShaderNode


class ShaderNodeFES_GI__Scene_Interaction(ShaderNode):
    bl_idname = 'ShaderNodeFES_GI__Scene_Interaction'
    bl_label = "FES_GI: Scene Interaction"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base Color"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["NormalMap"].default_value = (0.5, 0.5, 1.0, 1.0)
        self.inputs["Roughness"].default_value = 0.5
        self.inputs["Metallic"].default_value = 0.0
        self.inputs["Specular"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'FES_GI: Scene Interaction'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Emission', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('NormalMap', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Metallic', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Specular', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0

        # Build node tree
        self.rebuildNodetree(None)

    def rebuildNodetree(self, context):
        if context is not None:
            if self.node_tree.users > 1:
                self.duplicate()

        nt = self.node_tree

        # Clear existing nodes
        for node in list(nt.nodes):
            nt.nodes.remove(node)

        # Create group input/output
        GroupInput = nt.nodes.new('NodeGroupInput')
        GroupInput.location = (-400, 0)
        GroupOutput = nt.nodes.new('NodeGroupOutput')
        GroupOutput.location = (400, 0)

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (101.38098907470703, -271.2422790527344)
        Frame_001.label = "Skin shadow"
        Frame_001.name = "Frame.001"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (-465.604736328125, 605.0078125)
        Frame_003.label = "Threshold"
        Frame_003.name = "Frame.003"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-579.748779296875, 952.8850708007812)
        Frame.label = "Old threshold reference"
        Frame.name = "Frame"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (450.2518615722656, -478.066162109375)
        Frame_005.label = "Saturation threshold"
        Frame_005.name = "Frame.005"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (91.34136962890625, -282.8273620605469)
        Frame_006.label = "Camera-based threshold (connect to Add node)"
        Frame_006.name = "Frame.006"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (46.763427734375, 42.5770263671875)
        Frame_002.label = "Regular threshold (connect to Add node)"
        Frame_002.name = "Frame.002"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (126.33084106445312, -236.13287353515625)
        Frame_004.label = "Camera-based threshold (connect to Add node)"
        Frame_004.name = "Frame.004"

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (54.069244384765625, 40.13958740234375)
        Frame_007.label = "Regular threshold (connect to Add node)"
        Frame_007.name = "Frame.007"

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (79.74908447265625, 89.97789001464844)
        Shader_to_RGB.name = "Shader to RGB"

        Diffuse_BSDF = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF.location = (-119.14013671875, 62.84724044799805)
        Diffuse_BSDF.name = "Diffuse BSDF"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (238.96055603027344, 123.51708984375)
        ColorRamp.name = "ColorRamp"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (453.2306213378906, 215.9006805419922)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'ADD'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-269.32891845703125, 137.32728576660156)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1181.9190673828125, -82.55907440185547)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (704.4492797851562, -98.35372161865234)
        Hue_Saturation_Value.name = "Hue Saturation Value"

        RGB_Curves_002 = nt.nodes.new('ShaderNodeRGBCurve')
        RGB_Curves_002.location = (-218.51947021484375, 48.40130615234375)
        RGB_Curves_002.name = "RGB Curves.002"

        Layer_Weight_002 = nt.nodes.new('ShaderNodeLayerWeight')
        Layer_Weight_002.location = (-383.14251708984375, 14.54913330078125)
        Layer_Weight_002.name = "Layer Weight.002"

        Shader_to_RGB_001 = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB_001.location = (-32.14910888671875, -51.34002685546875)
        Shader_to_RGB_001.name = "Shader to RGB.001"

        Diffuse_BSDF_001 = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF_001.location = (-325.3837890625, -16.66668701171875)
        Diffuse_BSDF_001.name = "Diffuse BSDF.001"

        RGB_Curves_001 = nt.nodes.new('ShaderNodeRGBCurve')
        RGB_Curves_001.location = (-218.51947021484375, 48.40130615234375)
        RGB_Curves_001.name = "RGB Curves.001"

        Layer_Weight_001 = nt.nodes.new('ShaderNodeLayerWeight')
        Layer_Weight_001.location = (-383.14251708984375, 14.54913330078125)
        Layer_Weight_001.name = "Layer Weight.001"

        ColorRamp_002 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_002.location = (110.77627563476562, 31.057647705078125)
        ColorRamp_002.name = "ColorRamp.002"

        ColorRamp_003 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_003.location = (57.312713623046875, 2.509857177734375)
        ColorRamp_003.name = "ColorRamp.003"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (2252.60205078125, 43.44681930541992)
        Mix_Shader.name = "Mix Shader"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (1553.8638916015625, -95.7667236328125)
        Emission.name = "Emission"

        ColorRamp_008 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_008.location = (184.7190399169922, 25.6153564453125)
        ColorRamp_008.name = "ColorRamp.008"

        Diffuse_BSDF_002 = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF_002.location = (-325.3837890625, -16.66668701171875)
        Diffuse_BSDF_002.name = "Diffuse BSDF.002"

        Shader_to_RGB_002 = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB_002.location = (-76.42486572265625, -50.740997314453125)
        Shader_to_RGB_002.name = "Shader to RGB.002"

        ColorRamp_009 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_009.location = (141.92010498046875, 28.53045654296875)
        ColorRamp_009.name = "ColorRamp.009"

        Normal_Map = nt.nodes.new('ShaderNodeNormalMap')
        Normal_Map.location = (1414.9747314453125, -730.3173828125)
        Normal_Map.name = "Normal Map"

        Principled_BSDF = nt.nodes.new('ShaderNodeBsdfPrincipled')
        Principled_BSDF.location = (1741.7601318359375, -242.10362243652344)
        Principled_BSDF.name = "Principled BSDF"

        # Create internal links
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[7])
        nt.links.new(Diffuse_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Shader_to_RGB.outputs[0], ColorRamp.inputs[0])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(Diffuse_BSDF_001.outputs[0], Shader_to_RGB_001.inputs[0])
        nt.links.new(Layer_Weight_001.outputs[0], RGB_Curves_001.inputs[1])
        nt.links.new(RGB_Curves_001.outputs[0], ColorRamp_002.inputs[0])
        nt.links.new(Shader_to_RGB_001.outputs[0], ColorRamp_008.inputs[0])
        nt.links.new(Diffuse_BSDF_002.outputs[0], Shader_to_RGB_002.inputs[0])
        nt.links.new(Layer_Weight_002.outputs[0], RGB_Curves_002.inputs[1])
        nt.links.new(RGB_Curves_002.outputs[0], ColorRamp_003.inputs[0])
        nt.links.new(Shader_to_RGB_002.outputs[0], ColorRamp_009.inputs[0])
        nt.links.new(Hue_Saturation_Value.outputs[0], Mix_002.inputs[7])
        nt.links.new(Mix_001.outputs[2], Hue_Saturation_Value.inputs[4])
        nt.links.new(Mix_001.outputs[2], Mix_002.inputs[6])
        nt.links.new(Mix_002.outputs[2], Emission.inputs[0])
        nt.links.new(Emission.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Principled_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(GroupInput.outputs[0], Principled_BSDF.inputs[0])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[1], Normal_Map.inputs[1])
        nt.links.new(GroupInput.outputs[2], Principled_BSDF.inputs[2])
        nt.links.new(GroupInput.outputs[3], Principled_BSDF.inputs[1])
        nt.links.new(ColorRamp_008.outputs[0], Mix_001.inputs[0])
        nt.links.new(ColorRamp_009.outputs[0], Mix_002.inputs[0])
        nt.links.new(Normal_Map.outputs[0], Principled_BSDF.inputs[5])

        # Set default values
        Diffuse_BSDF.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF.inputs[1].default_value = 0.0
        Diffuse_BSDF.inputs[2].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF.inputs[3].default_value = 0.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[0].default_value = 0.6666663289070129
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[7].default_value = (0.4782622754573822, 0.47619470953941345, 0.7479339241981506, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[1].default_value = 4.0
        Hue_Saturation_Value.inputs[2].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        RGB_Curves_002.inputs[0].default_value = 1.0
        Layer_Weight_002.inputs[0].default_value = 0.5
        Layer_Weight_002.inputs[1].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF_001.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF_001.inputs[1].default_value = 0.0
        Diffuse_BSDF_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF_001.inputs[3].default_value = 0.0
        RGB_Curves_001.inputs[0].default_value = 1.0
        Layer_Weight_001.inputs[0].default_value = 0.5
        Layer_Weight_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Mix_Shader.inputs[0].default_value = 0.10000000149011612
        Emission.inputs[1].default_value = 1.0
        Emission.inputs[2].default_value = 0.0
        Diffuse_BSDF_002.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF_002.inputs[1].default_value = 0.0
        Diffuse_BSDF_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF_002.inputs[3].default_value = 0.0
        Normal_Map.inputs[0].default_value = 1.0
        Principled_BSDF.inputs[3].default_value = 1.4500000476837158
        Principled_BSDF.inputs[4].default_value = 1.0
        Principled_BSDF.inputs[6].default_value = 0.0
        Principled_BSDF.inputs[7].default_value = 0.0
        Principled_BSDF.inputs[8].default_value = 0.0
        Principled_BSDF.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
        Principled_BSDF.inputs[10].default_value = 0.05000000074505806
        Principled_BSDF.inputs[11].default_value = 1.399999976158142
        Principled_BSDF.inputs[12].default_value = 0.0
        Principled_BSDF.inputs[13].default_value = 0.0
        Principled_BSDF.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs[15].default_value = 0.0
        Principled_BSDF.inputs[16].default_value = 0.0
        Principled_BSDF.inputs[17].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs[18].default_value = 0.0
        Principled_BSDF.inputs[19].default_value = 0.0
        Principled_BSDF.inputs[20].default_value = 0.029999999329447746
        Principled_BSDF.inputs[21].default_value = 1.5
        Principled_BSDF.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs[23].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs[24].default_value = 0.0
        Principled_BSDF.inputs[25].default_value = 0.5
        Principled_BSDF.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
        Principled_BSDF.inputs[28].default_value = 1.0
        Principled_BSDF.inputs[29].default_value = 0.0
        Principled_BSDF.inputs[30].default_value = 1.3300000429153442

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
