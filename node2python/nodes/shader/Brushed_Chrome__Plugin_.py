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


class ShaderNodeBrushed_Chrome__Plugin_(ShaderNode):
    bl_idname = 'ShaderNodeBrushed_Chrome__Plugin_'
    bl_label = "Brushed Chrome (Plugin)"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Multiplier"].default_value = 2.0
        self.inputs["Up Pattern Value"].default_value = 2.0
        self.inputs["Strength"].default_value = 0.05000000074505806
        self.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        self.inputs["W"].default_value = 1.0
        self.inputs["Scale"].default_value = 5.0
        self.inputs["Detail"].default_value = 15.0
        self.inputs["Roughness"].default_value = 0.4000000059604645
        self.inputs["Lacunarity"].default_value = 2.0
        self.inputs["Distortion"].default_value = 0.10000000149011612

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Brushed Chrome (Plugin)'

        # Create output sockets
        nt.interface.new_socket('Pattern', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Multiplier', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Up Pattern Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Location', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Rotation', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('W', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 5.0
        input_socket = nt.interface.new_socket('Detail', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 15.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.4000000059604645
        input_socket = nt.interface.new_socket('Lacunarity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Distortion', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612

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
        Noise_Texture.location = (405.426513671875, 170.67596435546875)
        Noise_Texture.name = "Noise Texture"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-15.804824829101562, 130.67596435546875)
        Mapping.name = "Mapping"

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (-255.062255859375, 82.73056030273438)
        Texture_Coordinate.name = "Texture Coordinate"

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (215.8304443359375, 130.67596435546875)
        Mapping_001.name = "Mapping.001"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (39.03759765625, -170.6759490966797)
        Combine_XYZ.name = "Combine XYZ"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-159.4625244140625, -169.7908477783203)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (568.129638671875, 165.532958984375)
        Map_Range.name = "Map Range"

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (745.187255859375, 156.51930236816406)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (656.6054077148438, -93.57685852050781)
        Bump.name = "Bump"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-311.7032470703125, -174.04713439941406)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-311.7032470703125, 192.38107299804688)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (708.7862548828125, 192.38107299804688)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-410.13726806640625, -127.14944458007812)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-410.13726806640625, -149.40597534179688)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-65.33291625976562, -127.14944458007812)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-410.13726806640625, -193.1241912841797)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-410.13726806640625, -340.787353515625)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (518.0396728515625, -340.787353515625)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (518.0396728515625, -176.8378143310547)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-389.59039306640625, -236.90768432617188)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-363.26385498046875, -214.95681762695312)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (-389.59039306640625, 236.60595703125)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-363.26385498046875, 215.11712646484375)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-50.23329544067383, 236.60595703125)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (-75.37831115722656, 215.11712646484375)
        Reroute_015.name = "Reroute.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (-50.23329544067383, 25.922672271728516)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (-75.37831115722656, 3.4315948486328125)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (182.41249084472656, 236.60595703125)
        Reroute_018.name = "Reroute.018"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (157.26747131347656, 215.11712646484375)
        Reroute_019.name = "Reroute.019"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (182.41249084472656, 25.922672271728516)
        Reroute_020.name = "Reroute.020"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (157.26747131347656, 3.4315948486328125)
        Reroute_021.name = "Reroute.021"

        # Create internal links
        nt.links.new(Mapping.outputs[0], Mapping_001.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Texture_Coordinate.outputs[3], Mapping.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mapping_001.inputs[3])
        nt.links.new(Reroute_003.outputs[0], Math.inputs[0])
        nt.links.new(Math.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Math.inputs[1])
        nt.links.new(Noise_Texture.outputs[0], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(Hue_Saturation_Value.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Noise_Texture.outputs[0], Bump.inputs[2])
        nt.links.new(Bump.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[6], Noise_Texture.inputs[1])
        nt.links.new(GroupInput.outputs[7], Noise_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[8], Noise_Texture.inputs[3])
        nt.links.new(GroupInput.outputs[9], Noise_Texture.inputs[4])
        nt.links.new(GroupInput.outputs[10], Noise_Texture.inputs[5])
        nt.links.new(GroupInput.outputs[11], Noise_Texture.inputs[8])
        nt.links.new(GroupInput.outputs[2], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Hue_Saturation_Value.inputs[2])
        nt.links.new(GroupInput.outputs[0], Reroute_003.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_004.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Mapping.inputs[3])
        nt.links.new(GroupInput.outputs[3], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Bump.inputs[0])
        nt.links.new(GroupInput.outputs[5], Reroute_010.inputs[0])
        nt.links.new(GroupInput.outputs[4], Reroute_011.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Mapping.inputs[1])
        nt.links.new(Reroute_017.outputs[0], Mapping.inputs[2])
        nt.links.new(Reroute_019.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Mapping_001.inputs[1])
        nt.links.new(Reroute_021.outputs[0], Mapping_001.inputs[2])

        # Set default values
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Combine_XYZ.inputs[1].default_value = 0.0
        Combine_XYZ.inputs[2].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = -1.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[1].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Bump.inputs[1].default_value = 1.0
        Bump.inputs[3].default_value = (0.0, 0.0, 0.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
