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


class ShaderNodeGI__Build_Body_Package(ShaderNode):
    bl_idname = 'ShaderNodeGI__Build_Body_Package'
    bl_label = "GI: Build Body Package"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Body Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Body Alpha"].default_value = 0.0
        self.inputs["Lightmap Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Lighmap  Alpha Texture"].default_value = 0.0
        self.inputs["Normal Map"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Mix Core And Dot"].default_value = 0.0
        self.inputs["Roughness"].default_value = 0.20000000298023224
        self.inputs["Emission Strength"].default_value = 1.0
        self.inputs["Range 1"].default_value = 0.10000000149011612
        self.inputs["Range 2"].default_value = 0.30000001192092896
        self.inputs["Range 3"].default_value = 0.44999998807907104
        self.inputs["Range 4"].default_value = 0.6200000047683716
        self.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GI: Build Body Package'

        # Create output sockets
        nt.interface.new_socket('Base Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Shadow Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('SSS Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Body Alpha', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Emission', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Emission Strength', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Enable Metal Ramp', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Metal Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Metal Mask', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Shadow Mask', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Body Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Body Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Lightmap Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Lighmap  Alpha Texture', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Normal Map', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Mix Core And Dot', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.20000000298023224
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Range 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Range 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Range 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.44999998807907104
        input_socket = nt.interface.new_socket('Range 4', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.6200000047683716
        input_socket = nt.interface.new_socket('Map 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 5', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 5', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Map 5', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)

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

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (29.35137939453125, 197.34471130371094)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-292.2634582519531, -122.03985595703125)
        Reroute_004.name = "Reroute.004"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-292.2634582519531, 361.5968933105469)
        Reroute.name = "Reroute"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (54.47758483886719, -122.03985595703125)
        Reroute_005.name = "Reroute.005"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (29.35137939453125, 361.5968933105469)
        Reroute_002.name = "Reroute.002"

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (469.66668701171875, 286.6356506347656)
        Group_009.name = "Group.009"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-359.80499267578125, 385.0780334472656)
        Reroute_006.name = "Reroute.006"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (749.6708374023438, 548.0823364257812)
        Reroute_013.name = "Reroute.013"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (703.9854125976562, 469.8345031738281)
        Reroute_015.name = "Reroute.015"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (786.8346557617188, 249.42929077148438)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (786.8346557617188, -51.772850036621094)
        Reroute_018.name = "Reroute.018"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (749.6708374023438, -113.14118957519531)
        Reroute_014.name = "Reroute.014"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (703.9854125976562, -25.45301055908203)
        Reroute_016.name = "Reroute.016"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (243.6751708984375, -525.7843017578125)
        Group_014.name = "Group.014"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (915.252685546875, -563.0728759765625)
        Reroute_021.name = "Reroute.021"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (915.252685546875, -206.9132080078125)
        Reroute_022.name = "Reroute.022"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (851.361328125, -183.9280242919922)
        Reroute_020.name = "Reroute.020"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-183.88922119140625, -448.6891784667969)
        Group_013.name = "Group.013"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-359.80499267578125, -549.60595703125)
        Reroute_007.name = "Reroute.007"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-292.2634582519531, 222.040771484375)
        Reroute_001.name = "Reroute.001"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (851.361328125, -504.10174560546875)
        Reroute_008.name = "Reroute.008"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (945.45361328125, -504.10174560546875)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (945.45361328125, -227.25404357910156)
        Reroute_025.name = "Reroute.025"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (993.4732666015625, -483.2522277832031)
        Reroute_023.name = "Reroute.023"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (993.4732666015625, -250.20127868652344)
        Reroute_026.name = "Reroute.026"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (469.66668701171875, -33.64481735229492)
        Group_011.name = "Group.011"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-370.61279296875, 903.4631958007812)
        Frame.label = "Use GI Starter to quickly build GI material"
        Frame.name = "Frame"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (191.33860778808594, 510.07708740234375)
        Group.name = "Group"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (-217.91363525390625, 303.9656066894531)
        Group_010.name = "Group.010"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (143.24815368652344, 339.9540710449219)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (155.92575073242188, 319.05755615234375)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (90.51316833496094, 267.5625915527344)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (90.51316833496094, 384.7322998046875)
        Reroute_012.name = "Reroute.012"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (-482.5066833496094, -156.93911743164062)
        Reroute_019.name = "Reroute.019"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (-464.6040954589844, -178.6919708251953)
        Reroute_027.name = "Reroute.027"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (-446.70147705078125, -200.40292358398438)
        Reroute_028.name = "Reroute.028"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (-425.97216796875, -222.11387634277344)
        Reroute_029.name = "Reroute.029"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (-482.5066833496094, 92.94432830810547)
        Reroute_030.name = "Reroute.030"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (-464.6040954589844, 71.19147491455078)
        Reroute_031.name = "Reroute.031"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (-446.70147705078125, 49.48052215576172)
        Reroute_032.name = "Reroute.032"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (-425.97216796875, 27.769569396972656)
        Reroute_033.name = "Reroute.033"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (188.0257568359375, -156.93911743164062)
        Reroute_034.name = "Reroute.034"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (162.520263671875, -178.6919708251953)
        Reroute_035.name = "Reroute.035"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (138.86465454101562, -200.40292358398438)
        Reroute_036.name = "Reroute.036"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (113.32388305664062, -222.11387634277344)
        Reroute_037.name = "Reroute.037"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (188.0257568359375, 72.42876434326172)
        Reroute_038.name = "Reroute.038"

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (162.520263671875, 50.6759033203125)
        Reroute_039.name = "Reroute.039"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (138.86465454101562, 28.96495819091797)
        Reroute_040.name = "Reroute.040"

        Reroute_041 = nt.nodes.new('NodeReroute')
        Reroute_041.location = (113.32388305664062, 7.253997802734375)
        Reroute_041.name = "Reroute.041"

        Reroute_042 = nt.nodes.new('NodeReroute')
        Reroute_042.location = (113.32388305664062, -311.9578552246094)
        Reroute_042.name = "Reroute.042"

        Reroute_043 = nt.nodes.new('NodeReroute')
        Reroute_043.location = (138.86465454101562, -290.7949523925781)
        Reroute_043.name = "Reroute.043"

        Reroute_044 = nt.nodes.new('NodeReroute')
        Reroute_044.location = (162.520263671875, -269.6727294921875)
        Reroute_044.name = "Reroute.044"

        Reroute_045 = nt.nodes.new('NodeReroute')
        Reroute_045.location = (188.0257568359375, -248.550537109375)
        Reroute_045.name = "Reroute.045"

        Reroute_046 = nt.nodes.new('NodeReroute')
        Reroute_046.location = (964.3346557617188, 626.4466552734375)
        Reroute_046.name = "Reroute.046"

        Reroute_047 = nt.nodes.new('NodeReroute')
        Reroute_047.location = (964.3346557617188, -95.86810302734375)
        Reroute_047.name = "Reroute.047"

        Reroute_048 = nt.nodes.new('NodeReroute')
        Reroute_048.location = (-307.2923278808594, 626.4466552734375)
        Reroute_048.name = "Reroute.048"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (773.36083984375, 586.384033203125)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Reroute_049 = nt.nodes.new('NodeReroute')
        Reroute_049.location = (703.9854125976562, -139.3238067626953)
        Reroute_049.name = "Reroute.049"

        Reroute_050 = nt.nodes.new('NodeReroute')
        Reroute_050.location = (987.0357055664062, 550.7222900390625)
        Reroute_050.name = "Reroute.050"

        Reroute_051 = nt.nodes.new('NodeReroute')
        Reroute_051.location = (987.0357055664062, -161.08700561523438)
        Reroute_051.name = "Reroute.051"

        # Create internal links
        nt.links.new(GroupInput.outputs[3], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Group_009.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Group_011.inputs[0])
        nt.links.new(GroupInput.outputs[2], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Group_013.outputs[1], Reroute_008.inputs[0])
        nt.links.new(GroupInput.outputs[12], Group_009.inputs[2])
        nt.links.new(GroupInput.outputs[13], Group_009.inputs[3])
        nt.links.new(GroupInput.outputs[14], Group_009.inputs[4])
        nt.links.new(GroupInput.outputs[15], Group_009.inputs[5])
        nt.links.new(GroupInput.outputs[17], Group_011.inputs[2])
        nt.links.new(GroupInput.outputs[18], Group_011.inputs[3])
        nt.links.new(GroupInput.outputs[19], Group_011.inputs[4])
        nt.links.new(GroupInput.outputs[20], Group_011.inputs[5])
        nt.links.new(GroupInput.outputs[1], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Reroute_015.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_009.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Reroute_008.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], GroupOutput.inputs[7])
        nt.links.new(Group_014.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], GroupOutput.inputs[8])
        nt.links.new(Reroute_007.outputs[0], Group_013.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], GroupOutput.inputs[9])
        nt.links.new(Reroute_023.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], GroupOutput.inputs[10])
        nt.links.new(GroupInput.outputs[21], Group_011.inputs[6])
        nt.links.new(GroupInput.outputs[16], Group_009.inputs[6])
        nt.links.new(Group.outputs[0], Reroute_015.inputs[0])
        nt.links.new(GroupInput.outputs[0], Group.inputs[1])
        nt.links.new(Reroute_009.outputs[0], Group.inputs[3])
        nt.links.new(Reroute_010.outputs[0], Group.inputs[4])
        nt.links.new(Reroute_001.outputs[0], Group_010.inputs[0])
        nt.links.new(Group_013.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Group_011.outputs[0], GroupOutput.inputs[2])
        nt.links.new(GroupInput.outputs[5], Reroute_009.inputs[0])
        nt.links.new(GroupInput.outputs[6], Reroute_010.inputs[0])
        nt.links.new(Group_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Group.inputs[2])
        nt.links.new(GroupInput.outputs[22], Group_010.inputs[2])
        nt.links.new(GroupInput.outputs[23], Group_010.inputs[3])
        nt.links.new(GroupInput.outputs[24], Group_010.inputs[4])
        nt.links.new(GroupInput.outputs[25], Group_010.inputs[5])
        nt.links.new(GroupInput.outputs[26], Group_010.inputs[6])
        nt.links.new(GroupInput.outputs[8], Reroute_019.inputs[0])
        nt.links.new(GroupInput.outputs[9], Reroute_027.inputs[0])
        nt.links.new(GroupInput.outputs[10], Reroute_028.inputs[0])
        nt.links.new(GroupInput.outputs[11], Reroute_029.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_030.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_031.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Reroute_032.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Group_010.inputs[10])
        nt.links.new(Reroute_032.outputs[0], Group_010.inputs[9])
        nt.links.new(Reroute_031.outputs[0], Group_010.inputs[8])
        nt.links.new(Reroute_030.outputs[0], Group_010.inputs[7])
        nt.links.new(Reroute_029.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Reroute_038.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_039.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Reroute_040.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Reroute_041.inputs[0])
        nt.links.new(Reroute_038.outputs[0], Group_009.inputs[7])
        nt.links.new(Reroute_039.outputs[0], Group_009.inputs[8])
        nt.links.new(Reroute_040.outputs[0], Group_009.inputs[9])
        nt.links.new(Reroute_041.outputs[0], Group_009.inputs[10])
        nt.links.new(Reroute_037.outputs[0], Reroute_042.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Reroute_043.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_044.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Reroute_045.inputs[0])
        nt.links.new(Reroute_045.outputs[0], Group_011.inputs[7])
        nt.links.new(Reroute_044.outputs[0], Group_011.inputs[8])
        nt.links.new(Reroute_043.outputs[0], Group_011.inputs[9])
        nt.links.new(Reroute_042.outputs[0], Group_011.inputs[10])
        nt.links.new(Reroute_048.outputs[0], Reroute_046.inputs[0])
        nt.links.new(Reroute_046.outputs[0], Reroute_047.inputs[0])
        nt.links.new(Reroute_047.outputs[0], GroupOutput.inputs[3])
        nt.links.new(GroupInput.outputs[4], Reroute_048.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_049.inputs[0])
        nt.links.new(Reroute_049.outputs[0], GroupOutput.inputs[5])
        nt.links.new(Reroute_013.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[7], Math.inputs[1])
        nt.links.new(Math.outputs[0], Reroute_050.inputs[0])
        nt.links.new(Reroute_050.outputs[0], Reroute_051.inputs[0])
        nt.links.new(Reroute_051.outputs[0], GroupOutput.inputs[6])

        # Set default values
        Group_009.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_014.inputs[1].default_value = 0.5800000429153442
        Group_014.inputs[2].default_value = 0.800000011920929
        Group_014.inputs[3].default_value = 0.949999988079071
        Group_014.inputs[4].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_014.inputs[5].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        Group_014.inputs[6].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        Group_014.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Group_011.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        Group.inputs[0].default_value = 1.0
        Group.inputs[5].default_value = (0.0, 0.0, 0.0)
        Group_010.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
