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


class ShaderNodeGloTAni__Stylized_Glass(ShaderNode):
    bl_idname = 'ShaderNodeGloTAni__Stylized_Glass'
    bl_label = "GloTAni: Stylized Glass"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Factor"].default_value = 1.0
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Emission Strength"].default_value = 1.2000000476837158
        self.inputs["Fill"].default_value = 0.4000000059604645
        self.inputs["Sharpness"].default_value = 0.019999999552965164
        self.inputs["Refrection"].default_value = 0.0
        self.inputs["Opacity"].default_value = 0.5
        self.inputs["Rotation"].default_value = 45.0
        self.inputs["Density"].default_value = 6.5
        self.inputs["Seed"].default_value = 0.0
        self.inputs["Opacity"].default_value = 0.20000000298023224

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GloTAni: Stylized Glass'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.2000000476837158
        input_socket = nt.interface.new_socket('Fill', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.4000000059604645
        input_socket = nt.interface.new_socket('Sharpness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.019999999552965164
        input_socket = nt.interface.new_socket('Refrection', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Opacity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Rotation', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 45.0
        input_socket = nt.interface.new_socket('Density', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 6.5
        input_socket = nt.interface.new_socket('Seed', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Opacity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.20000000298023224

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

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (415.8453369140625, -148.1470947265625)
        Noise_Texture.name = "Noise Texture"

        Bright_or_Contrast_001 = nt.nodes.new('ShaderNodeBrightContrast')
        Bright_or_Contrast_001.location = (3228.025146484375, 449.2797546386719)
        Bright_or_Contrast_001.name = "Bright or Contrast.001"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (475.9900207519531, 3.921905517578125)
        Math_002.name = "Math.002"
        Math_002.operation = 'ADD'

        Math_008 = nt.nodes.new('ShaderNodeMath')
        Math_008.location = (664.2549438476562, 134.32598876953125)
        Math_008.name = "Math.008"
        Math_008.operation = 'MULTIPLY'

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (-251.1214599609375, -367.15228271484375)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-429.1195068359375, -367.15228271484375)
        Math_003.name = "Math.003"
        Math_003.operation = 'MULTIPLY'

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (586.6297607421875, -155.177978515625)
        ColorRamp.name = "ColorRamp"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (-152.8046875, -390.91943359375)
        Emission.name = "Emission"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (2951.715576171875, 696.888671875)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Bright_or_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Bright_or_Contrast.location = (2723.4609375, 566.465087890625)
        Bright_or_Contrast.name = "Bright or Contrast"

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (175.8458251953125, -168.1470947265625)
        Mapping_001.name = "Mapping.001"

        Combine_XYZ_002 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_002.location = (-43.6839599609375, -460.36474609375)
        Combine_XYZ_002.name = "Combine XYZ.002"

        Mapping_003 = nt.nodes.new('ShaderNodeMapping')
        Mapping_003.location = (-43.6839599609375, -146.75506591796875)
        Mapping_003.name = "Mapping.003"

        Camera_Data = nt.nodes.new('ShaderNodeCameraData')
        Camera_Data.location = (-251.1214599609375, -148.3348388671875)
        Camera_Data.name = "Camera Data"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (3455.19677734375, 696.888671875)
        Mix.name = "Mix"
        Mix.blend_type = 'ADD'

        Clamp = nt.nodes.new('ShaderNodeClamp')
        Clamp.location = (-152.8046875, -225.51312255859375)
        Clamp.name = "Clamp"

        Mix_Shader_002 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_002.location = (143.49365234375, -392.4854736328125)
        Mix_Shader_002.name = "Mix Shader.002"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-251.1214599609375, -207.2025146484375)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (1784.977783203125, -9.992034912109375)
        Frame.label = "Glass Normal"
        Frame.name = "Frame"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (-152.8046875, -506.60302734375)
        Transparent_BSDF.name = "Transparent BSDF"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (1775.5081787109375, 787.562744140625)
        Frame_001.label = "Denormalize Glass"
        Frame_001.name = "Frame.001"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (1731.8045654296875, 973.015869140625)
        Frame_002.label = "Author: Gloria_3D archive on Gumroad"
        Frame_002.name = "Frame.002"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (1731.8045654296875, 905.9319458007812)
        Frame_003.label = "Edited: Lvoxx"
        Frame_003.name = "Frame.003"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-536.6612548828125, -411.7841491699219)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-536.6612548828125, -559.9351196289062)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-92.2518310546875, -559.9351196289062)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-536.6612548828125, -411.7841491699219)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (2669.3017578125, 937.433349609375)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (2669.3017578125, 462.33099365234375)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (2639.510009765625, 596.3856201171875)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (2639.510009765625, 507.5900573730469)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (3145.336669921875, 911.6689453125)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (3145.336669921875, 345.0815124511719)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (2912.028564453125, 897.8241577148438)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (2912.028564453125, 546.0043334960938)
        Reroute_011.name = "Reroute.011"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (2723.4609375, 934.4116821289062)
        Math_001.name = "Math.001"
        Math_001.operation = 'SUBTRACT'

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (2388.1171875, 862.2290649414062)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (2388.1171875, 1001.1736450195312)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (3306.556640625, 1001.1736450195312)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (3306.556640625, 537.2256469726562)
        Reroute_015.name = "Reroute.015"

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (2738.505859375, 293.2312927246094)
        Invert_Color.name = "Invert Color"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (3179.943603515625, 662.4894409179688)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (3179.943603515625, 514.0790405273438)
        Reroute_017.name = "Reroute.017"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (4116.40869140625, 919.4625244140625)
        Frame_004.label = "Final"
        Frame_004.name = "Frame.004"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-496.68115234375, -113.6448974609375)
        Map_Range.name = "Map Range"

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (2950.85595703125, 947.5277099609375)
        Map_Range_001.name = "Map Range.001"

        Map_Range_002 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_002.location = (2449.85107421875, 972.9359130859375)
        Map_Range_002.name = "Map Range.002"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (2618.274169921875, 862.2290649414062)
        Reroute_018.name = "Reroute.018"

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (258.4005126953125, -191.30224609375)
        Texture_Coordinate.name = "Texture Coordinate"

        Separate_XYZ_004 = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ_004.location = (260.83642578125, -109.73404693603516)
        Separate_XYZ_004.name = "Separate XYZ.004"

        Map_Range_003 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_003.location = (159.02220153808594, 144.49229431152344)
        Map_Range_003.name = "Map Range.003"

        # Create internal links
        nt.links.new(Noise_Texture.outputs[1], ColorRamp.inputs[0])
        nt.links.new(Camera_Data.outputs[0], Mapping_003.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Mapping_003.outputs[0], Mapping_001.inputs[0])
        nt.links.new(Emission.outputs[0], Mix_Shader_002.inputs[1])
        nt.links.new(Clamp.outputs[0], Mix_Shader_002.inputs[0])
        nt.links.new(Mix.outputs[2], Clamp.inputs[0])
        nt.links.new(Bright_or_Contrast_001.outputs[0], Mix.inputs[7])
        nt.links.new(Mix_Shader_002.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Math_003.outputs[0], Combine_XYZ_001.inputs[2])
        nt.links.new(Combine_XYZ_001.outputs[0], Mapping_003.inputs[2])
        nt.links.new(GroupInput.outputs[7], Math_003.inputs[0])
        nt.links.new(Combine_XYZ_002.outputs[0], Mapping_001.inputs[3])
        nt.links.new(GroupInput.outputs[1], Emission.inputs[0])
        nt.links.new(GroupInput.outputs[2], Emission.inputs[1])
        nt.links.new(Bright_or_Contrast.outputs[0], Mix_003.inputs[6])
        nt.links.new(Math.outputs[0], Mapping_003.inputs[1])
        nt.links.new(Map_Range.outputs[0], Math.inputs[0])
        nt.links.new(Map_Range_003.outputs[0], Math_002.inputs[0])
        nt.links.new(Math_002.outputs[0], Math_008.inputs[1])
        nt.links.new(GroupInput.outputs[0], Math_008.inputs[0])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader_002.inputs[2])
        nt.links.new(GroupInput.outputs[8], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Combine_XYZ_002.inputs[0])
        nt.links.new(Map_Range_002.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Bright_or_Contrast.inputs[2])
        nt.links.new(ColorRamp.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Bright_or_Contrast.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Bright_or_Contrast_001.inputs[2])
        nt.links.new(Math_001.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[6], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Mix.inputs[0])
        nt.links.new(Math_008.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Invert_Color.outputs[0], Bright_or_Contrast_001.inputs[0])
        nt.links.new(Mix_003.outputs[2], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[9], Map_Range.inputs[0])
        nt.links.new(GroupInput.outputs[5], Map_Range_001.inputs[0])
        nt.links.new(GroupInput.outputs[4], Map_Range_002.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Math_001.inputs[1])
        nt.links.new(Texture_Coordinate.outputs[3], Separate_XYZ_004.inputs[0])
        nt.links.new(Separate_XYZ_004.outputs[2], Math_002.inputs[1])
        nt.links.new(GroupInput.outputs[3], Map_Range_003.inputs[0])

        # Set default values
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[2].default_value = 10.0
        Noise_Texture.inputs[3].default_value = 0.0
        Noise_Texture.inputs[4].default_value = 0.0
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = -0.10000000149011612
        Bright_or_Contrast_001.inputs[1].default_value = 0.0
        Math_002.inputs[2].default_value = 0.5
        Math_008.inputs[2].default_value = 0.5
        Combine_XYZ_001.inputs[0].default_value = 0.0
        Combine_XYZ_001.inputs[1].default_value = 0.0
        Math_003.inputs[1].default_value = 0.017400000244379044
        Math_003.inputs[2].default_value = 0.5
        Emission.inputs[2].default_value = 0.0
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Bright_or_Contrast.inputs[1].default_value = 0.0
        Mapping_001.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_001.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Combine_XYZ_002.inputs[1].default_value = 0.0
        Combine_XYZ_002.inputs[2].default_value = 0.09999999403953552
        Mapping_003.inputs[3].default_value = Vector((1.0, 1.0, 1.0))
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Clamp.inputs[1].default_value = 0.0
        Clamp.inputs[2].default_value = 1.0
        Math.inputs[1].default_value = 0.10000000149011612
        Math.inputs[2].default_value = 0.5
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0
        Reroute_003.inputs[0].default_value = 0.0
        Math_001.inputs[0].default_value = 1.0
        Math_001.inputs[2].default_value = 0.5
        Invert_Color.inputs[0].default_value = 1.0
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 200.0
        Map_Range.inputs[3].default_value = -100.0
        Map_Range.inputs[4].default_value = 100.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_001.inputs[1].default_value = 0.0
        Map_Range_001.inputs[2].default_value = 1.0
        Map_Range_001.inputs[3].default_value = 0.0
        Map_Range_001.inputs[4].default_value = 20.0
        Map_Range_001.inputs[5].default_value = 4.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_002.inputs[1].default_value = 0.0
        Map_Range_002.inputs[2].default_value = 1.0
        Map_Range_002.inputs[3].default_value = 0.0
        Map_Range_002.inputs[4].default_value = 100.0
        Map_Range_002.inputs[5].default_value = 4.0
        Map_Range_002.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_002.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_002.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_003.inputs[1].default_value = 0.0
        Map_Range_003.inputs[2].default_value = 1.0
        Map_Range_003.inputs[3].default_value = -1.0
        Map_Range_003.inputs[4].default_value = 1.0
        Map_Range_003.inputs[5].default_value = 4.0
        Map_Range_003.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_003.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_003.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
