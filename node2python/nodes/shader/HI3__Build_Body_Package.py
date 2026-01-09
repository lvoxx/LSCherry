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


class ShaderNodeHI3__Build_Body_Package(ShaderNode):
    bl_idname = 'ShaderNodeHI3__Build_Body_Package'
    bl_label = "HI3: Build Body Package"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Body Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Body Alpha"].default_value = 0.0
        self.inputs["Lightmap Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Lighmap  Alpha Texture"].default_value = 0.0
        self.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Range 1"].default_value = 0.10000000149011612
        self.inputs["Range 2"].default_value = 0.30000001192092896
        self.inputs["Range 3"].default_value = 0.44999998807907104
        self.inputs["Range 4"].default_value = 0.6200000047683716
        self.inputs["Map 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Map 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Range 1"].default_value = 0.10000000149011612
        self.inputs["Range 2"].default_value = 0.30000001192092896
        self.inputs["Range 3"].default_value = 0.44999998807907104
        self.inputs["Range 4"].default_value = 0.6200000047683716

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HI3: Build Body Package'

        # Create output sockets
        nt.interface.new_socket('Base Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Shadow Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('SSS Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Body Alpha', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Enable Custom Ramp', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Custom Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')
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
        nt.interface.new_socket('--- Shadow ---', in_out='INPUT', socket_type='NodeSocketShader')
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
        input_socket = nt.interface.new_socket('Range 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Range 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Range 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.44999998807907104
        input_socket = nt.interface.new_socket('Range 4', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.6200000047683716
        nt.interface.new_socket('--- SSS ---', in_out='INPUT', socket_type='NodeSocketShader')
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
        input_socket = nt.interface.new_socket('Range 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Range 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Range 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.44999998807907104
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

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (-163.25311279296875, 176.67845153808594)
        Group_012.name = "Group.012"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (119.60452270507812, 337.15423583984375)
        Reroute_012.name = "Reroute.012"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (119.60452270507812, 140.53842163085938)
        Reroute_011.name = "Reroute.011"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-359.80499267578125, 385.0780334472656)
        Reroute_006.name = "Reroute.006"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (749.6708374023438, 548.0823364257812)
        Reroute_013.name = "Reroute.013"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (703.9854125976562, 459.8439025878906)
        Reroute_015.name = "Reroute.015"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (786.8346557617188, 249.42929077148438)
        Reroute_017.name = "Reroute.017"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (699.9108276367188, -69.5866470336914)
        Reroute_019.name = "Reroute.019"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (786.8346557617188, -50.58142852783203)
        Reroute_018.name = "Reroute.018"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (749.6708374023438, -95.37936401367188)
        Reroute_014.name = "Reroute.014"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (703.9854125976562, -30.21869659423828)
        Reroute_016.name = "Reroute.016"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (243.6751708984375, -346.0987243652344)
        Group_014.name = "Group.014"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (915.252685546875, -383.3872375488281)
        Reroute_021.name = "Reroute.021"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (915.252685546875, -141.6001434326172)
        Reroute_022.name = "Reroute.022"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (851.361328125, -118.61495208740234)
        Reroute_020.name = "Reroute.020"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-183.88922119140625, -274.15557861328125)
        Group_013.name = "Group.013"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-359.80499267578125, -386.8644104003906)
        Reroute_007.name = "Reroute.007"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-292.2634582519531, 88.91595458984375)
        Reroute_001.name = "Reroute.001"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (80.90692901611328, 360.7911376953125)
        Reroute_010.name = "Reroute.010"

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (509.58935546875, 494.6773376464844)
        Group_008.name = "Group.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (80.90692901611328, -331.902587890625)
        Reroute_009.name = "Reroute.009"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (851.361328125, -312.82415771484375)
        Reroute_008.name = "Reroute.008"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (945.45361328125, -312.82415771484375)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (945.45361328125, -161.94097900390625)
        Reroute_025.name = "Reroute.025"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (993.4732666015625, -331.902587890625)
        Reroute_023.name = "Reroute.023"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (993.4732666015625, -184.88821411132812)
        Reroute_026.name = "Reroute.026"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (469.66668701171875, -33.64481735229492)
        Group_011.name = "Group.011"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group_008.inputs[0])
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
        nt.links.new(Group_013.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Group_013.outputs[1], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_010.inputs[0])
        nt.links.new(GroupInput.outputs[5], Group_009.inputs[2])
        nt.links.new(GroupInput.outputs[6], Group_009.inputs[3])
        nt.links.new(GroupInput.outputs[7], Group_009.inputs[4])
        nt.links.new(GroupInput.outputs[8], Group_009.inputs[5])
        nt.links.new(GroupInput.outputs[10], Group_009.inputs[7])
        nt.links.new(GroupInput.outputs[11], Group_009.inputs[8])
        nt.links.new(GroupInput.outputs[12], Group_009.inputs[9])
        nt.links.new(Group_012.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Group_008.inputs[3])
        nt.links.new(Reroute_019.outputs[0], GroupOutput.inputs[2])
        nt.links.new(GroupInput.outputs[15], Group_011.inputs[2])
        nt.links.new(GroupInput.outputs[16], Group_011.inputs[3])
        nt.links.new(GroupInput.outputs[17], Group_011.inputs[4])
        nt.links.new(GroupInput.outputs[18], Group_011.inputs[5])
        nt.links.new(GroupInput.outputs[20], Group_011.inputs[7])
        nt.links.new(GroupInput.outputs[21], Group_011.inputs[8])
        nt.links.new(GroupInput.outputs[22], Group_011.inputs[9])
        nt.links.new(GroupInput.outputs[1], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Group_008.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_009.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Group_011.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Group_014.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], GroupOutput.inputs[5])
        nt.links.new(Reroute_007.outputs[0], Group_013.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Group_008.inputs[2])
        nt.links.new(Reroute_009.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], GroupOutput.inputs[6])
        nt.links.new(Reroute_023.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], GroupOutput.inputs[7])
        nt.links.new(GroupInput.outputs[19], Group_011.inputs[6])
        nt.links.new(GroupInput.outputs[23], Group_011.inputs[10])
        nt.links.new(GroupInput.outputs[9], Group_009.inputs[6])
        nt.links.new(GroupInput.outputs[13], Group_009.inputs[10])

        # Set default values
        Group_009.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[0].default_value = 0.0
        Group_012.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[4].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[5].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_012.inputs[7].default_value = 0.10000000149011612
        Group_012.inputs[8].default_value = 0.30000001192092896
        Group_012.inputs[9].default_value = 0.44999998807907104
        Group_012.inputs[10].default_value = 0.6200000047683716
        Group_014.inputs[1].default_value = 0.5800000429153442
        Group_014.inputs[2].default_value = 0.800000011920929
        Group_014.inputs[3].default_value = 0.949999988079071
        Group_014.inputs[4].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_014.inputs[5].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        Group_014.inputs[6].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        Group_014.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Group_008.inputs[1].default_value = 0.0
        Group_011.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
