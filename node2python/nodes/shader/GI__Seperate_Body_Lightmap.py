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


class ShaderNodeGI__Seperate_Body_Lightmap(ShaderNode):
    bl_idname = 'ShaderNodeGI__Seperate_Body_Lightmap'
    bl_label = "GI: Seperate Body Lightmap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lightmap"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GI: Seperate Body Lightmap'

        # Create output sockets
        nt.interface.new_socket('Shadow', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Metal', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Lightmap', in_out='INPUT', socket_type='NodeSocketColor')
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

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-251.99998474121094, 0.0)
        Group.name = "Group"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (187.8311004638672, -235.7021484375)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (403.8800964355469, -228.09619140625)
        Math_002.name = "Math.002"
        Math_002.operation = 'GREATER_THAN'

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (21.196884155273438, 194.7568817138672)
        Map_Range.name = "Map Range"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (243.0, 181.30575561523438)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (464.0, 95.79544067382812)
        Math_003.name = "Math.003"
        Math_003.operation = 'MULTIPLY'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (684.0001220703125, 69.20967102050781)
        Invert_Color.name = "Invert Color"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (623.9999389648438, -111.06930541992188)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (-4.974416732788086, -156.86618041992188)
        Map_Range_001.name = "Map Range.001"

        Map_Range_002 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_002.location = (-4.974416732788086, -420.8045654296875)
        Map_Range_002.name = "Map Range.002"

        Map_Range_003 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_003.location = (21.18216323852539, 472.1224670410156)
        Map_Range_003.name = "Map Range.003"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Math_002.inputs[0])
        nt.links.new(Group.outputs[0], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], Mix.inputs[0])
        nt.links.new(Group.outputs[0], Mix.inputs[2])
        nt.links.new(Mix.outputs[0], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Math_002.outputs[0], Mix_001.inputs[0])
        nt.links.new(Group.outputs[2], Map_Range_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix_001.inputs[3])
        nt.links.new(Group.outputs[1], Map_Range_002.inputs[0])
        nt.links.new(Map_Range_002.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group.outputs[0], Map_Range_003.inputs[0])
        nt.links.new(Map_Range_003.outputs[0], GroupOutput.inputs[1])

        # Set default values
        Math_001.inputs[1].default_value = 10.0
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 0.10000000149011612
        Math_002.inputs[2].default_value = 0.5
        Map_Range.inputs[1].default_value = 0.8999999761581421
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[3].default_value = 1.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_003.inputs[1].default_value = 10.0
        Math_003.inputs[2].default_value = 0.5
        Invert_Color.inputs[0].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Map_Range_001.inputs[1].default_value = 0.009999999776482582
        Map_Range_001.inputs[2].default_value = 1.0
        Map_Range_001.inputs[3].default_value = 0.0
        Map_Range_001.inputs[4].default_value = 1.0
        Map_Range_001.inputs[5].default_value = 4.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_002.inputs[1].default_value = 0.0
        Map_Range_002.inputs[2].default_value = 0.20999999344348907
        Map_Range_002.inputs[3].default_value = 0.0
        Map_Range_002.inputs[4].default_value = 1.0
        Map_Range_002.inputs[5].default_value = 4.0
        Map_Range_002.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_002.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_002.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_003.inputs[1].default_value = 0.20999999344348907
        Map_Range_003.inputs[2].default_value = 1.0
        Map_Range_003.inputs[3].default_value = 0.0
        Map_Range_003.inputs[4].default_value = 1.0
        Map_Range_003.inputs[5].default_value = 4.0
        Map_Range_003.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_003.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_003.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
