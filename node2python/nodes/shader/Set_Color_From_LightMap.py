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


class ShaderNodeSet_Color_From_LightMap(ShaderNode):
    bl_idname = 'ShaderNodeSet_Color_From_LightMap'
    bl_label = "Set Color From LightMap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lighmap Alpha"].default_value = 0.0
        self.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 1"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["Map 2"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Range 1"].default_value = 0.125
        self.inputs["Range 2"].default_value = 0.25
        self.inputs["Range 3"].default_value = 0.375
        self.inputs["Range 4"].default_value = 0.6200000047683716

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Set Color From LightMap'

        # Create output sockets
        nt.interface.new_socket('Color Map', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Lighmap Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Map 0', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('Map 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('Map 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 5', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Range 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.125
        input_socket = nt.interface.new_socket('Range 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.25
        input_socket = nt.interface.new_socket('Range 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.375
        input_socket = nt.interface.new_socket('Range 4', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.6200000047683716

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
        Frame.location = (30.667633056640625, -667.5250244140625)
        Frame.label = "SC 1"
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (299.2472229003906, -667.5250244140625)
        Frame_001.label = "SC 2"
        Frame_001.name = "Frame.001"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (543.0482177734375, -667.5250244140625)
        Frame_002.label = "SC 3"
        Frame_002.name = "Frame.002"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (770.0927124023438, -667.5250244140625)
        Frame_003.label = "SC 4"
        Frame_003.name = "Frame.003"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (1094.8883056640625, -667.5250244140625)
        Frame_004.label = "SC 5"
        Frame_004.name = "Frame.004"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (-199.6328887939453, -298.7019348144531)
        Frame_005.label = "value <= 0.125"
        Frame_005.name = "Frame.005"

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (-293.37939453125, 607.97216796875)
        Frame_007.label = "0.375 <= value <= 0.620"
        Frame_007.name = "Frame.007"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (-288.67315673828125, 11.44439697265625)
        Frame_006.label = "0.125 <= value <= 0.25"
        Frame_006.name = "Frame.006"

        Frame_008 = nt.nodes.new('NodeFrame')
        Frame_008.location = (-242.65359497070312, 285.47021484375)
        Frame_008.label = "0.250 <= value <= 0.375"
        Frame_008.name = "Frame.008"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-495.1866149902344, -717.140625)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (-505.9344177246094, -737.4423828125)
        Reroute_012.name = "Reroute.012"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (86.0718994140625, -49.6156005859375)
        Reroute_016.name = "Reroute.016"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-520.2648315429688, -760.7019653320312)
        Reroute_013.name = "Reroute.013"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (92.6072998046875, -69.9173583984375)
        Reroute_018.name = "Reroute.018"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-534.59521484375, -784.58642578125)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (-552.5081787109375, -805.5131225585938)
        Reroute_015.name = "Reroute.015"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (88.6785888671875, -93.17694091796875)
        Reroute_020.name = "Reroute.020"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-495.1866149902344, -191.36065673828125)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-505.9344177246094, -211.66244506835938)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-520.2648315429688, -233.15846252441406)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-534.59521484375, -257.04290771484375)
        Reroute_009.name = "Reroute.009"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (855.5302124023438, 312.8330078125)
        Reroute_026.name = "Reroute.026"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (85.4375, -117.0614013671875)
        Reroute_024.name = "Reroute.024"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (832.6552124023438, 334.69036865234375)
        Reroute_028.name = "Reroute.028"

        Reroute_045 = nt.nodes.new('NodeReroute')
        Reroute_045.location = (737.8606567382812, 361.5754699707031)
        Reroute_045.name = "Reroute.045"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (832.6552124023438, 188.00936889648438)
        Reroute_027.name = "Reroute.027"

        Reroute_047 = nt.nodes.new('NodeReroute')
        Reroute_047.location = (514.1026000976562, 60.175350189208984)
        Reroute_047.name = "Reroute.047"

        Reroute_041 = nt.nodes.new('NodeReroute')
        Reroute_041.location = (610.5150146484375, 36.48591232299805)
        Reroute_041.name = "Reroute.041"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (631.726806640625, 14.40898609161377)
        Reroute_021.name = "Reroute.021"

        Reroute_044 = nt.nodes.new('NodeReroute')
        Reroute_044.location = (738.1204223632812, 430.5069885253906)
        Reroute_044.name = "Reroute.044"

        Reroute_046 = nt.nodes.new('NodeReroute')
        Reroute_046.location = (514.1026000976562, 116.64396667480469)
        Reroute_046.name = "Reroute.046"

        Reroute_048 = nt.nodes.new('NodeReroute')
        Reroute_048.location = (313.4267578125, -155.08016967773438)
        Reroute_048.name = "Reroute.048"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (610.5150146484375, -96.34208679199219)
        Reroute_040.name = "Reroute.040"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (391.8545227050781, -271.4598388671875)
        Reroute_019.name = "Reroute.019"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (359.75311279296875, -249.5117645263672)
        Reroute_023.name = "Reroute.023"

        Reroute_049 = nt.nodes.new('NodeReroute')
        Reroute_049.location = (313.4267578125, -225.42100524902344)
        Reroute_049.name = "Reroute.049"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (359.75311279296875, -333.16766357421875)
        Reroute_022.name = "Reroute.022"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (116.73953247070312, -504.5400085449219)
        Reroute_017.name = "Reroute.017"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (438.9729919433594, -62.5921630859375)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-361.1925048828125, -251.5056610107422)
        Reroute_004.name = "Reroute.004"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (906.6698608398438, 522.9893188476562)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-552.5081787109375, -279.733154296875)
        Reroute_010.name = "Reroute.010"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (102.971435546875, -137.98809814453125)
        Reroute_025.name = "Reroute.025"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (1197.8597412109375, 520.4842529296875)
        Reroute_029.name = "Reroute.029"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (1152.9039306640625, 542.9382934570312)
        Reroute_031.name = "Reroute.031"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (1242.59228515625, 729.4307250976562)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (1152.9039306640625, 486.0926513671875)
        Reroute_030.name = "Reroute.030"

        Reroute_043 = nt.nodes.new('NodeReroute')
        Reroute_043.location = (1079.2274169921875, 567.0616455078125)
        Reroute_043.name = "Reroute.043"

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (180.7213134765625, -296.008544921875)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (661.3955078125, 222.58270263671875)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (25.710861206054688, -89.328369140625)
        Group_002.name = "Group.002"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (133.28594970703125, -162.08978271484375)
        Group.name = "Group"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-361.1925048828125, -168.4062042236328)
        Reroute.name = "Reroute"

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (84.99075317382812, -125.42955017089844)
        Group_001.name = "Group.001"

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (-165.55682373046875, 681.7037963867188)
        Group_003.name = "Group.003"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (-286.8544921875, -208.77713012695312)
        Reroute_033.name = "Reroute.033"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (-286.8544921875, -500.4668884277344)
        Reroute_034.name = "Reroute.034"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-361.1925048828125, -475.3236389160156)
        Reroute_005.name = "Reroute.005"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (-322.4431457519531, -229.9558868408203)
        Reroute_036.name = "Reroute.036"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (-322.4431457519531, 70.39837646484375)
        Reroute_037.name = "Reroute.037"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (-286.8544921875, -300.2310485839844)
        Reroute_032.name = "Reroute.032"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (-322.4431457519531, -324.2978820800781)
        Reroute_035.name = "Reroute.035"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-361.1925048828125, 23.253538131713867)
        Reroute_001.name = "Reroute.001"

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (-391.4541931152344, 44.2531623840332)
        Reroute_039.name = "Reroute.039"

        Reroute_050 = nt.nodes.new('NodeReroute')
        Reroute_050.location = (-391.4541931152344, 355.63629150390625)
        Reroute_050.name = "Reroute.050"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (-391.4541931152344, -346.1920166015625)
        Reroute_038.name = "Reroute.038"

        Reroute_051 = nt.nodes.new('NodeReroute')
        Reroute_051.location = (-434.6198425292969, -367.7909240722656)
        Reroute_051.name = "Reroute.051"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-361.1925048828125, 594.4157104492188)
        Reroute_003.name = "Reroute.003"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-361.1925048828125, 311.29632568359375)
        Reroute_002.name = "Reroute.002"

        Reroute_052 = nt.nodes.new('NodeReroute')
        Reroute_052.location = (-434.6198425292969, 336.6661071777344)
        Reroute_052.name = "Reroute.052"

        Reroute_053 = nt.nodes.new('NodeReroute')
        Reroute_053.location = (-434.6198425292969, 570.7300415039062)
        Reroute_053.name = "Reroute.053"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (125.93382263183594, -129.94737243652344)
        Group_004.name = "Group.004"

        Reroute_042 = nt.nodes.new('NodeReroute')
        Reroute_042.location = (1079.2274169921875, 627.8395385742188)
        Reroute_042.name = "Reroute.042"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(GroupInput.outputs[2], Reroute_006.inputs[0])
        nt.links.new(GroupInput.outputs[3], Reroute_007.inputs[0])
        nt.links.new(GroupInput.outputs[4], Reroute_008.inputs[0])
        nt.links.new(GroupInput.outputs[5], Reroute_009.inputs[0])
        nt.links.new(GroupInput.outputs[6], Reroute_010.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Mix_004.inputs[7])
        nt.links.new(Reroute_012.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Mix_003.inputs[7])
        nt.links.new(Reroute_013.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Mix_002.inputs[7])
        nt.links.new(Mix_004.outputs[2], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Mix_003.inputs[6])
        nt.links.new(Reroute_014.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Mix_001.inputs[7])
        nt.links.new(Mix_002.outputs[2], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Mix_001.inputs[6])
        nt.links.new(Reroute_025.outputs[0], Reroute_029.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Mix.inputs[7])
        nt.links.new(Reroute_030.outputs[0], Reroute_031.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Mix.inputs[6])
        nt.links.new(Mix_003.outputs[2], Reroute_040.inputs[0])
        nt.links.new(Reroute_040.outputs[0], Reroute_041.inputs[0])
        nt.links.new(Reroute_041.outputs[0], Mix_002.inputs[6])
        nt.links.new(Reroute_042.outputs[0], Reroute_043.inputs[0])
        nt.links.new(Reroute_043.outputs[0], Mix.inputs[0])
        nt.links.new(Reroute_044.outputs[0], Reroute_045.inputs[0])
        nt.links.new(Reroute_045.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_046.outputs[0], Reroute_047.inputs[0])
        nt.links.new(Reroute_047.outputs[0], Mix_002.inputs[0])
        nt.links.new(Reroute_048.outputs[0], Reroute_049.inputs[0])
        nt.links.new(Reroute_049.outputs[0], Mix_003.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Mix_001.outputs[2], Reroute_030.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Group_002.inputs[0])
        nt.links.new(Group_002.outputs[0], Mix_004.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Group_003.inputs[0])
        nt.links.new(Group_003.outputs[0], Reroute_042.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Group.inputs[2])
        nt.links.new(Group.outputs[0], Reroute_044.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Group_001.inputs[2])
        nt.links.new(Reroute.outputs[0], Group_004.inputs[2])
        nt.links.new(Group_004.outputs[0], Reroute_048.inputs[0])
        nt.links.new(Group_001.outputs[0], Reroute_046.inputs[0])
        nt.links.new(GroupInput.outputs[7], Reroute_032.inputs[0])
        nt.links.new(Reroute_032.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Group_004.inputs[0])
        nt.links.new(Reroute_032.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Group_002.inputs[1])
        nt.links.new(GroupInput.outputs[8], Reroute_035.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Group_004.inputs[1])
        nt.links.new(Reroute_036.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Group_001.inputs[0])
        nt.links.new(GroupInput.outputs[9], Reroute_038.inputs[0])
        nt.links.new(Reroute_038.outputs[0], Reroute_039.inputs[0])
        nt.links.new(Reroute_039.outputs[0], Group_001.inputs[1])
        nt.links.new(Reroute_039.outputs[0], Reroute_050.inputs[0])
        nt.links.new(Reroute_050.outputs[0], Group.inputs[0])
        nt.links.new(GroupInput.outputs[10], Reroute_051.inputs[0])
        nt.links.new(Reroute_051.outputs[0], Reroute_052.inputs[0])
        nt.links.new(Reroute_052.outputs[0], Group.inputs[1])
        nt.links.new(Reroute_052.outputs[0], Reroute_053.inputs[0])
        nt.links.new(Reroute_053.outputs[0], Group_003.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_004.inputs[6])

        # Set default values
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
