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


class ShaderNodeHSR__Seperate_Body_Lightmap(ShaderNode):
    bl_idname = 'ShaderNodeHSR__Seperate_Body_Lightmap'
    bl_label = "HSR: Seperate Body Lightmap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lightmap"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HSR: Seperate Body Lightmap'

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
        Group.location = (-410.74688720703125, -17.871360778808594)
        Group.name = "Group"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (154.398681640625, 317.74566650390625)
        Map_Range.name = "Map Range"

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (143.47811889648438, -268.27618408203125)
        Map_Range_001.name = "Map Range.001"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (388.5966796875, 181.65969848632812)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (609.0000610351562, 158.89093017578125)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (882.7385864257812, 77.95582580566406)
        Invert_Color.name = "Invert Color"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (330.1296691894531, -271.1135559082031)
        Math_002.name = "Math.002"
        Math_002.operation = 'MULTIPLY'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (762.283203125, -50.005741119384766)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (555.8516845703125, -271.85675048828125)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(Map_Range.outputs[0], Mix.inputs[0])
        nt.links.new(Invert_Color.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group.outputs[0], Map_Range.inputs[0])
        nt.links.new(Group.outputs[0], Mix.inputs[2])
        nt.links.new(Mix.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Group.outputs[2], Map_Range_001.inputs[0])
        nt.links.new(Math_002.outputs[0], Math.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Math_002.inputs[0])
        nt.links.new(Mix_001.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Math.outputs[0], Mix_001.inputs[0])
        nt.links.new(Math_002.outputs[0], Mix_001.inputs[3])

        # Set default values
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
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[3].default_value = 1.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_001.inputs[1].default_value = 10.0
        Math_001.inputs[2].default_value = 0.5
        Invert_Color.inputs[0].default_value = 1.0
        Math_002.inputs[1].default_value = 10.0
        Math_002.inputs[2].default_value = 0.5
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 0.10000000149011612
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
