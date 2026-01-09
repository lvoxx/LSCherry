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


class ShaderNodeSST1__Blemishes(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Blemishes'
    bl_label = "SST1: Blemishes"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Builder"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Red Color"].default_value = (0.8999999761581421, 0.19262465834617615, 0.13571682572364807, 1.0)
        self.inputs["Blue Color"].default_value = (0.3672824203968048, 0.24802467226982117, 0.8999999761581421, 1.0)
        self.inputs["Size"].default_value = 1.100000023841858
        self.inputs["Strength"].default_value = 1.0
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Blemishes'

        # Create output sockets
        nt.interface.new_socket('Builder', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Builder', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8999999761581421, 0.19262465834617615, 0.13571682572364807, 1.0)
        input_socket = nt.interface.new_socket('Blue Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.3672824203968048, 0.24802467226982117, 0.8999999761581421, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.100000023841858
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

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (-217.18475341796875, 358.1181640625)
        Mapping_001.name = "Mapping.001"

        Noise_Texture_001 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_001.location = (14.221753120422363, 505.1114501953125)
        Noise_Texture_001.name = "Noise Texture.001"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (206.98255920410156, 215.9663543701172)
        ColorRamp.name = "ColorRamp"

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (26.512100219726562, 182.0371551513672)
        Noise_Texture.name = "Noise Texture"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-216.86880493164062, 275.5738525390625)
        Mapping.name = "Mapping"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (590.14599609375, 243.8597412109375)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        ColorRamp_002 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_002.location = (208.282958984375, 955.2742309570312)
        ColorRamp_002.name = "ColorRamp.002"

        Noise_Texture_002 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_002.location = (27.81256103515625, 921.3450317382812)
        Noise_Texture_002.name = "Noise Texture.002"

        Mapping_002 = nt.nodes.new('ShaderNodeMapping')
        Mapping_002.location = (-216.5802764892578, 439.599365234375)
        Mapping_002.name = "Mapping.002"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (596.834228515625, 889.9492797851562)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MULTIPLY'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1402.8897705078125, 375.63250732421875)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'OVERLAY'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (1148.755126953125, 109.32256317138672)
        Mix.name = "Mix"
        Mix.blend_type = 'OVERLAY'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (930.453369140625, 200.7408447265625)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (818.7147827148438, 709.9691162109375)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (217.14248657226562, 501.28955078125)
        ColorRamp_001.name = "ColorRamp.001"

        # Create internal links
        nt.links.new(GroupInput.outputs[3], Noise_Texture.inputs[2])
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Noise_Texture.outputs[1], ColorRamp.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix.inputs[2])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(Noise_Texture_001.outputs[1], ColorRamp_001.inputs[0])
        nt.links.new(ColorRamp_001.outputs[0], Mix_001.inputs[0])
        nt.links.new(Mapping_001.outputs[0], Noise_Texture_001.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix_001.inputs[6])
        nt.links.new(Mix_001.outputs[2], Math.inputs[0])
        nt.links.new(GroupInput.outputs[4], Math.inputs[1])
        nt.links.new(Noise_Texture_002.outputs[1], ColorRamp_002.inputs[0])
        nt.links.new(Mapping_002.outputs[0], Noise_Texture_002.inputs[0])
        nt.links.new(ColorRamp_002.outputs[0], Mix_003.inputs[6])
        nt.links.new(GroupInput.outputs[3], Noise_Texture_002.inputs[2])
        nt.links.new(Mix.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[4], Math_001.inputs[1])
        nt.links.new(Mix_003.outputs[2], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix_002.inputs[0])
        nt.links.new(ColorRamp_001.outputs[0], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[5], Mapping_001.inputs[0])
        nt.links.new(GroupInput.outputs[5], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[5], Mapping_002.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix_002.inputs[7])
        nt.links.new(GroupInput.outputs[5], GroupOutput.inputs[1])

        # Set default values
        Mapping_001.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_001.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_001.inputs[3].default_value = Vector((1.0, 1.0, 1.0))
        Noise_Texture_001.inputs[1].default_value = 0.0
        Noise_Texture_001.inputs[2].default_value = 50.0
        Noise_Texture_001.inputs[3].default_value = 2.0
        Noise_Texture_001.inputs[4].default_value = 0.5
        Noise_Texture_001.inputs[5].default_value = 2.0
        Noise_Texture_001.inputs[6].default_value = 0.0
        Noise_Texture_001.inputs[7].default_value = 1.0
        Noise_Texture_001.inputs[8].default_value = 0.0
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[3].default_value = 2.0
        Noise_Texture.inputs[4].default_value = 0.5
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping.inputs[3].default_value = Vector((500.0, 500.0, 500.0))
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture_002.inputs[1].default_value = 0.0
        Noise_Texture_002.inputs[3].default_value = 2.0
        Noise_Texture_002.inputs[4].default_value = 0.5
        Noise_Texture_002.inputs[5].default_value = 2.0
        Noise_Texture_002.inputs[6].default_value = 0.0
        Noise_Texture_002.inputs[7].default_value = 1.0
        Noise_Texture_002.inputs[8].default_value = 0.0
        Mapping_002.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_002.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_002.inputs[3].default_value = Vector((450.0, 450.0, 450.0))
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
