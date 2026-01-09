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


class ShaderNodeSST1__Skin_Bump(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Skin_Bump'
    bl_label = "SST1: Skin Bump"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Pores (require)"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Goose Bumps"].default_value = 0.0
        self.inputs["Details"].default_value = 0.30000001192092896
        self.inputs["Skin Scale"].default_value = 9.0
        self.inputs["Noise Scale"].default_value = 50.0
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Skin Bump'

        # Create output sockets
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Pores (require)', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Goose Bumps', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Details', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Skin Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 9.0
        input_socket = nt.interface.new_socket('Noise Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 50.0
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
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

        ColorRamp_005 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_005.location = (68.5015869140625, -249.48028564453125)
        ColorRamp_005.name = "ColorRamp.005"

        ColorRamp_006 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_006.location = (69.91107177734375, 4.5892333984375)
        ColorRamp_006.name = "ColorRamp.006"

        ColorRamp_004 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_004.location = (89.59808349609375, 248.72756958007812)
        ColorRamp_004.name = "ColorRamp.004"

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (427.24053955078125, 78.65878295898438)
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MULTIPLY'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (786.3019409179688, 180.87889099121094)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MULTIPLY'

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (128.5283966064453, 530.4926147460938)
        ColorRamp.name = "ColorRamp"

        Noise_Texture_002 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_002.location = (-139.1096649169922, 530.7962036132812)
        Noise_Texture_002.name = "Noise Texture.002"

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (-141.70558166503906, 239.77838134765625)
        Noise_Texture.name = "Noise Texture"

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (-547.6753540039062, 37.490234375)
        Mapping_001.name = "Mapping.001"

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (-135.90493774414062, -51.195247650146484)
        Voronoi_Texture.name = "Voronoi Texture"

        Noise_Texture_001 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_001.location = (-140.345947265625, -326.91839599609375)
        Noise_Texture_001.name = "Noise Texture.001"

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (1016.4611206054688, 398.5201110839844)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MIX'

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (1216.7667236328125, 404.4734802246094)
        Bump.name = "Bump"

        Bump_001 = nt.nodes.new('ShaderNodeBump')
        Bump_001.location = (1390.9560546875, 406.4095153808594)
        Bump_001.name = "Bump.001"

        Invert = nt.nodes.new('ShaderNodeInvert')
        Invert.location = (1203.473388671875, 225.90773010253906)
        Invert.label = "Goosebumps"
        Invert.name = "Invert"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-782.0856323242188, -209.17237854003906)
        Combine_XYZ.name = "Combine XYZ"

        # Create internal links
        nt.links.new(Combine_XYZ.outputs[0], Mapping_001.inputs[3])
        nt.links.new(Noise_Texture.outputs[1], ColorRamp_004.inputs[0])
        nt.links.new(Voronoi_Texture.outputs[0], ColorRamp_006.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Noise_Texture_001.inputs[0])
        nt.links.new(Noise_Texture_001.outputs[1], ColorRamp_005.inputs[0])
        nt.links.new(ColorRamp_006.outputs[0], Mix_007.inputs[7])
        nt.links.new(ColorRamp_005.outputs[0], Mix_007.inputs[6])
        nt.links.new(Mix_007.outputs[2], Mix_005.inputs[6])
        nt.links.new(ColorRamp_004.outputs[0], Mix_005.inputs[7])
        nt.links.new(Mapping_001.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Voronoi_Texture.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Noise_Texture_002.inputs[0])
        nt.links.new(Mix_005.outputs[2], Mix_006.inputs[6])
        nt.links.new(ColorRamp.outputs[0], Mix_006.inputs[7])
        nt.links.new(GroupInput.outputs[4], Noise_Texture_002.inputs[2])
        nt.links.new(GroupInput.outputs[2], Mix_006.inputs[0])
        nt.links.new(Noise_Texture_002.outputs[1], ColorRamp.inputs[0])
        nt.links.new(Mix_006.outputs[2], Bump.inputs[2])
        nt.links.new(Bump_001.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Invert.outputs[0], Bump_001.inputs[2])
        nt.links.new(Bump.outputs[0], Bump_001.inputs[3])
        nt.links.new(GroupInput.outputs[0], Invert.inputs[1])
        nt.links.new(GroupInput.outputs[1], Invert.inputs[0])
        nt.links.new(GroupInput.outputs[5], Mapping_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[3], Combine_XYZ.inputs[1])
        nt.links.new(GroupInput.outputs[3], Combine_XYZ.inputs[2])

        # Set default values
        Mix_007.inputs[0].default_value = 1.0
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[3].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[0].default_value = 1.0
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture_002.inputs[1].default_value = 0.0
        Noise_Texture_002.inputs[3].default_value = 2.0
        Noise_Texture_002.inputs[4].default_value = 0.5
        Noise_Texture_002.inputs[5].default_value = 2.0
        Noise_Texture_002.inputs[6].default_value = 0.0
        Noise_Texture_002.inputs[7].default_value = 1.0
        Noise_Texture_002.inputs[8].default_value = 0.0
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[2].default_value = 600.0
        Noise_Texture.inputs[3].default_value = 2.0
        Noise_Texture.inputs[4].default_value = 0.5
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Mapping_001.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_001.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[2].default_value = 550.0
        Voronoi_Texture.inputs[3].default_value = 0.0
        Voronoi_Texture.inputs[4].default_value = 0.5
        Voronoi_Texture.inputs[5].default_value = 2.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Voronoi_Texture.inputs[8].default_value = 1.0
        Noise_Texture_001.inputs[1].default_value = 0.0
        Noise_Texture_001.inputs[2].default_value = 500.0
        Noise_Texture_001.inputs[3].default_value = 2.0
        Noise_Texture_001.inputs[4].default_value = 0.5
        Noise_Texture_001.inputs[5].default_value = 2.0
        Noise_Texture_001.inputs[6].default_value = 0.0
        Noise_Texture_001.inputs[7].default_value = 1.0
        Noise_Texture_001.inputs[8].default_value = 0.0
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[2].default_value = 0.0
        Mix_006.inputs[3].default_value = 0.0
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Bump.inputs[0].default_value = 0.125
        Bump.inputs[1].default_value = 1.0
        Bump.inputs[3].default_value = (0.0, 0.0, 0.0)
        Bump_001.inputs[0].default_value = 0.15000000596046448
        Bump_001.inputs[1].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
