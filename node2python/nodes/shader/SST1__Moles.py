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


class ShaderNodeSST1__Moles(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Moles'
    bl_label = "SST1: Moles"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Builder"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Red Color"].default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        self.inputs["Scale"].default_value = 75.0
        self.inputs["Threadhold"].default_value = 0
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Moles'

        # Create output sockets
        nt.interface.new_socket('Builder', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Builder', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 75.0
        input_socket = nt.interface.new_socket('Threadhold', in_out='INPUT', socket_type='NodeSocketInt')
        input_socket.default_value = 0
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

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (-787.4796752929688, 299.2722473144531)
        Voronoi_Texture.name = "Voronoi Texture"

        Voronoi_Texture_001 = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture_001.location = (-792.2933959960938, 670.41943359375)
        Voronoi_Texture_001.name = "Voronoi Texture.001"

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (-613.2284545898438, 609.3649291992188)
        ColorRamp_001.name = "ColorRamp.001"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-967.4796752929688, 259.2722473144531)
        Mapping.name = "Mapping"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-271.3526611328125, 397.8365783691406)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (-972.2932739257812, 630.41943359375)
        Mapping_001.name = "Mapping.001"

        Mapping_002 = nt.nodes.new('ShaderNodeMapping')
        Mapping_002.location = (-958.6446533203125, 751.018798828125)
        Mapping_002.name = "Mapping.002"

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (-453.0848693847656, 1043.5096435546875)
        Noise_Texture.name = "Noise Texture"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (-587.3325805664062, 272.9144287109375)
        ColorRamp.name = "ColorRamp"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (561.3139038085938, 11.55462646484375)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        Invert = nt.nodes.new('ShaderNodeInvert')
        Invert.location = (-24.335580825805664, 139.37413024902344)
        Invert.name = "Invert"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (294.0952453613281, 221.1226043701172)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        ColorRamp_002 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_002.location = (-210.730224609375, 999.4328002929688)
        ColorRamp_002.name = "ColorRamp.002"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (90.96469116210938, 643.0156860351562)
        Math.name = "Math"
        Math.operation = 'ADD'

        # Create internal links
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[2], Voronoi_Texture_001.inputs[2])
        nt.links.new(GroupInput.outputs[2], Voronoi_Texture.inputs[2])
        nt.links.new(Voronoi_Texture.outputs[0], ColorRamp.inputs[0])
        nt.links.new(Mapping.outputs[0], Voronoi_Texture.inputs[0])
        nt.links.new(Voronoi_Texture_001.outputs[0], ColorRamp_001.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Voronoi_Texture_001.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix.inputs[3])
        nt.links.new(ColorRamp_001.outputs[0], Mix.inputs[2])
        nt.links.new(ColorRamp.outputs[0], Mix.inputs[7])
        nt.links.new(ColorRamp_001.outputs[0], Mix.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[2])
        nt.links.new(Mapping_002.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Noise_Texture.outputs[1], ColorRamp_002.inputs[0])
        nt.links.new(Invert.outputs[0], Mix_002.inputs[7])
        nt.links.new(ColorRamp_002.outputs[0], Math.inputs[0])
        nt.links.new(Mix.outputs[2], Invert.inputs[1])
        nt.links.new(Mix_002.outputs[2], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Math.inputs[1])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[4], Mapping_001.inputs[0])
        nt.links.new(GroupInput.outputs[4], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[4], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[4], Mapping_002.inputs[0])
        nt.links.new(GroupInput.outputs[3], Noise_Texture.inputs[2])
        nt.links.new(ColorRamp_002.outputs[0], Mix_002.inputs[0])

        # Set default values
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[3].default_value = 0.0
        Voronoi_Texture.inputs[4].default_value = 0.5
        Voronoi_Texture.inputs[5].default_value = 2.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Voronoi_Texture.inputs[8].default_value = 1.0
        Voronoi_Texture_001.inputs[1].default_value = 0.0
        Voronoi_Texture_001.inputs[3].default_value = 0.0
        Voronoi_Texture_001.inputs[4].default_value = 0.5
        Voronoi_Texture_001.inputs[5].default_value = 2.0
        Voronoi_Texture_001.inputs[6].default_value = 1.0
        Voronoi_Texture_001.inputs[7].default_value = 0.5
        Voronoi_Texture_001.inputs[8].default_value = 1.0
        Mapping.inputs[1].default_value = Vector((0.7999999523162842, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping.inputs[3].default_value = Vector((1.5, 1.0, 1.0))
        Mix.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_001.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_001.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_001.inputs[3].default_value = Vector((1.2000000476837158, 1.8000000715255737, 1.2000000476837158))
        Mapping_002.inputs[1].default_value = Vector((0.09999999403953552, 0.0, 0.0))
        Mapping_002.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_002.inputs[3].default_value = Vector((1.0, 1.0, 1.0))
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[3].default_value = 2.0
        Noise_Texture.inputs[4].default_value = 0.5
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert.inputs[0].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
