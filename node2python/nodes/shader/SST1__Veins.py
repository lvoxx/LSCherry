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


class ShaderNodeSST1__Veins(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Veins'
    bl_label = "SST1: Veins"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Builder"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Blue Color"].default_value = (0.35572776198387146, 0.082790806889534, 0.800000011920929, 1.0)
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Mask Scale"].default_value = 7.0
        self.inputs["Strength"].default_value = 1.0
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Veins'

        # Create output sockets
        nt.interface.new_socket('Builder', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Builder', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Blue Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.35572776198387146, 0.082790806889534, 0.800000011920929, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Mask Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 7.0
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
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

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (-406.425537109375, 100.4263916015625)
        Noise_Texture.name = "Noise Texture"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-603.987060546875, 72.609130859375)
        Mapping.name = "Mapping"

        Noise_Texture_001 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_001.location = (39.596435546875, 194.2781982421875)
        Noise_Texture_001.name = "Noise Texture.001"

        ColorRamp_002 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_002.location = (271.8576965332031, 471.7603454589844)
        ColorRamp_002.name = "ColorRamp.002"

        Noise_Texture_002 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_002.location = (36.507564544677734, 497.9704895019531)
        Noise_Texture_002.name = "Noise Texture.002"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (684.0132446289062, 170.9726104736328)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (263.0909118652344, 188.2017364501953)
        ColorRamp_001.name = "ColorRamp.001"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1557.9462890625, -37.04841613769531)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (323.5619812011719, -326.6441345214844)
        Voronoi_Texture.name = "Voronoi Texture"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (526.8511352539062, -304.5538635253906)
        ColorRamp.name = "ColorRamp"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (907.9888305664062, 152.14817810058594)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (1314.5264892578125, 44.909603118896484)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-849.4810791015625, -206.96209716796875)
        Combine_XYZ.name = "Combine XYZ"

        # Create internal links
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mapping.inputs[3])
        nt.links.new(Voronoi_Texture.outputs[0], ColorRamp.inputs[0])
        nt.links.new(Noise_Texture.outputs[1], Voronoi_Texture.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture_001.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix.inputs[6])
        nt.links.new(Mix_001.outputs[2], Mix.inputs[0])
        nt.links.new(Noise_Texture_001.outputs[1], ColorRamp_001.inputs[0])
        nt.links.new(ColorRamp_001.outputs[0], Mix_001.inputs[6])
        nt.links.new(Noise_Texture_002.outputs[1], ColorRamp_002.inputs[0])
        nt.links.new(ColorRamp_002.outputs[0], Mix_001.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture_002.inputs[0])
        nt.links.new(Math.outputs[0], Mix_002.inputs[0])
        nt.links.new(GroupInput.outputs[3], Noise_Texture_002.inputs[2])
        nt.links.new(Mix.outputs[2], Math.inputs[0])
        nt.links.new(GroupInput.outputs[2], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[2], Combine_XYZ.inputs[1])
        nt.links.new(GroupInput.outputs[2], Combine_XYZ.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix_002.inputs[7])
        nt.links.new(GroupInput.outputs[4], Math.inputs[1])
        nt.links.new(GroupInput.outputs[5], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[5], GroupOutput.inputs[1])

        # Set default values
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[2].default_value = 38.599998474121094
        Noise_Texture.inputs[3].default_value = 2.0
        Noise_Texture.inputs[4].default_value = 0.5
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Mapping.inputs[1].default_value = Vector((0.09999999403953552, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture_001.inputs[1].default_value = 0.0
        Noise_Texture_001.inputs[2].default_value = 50.0
        Noise_Texture_001.inputs[3].default_value = 2.0
        Noise_Texture_001.inputs[4].default_value = 0.5
        Noise_Texture_001.inputs[5].default_value = 2.0
        Noise_Texture_001.inputs[6].default_value = 0.0
        Noise_Texture_001.inputs[7].default_value = 1.0
        Noise_Texture_001.inputs[8].default_value = 0.0
        Noise_Texture_002.inputs[1].default_value = 0.0
        Noise_Texture_002.inputs[3].default_value = 2.0
        Noise_Texture_002.inputs[4].default_value = 0.5
        Noise_Texture_002.inputs[5].default_value = 2.0
        Noise_Texture_002.inputs[6].default_value = 0.0
        Noise_Texture_002.inputs[7].default_value = 1.0
        Noise_Texture_002.inputs[8].default_value = 0.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[2].default_value = 5.0
        Voronoi_Texture.inputs[3].default_value = 0.0
        Voronoi_Texture.inputs[4].default_value = 0.5
        Voronoi_Texture.inputs[5].default_value = 2.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Voronoi_Texture.inputs[8].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
