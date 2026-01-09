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


class ShaderNodeAnisotropic_Spherical__Plugin_(ShaderNode):
    bl_idname = 'ShaderNodeAnisotropic_Spherical__Plugin_'
    bl_label = "Anisotropic Spherical (Plugin)"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Mix Various"].default_value = 0.05000000074505806
        self.inputs["Up Pattern Value"].default_value = 1.0
        self.inputs["Strength"].default_value = 0.05000000074505806
        self.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
        self.inputs["W"].default_value = 1.0
        self.inputs["Scale"].default_value = 50.0
        self.inputs["Detail"].default_value = 15.0
        self.inputs["Roughness"].default_value = 0.20000000298023224
        self.inputs["Lacunarity"].default_value = 2.0
        self.inputs["Distortion"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Anisotropic Spherical (Plugin)'

        # Create output sockets
        nt.interface.new_socket('Pattern', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Mix Various', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Up Pattern Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Location', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Rotation', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('W', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 50.0
        input_socket = nt.interface.new_socket('Detail', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 15.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.20000000298023224
        input_socket = nt.interface.new_socket('Lacunarity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Distortion', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Gradient_Texture = nt.nodes.new('ShaderNodeTexGradient')
        Gradient_Texture.location = (-112.9836654663086, 75.9822998046875)
        Gradient_Texture.name = "Gradient Texture"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-349.1093444824219, -11.37994384765625)
        Mapping.name = "Mapping"

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (-571.1637573242188, -45.572998046875)
        Texture_Coordinate.name = "Texture Coordinate"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (51.993896484375, 2.7601318359375)
        Mix.name = "Mix"
        Mix.blend_type = 'LINEAR_LIGHT'

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (212.4324493408203, -7.9222412109375)
        Noise_Texture.name = "Noise Texture"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (400.3648986816406, 127.16937255859375)
        Map_Range.name = "Map Range"

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (572.1372680664062, 102.8538818359375)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (494.8610534667969, -127.1693115234375)
        Bump.name = "Bump"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-98.68272399902344, -229.10296630859375)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-98.68272399902344, -157.5101776123047)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-169.00001525878906, -46.38099670410156)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-169.00001525878906, -201.3207244873047)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-372.65850830078125, -250.9442901611328)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-372.65850830078125, 144.22329711914062)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (542.8218994140625, 144.22329711914062)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-372.65850830078125, -273.6918029785156)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-372.65850830078125, -340.5963134765625)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (417.1956787109375, -340.5963134765625)
        Reroute_009.name = "Reroute.009"

        # Create internal links
        nt.links.new(Reroute_002.outputs[0], Gradient_Texture.inputs[0])
        nt.links.new(Texture_Coordinate.outputs[3], Mapping.inputs[0])
        nt.links.new(Map_Range.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(Mix.outputs[2], Noise_Texture.inputs[0])
        nt.links.new(Noise_Texture.outputs[0], Bump.inputs[2])
        nt.links.new(Noise_Texture.outputs[0], Map_Range.inputs[0])
        nt.links.new(Gradient_Texture.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[3], Mapping.inputs[1])
        nt.links.new(GroupInput.outputs[4], Mapping.inputs[2])
        nt.links.new(GroupInput.outputs[5], Mapping.inputs[3])
        nt.links.new(Hue_Saturation_Value.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Bump.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Mix.inputs[0])
        nt.links.new(Mapping.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[6], Noise_Texture.inputs[1])
        nt.links.new(GroupInput.outputs[7], Noise_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[8], Noise_Texture.inputs[3])
        nt.links.new(GroupInput.outputs[9], Noise_Texture.inputs[4])
        nt.links.new(GroupInput.outputs[10], Noise_Texture.inputs[5])
        nt.links.new(GroupInput.outputs[11], Noise_Texture.inputs[8])
        nt.links.new(GroupInput.outputs[1], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Hue_Saturation_Value.inputs[3])
        nt.links.new(GroupInput.outputs[2], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Bump.inputs[0])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
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
        Hue_Saturation_Value.inputs[2].default_value = 2.0
        Bump.inputs[1].default_value = 1.0
        Bump.inputs[3].default_value = (0.0, 0.0, 0.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
