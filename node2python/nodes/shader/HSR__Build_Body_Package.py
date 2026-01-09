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


class ShaderNodeHSR__Build_Body_Package(ShaderNode):
    bl_idname = 'ShaderNodeHSR__Build_Body_Package'
    bl_label = "HSR: Build Body Package"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Body Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Body Alpha"].default_value = 0.0
        self.inputs["Lightmap Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Lighmap  Alpha Texture"].default_value = 0.0
        self.inputs["Fac"].default_value = 0.0
        self.inputs["Map 1"].default_value = (0.8518279790878296, 0.8518394231796265, 0.8518364429473877, 1.0)
        self.inputs["Map 2"].default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        self.inputs["Map 3"].default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        self.inputs["Map 4"].default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        self.inputs["Map 5"].default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
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
        nt.description = 'HSR: Build Body Package'

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
        nt.interface.new_socket('-- Fake Shadow --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Map 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8518279790878296, 0.8518394231796265, 0.8518364429473877, 1.0)
        input_socket = nt.interface.new_socket('Map 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        input_socket = nt.interface.new_socket('Map 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        input_socket = nt.interface.new_socket('Map 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        input_socket = nt.interface.new_socket('Map 5', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8549872040748596, 0.854993462562561, 0.8549931645393372, 1.0)
        input_socket = nt.interface.new_socket('Range 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Range 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Range 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.44999998807907104
        input_socket = nt.interface.new_socket('Range 4', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.6200000047683716
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

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (469.66668701171875, 54.39471435546875)
        Group_009.name = "Group.009"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (1187.905029296875, 794.9137573242188)
        Reroute_015.name = "Reroute.015"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (784.7681884765625, -75.69245147705078)
        Reroute_019.name = "Reroute.019"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (786.8346557617188, -52.32594299316406)
        Reroute_018.name = "Reroute.018"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (1187.905029296875, -29.346439361572266)
        Reroute_016.name = "Reroute.016"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (964.995361328125, -110.56251525878906)
        Group_014.name = "Group.014"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (1205.2579345703125, -118.61495971679688)
        Reroute_020.name = "Reroute.020"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-153.73291015625, -594.967529296875)
        Group_013.name = "Group.013"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (1205.2579345703125, -653.2064819335938)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (1205.2579345703125, -161.94097900390625)
        Reroute_025.name = "Reroute.025"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (1167.956787109375, -631.6388549804688)
        Reroute_023.name = "Reroute.023"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (1167.956787109375, -184.88821411132812)
        Reroute_026.name = "Reroute.026"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (469.66668701171875, -265.8857421875)
        Group_011.name = "Group.011"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (469.66668701171875, 378.1245422363281)
        Group_010.name = "Group.010"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (829.9855346679688, 641.1907348632812)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (992.2984008789062, 830.6312255859375)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (738.54150390625, -631.6388549804688)
        Reroute_027.name = "Reroute.027"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (738.54150390625, 480.8481750488281)
        Reroute_028.name = "Reroute.028"

        # Create internal links
        nt.links.new(GroupInput.outputs[16], Group_009.inputs[2])
        nt.links.new(GroupInput.outputs[17], Group_009.inputs[3])
        nt.links.new(GroupInput.outputs[18], Group_009.inputs[4])
        nt.links.new(GroupInput.outputs[19], Group_009.inputs[5])
        nt.links.new(GroupInput.outputs[21], Group_009.inputs[7])
        nt.links.new(GroupInput.outputs[22], Group_009.inputs[8])
        nt.links.new(GroupInput.outputs[23], Group_009.inputs[9])
        nt.links.new(Reroute_019.outputs[0], GroupOutput.inputs[2])
        nt.links.new(GroupInput.outputs[26], Group_011.inputs[2])
        nt.links.new(GroupInput.outputs[27], Group_011.inputs[3])
        nt.links.new(GroupInput.outputs[28], Group_011.inputs[4])
        nt.links.new(GroupInput.outputs[29], Group_011.inputs[5])
        nt.links.new(GroupInput.outputs[31], Group_011.inputs[7])
        nt.links.new(GroupInput.outputs[32], Group_011.inputs[8])
        nt.links.new(GroupInput.outputs[33], Group_011.inputs[9])
        nt.links.new(Reroute_015.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute_018.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Group_011.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_020.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], GroupOutput.inputs[6])
        nt.links.new(Reroute_023.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], GroupOutput.inputs[7])
        nt.links.new(GroupInput.outputs[30], Group_011.inputs[6])
        nt.links.new(GroupInput.outputs[34], Group_011.inputs[10])
        nt.links.new(GroupInput.outputs[20], Group_009.inputs[6])
        nt.links.new(GroupInput.outputs[24], Group_009.inputs[10])
        nt.links.new(Mix_001.outputs[2], Reroute_015.inputs[0])
        nt.links.new(Group_014.outputs[0], GroupOutput.inputs[5])
        nt.links.new(GroupInput.outputs[2], Group_013.inputs[0])
        nt.links.new(GroupInput.outputs[3], Group_009.inputs[0])
        nt.links.new(GroupInput.outputs[3], Group_011.inputs[0])
        nt.links.new(GroupInput.outputs[6], Group_010.inputs[2])
        nt.links.new(GroupInput.outputs[7], Group_010.inputs[3])
        nt.links.new(GroupInput.outputs[8], Group_010.inputs[4])
        nt.links.new(GroupInput.outputs[9], Group_010.inputs[5])
        nt.links.new(GroupInput.outputs[10], Group_010.inputs[6])
        nt.links.new(GroupInput.outputs[3], Group_010.inputs[0])
        nt.links.new(GroupInput.outputs[11], Group_010.inputs[7])
        nt.links.new(GroupInput.outputs[12], Group_010.inputs[8])
        nt.links.new(GroupInput.outputs[13], Group_010.inputs[9])
        nt.links.new(GroupInput.outputs[14], Group_010.inputs[10])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[5], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], GroupOutput.inputs[3])
        nt.links.new(Group_010.outputs[0], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(Reroute_027.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Group_013.outputs[1], Reroute_024.inputs[0])
        nt.links.new(Group_009.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Group_013.outputs[0], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Mix.inputs[0])

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
        Group_010.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
