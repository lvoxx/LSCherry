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


class ShaderNodeLS_Cherry_Main_Controller(ShaderNode):
    bl_idname = 'ShaderNodeLS_Cherry_Main_Controller'
    bl_label = "LS Cherry Main Controller"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base Color"].default_value = (1.0, 0.0, 0.0, 1.0)
        self.inputs["Shadow Color"].default_value = (0.7428570985794067, 0.6048978567123413, 0.6048978567123413, 1.0)
        self.inputs["SSS Color"].default_value = (1.0, 0.08650019019842148, 0.0, 1.0)
        self.inputs["Rim Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Back Color"].default_value = (0.04373471811413765, 0.08650025725364685, 0.42326751351356506, 1.0)
        self.inputs["Rim Strength"].default_value = 0.5
        self.inputs["Rim Size"].default_value = 0.5
        self.inputs["Rim Smooth"].default_value = 0.5
        self.inputs["Specular Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Specular Tint"].default_value = 0.0
        self.inputs["Roughness"].default_value = 0.10000000149011612
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Emission"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Emission Strength"].default_value = 1.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Disable Toon Style"].default_value = False
        self.inputs["Toon Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Disable SSS Style"].default_value = False
        self.inputs["SSS Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Disable Back Style"].default_value = False
        self.inputs["Back Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Enable Custom Ramp"].default_value = False
        self.inputs["Custom Ramp"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Blend With Custom Ramp"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'LS Cherry Main Controller'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Diffuse Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Post Diffuse Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('SSS Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Rim Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Back Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Light Sources Mask', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shadow Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.7428570985794067, 0.6048978567123413, 0.6048978567123413, 1.0)
        input_socket = nt.interface.new_socket('SSS Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.08650019019842148, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Rim Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Back Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.04373471811413765, 0.08650025725364685, 0.42326751351356506, 1.0)
        input_socket = nt.interface.new_socket('Rim Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Rim Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Rim Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Specular Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Specular Tint', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Emission', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Disable Toon Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Toon Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Disable SSS Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('SSS Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Disable Back Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Back Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Enable Custom Ramp', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Custom Ramp', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Blend With Custom Ramp', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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
        Frame.location = (459.18341064453125, 354.3673095703125)
        Frame.label = "Core"
        Frame.name = "Frame"

        Frame_038 = nt.nodes.new('NodeFrame')
        Frame_038.location = (883.126220703125, 812.0084228515625)
        Frame_038.label = "Diffuse Mask"
        Frame_038.name = "Frame.038"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (1038.559326171875, 210.93780517578125)
        Frame_001.label = "Main Stream"
        Frame_001.name = "Frame.001"

        Frame_032 = nt.nodes.new('NodeFrame')
        Frame_032.location = (4456.705078125, 403.6572265625)
        Frame_032.label = "Rim Core Mask"
        Frame_032.name = "Frame.032"

        Frame_009 = nt.nodes.new('NodeFrame')
        Frame_009.location = (2246.672119140625, 210.93780517578125)
        Frame_009.label = "Post Diffuse Mask"
        Frame_009.name = "Frame.009"

        Frame_011 = nt.nodes.new('NodeFrame')
        Frame_011.location = (2338.98583984375, 266.3586730957031)
        Frame_011.label = "SSS Stream"
        Frame_011.name = "Frame.011"

        Frame_033 = nt.nodes.new('NodeFrame')
        Frame_033.location = (2982.965087890625, 614.66552734375)
        Frame_033.label = "SSS Mask"
        Frame_033.name = "Frame.033"

        Frame_014 = nt.nodes.new('NodeFrame')
        Frame_014.location = (1915.04736328125, 542.74267578125)
        Frame_014.label = "Rim Stream"
        Frame_014.name = "Frame.014"

        Frame_015 = nt.nodes.new('NodeFrame')
        Frame_015.location = (2054.07470703125, 277.26544189453125)
        Frame_015.label = "Back Stream"
        Frame_015.name = "Frame.015"

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (2402.10009765625, 335.4244384765625)
        Frame_007.label = "Add Color"
        Frame_007.name = "Frame.007"

        Frame_018 = nt.nodes.new('NodeFrame')
        Frame_018.location = (3868.4482421875, 115.7103271484375)
        Frame_018.label = "Add Custom Ramp"
        Frame_018.name = "Frame.018"

        Frame_021 = nt.nodes.new('NodeFrame')
        Frame_021.location = (-57.74072265625, -477.0984191894531)
        Frame_021.label = "Add SSS Color"
        Frame_021.name = "Frame.021"

        Frame_022 = nt.nodes.new('NodeFrame')
        Frame_022.location = (-87.53382110595703, -859.188720703125)
        Frame_022.label = "Add Back Color"
        Frame_022.name = "Frame.022"

        Frame_016 = nt.nodes.new('NodeFrame')
        Frame_016.location = (-252.93408203125, 268.7161865234375)
        Frame_016.label = "Add Rim Color"
        Frame_016.name = "Frame.016"

        Frame_019 = nt.nodes.new('NodeFrame')
        Frame_019.location = (4786.8330078125, 604.140625)
        Frame_019.label = "Add World Color"
        Frame_019.name = "Frame.019"

        Frame_020 = nt.nodes.new('NodeFrame')
        Frame_020.location = (5259.64111328125, 187.893798828125)
        Frame_020.label = "Main Stream"
        Frame_020.name = "Frame.020"

        Frame_024 = nt.nodes.new('NodeFrame')
        Frame_024.location = (5136.67333984375, -46.35758972167969)
        Frame_024.label = "SSS Stream"
        Frame_024.name = "Frame.024"

        Frame_040 = nt.nodes.new('NodeFrame')
        Frame_040.location = (6361.93017578125, 614.66552734375)
        Frame_040.label = "SSS Mask"
        Frame_040.name = "Frame.040"

        Frame_023 = nt.nodes.new('NodeFrame')
        Frame_023.location = (5148.953125, -502.4356689453125)
        Frame_023.label = "Back Stream"
        Frame_023.name = "Frame.023"

        Frame_025 = nt.nodes.new('NodeFrame')
        Frame_025.location = (5890.8388671875, 314.12225341796875)
        Frame_025.label = "Combiner"
        Frame_025.name = "Frame.025"

        Frame_026 = nt.nodes.new('NodeFrame')
        Frame_026.location = (111.59093475341797, -35.545440673828125)
        Frame_026.label = "SSS"
        Frame_026.name = "Frame.026"

        Frame_029 = nt.nodes.new('NodeFrame')
        Frame_029.location = (619.3011474609375, -35.545440673828125)
        Frame_029.label = "Back Light"
        Frame_029.name = "Frame.029"

        Frame_017 = nt.nodes.new('NodeFrame')
        Frame_017.location = (4259.19873046875, 542.74267578125)
        Frame_017.label = "Rim Stream"
        Frame_017.name = "Frame.017"

        Frame_039 = nt.nodes.new('NodeFrame')
        Frame_039.location = (7470.1806640625, 812.0084228515625)
        Frame_039.label = "Diffuse Mask"
        Frame_039.name = "Frame.039"

        Frame_036 = nt.nodes.new('NodeFrame')
        Frame_036.location = (6729.4248046875, 862.8135375976562)
        Frame_036.label = "Back Mask"
        Frame_036.name = "Frame.036"

        Frame_031 = nt.nodes.new('NodeFrame')
        Frame_031.location = (4875.87646484375, 403.6572265625)
        Frame_031.label = "Rim Core Mask"
        Frame_031.name = "Frame.031"

        Frame_012 = nt.nodes.new('NodeFrame')
        Frame_012.location = (4851.314453125, 835.4397583007812)
        Frame_012.label = "Post Diffuse Mask"
        Frame_012.name = "Frame.012"

        Frame_034 = nt.nodes.new('NodeFrame')
        Frame_034.location = (8006.59423828125, 614.66552734375)
        Frame_034.label = "SSS Mask"
        Frame_034.name = "Frame.034"

        Frame_037 = nt.nodes.new('NodeFrame')
        Frame_037.location = (1191.4814453125, -35.545440673828125)
        Frame_037.label = "Emission"
        Frame_037.name = "Frame.037"

        Frame_028 = nt.nodes.new('NodeFrame')
        Frame_028.location = (929.729736328125, -35.545440673828125)
        Frame_028.label = "Rim"
        Frame_028.name = "Frame.028"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (138.4951171875, 835.4397583007812)
        Frame_003.label = "Post DiffuseMask"
        Frame_003.name = "Frame.003"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (1350.5869140625, 568.8885498046875)
        Frame_004.label = "Ramp Style"
        Frame_004.name = "Frame.004"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (551.3968505859375, -420.5313720703125)
        Frame_005.label = "Rim Core Style"
        Frame_005.name = "Frame.005"

        Frame_027 = nt.nodes.new('NodeFrame')
        Frame_027.location = (-29.11767578125, -888.8446044921875)
        Frame_027.label = "NOTE: Toon Size and SSS Size should be equal"
        Frame_027.name = "Frame.027"

        Frame_008 = nt.nodes.new('NodeFrame')
        Frame_008.location = (846.21630859375, -799.05615234375)
        Frame_008.label = "Toon Style"
        Frame_008.name = "Frame.008"

        Frame_013 = nt.nodes.new('NodeFrame')
        Frame_013.location = (1028.4638671875, -1622.3768310546875)
        Frame_013.label = "Back Style"
        Frame_013.name = "Frame.013"

        Frame_010 = nt.nodes.new('NodeFrame')
        Frame_010.location = (860.32177734375, -939.891845703125)
        Frame_010.label = "SSS Style"
        Frame_010.name = "Frame.010"

        Frame_035 = nt.nodes.new('NodeFrame')
        Frame_035.location = (3462.279541015625, 862.8135375976562)
        Frame_035.label = "Back Mask"
        Frame_035.name = "Frame.035"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-469.69439697265625, -141.33709716796875)
        Reroute_007.name = "Reroute.007"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (-469.69439697265625, -277.1350402832031)
        Reroute_021.name = "Reroute.021"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-175.89306640625, -210.9788055419922)
        Reroute_002.name = "Reroute.002"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-91.38693237304688, -51.725494384765625)
        Reroute.name = "Reroute"

        Reroute_054 = nt.nodes.new('NodeReroute')
        Reroute_054.location = (-599.8359375, 389.3453369140625)
        Reroute_054.name = "Reroute.054"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (-469.69439697265625, -509.8713684082031)
        Reroute_023.name = "Reroute.023"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (-367.5307312011719, -490.9928894042969)
        Group_004.name = "Group.004"

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (-366.7099304199219, -174.7638702392578)
        Group_002.name = "Group.002"

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (-366.3841857910156, -16.638916015625)
        Group_001.name = "Group.001"

        Reroute_089 = nt.nodes.new('NodeReroute')
        Reroute_089.location = (-2719.9326171875, 705.323974609375)
        Reroute_089.name = "Reroute.089"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (-154.6070556640625, 35.23017883300781)
        Reroute_015.name = "Reroute.015"

        Reroute_045 = nt.nodes.new('NodeReroute')
        Reroute_045.location = (43.08935546875, -903.5982055664062)
        Reroute_045.name = "Reroute.045"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (-227.75390625, -450.1736145019531)
        Reroute_036.name = "Reroute.036"

        Reroute_090 = nt.nodes.new('NodeReroute')
        Reroute_090.location = (-871.733154296875, 413.40185546875)
        Reroute_090.name = "Reroute.090"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (-227.2752685546875, -32.589508056640625)
        Reroute_034.name = "Reroute.034"

        Group_027 = nt.nodes.new('ShaderNodeGroup')
        Group_027.location = (133.5576171875, -118.94744873046875)
        Group_027.name = "Group.027"

        Mix_008 = nt.nodes.new('ShaderNodeMix')
        Mix_008.location = (301.595458984375, -100.792236328125)
        Mix_008.name = "Mix.008"
        Mix_008.blend_type = 'MULTIPLY'

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (255.33154296875, -83.77340698242188)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MULTIPLY'

        Group_026 = nt.nodes.new('ShaderNodeGroup')
        Group_026.location = (86.06103515625, -142.81695556640625)
        Group_026.name = "Group.026"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (-52.8935546875, -83.3677978515625)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (-534.3837890625, -170.23675537109375)
        Mix_004.label = "Add Base Color"
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MULTIPLY'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (-530.43798828125, 4.598724365234375)
        Invert_Color.name = "Invert Color"

        Reroute_050 = nt.nodes.new('NodeReroute')
        Reroute_050.location = (-328.07177734375, -31.333251953125)
        Reroute_050.name = "Reroute.050"

        Reroute_049 = nt.nodes.new('NodeReroute')
        Reroute_049.location = (-584.1845703125, -356.1180419921875)
        Reroute_049.name = "Reroute.049"

        Reroute_048 = nt.nodes.new('NodeReroute')
        Reroute_048.location = (-584.18408203125, -78.90228271484375)
        Reroute_048.name = "Reroute.048"

        Reroute_043 = nt.nodes.new('NodeReroute')
        Reroute_043.location = (-178.2755126953125, 42.246826171875)
        Reroute_043.name = "Reroute.043"

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (414.50634765625, 116.488525390625)
        Mix_005.label = "Add Rim Color"
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MULTIPLY'

        Reroute_053 = nt.nodes.new('NodeReroute')
        Reroute_053.location = (-584.1845703125, 76.32415771484375)
        Reroute_053.name = "Reroute.053"

        Reroute_100 = nt.nodes.new('NodeReroute')
        Reroute_100.location = (-89.234375, 76.32415771484375)
        Reroute_100.name = "Reroute.100"

        Reroute_052 = nt.nodes.new('NodeReroute')
        Reroute_052.location = (-317.0849609375, -205.59603881835938)
        Reroute_052.name = "Reroute.052"

        Reroute_109 = nt.nodes.new('NodeReroute')
        Reroute_109.location = (-89.234375, -245.49038696289062)
        Reroute_109.name = "Reroute.109"

        Reroute_111 = nt.nodes.new('NodeReroute')
        Reroute_111.location = (-121.32958984375, 29.133575439453125)
        Reroute_111.name = "Reroute.111"

        Reroute_112 = nt.nodes.new('NodeReroute')
        Reroute_112.location = (-121.32958984375, -268.393798828125)
        Reroute_112.name = "Reroute.112"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (-291.6435546875, 65.55670166015625)
        Mix_002.label = "Add Shadow Color"
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Reroute_110 = nt.nodes.new('NodeReroute')
        Reroute_110.location = (-317.0849609375, -290.4146423339844)
        Reroute_110.name = "Reroute.110"

        Reroute_051 = nt.nodes.new('NodeReroute')
        Reroute_051.location = (-328.07177734375, -96.14852905273438)
        Reroute_051.name = "Reroute.051"

        Mix_015 = nt.nodes.new('ShaderNodeMix')
        Mix_015.location = (84.534423828125, 56.8565673828125)
        Mix_015.name = "Mix.015"
        Mix_015.blend_type = 'MULTIPLY'

        Mix_012 = nt.nodes.new('ShaderNodeMix')
        Mix_012.location = (77.30517578125, -352.15460205078125)
        Mix_012.name = "Mix.012"
        Mix_012.blend_type = 'MULTIPLY'

        Mix_013 = nt.nodes.new('ShaderNodeMix')
        Mix_013.location = (84.534423828125, -720.8958740234375)
        Mix_013.name = "Mix.013"
        Mix_013.blend_type = 'MULTIPLY'

        Reroute_057 = nt.nodes.new('NodeReroute')
        Reroute_057.location = (4698.1591796875, -68.23938751220703)
        Reroute_057.name = "Reroute.057"

        Reroute_059 = nt.nodes.new('NodeReroute')
        Reroute_059.location = (4698.1591796875, 455.1097717285156)
        Reroute_059.name = "Reroute.059"

        Reroute_069 = nt.nodes.new('NodeReroute')
        Reroute_069.location = (4698.1591796875, -323.501953125)
        Reroute_069.name = "Reroute.069"

        Reroute_058 = nt.nodes.new('NodeReroute')
        Reroute_058.location = (4698.1591796875, 48.322998046875)
        Reroute_058.name = "Reroute.058"

        Reroute_062 = nt.nodes.new('NodeReroute')
        Reroute_062.location = (4745.1904296875, 215.45840454101562)
        Reroute_062.name = "Reroute.062"

        Reroute_067 = nt.nodes.new('NodeReroute')
        Reroute_067.location = (4675.962890625, -497.47454833984375)
        Reroute_067.name = "Reroute.067"

        Reroute_063 = nt.nodes.new('NodeReroute')
        Reroute_063.location = (4745.1904296875, 69.67971801757812)
        Reroute_063.name = "Reroute.063"

        Reroute_068 = nt.nodes.new('NodeReroute')
        Reroute_068.location = (4675.962890625, -300.92657470703125)
        Reroute_068.name = "Reroute.068"

        Reroute_061 = nt.nodes.new('NodeReroute')
        Reroute_061.location = (4675.962890625, 476.14202880859375)
        Reroute_061.name = "Reroute.061"

        Reroute_060 = nt.nodes.new('NodeReroute')
        Reroute_060.location = (4675.962890625, 685.7503051757812)
        Reroute_060.name = "Reroute.060"

        Reroute_078 = nt.nodes.new('NodeReroute')
        Reroute_078.location = (35.2568359375, -83.75820922851562)
        Reroute_078.name = "Reroute.078"

        Reroute_081 = nt.nodes.new('NodeReroute')
        Reroute_081.location = (479.017578125, -83.75820922851562)
        Reroute_081.name = "Reroute.081"

        Reroute_080 = nt.nodes.new('NodeReroute')
        Reroute_080.location = (5466.0673828125, 149.28424072265625)
        Reroute_080.name = "Reroute.080"

        Reroute_079 = nt.nodes.new('NodeReroute')
        Reroute_079.location = (206.42724609375, 28.572113037109375)
        Reroute_079.name = "Reroute.079"

        Reroute_082 = nt.nodes.new('NodeReroute')
        Reroute_082.location = (5615.6904296875, 126.24130249023438)
        Reroute_082.name = "Reroute.082"

        Reroute_105 = nt.nodes.new('NodeReroute')
        Reroute_105.location = (-1274.859375, 413.40185546875)
        Reroute_105.name = "Reroute.105"

        Reroute_108 = nt.nodes.new('NodeReroute')
        Reroute_108.location = (5087.0703125, -40.952850341796875)
        Reroute_108.name = "Reroute.108"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (5210.9453125, -39.983642578125)
        Math.label = "x 2"
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (5208.9208984375, -1.9827461242675781)
        Math_001.label = "Invert"
        Math_001.name = "Math.001"
        Math_001.operation = 'SUBTRACT'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (5425.33349609375, 92.49323272705078)
        Math_003.name = "Math.003"
        Math_003.operation = 'MULTIPLY'

        Reroute_107 = nt.nodes.new('NodeReroute')
        Reroute_107.location = (5698.26025390625, 56.59791564941406)
        Reroute_107.name = "Reroute.107"

        Reroute_106 = nt.nodes.new('NodeReroute')
        Reroute_106.location = (5698.26025390625, 172.70614624023438)
        Reroute_106.name = "Reroute.106"

        Mix_014 = nt.nodes.new('ShaderNodeMix')
        Mix_014.location = (84.5341796875, -1038.7926025390625)
        Mix_014.name = "Mix.014"
        Mix_014.blend_type = 'MULTIPLY'

        Reroute_076 = nt.nodes.new('NodeReroute')
        Reroute_076.location = (4698.1591796875, -619.2073364257812)
        Reroute_076.name = "Reroute.076"

        Reroute_077 = nt.nodes.new('NodeReroute')
        Reroute_077.location = (35.2568359375, 42.05438232421875)
        Reroute_077.name = "Reroute.077"

        Reroute_084 = nt.nodes.new('NodeReroute')
        Reroute_084.location = (947.853515625, 42.05438232421875)
        Reroute_084.name = "Reroute.084"

        Reroute_085 = nt.nodes.new('NodeReroute')
        Reroute_085.location = (201.9677734375, -186.31292724609375)
        Reroute_085.name = "Reroute.085"

        Mix_009 = nt.nodes.new('ShaderNodeMix')
        Mix_009.location = (-97.34521484375, 53.802490234375)
        Mix_009.name = "Mix.009"
        Mix_009.blend_type = 'ADD'

        Mix_011 = nt.nodes.new('ShaderNodeMix')
        Mix_011.location = (-354.95703125, 53.802490234375)
        Mix_011.name = "Mix.011"
        Mix_011.blend_type = 'ADD'

        Reroute_055 = nt.nodes.new('NodeReroute')
        Reroute_055.location = (23.751953125, 389.3453369140625)
        Reroute_055.name = "Reroute.055"

        Mix_017 = nt.nodes.new('ShaderNodeMix')
        Mix_017.location = (6924.15576171875, 15.00604248046875)
        Mix_017.name = "Mix.017"
        Mix_017.blend_type = 'MULTIPLY'

        Reroute_087 = nt.nodes.new('NodeReroute')
        Reroute_087.location = (2531.9052734375, 705.323974609375)
        Reroute_087.name = "Reroute.087"

        Reroute_093 = nt.nodes.new('NodeReroute')
        Reroute_093.location = (752.20703125, -1870.949462890625)
        Reroute_093.name = "Reroute.093"

        Reroute_096 = nt.nodes.new('NodeReroute')
        Reroute_096.location = (7481.6318359375, 190.77174377441406)
        Reroute_096.name = "Reroute.096"

        Reroute_094 = nt.nodes.new('NodeReroute')
        Reroute_094.location = (7407.7822265625, 213.98765563964844)
        Reroute_094.name = "Reroute.094"

        Reroute_095 = nt.nodes.new('NodeReroute')
        Reroute_095.location = (7325.63037109375, 235.4892120361328)
        Reroute_095.name = "Reroute.095"

        Reroute_086 = nt.nodes.new('NodeReroute')
        Reroute_086.location = (7238.35693359375, 257.3087463378906)
        Reroute_086.name = "Reroute.086"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (2387.04296875, 102.47039794921875)
        Reroute_037.name = "Reroute.037"

        Reroute_091 = nt.nodes.new('NodeReroute')
        Reroute_091.location = (-680.9609375, 413.40185546875)
        Reroute_091.name = "Reroute.091"

        Reroute_047 = nt.nodes.new('NodeReroute')
        Reroute_047.location = (2385.9521484375, 77.74774169921875)
        Reroute_047.name = "Reroute.047"

        Mix_016 = nt.nodes.new('ShaderNodeMix')
        Mix_016.location = (-141.8291015625, 53.802490234375)
        Mix_016.label = "Combine Emission"
        Mix_016.name = "Mix.016"
        Mix_016.blend_type = 'ADD'

        Reroute_083 = nt.nodes.new('NodeReroute')
        Reroute_083.location = (762.591796875, -183.37342834472656)
        Reroute_083.name = "Reroute.083"

        Mix_010 = nt.nodes.new('ShaderNodeMix')
        Mix_010.location = (-106.36328125, 53.802490234375)
        Mix_010.name = "Mix.010"
        Mix_010.blend_type = 'ADD'

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (1880.9017333984375, 102.47039794921875)
        Reroute_020.name = "Reroute.020"

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (-1206.54931640625, 459.5787353515625)
        Group_009.name = "Group.009"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (-1137.70654296875, 474.0872802734375)
        Reroute_030.name = "Reroute.030"

        Reroute_092 = nt.nodes.new('NodeReroute')
        Reroute_092.location = (-2585.53466796875, -1870.949462890625)
        Reroute_092.name = "Reroute.092"

        Reroute_042 = nt.nodes.new('NodeReroute')
        Reroute_042.location = (876.744873046875, -718.3939208984375)
        Reroute_042.name = "Reroute.042"

        Mix_021 = nt.nodes.new('ShaderNodeMix')
        Mix_021.location = (649.758056640625, 144.86611938476562)
        Mix_021.label = "Pattern"
        Mix_021.name = "Mix.021"
        Mix_021.blend_type = 'MULTIPLY'

        Mix_023 = nt.nodes.new('ShaderNodeMix')
        Mix_023.location = (649.758056640625, -136.38528442382812)
        Mix_023.label = "Pattern"
        Mix_023.name = "Mix.023"
        Mix_023.blend_type = 'MULTIPLY'

        Reroute_119 = nt.nodes.new('NodeReroute')
        Reroute_119.location = (615.9683837890625, -156.5281982421875)
        Reroute_119.name = "Reroute.119"

        Reroute_121 = nt.nodes.new('NodeReroute')
        Reroute_121.location = (615.9683837890625, 123.42390441894531)
        Reroute_121.name = "Reroute.121"

        Reroute_120 = nt.nodes.new('NodeReroute')
        Reroute_120.location = (615.9683837890625, 16.132808685302734)
        Reroute_120.name = "Reroute.120"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (876.7449340820312, -147.21719360351562)
        Reroute_026.name = "Reroute.026"

        Reroute_102 = nt.nodes.new('NodeReroute')
        Reroute_102.location = (7493.9345703125, 279.1435241699219)
        Reroute_102.name = "Reroute.102"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (505.51123046875, -36.5343017578125)
        Frame_002.label = "Stylized Diffuse"
        Frame_002.name = "Frame.002"

        Mix_020 = nt.nodes.new('ShaderNodeMix')
        Mix_020.location = (-234.333740234375, -179.70831298828125)
        Mix_020.name = "Mix.020"
        Mix_020.blend_type = 'MULTIPLY'

        Invert_Color_001 = nt.nodes.new('ShaderNodeInvert')
        Invert_Color_001.location = (-234.333740234375, -141.12286376953125)
        Invert_Color_001.name = "Invert Color.001"

        Frame_048 = nt.nodes.new('NodeFrame')
        Frame_048.location = (-334.54638671875, -199.21238708496094)
        Frame_048.label = "Learn more: https://www.youtube.com/watch?v=gwLQ0cDb4cE"
        Frame_048.name = "Frame.048"

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (-39.045654296875, -7.0582275390625)
        Group_003.name = "Group.003"

        Reroute_131 = nt.nodes.new('NodeReroute')
        Reroute_131.location = (345.42578125, -68.84832000732422)
        Reroute_131.name = "Reroute.131"

        Reroute_132 = nt.nodes.new('NodeReroute')
        Reroute_132.location = (-745.607421875, -78.90228271484375)
        Reroute_132.name = "Reroute.132"

        Reroute_117 = nt.nodes.new('NodeReroute')
        Reroute_117.location = (4712.5244140625, -711.3209228515625)
        Reroute_117.name = "Reroute.117"

        Reroute_124 = nt.nodes.new('NodeReroute')
        Reroute_124.location = (4712.5244140625, -641.1705932617188)
        Reroute_124.name = "Reroute.124"

        Reroute_145 = nt.nodes.new('NodeReroute')
        Reroute_145.location = (108.095703125, 128.84007263183594)
        Reroute_145.name = "Reroute.145"

        Reroute_146 = nt.nodes.new('NodeReroute')
        Reroute_146.location = (345.42578125, 99.74807739257812)
        Reroute_146.name = "Reroute.146"

        Group_019 = nt.nodes.new('ShaderNodeGroup')
        Group_019.location = (96.3355712890625, -380.5669860839844)
        Group_019.name = "Group.019"

        Mix_018 = nt.nodes.new('ShaderNodeMix')
        Mix_018.location = (150.50634765625, -34.03416442871094)
        Mix_018.name = "Mix.018"
        Mix_018.blend_type = 'MIX'

        Reroute_148 = nt.nodes.new('NodeReroute')
        Reroute_148.location = (108.095703125, -216.45858764648438)
        Reroute_148.name = "Reroute.148"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-990.4332275390625, 449.739013671875)
        Group_013.name = "Group.013"

        Group_017 = nt.nodes.new('ShaderNodeGroup')
        Group_017.location = (-779.7095947265625, 300.991943359375)
        Group_017.name = "Group.017"

        Reroute_162 = nt.nodes.new('NodeReroute')
        Reroute_162.location = (40.7130126953125, -406.91094970703125)
        Reroute_162.name = "Reroute.162"

        Reroute_103 = nt.nodes.new('NodeReroute')
        Reroute_103.location = (1793.17041015625, 102.47039794921875)
        Reroute_103.name = "Reroute.103"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (1244.590576171875, 388.3695068359375)
        Reroute_003.name = "Reroute.003"

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (-52.64447021484375, -209.85455322265625)
        Mix_007.label = "Mix Custom And Dot"
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MIX'

        Frame_041 = nt.nodes.new('NodeFrame')
        Frame_041.location = (7553.0634765625, 911.1820068359375)
        Frame_041.label = "Light Sources Mask"
        Frame_041.name = "Frame.041"

        Reroute_073 = nt.nodes.new('NodeReroute')
        Reroute_073.location = (23.751953125, 388.3695068359375)
        Reroute_073.name = "Reroute.073"

        Reroute_104 = nt.nodes.new('NodeReroute')
        Reroute_104.location = (7576.8154296875, 168.25845336914062)
        Reroute_104.name = "Reroute.104"

        Frame_042 = nt.nodes.new('NodeFrame')
        Frame_042.location = (252.91009521484375, 911.1820068359375)
        Frame_042.label = "Light Sources Mask"
        Frame_042.name = "Frame.042"

        Reroute_116 = nt.nodes.new('NodeReroute')
        Reroute_116.location = (114.88641357421875, 388.3695068359375)
        Reroute_116.name = "Reroute.116"

        Frame_030 = nt.nodes.new('NodeFrame')
        Frame_030.location = (1330.670166015625, 835.4397583007812)
        Frame_030.label = "Post DiffuseMask"
        Frame_030.name = "Frame.030"

        Reroute_166 = nt.nodes.new('NodeReroute')
        Reroute_166.location = (40.7130126953125, -786.0581665039062)
        Reroute_166.name = "Reroute.166"

        Frame_044 = nt.nodes.new('NodeFrame')
        Frame_044.location = (658.561767578125, 911.1820068359375)
        Frame_044.label = "Light Sources Mask"
        Frame_044.name = "Frame.044"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (-288.3812255859375, -763.48779296875)
        Reroute_033.name = "Reroute.033"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-367.5307312011719, -454.6863708496094)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'LENGTH'

        Mix_019 = nt.nodes.new('ShaderNodeMix')
        Mix_019.location = (-72.18814086914062, -489.0179138183594)
        Mix_019.name = "Mix.019"
        Mix_019.blend_type = 'MIX'

        Frame_050 = nt.nodes.new('NodeFrame')
        Frame_050.location = (670.247314453125, -35.545440673828125)
        Frame_050.label = "Specular"
        Frame_050.name = "Frame.050"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (-673.5798950195312, 2016.542724609375)
        Frame_006.label = "Input"
        Frame_006.name = "Frame.006"

        Group_023 = nt.nodes.new('ShaderNodeGroup')
        Group_023.location = (48.9500732421875, -49.0107421875)
        Group_023.name = "Group.023"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (224.80108642578125, -83.8529052734375)
        Reroute_001.name = "Reroute.001"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (224.80108642578125, -105.747802734375)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (224.80108642578125, -127.642578125)
        Reroute_018.name = "Reroute.018"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (1277.9462890625, 396.7091064453125)
        Reroute_019.name = "Reroute.019"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (1245.9075927734375, 410.35546875)
        Reroute_022.name = "Reroute.022"

        Reroute_070 = nt.nodes.new('NodeReroute')
        Reroute_070.location = (3994.2578125, -79.14823150634766)
        Reroute_070.name = "Reroute.070"

        Reroute_071 = nt.nodes.new('NodeReroute')
        Reroute_071.location = (1246.87646484375, 418.4129638671875)
        Reroute_071.name = "Reroute.071"

        Reroute_114 = nt.nodes.new('NodeReroute')
        Reroute_114.location = (1227.5, 545.4317626953125)
        Reroute_114.name = "Reroute.114"

        Group_018 = nt.nodes.new('ShaderNodeGroup')
        Group_018.location = (-149.15234375, 53.802490234375)
        Group_018.name = "Group.018"

        Reroute_129 = nt.nodes.new('NodeReroute')
        Reroute_129.location = (1298.4580078125, 396.7091064453125)
        Reroute_129.name = "Reroute.129"

        Reroute_130 = nt.nodes.new('NodeReroute')
        Reroute_130.location = (201.30126953125, -142.96678161621094)
        Reroute_130.name = "Reroute.130"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (53.82861328125, -283.976318359375)
        Group_012.name = "Group.012"

        Reroute_133 = nt.nodes.new('NodeReroute')
        Reroute_133.location = (224.801025390625, -293.4720458984375)
        Reroute_133.name = "Reroute.133"

        Reroute_134 = nt.nodes.new('NodeReroute')
        Reroute_134.location = (-10.511016845703125, 1723.070556640625)
        Reroute_134.name = "Reroute.134"

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (244.742431640625, -376.1934814453125)
        Group_008.name = "Group.008"

        Reroute_136 = nt.nodes.new('NodeReroute')
        Reroute_136.location = (423.5985107421875, -386.9632568359375)
        Reroute_136.name = "Reroute.136"

        Reroute_137 = nt.nodes.new('NodeReroute')
        Reroute_137.location = (997.8430786132812, 1629.5794677734375)
        Reroute_137.name = "Reroute.137"

        Reroute_144 = nt.nodes.new('NodeReroute')
        Reroute_144.location = (-1198.960205078125, 302.238037109375)
        Reroute_144.name = "Reroute.144"

        Reroute_149 = nt.nodes.new('NodeReroute')
        Reroute_149.location = (997.8430786132812, -740.0789794921875)
        Reroute_149.name = "Reroute.149"

        Reroute_098 = nt.nodes.new('NodeReroute')
        Reroute_098.location = (2914.094482421875, -497.47454833984375)
        Reroute_098.name = "Reroute.098"

        Reroute_138 = nt.nodes.new('NodeReroute')
        Reroute_138.location = (2968.224853515625, -711.3209228515625)
        Reroute_138.name = "Reroute.138"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (1127.52587890625, -938.6796875)
        Reroute_005.name = "Reroute.005"

        Frame_045 = nt.nodes.new('NodeFrame')
        Frame_045.location = (-1183.0345458984375, 812.3239135742188)
        Frame_045.label = "Enviroment Mask"
        Frame_045.name = "Frame.045"

        Mix_024 = nt.nodes.new('ShaderNodeMix')
        Mix_024.location = (79.057861328125, -33.942474365234375)
        Mix_024.name = "Mix.024"
        Mix_024.blend_type = 'MULTIPLY'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (76.6273193359375, -150.17176818847656)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (76.6273193359375, -116.49034118652344)
        Separate_Color.name = "Separate Color"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (1266.864013671875, 396.7091064453125)
        Reroute_028.name = "Reroute.028"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (46.9161376953125, -147.6979522705078)
        Reroute_031.name = "Reroute.031"

        Frame_049 = nt.nodes.new('NodeFrame')
        Frame_049.location = (1958.6611328125, -247.85740661621094)
        Frame_049.label = "Case: Blend With Light Sources"
        Frame_049.name = "Frame.049"

        Frame_052 = nt.nodes.new('NodeFrame')
        Frame_052.location = (738.7132568359375, 1535.980712890625)
        Frame_052.label = "Disable Enviroment"
        Frame_052.name = "Frame.052"

        Frame_053 = nt.nodes.new('NodeFrame')
        Frame_053.location = (2716.3115234375, 1535.980712890625)
        Frame_053.label = "Disable Enviroment"
        Frame_053.name = "Frame.053"

        Frame_054 = nt.nodes.new('NodeFrame')
        Frame_054.location = (4784.40234375, 1535.980712890625)
        Frame_054.label = "Disable Enviroment"
        Frame_054.name = "Frame.054"

        Frame_055 = nt.nodes.new('NodeFrame')
        Frame_055.location = (275.198974609375, 1500.439453125)
        Frame_055.label = "Value Enhance"
        Frame_055.name = "Frame.055"

        Frame_056 = nt.nodes.new('NodeFrame')
        Frame_056.location = (293.6065673828125, -277.16229248046875)
        Frame_056.label = "Value Enhance"
        Frame_056.name = "Frame.056"

        Mix_025 = nt.nodes.new('ShaderNodeMix')
        Mix_025.location = (120.292236328125, -79.31011962890625)
        Mix_025.name = "Mix.025"
        Mix_025.blend_type = 'MULTIPLY'

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (243.625, -161.4825897216797)
        Reroute_032.name = "Reroute.032"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (2202.2861328125, -197.2687530517578)
        Reroute_035.name = "Reroute.035"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (2202.2861328125, -629.8663330078125)
        Reroute_040.name = "Reroute.040"

        Frame_057 = nt.nodes.new('NodeFrame')
        Frame_057.location = (3082.1123046875, 1470.4871826171875)
        Frame_057.label = "World Color"
        Frame_057.name = "Frame.057"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (1127.5257568359375, -982.37841796875)
        Reroute_008.name = "Reroute.008"

        Frame_059 = nt.nodes.new('NodeFrame')
        Frame_059.location = (775.6265869140625, 1310.589599609375)
        Frame_059.label = "Enviroment Mask"
        Frame_059.name = "Frame.059"

        Separate_Color_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_001.location = (-570.122802734375, 37.017608642578125)
        Separate_Color_001.name = "Separate Color.001"

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (-190.08544921875, 33.5531005859375)
        Combine_Color.name = "Combine Color"

        Separate_Color_002 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_002.location = (4456.59619140625, -16.764665603637695)
        Separate_Color_002.name = "Separate Color.002"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-411.08642578125, 24.9307861328125)
        Math_002.label = "x1.2 (Up value 4toon)"
        Math_002.name = "Math.002"
        Math_002.operation = 'MULTIPLY'

        Frame_062 = nt.nodes.new('NodeFrame')
        Frame_062.location = (2246.672119140625, 127.52801513671875)
        Frame_062.label = "Diffuse Mask"
        Frame_062.name = "Frame.062"

        Reroute_056 = nt.nodes.new('NodeReroute')
        Reroute_056.location = (-227.2752685546875, -38.36371612548828)
        Reroute_056.name = "Reroute.056"

        Reroute_064 = nt.nodes.new('NodeReroute')
        Reroute_064.location = (76.3944091796875, -476.1026306152344)
        Reroute_064.name = "Reroute.064"

        Reroute_065 = nt.nodes.new('NodeReroute')
        Reroute_065.location = (76.3944091796875, -383.39422607421875)
        Reroute_065.name = "Reroute.065"

        Reroute_066 = nt.nodes.new('NodeReroute')
        Reroute_066.location = (-78.021484375, -189.796875)
        Reroute_066.name = "Reroute.066"

        Reroute_101 = nt.nodes.new('NodeReroute')
        Reroute_101.location = (318.781494140625, -19.151123046875)
        Reroute_101.name = "Reroute.101"

        Reroute_072 = nt.nodes.new('NodeReroute')
        Reroute_072.location = (4643.30908203125, 1.1163150072097778)
        Reroute_072.name = "Reroute.072"

        Reroute_088 = nt.nodes.new('NodeReroute')
        Reroute_088.location = (4643.30908203125, 89.22980499267578)
        Reroute_088.name = "Reroute.088"

        Reroute_099 = nt.nodes.new('NodeReroute')
        Reroute_099.location = (4643.30908203125, 495.741943359375)
        Reroute_099.name = "Reroute.099"

        Reroute_115 = nt.nodes.new('NodeReroute')
        Reroute_115.location = (4643.30908203125, -279.98040771484375)
        Reroute_115.name = "Reroute.115"

        Reroute_123 = nt.nodes.new('NodeReroute')
        Reroute_123.location = (4643.30908203125, -598.6235961914062)
        Reroute_123.name = "Reroute.123"

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (4456.59619140625, -57.52519989013672)
        Map_Range_001.name = "Map Range.001"

        Value = nt.nodes.new('ShaderNodeValue')
        Value.location = (4287.09619140625, -93.23834991455078)
        Value.label = "Threshhold"
        Value.name = "Value"

        Reroute_113 = nt.nodes.new('NodeReroute')
        Reroute_113.location = (1246.87646484375, -1291.5692138671875)
        Reroute_113.name = "Reroute.113"

        Frame_058 = nt.nodes.new('NodeFrame')
        Frame_058.location = (3082.1123046875, 1265.293701171875)
        Frame_058.label = "World Color"
        Frame_058.name = "Frame.058"

        Reroute_147 = nt.nodes.new('NodeReroute')
        Reroute_147.location = (-703.21533203125, 128.84007263183594)
        Reroute_147.name = "Reroute.147"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (1777.6129150390625, -183.81494140625)
        Reroute_038.name = "Reroute.038"

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-411.08642578125, -9.60260009765625)
        Math_004.name = "Math.004"
        Math_004.operation = 'MULTIPLY'

        Mix_026 = nt.nodes.new('ShaderNodeMix')
        Mix_026.location = (150.50634765625, -261.41009521484375)
        Mix_026.name = "Mix.026"
        Mix_026.blend_type = 'MIX'

        Reroute_125 = nt.nodes.new('NodeReroute')
        Reroute_125.location = (125.8095703125, -421.95849609375)
        Reroute_125.name = "Reroute.125"

        Reroute_150 = nt.nodes.new('NodeReroute')
        Reroute_150.location = (-2.391845703125, 100.94866943359375)
        Reroute_150.name = "Reroute.150"

        Reroute_151 = nt.nodes.new('NodeReroute')
        Reroute_151.location = (-2.391845703125, -443.00921630859375)
        Reroute_151.name = "Reroute.151"

        Reroute_126 = nt.nodes.new('NodeReroute')
        Reroute_126.location = (-89.234375, -462.7850646972656)
        Reroute_126.name = "Reroute.126"

        Reroute_135 = nt.nodes.new('NodeReroute')
        Reroute_135.location = (6003.52099609375, -180.71017456054688)
        Reroute_135.name = "Reroute.135"

        Math_005 = nt.nodes.new('ShaderNodeMath')
        Math_005.location = (6137.70458984375, -100.00779724121094)
        Math_005.name = "Math.005"
        Math_005.operation = 'MULTIPLY'

        Group_025 = nt.nodes.new('ShaderNodeGroup')
        Group_025.location = (56.0694580078125, -431.951904296875)
        Group_025.name = "Group.025"

        Reroute_139 = nt.nodes.new('NodeReroute')
        Reroute_139.location = (251.22869873046875, -468.836669921875)
        Reroute_139.name = "Reroute.139"

        Reroute_140 = nt.nodes.new('NodeReroute')
        Reroute_140.location = (251.22869873046875, -492.9169921875)
        Reroute_140.name = "Reroute.140"

        Reroute_141 = nt.nodes.new('NodeReroute')
        Reroute_141.location = (-95.18817138671875, 1547.7060546875)
        Reroute_141.name = "Reroute.141"

        Reroute_142 = nt.nodes.new('NodeReroute')
        Reroute_142.location = (-126.12994384765625, 1523.625732421875)
        Reroute_142.name = "Reroute.142"

        Reroute_152 = nt.nodes.new('NodeReroute')
        Reroute_152.location = (-554.37158203125, -253.88436889648438)
        Reroute_152.name = "Reroute.152"

        Reroute_153 = nt.nodes.new('NodeReroute')
        Reroute_153.location = (-585.3133544921875, -479.6505432128906)
        Reroute_153.name = "Reroute.153"

        Group_028 = nt.nodes.new('ShaderNodeGroup')
        Group_028.location = (-371.22308349609375, 153.185546875)
        Group_028.name = "Group.028"

        Fresnel_003 = nt.nodes.new('ShaderNodeFresnel')
        Fresnel_003.location = (-880.489013671875, 561.1982421875)
        Fresnel_003.name = "Fresnel.003"

        Reroute_154 = nt.nodes.new('NodeReroute')
        Reroute_154.location = (-554.37158203125, 72.29629516601562)
        Reroute_154.name = "Reroute.154"

        Mix_028 = nt.nodes.new('ShaderNodeMix')
        Mix_028.location = (-707.7691650390625, 654.953369140625)
        Mix_028.name = "Mix.028"
        Mix_028.blend_type = 'MULTIPLY'

        Map_Range_006 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_006.location = (-882.5166625976562, 456.086181640625)
        Map_Range_006.name = "Map Range.006"

        Map_Range_007 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_007.location = (-540.2501220703125, 632.6527099609375)
        Map_Range_007.name = "Map Range.007"

        Math_006 = nt.nodes.new('ShaderNodeMath')
        Math_006.location = (-876.761474609375, 597.5272216796875)
        Math_006.name = "Math.006"
        Math_006.operation = 'MULTIPLY'

        Math_007 = nt.nodes.new('ShaderNodeMath')
        Math_007.location = (-546.38330078125, 669.6761474609375)
        Math_007.name = "Math.007"
        Math_007.operation = 'DIVIDE'

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-244.2042236328125, -845.060546875)
        Reroute_004.name = "Reroute.004"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-2.6510009765625, -889.7938232421875)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-244.2042236328125, -933.171875)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-244.2042236328125, -1265.37744140625)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (-2.6510009765625, -741.1410522460938)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-1090.4205322265625, 347.454345703125)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-222.70654296875, -867.0713500976562)
        Reroute_014.name = "Reroute.014"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (-203.5269775390625, -912.841796875)
        Reroute_016.name = "Reroute.016"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (-232.54248046875, -954.79345703125)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (-232.54248046875, -1331.893798828125)
        Reroute_025.name = "Reroute.025"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (-203.5269775390625, -806.3650512695312)
        Reroute_027.name = "Reroute.027"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (-1068.9228515625, 280.37066650390625)
        Reroute_029.name = "Reroute.029"

        Reroute_074 = nt.nodes.new('NodeReroute')
        Reroute_074.location = (3066.95654296875, 216.65899658203125)
        Reroute_074.name = "Reroute.074"

        Reroute_156 = nt.nodes.new('NodeReroute')
        Reroute_156.location = (-260.38671875, -82.23114013671875)
        Reroute_156.name = "Reroute.156"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-493.865234375, -120.54183959960938)
        Reroute_006.name = "Reroute.006"

        # Create internal links
        nt.links.new(Group_002.outputs[1], Reroute_002.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Group_001.inputs[2])
        nt.links.new(Reroute_007.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Mix_023.outputs[2], Reroute_026.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_030.inputs[0])
        nt.links.new(Reroute_103.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Reroute_042.inputs[0])
        nt.links.new(Reroute_042.outputs[0], Group_009.inputs[1])
        nt.links.new(Group_009.outputs[0], Reroute_045.inputs[0])
        nt.links.new(Reroute_048.outputs[0], Reroute_049.inputs[0])
        nt.links.new(Invert_Color.outputs[0], Reroute_050.inputs[0])
        nt.links.new(Reroute_050.outputs[0], Reroute_051.inputs[0])
        nt.links.new(Reroute_057.outputs[0], Reroute_058.inputs[0])
        nt.links.new(Reroute_058.outputs[0], Reroute_059.inputs[0])
        nt.links.new(Reroute_060.outputs[0], Reroute_061.inputs[0])
        nt.links.new(Reroute_062.outputs[0], Reroute_063.inputs[0])
        nt.links.new(Reroute_067.outputs[0], Reroute_068.inputs[0])
        nt.links.new(Reroute_057.outputs[0], Reroute_069.inputs[0])
        nt.links.new(Reroute_069.outputs[0], Reroute_076.inputs[0])
        nt.links.new(Mix_012.outputs[2], Reroute_079.inputs[0])
        nt.links.new(Reroute_079.outputs[0], Reroute_080.inputs[0])
        nt.links.new(Reroute_078.outputs[0], Reroute_081.inputs[0])
        nt.links.new(Reroute_081.outputs[0], Reroute_082.inputs[0])
        nt.links.new(Reroute_047.outputs[0], Reroute_083.inputs[0])
        nt.links.new(Reroute_077.outputs[0], Reroute_084.inputs[0])
        nt.links.new(Reroute_084.outputs[0], Reroute_085.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Reroute_086.inputs[0])
        nt.links.new(Reroute_086.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Reroute_089.outputs[0], Reroute_087.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Reroute_090.inputs[0])
        nt.links.new(Reroute_092.outputs[0], Reroute_093.inputs[0])
        nt.links.new(Reroute_087.outputs[0], Reroute_094.inputs[0])
        nt.links.new(Reroute_091.outputs[0], Reroute_095.inputs[0])
        nt.links.new(Reroute_095.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Reroute_094.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Reroute_096.outputs[0], GroupOutput.inputs[5])
        nt.links.new(Reroute_093.outputs[0], Reroute_096.inputs[0])
        nt.links.new(GroupInput.outputs[2], Group_026.inputs[0])
        nt.links.new(GroupInput.outputs[0], Group_026.inputs[1])
        nt.links.new(GroupInput.outputs[4], Group_027.inputs[0])
        nt.links.new(GroupInput.outputs[0], Group_027.inputs[1])
        nt.links.new(Reroute_049.outputs[0], Mix_004.inputs[6])
        nt.links.new(GroupInput.outputs[0], Mix_004.inputs[7])
        nt.links.new(Mix_004.outputs[2], Reroute_052.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix_005.inputs[7])
        nt.links.new(Mix_005.outputs[2], Reroute_060.inputs[0])
        nt.links.new(Group_026.outputs[0], Mix_006.inputs[7])
        nt.links.new(Group_027.outputs[0], Mix_008.inputs[7])
        nt.links.new(Reroute_082.outputs[0], Mix_009.inputs[7])
        nt.links.new(Reroute_080.outputs[0], Mix_009.inputs[6])
        nt.links.new(Reroute_083.outputs[0], Mix_010.inputs[7])
        nt.links.new(Reroute_085.outputs[0], Mix_011.inputs[7])
        nt.links.new(Reroute_058.outputs[0], Mix_012.inputs[7])
        nt.links.new(Reroute_063.outputs[0], Mix_012.inputs[6])
        nt.links.new(Reroute_068.outputs[0], Mix_013.inputs[6])
        nt.links.new(Reroute_069.outputs[0], Mix_013.inputs[7])
        nt.links.new(Reroute_076.outputs[0], Mix_014.inputs[6])
        nt.links.new(Reroute_061.outputs[0], Mix_015.inputs[6])
        nt.links.new(Reroute_059.outputs[0], Mix_015.inputs[7])
        nt.links.new(Reroute_042.outputs[0], Reroute_092.inputs[0])
        nt.links.new(Mix_016.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[12], Mix_017.inputs[6])
        nt.links.new(GroupInput.outputs[13], Mix_017.inputs[7])
        nt.links.new(Mix_017.outputs[2], Mix_016.inputs[7])
        nt.links.new(Reroute_090.outputs[0], Reroute_105.inputs[0])
        nt.links.new(Reroute_105.outputs[0], Reroute_091.inputs[0])
        nt.links.new(Reroute_106.outputs[0], Mix_009.inputs[0])
        nt.links.new(Reroute_105.outputs[0], Reroute_108.inputs[0])
        nt.links.new(Reroute_108.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_002.inputs[7])
        nt.links.new(Reroute_048.outputs[0], Reroute_053.inputs[0])
        nt.links.new(Reroute_053.outputs[0], Reroute_100.inputs[0])
        nt.links.new(Reroute_100.outputs[0], Reroute_109.inputs[0])
        nt.links.new(Reroute_109.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_052.outputs[0], Reroute_110.inputs[0])
        nt.links.new(Reroute_110.outputs[0], Mix_001.inputs[7])
        nt.links.new(Mix_002.outputs[2], Reroute_111.inputs[0])
        nt.links.new(Reroute_111.outputs[0], Reroute_112.inputs[0])
        nt.links.new(Reroute_112.outputs[0], Mix_001.inputs[6])
        nt.links.new(Reroute_051.outputs[0], Mix_002.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_002.inputs[6])
        nt.links.new(Math_001.outputs[0], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Reroute_107.inputs[0])
        nt.links.new(Reroute_107.outputs[0], Reroute_106.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Group_004.inputs[3])
        nt.links.new(Reroute_021.outputs[0], Group_002.inputs[3])
        nt.links.new(Mix_009.outputs[2], Mix_011.inputs[6])
        nt.links.new(Mix_019.outputs[2], Mix_023.inputs[6])
        nt.links.new(Reroute_119.outputs[0], Mix_023.inputs[7])
        nt.links.new(Reroute_120.outputs[0], Reroute_121.inputs[0])
        nt.links.new(Reroute_121.outputs[0], Mix_021.inputs[7])
        nt.links.new(Reroute_043.outputs[0], Reroute_089.inputs[0])
        nt.links.new(Mix_013.outputs[2], Reroute_078.inputs[0])
        nt.links.new(Mix_014.outputs[2], Reroute_077.inputs[0])
        nt.links.new(Mix_015.outputs[2], Reroute_047.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_055.outputs[0], Reroute_102.inputs[0])
        nt.links.new(Reroute_102.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Reroute_117.outputs[0], Reroute_124.inputs[0])
        nt.links.new(Reroute_124.outputs[0], Mix_014.inputs[7])
        nt.links.new(Reroute_146.outputs[0], Reroute_062.inputs[0])
        nt.links.new(Reroute_145.outputs[0], Reroute_148.inputs[0])
        nt.links.new(Reroute_148.outputs[0], Mix_018.inputs[6])
        nt.links.new(Mix_001.outputs[2], Mix_018.inputs[7])
        nt.links.new(Mix_018.outputs[2], Reroute_131.inputs[0])
        nt.links.new(Group_013.outputs[1], Reroute_162.inputs[0])
        nt.links.new(Reroute_131.outputs[0], Reroute_146.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_020.inputs[6])
        nt.links.new(Reroute_066.outputs[0], Group_003.inputs[1])
        nt.links.new(Reroute_034.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Mix_021.outputs[2], Reroute_015.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Reroute_103.inputs[0])
        nt.links.new(Group_019.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Mix_010.outputs[2], Mix_016.inputs[6])
        nt.links.new(Reroute_038.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_030.outputs[0], Group_013.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_020.inputs[7])
        nt.links.new(Reroute_132.outputs[0], Reroute_048.inputs[0])
        nt.links.new(Reroute_103.outputs[0], Reroute_132.inputs[0])
        nt.links.new(Reroute_048.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Reroute_002.outputs[0], Mix_007.inputs[6])
        nt.links.new(GroupInput.outputs[21], Mix_007.inputs[0])
        nt.links.new(GroupInput.outputs[22], Mix_007.inputs[7])
        nt.links.new(Reroute_002.outputs[0], Reroute_054.inputs[0])
        nt.links.new(Group_001.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute_073.outputs[0], Reroute_104.inputs[0])
        nt.links.new(Reroute_104.outputs[0], GroupOutput.inputs[6])
        nt.links.new(Reroute_162.outputs[0], Reroute_166.inputs[0])
        nt.links.new(Math.outputs[0], Math_003.inputs[1])
        nt.links.new(Reroute_116.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_116.inputs[0])
        nt.links.new(Reroute_054.outputs[0], Reroute_055.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_073.inputs[0])
        nt.links.new(Reroute_030.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Group_017.inputs[1])
        nt.links.new(Group_004.outputs[1], Mix_019.inputs[7])
        nt.links.new(Group_023.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Group_023.outputs[1], Reroute_017.inputs[0])
        nt.links.new(Group_023.outputs[2], Reroute_018.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_070.inputs[0])
        nt.links.new(Reroute_070.outputs[0], Mix_018.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Reroute_114.inputs[0])
        nt.links.new(Reroute_114.outputs[0], Group_019.inputs[1])
        nt.links.new(GroupInput.outputs[10], Group_018.inputs[3])
        nt.links.new(GroupInput.outputs[14], Group_018.inputs[4])
        nt.links.new(GroupInput.outputs[8], Group_018.inputs[2])
        nt.links.new(Mix_011.outputs[2], Group_018.inputs[1])
        nt.links.new(Group_018.outputs[0], Mix_010.inputs[6])
        nt.links.new(Reroute_019.outputs[0], Reroute_129.inputs[0])
        nt.links.new(Reroute_129.outputs[0], Reroute_130.inputs[0])
        nt.links.new(Reroute_130.outputs[0], Mix_011.inputs[0])
        nt.links.new(GroupInput.outputs[21], Math_001.inputs[1])
        nt.links.new(GroupInput.outputs[14], Group_012.inputs[0])
        nt.links.new(Group_012.outputs[0], Reroute_133.inputs[0])
        nt.links.new(Reroute_133.outputs[0], Reroute_134.inputs[0])
        nt.links.new(Reroute_134.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Vector_Math.outputs[1], Mix_019.inputs[0])
        nt.links.new(GroupInput.outputs[10], Group_008.inputs[0])
        nt.links.new(Group_008.outputs[0], Reroute_136.inputs[0])
        nt.links.new(Reroute_136.outputs[0], Reroute_137.inputs[0])
        nt.links.new(Reroute_144.outputs[0], Group_013.inputs[2])
        nt.links.new(Reroute_137.outputs[0], Reroute_144.inputs[0])
        nt.links.new(Reroute_144.outputs[0], Reroute_149.inputs[0])
        nt.links.new(Reroute_149.outputs[0], Group_009.inputs[2])
        nt.links.new(Mix_007.outputs[2], Mix_021.inputs[6])
        nt.links.new(Reroute_098.outputs[0], Reroute_067.inputs[0])
        nt.links.new(Reroute_138.outputs[0], Reroute_117.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Mix_024.inputs[6])
        nt.links.new(Reroute_005.outputs[0], Separate_Color.inputs[0])
        nt.links.new(Separate_Color.outputs[2], Mix.inputs[2])
        nt.links.new(Reroute_028.outputs[0], Reroute_031.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Mix.inputs[0])
        nt.links.new(Mix_024.outputs[2], Mix_006.inputs[6])
        nt.links.new(Reroute_001.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_166.outputs[0], Group_017.inputs[2])
        nt.links.new(Map_Range_007.outputs[0], Reroute_043.inputs[0])
        nt.links.new(Reroute_045.outputs[0], Mix_025.inputs[6])
        nt.links.new(Mix_025.outputs[2], Mix_008.inputs[6])
        nt.links.new(Mix.outputs[0], Reroute_032.inputs[0])
        nt.links.new(Reroute_032.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Mix_024.inputs[7])
        nt.links.new(Reroute_032.outputs[0], Reroute_040.inputs[0])
        nt.links.new(Reroute_040.outputs[0], Mix_025.inputs[7])
        nt.links.new(Mix_008.outputs[2], Reroute_138.inputs[0])
        nt.links.new(Mix_006.outputs[2], Reroute_098.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Separate_Color_001.inputs[0])
        nt.links.new(Separate_Color_001.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Separate_Color_001.outputs[1], Math_002.inputs[0])
        nt.links.new(Math_002.outputs[0], Combine_Color.inputs[1])
        nt.links.new(Group_013.outputs[0], Reroute_065.inputs[0])
        nt.links.new(Reroute_065.outputs[0], Group_019.inputs[0])
        nt.links.new(Reroute_065.outputs[0], Reroute_064.inputs[0])
        nt.links.new(Reroute_064.outputs[0], Reroute_056.inputs[0])
        nt.links.new(Mix_020.outputs[2], Reroute_066.inputs[0])
        nt.links.new(Reroute_043.outputs[0], Reroute_101.inputs[0])
        nt.links.new(Reroute_101.outputs[0], Mix_005.inputs[6])
        nt.links.new(Reroute_147.outputs[0], Reroute_145.inputs[0])
        nt.links.new(Reroute_072.outputs[0], Reroute_088.inputs[0])
        nt.links.new(Reroute_088.outputs[0], Mix_012.inputs[0])
        nt.links.new(Reroute_088.outputs[0], Reroute_099.inputs[0])
        nt.links.new(Reroute_099.outputs[0], Mix_015.inputs[0])
        nt.links.new(Reroute_072.outputs[0], Reroute_115.inputs[0])
        nt.links.new(Reroute_115.outputs[0], Mix_013.inputs[0])
        nt.links.new(Reroute_115.outputs[0], Reroute_123.inputs[0])
        nt.links.new(Reroute_123.outputs[0], Mix_014.inputs[0])
        nt.links.new(Value.outputs[0], Map_Range_001.inputs[3])
        nt.links.new(Reroute_071.outputs[0], Reroute_113.inputs[0])
        nt.links.new(Reroute_113.outputs[0], Separate_Color_002.inputs[0])
        nt.links.new(Separate_Color_002.outputs[2], Map_Range_001.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Reroute_057.inputs[0])
        nt.links.new(Group_003.outputs[0], Reroute_147.inputs[0])
        nt.links.new(Group_017.outputs[0], Reroute_038.inputs[0])
        nt.links.new(Invert_Color_001.outputs[0], Mix_020.inputs[0])
        nt.links.new(Separate_Color_001.outputs[2], Math_004.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Math_004.inputs[1])
        nt.links.new(Reroute_070.outputs[0], Reroute_125.inputs[0])
        nt.links.new(Reroute_125.outputs[0], Mix_026.inputs[0])
        nt.links.new(Reroute_074.outputs[0], Reroute_150.inputs[0])
        nt.links.new(Reroute_150.outputs[0], Reroute_151.inputs[0])
        nt.links.new(Reroute_151.outputs[0], Mix_026.inputs[6])
        nt.links.new(Reroute_109.outputs[0], Reroute_126.inputs[0])
        nt.links.new(Reroute_126.outputs[0], Mix_026.inputs[7])
        nt.links.new(Mix_026.outputs[2], Reroute_135.inputs[0])
        nt.links.new(GroupInput.outputs[9], Math_005.inputs[0])
        nt.links.new(Reroute_135.outputs[0], Math_005.inputs[1])
        nt.links.new(Math_005.outputs[0], Group_018.inputs[0])
        nt.links.new(Group_025.outputs[0], Reroute_139.inputs[0])
        nt.links.new(Group_025.outputs[1], Reroute_140.inputs[0])
        nt.links.new(Reroute_139.outputs[0], Reroute_141.inputs[0])
        nt.links.new(Reroute_140.outputs[0], Reroute_142.inputs[0])
        nt.links.new(Reroute_142.outputs[0], Reroute_153.inputs[0])
        nt.links.new(Reroute_154.outputs[0], Reroute_152.inputs[0])
        nt.links.new(Reroute_152.outputs[0], Group_002.inputs[1])
        nt.links.new(Reroute_153.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Reroute_153.outputs[0], Group_004.inputs[1])
        nt.links.new(Reroute_141.outputs[0], Reroute_154.inputs[0])
        nt.links.new(Reroute_154.outputs[0], Group_028.inputs[1])
        nt.links.new(Map_Range_006.outputs[0], Mix_028.inputs[7])
        nt.links.new(Group_028.outputs[1], Map_Range_006.inputs[0])
        nt.links.new(Fresnel_003.outputs[0], Mix_028.inputs[6])
        nt.links.new(Mix_028.outputs[2], Map_Range_007.inputs[0])
        nt.links.new(GroupInput.outputs[6], Math_006.inputs[0])
        nt.links.new(Math_006.outputs[0], Map_Range_006.inputs[1])
        nt.links.new(GroupInput.outputs[7], Math_007.inputs[0])
        nt.links.new(Math_007.outputs[0], Map_Range_007.inputs[1])
        nt.links.new(GroupInput.outputs[5], Map_Range_007.inputs[4])
        nt.links.new(GroupInput.outputs[15], Reroute_004.inputs[0])
        nt.links.new(GroupInput.outputs[17], Reroute_009.inputs[0])
        nt.links.new(GroupInput.outputs[19], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Group_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Group_017.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Group_013.inputs[0])
        nt.links.new(GroupInput.outputs[16], Reroute_014.inputs[0])
        nt.links.new(GroupInput.outputs[18], Reroute_016.inputs[0])
        nt.links.new(GroupInput.outputs[20], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Group_009.inputs[3])
        nt.links.new(Reroute_016.outputs[0], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Group_017.inputs[3])
        nt.links.new(Reroute_014.outputs[0], Reroute_029.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Group_013.inputs[3])
        nt.links.new(Reroute_156.outputs[0], Combine_Color.inputs[2])
        nt.links.new(Reroute_156.outputs[0], Reroute_074.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_071.inputs[0])
        nt.links.new(Math_004.outputs[0], Reroute_156.inputs[0])
        nt.links.new(GroupInput.outputs[11], Reroute_120.inputs[0])
        nt.links.new(Reroute_120.outputs[0], Reroute_119.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Invert_Color_001.inputs[1])
        nt.links.new(GroupInput.outputs[23], Group_003.inputs[0])
        nt.links.new(Combine_Color.outputs[0], Group_003.inputs[2])

        # Set default values
        Group_004.inputs[0].default_value = False
        Group_004.inputs[2].default_value = 0.0
        Group_002.inputs[0].default_value = False
        Group_002.inputs[2].default_value = 0.0
        Group_001.inputs[0].default_value = 1.0
        Group_001.inputs[1].default_value = 0.0
        Group_027.inputs[2].default_value = 0.44999998807907104
        Mix_008.inputs[0].default_value = 1.0
        Mix_008.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_008.inputs[2].default_value = 0.0
        Mix_008.inputs[3].default_value = 0.0
        Mix_008.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_008.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[0].default_value = 1.0
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[2].default_value = 0.0
        Mix_006.inputs[3].default_value = 0.0
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_026.inputs[2].default_value = 0.8999999761581421
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[0].default_value = 1.0
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_Color.inputs[0].default_value = 1.0
        Mix_005.inputs[0].default_value = 1.0
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_015.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_015.inputs[2].default_value = 0.0
        Mix_015.inputs[3].default_value = 0.0
        Mix_015.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_015.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_015.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_015.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_012.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_012.inputs[2].default_value = 0.0
        Mix_012.inputs[3].default_value = 0.0
        Mix_012.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_012.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_012.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_012.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_013.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_013.inputs[2].default_value = 0.0
        Mix_013.inputs[3].default_value = 0.0
        Mix_013.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_013.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_013.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_013.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 2.0
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[0].default_value = 1.0
        Math_001.inputs[2].default_value = 0.5
        Math_003.inputs[2].default_value = 0.5
        Mix_014.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_014.inputs[2].default_value = 0.0
        Mix_014.inputs[3].default_value = 0.0
        Mix_014.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_014.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_014.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_014.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_009.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_009.inputs[2].default_value = 0.0
        Mix_009.inputs[3].default_value = 0.0
        Mix_009.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_009.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_011.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_011.inputs[2].default_value = 0.0
        Mix_011.inputs[3].default_value = 0.0
        Mix_011.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_011.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_011.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_011.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_017.inputs[0].default_value = 1.0
        Mix_017.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_017.inputs[2].default_value = 0.0
        Mix_017.inputs[3].default_value = 0.0
        Mix_017.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_017.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_017.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_017.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_016.inputs[0].default_value = 1.0
        Mix_016.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_016.inputs[2].default_value = 0.0
        Mix_016.inputs[3].default_value = 0.0
        Mix_016.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_016.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_016.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_016.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_010.inputs[0].default_value = 1.0
        Mix_010.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_010.inputs[2].default_value = 0.0
        Mix_010.inputs[3].default_value = 0.0
        Mix_010.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_010.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_010.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_010.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_009.inputs[4].default_value = 0.8999999761581421
        Group_009.inputs[5].default_value = 1.0
        Group_009.inputs[6].default_value = 0.75
        Group_009.inputs[7].default_value = 0.800000011920929
        Mix_021.inputs[0].default_value = 1.0
        Mix_021.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_021.inputs[2].default_value = 0.0
        Mix_021.inputs[3].default_value = 0.0
        Mix_021.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_021.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_021.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_021.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_023.inputs[0].default_value = 1.0
        Mix_023.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_023.inputs[2].default_value = 0.0
        Mix_023.inputs[3].default_value = 0.0
        Mix_023.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_023.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_023.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_023.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_020.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_020.inputs[2].default_value = 0.0
        Mix_020.inputs[3].default_value = 0.0
        Mix_020.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_020.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_020.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_020.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_Color_001.inputs[0].default_value = 1.0
        Mix_018.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_018.inputs[2].default_value = 0.0
        Mix_018.inputs[3].default_value = 0.0
        Mix_018.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_018.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_018.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_018.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_013.inputs[4].default_value = 0.8999999761581421
        Group_013.inputs[5].default_value = 0.10000000149011612
        Group_013.inputs[6].default_value = 0.0
        Group_013.inputs[7].default_value = 0.0
        Group_017.inputs[4].default_value = 0.15000000596046448
        Group_017.inputs[5].default_value = 5.0
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[3].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Mix_019.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_019.inputs[2].default_value = 0.0
        Mix_019.inputs[3].default_value = 0.0
        Mix_019.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_019.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_019.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_019.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_019.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_008.inputs[1].default_value = (0.0, 0.0, 0.0)
        Mix_024.inputs[0].default_value = 1.0
        Mix_024.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_024.inputs[2].default_value = 0.0
        Mix_024.inputs[3].default_value = 0.0
        Mix_024.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_024.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_024.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_024.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[3].default_value = 1.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_025.inputs[0].default_value = 1.0
        Mix_025.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_025.inputs[2].default_value = 0.0
        Mix_025.inputs[3].default_value = 0.0
        Mix_025.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_025.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_025.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_025.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_002.inputs[1].default_value = 1.2000000476837158
        Math_002.inputs[2].default_value = 0.5
        Reroute_072.inputs[0].default_value = 0.0
        Map_Range_001.inputs[1].default_value = 0.0
        Map_Range_001.inputs[2].default_value = 1.0
        Map_Range_001.inputs[4].default_value = 1.0
        Map_Range_001.inputs[5].default_value = 4.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_004.inputs[2].default_value = 0.5
        Mix_026.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_026.inputs[2].default_value = 0.0
        Mix_026.inputs[3].default_value = 0.0
        Mix_026.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_026.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_026.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_026.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_005.inputs[2].default_value = 0.5
        Group_028.inputs[0].default_value = True
        Group_028.inputs[2].default_value = 0.0
        Group_028.inputs[3].default_value = (0.0, 0.0, 0.0)
        Fresnel_003.inputs[0].default_value = 1.100000023841858
        Fresnel_003.inputs[1].default_value = (0.0, 0.0, 0.0)
        Mix_028.inputs[0].default_value = 1.0
        Mix_028.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_028.inputs[2].default_value = 0.0
        Mix_028.inputs[3].default_value = 0.0
        Mix_028.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_028.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_028.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_028.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Map_Range_006.inputs[2].default_value = 1.0
        Map_Range_006.inputs[3].default_value = 0.0
        Map_Range_006.inputs[4].default_value = 1.0
        Map_Range_006.inputs[5].default_value = 4.0
        Map_Range_006.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_006.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_006.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_006.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_006.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_006.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_007.inputs[2].default_value = 0.10000000149011612
        Map_Range_007.inputs[3].default_value = 0.0
        Map_Range_007.inputs[5].default_value = 4.0
        Map_Range_007.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_007.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_007.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_007.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_007.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_007.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_006.inputs[1].default_value = -1.0
        Math_006.inputs[2].default_value = 0.5
        Math_007.inputs[1].default_value = 10.0
        Math_007.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
