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


class ShaderNodeSSS_Style(ShaderNode):
    bl_idname = 'ShaderNodeSSS_Style'
    bl_label = "SSS Style"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Disable SSS Style"].default_value = False
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Toon Style (If only using Toon Style)"].default_value = (0.0, 0.0, 0.0)
        self.inputs["SSS Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Smooth"].default_value = 0.15000000596046448
        self.inputs["SSS Intensity"].default_value = 5.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SSS Style'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('SSS Style', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Disable SSS Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Toon Style (If only using Toon Style)', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('SSS Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.15000000596046448
        input_socket = nt.interface.new_socket('SSS Intensity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 5.0

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
        Frame.location = (1238.00341796875, 67.6219711303711)
        Frame.label = "Args Compress"
        Frame.name = "Frame"

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (-688.0994873046875, -163.498291015625)
        Frame_007.label = "Args Extract"
        Frame_007.name = "Frame.007"

        Frame_009 = nt.nodes.new('NodeFrame')
        Frame_009.location = (140.0347900390625, 877.7711791992188)
        Frame_009.label = "Size"
        Frame_009.name = "Frame.009"

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (760.5214233398438, 296.70355224609375)
        Invert_Color.name = "Invert Color"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (956.4403076171875, 238.19834899902344)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (956.4403076171875, 122.7415542602539)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (1284.5455322265625, 327.1082458496094)
        Reroute_005.name = "Reroute.005"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (999.6919555664062, 304.1543273925781)
        Math_001.name = "Math.001"
        Math_001.operation = 'GREATER_THAN'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (1400.8521728515625, 458.9847412109375)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1188.1192626953125, 283.9954528808594)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (1662.4051513671875, 291.8478088378906)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (509.2532958984375, 244.51991271972656)
        Reroute_002.name = "Reroute.002"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (1611.4578857421875, 174.94662475585938)
        Reroute_007.name = "Reroute.007"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (619.2569580078125, 74.0623779296875)
        Reroute_018.name = "Reroute.018"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (1582.530029296875, 74.0623779296875)
        Reroute_021.name = "Reroute.021"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (1900.7923583984375, 412.13568115234375)
        Math_002.name = "Math.002"
        Math_002.operation = 'MULTIPLY'

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (252.05218505859375, 50.98263931274414)
        Reroute_031.name = "Reroute.031"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (1611.4578857421875, 879.4537353515625)
        Reroute_006.name = "Reroute.006"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (619.2569580078125, -85.91157531738281)
        Reroute_017.name = "Reroute.017"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (570.0657958984375, 362.00244140625)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (509.2532958984375, 879.4537353515625)
        Reroute_001.name = "Reroute.001"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (252.05218505859375, 264.3453674316406)
        Reroute_032.name = "Reroute.032"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (215.50836181640625, 651.8941040039062)
        Reroute_033.name = "Reroute.033"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (215.50836181640625, 27.916229248046875)
        Reroute_034.name = "Reroute.034"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (201.7791748046875, -114.72412109375)
        Combine_XYZ.name = "Combine XYZ"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (-62.09632110595703, -85.91157531738281)
        Reroute_016.name = "Reroute.016"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-26.080875396728516, 222.7157440185547)
        Reroute_011.name = "Reroute.011"

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (308.06121826171875, 353.60882568359375)
        Group_002.name = "Group.002"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (674.46728515625, 938.2427978515625)
        Reroute_008.name = "Reroute.008"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (629.43798828125, 690.698486328125)
        Reroute_020.name = "Reroute.020"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (674.46728515625, 733.836181640625)
        Reroute_009.name = "Reroute.009"

        Separate_XYZ = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ.location = (428.36224365234375, 592.2326049804688)
        Separate_XYZ.name = "Separate XYZ"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (660.0187377929688, 555.3638916015625)
        Reroute_012.name = "Reroute.012"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (626.003173828125, 534.9234619140625)
        Reroute_015.name = "Reroute.015"

        Group_017 = nt.nodes.new('ShaderNodeGroup')
        Group_017.location = (46.729736328125, -19.95025634765625)
        Group_017.name = "Group.017"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-208.1873779296875, 1078.2200927734375)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-208.1873779296875, 911.917236328125)
        Math_003.name = "Math.003"
        Math_003.operation = 'GREATER_THAN'

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-36.7691650390625, 938.2427978515625)
        Reroute_010.name = "Reroute.010"

        Separate_XYZ_001 = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ_001.location = (-207.4635009765625, 737.2314453125)
        Separate_XYZ_001.name = "Separate XYZ.001"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (-22.391357421875, 846.4981079101562)
        Group_012.name = "Group.012"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-404.0948486328125, 965.1768798828125)
        Reroute_014.name = "Reroute.014"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (-370.2911376953125, 598.7947998046875)
        Reroute_022.name = "Reroute.022"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (-370.2911376953125, 798.3321533203125)
        Reroute_023.name = "Reroute.023"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-404.0948486328125, 490.6129455566406)
        Reroute_013.name = "Reroute.013"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-404.0948486328125, 576.2481689453125)
        Reroute.name = "Reroute"

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (308.06121826171875, 140.9680633544922)
        Group_001.name = "Group.001"

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (428.22021484375, 869.1403198242188)
        Math_004.name = "Math.004"
        Math_004.operation = 'SUBTRACT'

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (629.44873046875, 833.9447021484375)
        Reroute_026.name = "Reroute.026"

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (718.3782958984375, 850.16357421875)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (2253.012939453125, 184.26473999023438)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MIX'

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (2093.28125, 879.4537353515625)
        Reroute_019.name = "Reroute.019"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (2093.28125, 48.293128967285156)
        Reroute_024.name = "Reroute.024"

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (2212.6728515625, 409.2442321777344)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MIX'

        # Create internal links
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_011.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_031.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Reroute_032.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Mix_001.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Reroute_003.outputs[0], Math_001.inputs[0])
        nt.links.new(Invert_Color.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix_002.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Mix_002.inputs[3])
        nt.links.new(Mix_001.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Mix_002.outputs[0], Mix.inputs[7])
        nt.links.new(Reroute_005.outputs[0], Mix.inputs[0])
        nt.links.new(Mix.outputs[2], Math_002.inputs[0])
        nt.links.new(GroupInput.outputs[5], Mix_003.inputs[2])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Mix_003.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Mix_003.inputs[3])
        nt.links.new(Mix_006.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[4], Group_001.inputs[2])
        nt.links.new(Reroute_031.outputs[0], Group_001.inputs[0])
        nt.links.new(Group_001.outputs[0], Mix_001.inputs[2])
        nt.links.new(Reroute_032.outputs[0], Group_002.inputs[0])
        nt.links.new(Group_002.outputs[0], Mix_001.inputs[3])
        nt.links.new(Mix_003.outputs[0], Math_002.inputs[1])
        nt.links.new(Mix_005.outputs[1], GroupOutput.inputs[1])
        nt.links.new(Separate_XYZ_001.outputs[0], Group_012.inputs[0])
        nt.links.new(Group_012.outputs[0], Group_017.inputs[0])
        nt.links.new(Math_004.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Mix_004.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Mix_004.inputs[3])
        nt.links.new(Mix_004.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Group_001.inputs[1])
        nt.links.new(Reroute_034.outputs[0], Group_002.inputs[1])
        nt.links.new(Math.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Math_003.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_008.inputs[0])
        nt.links.new(GroupInput.outputs[4], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[5], Combine_XYZ.inputs[1])
        nt.links.new(Separate_XYZ.outputs[1], Reroute_015.inputs[0])
        nt.links.new(Separate_XYZ.outputs[0], Reroute_012.inputs[0])
        nt.links.new(GroupInput.outputs[3], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Separate_XYZ.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[2], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Math_003.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Separate_XYZ_001.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Group_002.inputs[2])
        nt.links.new(Group_017.outputs[1], Math_004.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mix_005.inputs[4])
        nt.links.new(Reroute_006.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Mix_005.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix_005.inputs[5])
        nt.links.new(Math_002.outputs[0], Mix_006.inputs[2])
        nt.links.new(GroupInput.outputs[1], Mix_006.inputs[3])
        nt.links.new(GroupInput.outputs[0], Mix_006.inputs[0])

        # Set default values
        Invert_Color.inputs[0].default_value = 1.0
        Math_001.inputs[1].default_value = 0.10000000149011612
        Math_001.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_002.inputs[2].default_value = 0.5
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Combine_XYZ.inputs[2].default_value = 0.0
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Math_003.inputs[1].default_value = 0.0
        Math_003.inputs[2].default_value = 0.5
        Math_004.inputs[1].default_value = 0.10000000149011612
        Math_004.inputs[2].default_value = 0.5
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.8999999761581421
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_005.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_006.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
