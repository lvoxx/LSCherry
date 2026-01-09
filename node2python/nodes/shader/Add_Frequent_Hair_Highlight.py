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


class ShaderNodeAdd_Frequent_Hair_Highlight(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Frequent_Hair_Highlight'
    bl_label = "Add Frequent Hair Highlight"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 1.0
        self.inputs["Combined"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Toon"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Mix High And Low Frequent"].default_value = 0.5
        self.inputs["Size"].default_value = 0.0
        self.inputs["Frequency"].default_value = 1.0
        self.inputs["Fill Gap"].default_value = 0.0
        self.inputs["Offset-Z"].default_value = 0.0
        self.inputs["Z-View Instensity"].default_value = 0.0
        self.inputs["Z-limit - top"].default_value = 0.4000000059604645
        self.inputs["Z-limit- bot"].default_value = 0.6000000238418579
        self.inputs["Planar UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Frequent Hair Highlight'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Toon', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Mix High And Low Frequent', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Frequency', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Fill Gap', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Offset-Z', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Z-View Instensity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Z-limit - top', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.4000000059604645
        input_socket = nt.interface.new_socket('Z-limit- bot', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.6000000238418579
        input_socket = nt.interface.new_socket('Planar UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)

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

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (67.27474975585938, -90.52102661132812)
        Frame.label = "Change in the z-view directio"
        Frame.name = "Frame"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (2401.167724609375, 214.02178955078125)
        Frame_003.label = "Light Mask"
        Frame_003.name = "Frame.003"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (1178.237060546875, 68.4765625)
        Frame_002.label = "Frequency Limit"
        Frame_002.name = "Frame.002"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (1937.5301513671875, 552.9666748046875)
        Frame_004.label = "Gap Mask"
        Frame_004.name = "Frame.004"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (319.7497863769531, 402.4115905761719)
        Frame_001.label = "Highlight Frequency"
        Frame_001.name = "Frame.001"

        Separate_XYZ_001 = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ_001.location = (91.67711639404297, -97.78819274902344)
        Separate_XYZ_001.name = "Separate XYZ.001"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (316.1763000488281, -63.783966064453125)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-901.0721435546875, -395.74884033203125)
        Combine_XYZ.name = "Combine XYZ"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (672.839599609375, 10.947555541992188)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (892.839599609375, 6.9261474609375)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'ADD'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (453.143310546875, -5.1380157470703125)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (750.570556640625, 52.86041259765625)
        Math.name = "Math"
        Math.operation = 'ADD'

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (191.312255859375, -176.08584594726562)
        Map_Range_001.name = "Map Range.001"

        Math_005 = nt.nodes.new('ShaderNodeMath')
        Math_005.location = (-22.70556640625, -414.4844970703125)
        Math_005.name = "Math.005"
        Math_005.operation = 'ADD'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (411.16314697265625, 25.117401123046875)
        Math_004.name = "Math.004"
        Math_004.operation = 'MINIMUM'

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (191.312255859375, 91.26068115234375)
        Map_Range.name = "Map Range"

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-136.16873168945312, -241.92381286621094)
        Math_003.name = "Math.003"
        Math_003.operation = 'SUBTRACT'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (107.3121337890625, -314.4951171875)
        Math_002.name = "Math.002"
        Math_002.operation = 'ADD'

        Bright_or_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Bright_or_Contrast.location = (-332.8984069824219, -232.31329345703125)
        Bright_or_Contrast.name = "Bright or Contrast"

        Noise_Texture_001 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_001.location = (-576.3134765625, 241.05685424804688)
        Noise_Texture_001.name = "Noise Texture.001"

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (-576.3134765625, -188.19239807128906)
        Noise_Texture.name = "Noise Texture"

        Bright_or_Contrast_001 = nt.nodes.new('ShaderNodeBrightContrast')
        Bright_or_Contrast_001.location = (-332.8984069824219, 144.63406372070312)
        Bright_or_Contrast_001.name = "Bright or Contrast.001"

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (-901.0721435546875, -249.64097595214844)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-690.157958984375, -50.762939453125)
        Mapping.name = "Mapping"

        Separate_XYZ = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ.location = (-491.17547607421875, 24.411346435546875)
        Separate_XYZ.name = "Separate XYZ"

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (-19.554443359375, -102.7694091796875)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-312.0650634765625, -321.73260498046875)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'MULTIPLY'

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (-128.3623504638672, -147.65667724609375)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'ADD'

        Vector_Transform_001 = nt.nodes.new('ShaderNodeVectorTransform')
        Vector_Transform_001.location = (-505.9357604980469, -305.82958984375)
        Vector_Transform_001.name = "Vector Transform.001"
        Vector_Transform_001.convert_to = 'WORLD'

        Vector_Transform = nt.nodes.new('ShaderNodeVectorTransform')
        Vector_Transform.location = (-348.9312438964844, -74.17208862304688)
        Vector_Transform.name = "Vector Transform"
        Vector_Transform.convert_to = 'CAMERA'

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (-93.420166015625, 38.51716613769531)
        ColorRamp_001.name = "ColorRamp.001"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (251.603271484375, -13.38519287109375)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        ColorRamp_002 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_002.location = (-92.369873046875, -177.6376953125)
        ColorRamp_002.name = "ColorRamp.002"

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (3514.0, 428.03900146484375)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MIX'

        # Create internal links
        nt.links.new(Math_002.outputs[0], Math.inputs[0])
        nt.links.new(Separate_XYZ_001.outputs[2], Math_001.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], Separate_XYZ_001.inputs[0])
        nt.links.new(Mapping.outputs[0], Separate_XYZ.inputs[0])
        nt.links.new(Bright_or_Contrast.outputs[0], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Math_002.inputs[1])
        nt.links.new(Separate_XYZ.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Separate_XYZ.outputs[1], Math_002.inputs[0])
        nt.links.new(Math_001.outputs[0], Math.inputs[1])
        nt.links.new(Noise_Texture.outputs[0], Bright_or_Contrast.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mapping.inputs[3])
        nt.links.new(GroupInput.outputs[6], Combine_XYZ.inputs[0])
        nt.links.new(Combine_XYZ_001.outputs[0], Mapping.inputs[1])
        nt.links.new(GroupInput.outputs[8], Combine_XYZ_001.inputs[1])
        nt.links.new(Map_Range.outputs[0], Math_004.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Math_004.inputs[1])
        nt.links.new(GroupInput.outputs[9], Math_001.inputs[1])
        nt.links.new(GroupInput.outputs[10], Map_Range.inputs[1])
        nt.links.new(GroupInput.outputs[11], Map_Range_001.inputs[2])
        nt.links.new(GroupInput.outputs[10], Math_005.inputs[0])
        nt.links.new(Math_005.outputs[0], Map_Range.inputs[2])
        nt.links.new(Math_005.outputs[0], Map_Range_001.inputs[1])
        nt.links.new(Mix_003.outputs[2], Mix.inputs[7])
        nt.links.new(Mix_005.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix_001.inputs[7])
        nt.links.new(Mix_001.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix_002.inputs[7])
        nt.links.new(ColorRamp_001.outputs[0], Mix_003.inputs[6])
        nt.links.new(ColorRamp_002.outputs[0], Mix_003.inputs[7])
        nt.links.new(GroupInput.outputs[5], Bright_or_Contrast.inputs[2])
        nt.links.new(Noise_Texture_001.outputs[0], Bright_or_Contrast_001.inputs[0])
        nt.links.new(Separate_XYZ.outputs[0], Noise_Texture_001.inputs[0])
        nt.links.new(Bright_or_Contrast_001.outputs[0], Mix_004.inputs[0])
        nt.links.new(Math.outputs[0], Map_Range.inputs[0])
        nt.links.new(Math.outputs[0], Map_Range_001.inputs[0])
        nt.links.new(Math_004.outputs[0], Mix_004.inputs[2])
        nt.links.new(Mix_004.outputs[0], ColorRamp_001.inputs[0])
        nt.links.new(Mix_004.outputs[0], ColorRamp_002.inputs[0])
        nt.links.new(GroupInput.outputs[7], Bright_or_Contrast_001.inputs[1])
        nt.links.new(GroupInput.outputs[12], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[0])
        nt.links.new(Vector_Transform_001.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Vector_Transform.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Vector_Math_001.inputs[1])
        nt.links.new(GroupInput.outputs[4], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_005.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_005.inputs[6])
        nt.links.new(Mix_002.outputs[2], Mix_005.inputs[7])

        # Set default values
        Math_001.inputs[2].default_value = 0.5
        Combine_XYZ.inputs[1].default_value = 1.0
        Combine_XYZ.inputs[2].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[0].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5
        Map_Range_001.inputs[3].default_value = 1.0
        Map_Range_001.inputs[4].default_value = 0.0
        Map_Range_001.inputs[5].default_value = 4.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_005.inputs[1].default_value = 0.10000000149011612
        Math_005.inputs[2].default_value = 0.5
        Math_004.inputs[2].default_value = 0.5
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_003.inputs[1].default_value = 0.5
        Math_003.inputs[2].default_value = 0.5
        Math_002.inputs[2].default_value = 0.5
        Bright_or_Contrast.inputs[1].default_value = 0.0
        Noise_Texture_001.inputs[1].default_value = 0.0
        Noise_Texture_001.inputs[2].default_value = 19.299999237060547
        Noise_Texture_001.inputs[3].default_value = 0.0
        Noise_Texture_001.inputs[4].default_value = 0.5416666865348816
        Noise_Texture_001.inputs[5].default_value = 2.0
        Noise_Texture_001.inputs[6].default_value = 0.0
        Noise_Texture_001.inputs[7].default_value = 1.0
        Noise_Texture_001.inputs[8].default_value = 0.0
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[2].default_value = 19.299999237060547
        Noise_Texture.inputs[3].default_value = 0.0
        Noise_Texture.inputs[4].default_value = 0.5416666865348816
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Bright_or_Contrast_001.inputs[2].default_value = 10.0
        Combine_XYZ_001.inputs[0].default_value = 0.0
        Combine_XYZ_001.inputs[2].default_value = 0.0
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Vector_Math.inputs[1].default_value = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Vector_Transform_001.inputs[0].default_value = (0.0, 0.0, 1.0)
        Vector_Transform.inputs[0].default_value = (0.0, 0.0, 1.0)
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
