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


class ShaderNodeBlend_It(ShaderNode):
    bl_idname = 'ShaderNodeBlend_It'
    bl_label = "Blend It"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 1.0
        self.inputs["Color A"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Color B"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Blend It'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Color A', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Color B', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)

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

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (174.92910766601562, -510.36932373046875)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'COLOR'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (173.12796020507812, -548.8197021484375)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MULTIPLY'

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (356.3647766113281, -530.2689208984375)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MIX'

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (530.0919799804688, -571.5687255859375)
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MIX'

        Mix_008 = nt.nodes.new('ShaderNodeMix')
        Mix_008.location = (173.12796020507812, -594.1279296875)
        Mix_008.name = "Mix.008"
        Mix_008.blend_type = 'SOFT_LIGHT'

        Mix_009 = nt.nodes.new('ShaderNodeMix')
        Mix_009.location = (267.15576171875, -143.67227172851562)
        Mix_009.name = "Mix.009"
        Mix_009.blend_type = 'SOFT_LIGHT'

        Mix_010 = nt.nodes.new('ShaderNodeMix')
        Mix_010.location = (710.0000610351562, -475.3290100097656)
        Mix_010.name = "Mix.010"
        Mix_010.blend_type = 'MIX'

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Mix_004.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix_004.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix_005.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix_005.inputs[7])
        nt.links.new(Mix_004.outputs[2], Mix_006.inputs[6])
        nt.links.new(Mix_005.outputs[2], Mix_006.inputs[7])
        nt.links.new(Mix_006.outputs[2], Mix_007.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix_008.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix_008.inputs[7])
        nt.links.new(Mix_008.outputs[2], Mix_007.inputs[7])
        nt.links.new(GroupInput.outputs[2], Mix_009.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_009.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_009.inputs[6])
        nt.links.new(Mix_010.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_010.inputs[0])
        nt.links.new(Mix_007.outputs[2], Mix_010.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix_010.inputs[6])

        # Set default values
        Mix_004.inputs[0].default_value = 1.0
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[0].default_value = 1.0
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[0].default_value = 0.30000001192092896
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[2].default_value = 0.0
        Mix_006.inputs[3].default_value = 0.0
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[0].default_value = 0.699999988079071
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[3].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_008.inputs[0].default_value = 1.0
        Mix_008.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_008.inputs[2].default_value = 0.0
        Mix_008.inputs[3].default_value = 0.0
        Mix_008.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_008.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_009.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_009.inputs[2].default_value = 0.0
        Mix_009.inputs[3].default_value = 0.0
        Mix_009.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_009.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_010.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_010.inputs[2].default_value = 0.0
        Mix_010.inputs[3].default_value = 0.0
        Mix_010.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_010.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_010.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_010.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
