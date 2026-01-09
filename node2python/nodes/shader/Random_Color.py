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


class ShaderNodeRandom_Color(ShaderNode):
    bl_idname = 'ShaderNodeRandom_Color'
    bl_label = "Random Color"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Random Color'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets

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

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (541.9999389648438, 10.383028984069824)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (-102.65557861328125, -21.80877685546875)
        Noise_Texture.name = "Noise Texture"

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (-588.892578125, -25.754043579101562)
        Texture_Coordinate.name = "Texture Coordinate"

        Color_Ramp = nt.nodes.new('ShaderNodeValToRGB')
        Color_Ramp.location = (222.058837890625, 34.6854248046875)
        Color_Ramp.name = "Color Ramp"

        # Create internal links
        nt.links.new(Hue_Saturation_Value.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Color_Ramp.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(Noise_Texture.outputs[0], Color_Ramp.inputs[0])
        nt.links.new(Texture_Coordinate.outputs[2], Noise_Texture.inputs[0])

        # Set default values
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[1].default_value = 1.0
        Hue_Saturation_Value.inputs[2].default_value = 1.5
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[2].default_value = 12.09999942779541
        Noise_Texture.inputs[3].default_value = 0.0
        Noise_Texture.inputs[4].default_value = 0.0
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 1.2999999523162842

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
