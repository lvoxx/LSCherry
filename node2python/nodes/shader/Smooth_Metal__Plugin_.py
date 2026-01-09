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


class ShaderNodeSmooth_Metal__Plugin_(ShaderNode):
    bl_idname = 'ShaderNodeSmooth_Metal__Plugin_'
    bl_label = "Smooth Metal (Plugin)"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Mix Various"].default_value = 0.10000000149011612
        self.inputs["Strength"].default_value = 0.05000000074505806
        self.inputs["Increase Pattern Value"].default_value = 2.0
        self.inputs["Scale"].default_value = 0.10000000149011612
        self.inputs["Detail"].default_value = 10.0
        self.inputs["Roughness"].default_value = 0.20000000298023224
        self.inputs["Lacunarity"].default_value = 2.0
        self.inputs["Randomness"].default_value = 1.0
        self.inputs["W"].default_value = 1.0
        self.inputs["Scale"].default_value = 0.10000000149011612
        self.inputs["Detail"].default_value = 10.0
        self.inputs["Roughness"].default_value = 0.44999998807907104
        self.inputs["Lacunarity"].default_value = 2.0
        self.inputs["Distortion"].default_value = 0.0
        self.inputs["W"].default_value = 1.0
        self.inputs["Scale"].default_value = 0.05000000074505806
        self.inputs["Detail"].default_value = 10.0
        self.inputs["Roughness"].default_value = 1.0
        self.inputs["Lacunarity"].default_value = 2.0
        self.inputs["Distortion"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Smooth Metal (Plugin)'

        # Create output sockets
        nt.interface.new_socket('Pattern', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Mix Various', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Increase Pattern Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Detail', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 10.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.20000000298023224
        input_socket = nt.interface.new_socket('Lacunarity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Randomness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('W', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Detail', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 10.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.44999998807907104
        input_socket = nt.interface.new_socket('Lacunarity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.0
        input_socket = nt.interface.new_socket('Distortion', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('W', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Detail', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 10.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
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

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-625.64013671875, 158.6919708251953)
        Mapping.name = "Mapping"

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (-779.7080078125, 146.48004150390625)
        Texture_Coordinate.name = "Texture Coordinate"

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (-380.1769714355469, 470.43450927734375)
        Voronoi_Texture.name = "Voronoi Texture"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (-151.98388671875, 172.9978790283203)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'LINEAR_LIGHT'

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (24.061962127685547, 141.7974853515625)
        Noise_Texture.name = "Noise Texture"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (231.34600830078125, 25.03679656982422)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'LINEAR_LIGHT'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-459.57098388671875, 123.51231384277344)
        Reroute.name = "Reroute"

        Noise_Texture_001 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_001.location = (445.81500244140625, 2.70361328125)
        Noise_Texture_001.name = "Noise Texture.001"

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (667.0501098632812, 58.16465377807617)
        Map_Range_001.name = "Map Range.001"

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (850.0393676757812, 65.47665405273438)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (733.6646118164062, -196.75672912597656)
        Bump.name = "Bump"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-753.4114379882812, -59.01238250732422)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-753.4114379882812, -324.8916320800781)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-205.845947265625, -225.5001220703125)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-459.57098388671875, -8.037156105041504)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-459.57098388671875, -163.84933471679688)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-205.845947265625, 11.619425773620605)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (196.516357421875, -225.5001220703125)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (196.516357421875, -135.60838317871094)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-753.4114379882812, -36.23979949951172)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-178.66177368164062, 412.75909423828125)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-178.66177368164062, -31.127639770507812)
        Reroute_011.name = "Reroute.011"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-625.6443481445312, -189.01918029785156)
        Map_Range.name = "Map Range"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (134.98135375976562, 314.35986328125)
        Frame.label = "May causes performance issue, try to use matcap instead"
        Frame.name = "Frame"

        # Create internal links
        nt.links.new(Mix_003.outputs[2], Noise_Texture_001.inputs[0])
        nt.links.new(Texture_Coordinate.outputs[3], Mapping.inputs[0])
        nt.links.new(Noise_Texture.outputs[1], Mix_003.inputs[7])
        nt.links.new(Noise_Texture_001.outputs[0], Map_Range_001.inputs[0])
        nt.links.new(Mix_002.outputs[2], Noise_Texture.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(Mapping.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Voronoi_Texture.inputs[0])
        nt.links.new(Hue_Saturation_Value.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Bump.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Reroute_009.outputs[0], Mapping.inputs[3])
        nt.links.new(GroupInput.outputs[1], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Map_Range.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Mix_002.inputs[6])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Mix_003.inputs[6])
        nt.links.new(Reroute_003.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Mix_002.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Mix_002.inputs[7])
        nt.links.new(Reroute_002.outputs[0], Map_Range.inputs[0])
        nt.links.new(Voronoi_Texture.outputs[1], Reroute_010.inputs[0])
        nt.links.new(Noise_Texture_001.outputs[0], Bump.inputs[2])
        nt.links.new(GroupInput.outputs[4], Voronoi_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[5], Voronoi_Texture.inputs[3])
        nt.links.new(GroupInput.outputs[6], Voronoi_Texture.inputs[4])
        nt.links.new(GroupInput.outputs[7], Voronoi_Texture.inputs[5])
        nt.links.new(GroupInput.outputs[8], Voronoi_Texture.inputs[8])
        nt.links.new(GroupInput.outputs[10], Noise_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[11], Noise_Texture.inputs[3])
        nt.links.new(GroupInput.outputs[12], Noise_Texture.inputs[4])
        nt.links.new(GroupInput.outputs[13], Noise_Texture.inputs[5])
        nt.links.new(GroupInput.outputs[14], Noise_Texture.inputs[8])
        nt.links.new(GroupInput.outputs[9], Noise_Texture.inputs[1])
        nt.links.new(GroupInput.outputs[15], Noise_Texture_001.inputs[1])
        nt.links.new(GroupInput.outputs[17], Noise_Texture_001.inputs[3])
        nt.links.new(GroupInput.outputs[18], Noise_Texture_001.inputs[4])
        nt.links.new(GroupInput.outputs[19], Noise_Texture_001.inputs[5])
        nt.links.new(GroupInput.outputs[20], Noise_Texture_001.inputs[8])
        nt.links.new(GroupInput.outputs[16], Noise_Texture_001.inputs[2])
        nt.links.new(GroupInput.outputs[2], Bump.inputs[0])
        nt.links.new(GroupInput.outputs[3], Hue_Saturation_Value.inputs[2])

        # Set default values
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture_001.inputs[6].default_value = 0.0
        Noise_Texture_001.inputs[7].default_value = 1.0
        Map_Range_001.inputs[1].default_value = 0.0
        Map_Range_001.inputs[2].default_value = 1.0
        Map_Range_001.inputs[3].default_value = -1.0
        Map_Range_001.inputs[4].default_value = 1.0
        Map_Range_001.inputs[5].default_value = 4.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[1].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Bump.inputs[1].default_value = 1.0
        Bump.inputs[3].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.009999999776482582
        Map_Range.inputs[4].default_value = 0.9900000095367432
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
