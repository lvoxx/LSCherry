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


class ShaderNodeBlend_Dark(ShaderNode):
    bl_idname = 'ShaderNodeBlend_Dark'
    bl_label = "Blend Dark"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Factor"].default_value = 1.0
        self.inputs["Mix Multiply And Blend"].default_value = 1.0
        self.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Blend Color"].default_value = (0.0, 0.0, 0.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Blend Dark'

        # Create output sockets
        nt.interface.new_socket('Blended Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Mix Multiply And Blend', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Blend Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)

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

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (-58.180564880371094, 417.8006286621094)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-668.17138671875, 476.02691650390625)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (523.4609375, 476.02691650390625)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (523.4609375, 28.1114501953125)
        Reroute_003.name = "Reroute.003"

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-788.0956420898438, -271.0006408691406)
        Separate_Color.name = "Separate Color"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (592.9998779296875, 180.3450927734375)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (373.0000305175781, -43.70854187011719)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-668.17138671875, 60.91716766357422)
        Reroute.name = "Reroute"

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (152.62855529785156, -288.7783203125)
        Combine_Color.name = "Combine Color"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-542.53515625, -93.56166076660156)
        Math.name = "Math"
        Math.operation = 'ADD'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-542.53515625, -291.0170593261719)
        Math_003.name = "Math.003"
        Math_003.operation = 'ADD'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-542.53515625, -452.8582763671875)
        Math_004.name = "Math.004"
        Math_004.operation = 'ADD'

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-885.9739990234375, 77.80416870117188)
        Reroute_004.name = "Reroute.004"

        Separate_Color_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_001.location = (-788.0956420898438, -455.009521484375)
        Separate_Color_001.name = "Separate Color.001"

        Math_006 = nt.nodes.new('ShaderNodeMath')
        Math_006.location = (-92.74543762207031, -93.56166076660156)
        Math_006.name = "Math.006"
        Math_006.operation = 'MODULO'

        Math_007 = nt.nodes.new('ShaderNodeMath')
        Math_007.location = (-85.99999237060547, -281.081298828125)
        Math_007.name = "Math.007"
        Math_007.operation = 'MODULO'

        Math_008 = nt.nodes.new('ShaderNodeMath')
        Math_008.location = (-86.00000762939453, -447.4449157714844)
        Math_008.name = "Math.008"
        Math_008.operation = 'MODULO'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-306.30902099609375, -93.56166076660156)
        Math_001.name = "Math.001"
        Math_001.operation = 'DIVIDE'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-306.30902099609375, -291.0170593261719)
        Math_002.name = "Math.002"
        Math_002.operation = 'DIVIDE'

        Math_005 = nt.nodes.new('ShaderNodeMath')
        Math_005.location = (-306.30902099609375, -452.8582763671875)
        Math_005.name = "Math.005"
        Math_005.operation = 'DIVIDE'

        # Create internal links
        nt.links.new(GroupInput.outputs[2], Separate_Color.inputs[0])
        nt.links.new(GroupInput.outputs[3], Separate_Color_001.inputs[0])
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Separate_Color.outputs[0], Math.inputs[0])
        nt.links.new(Separate_Color_001.outputs[0], Math.inputs[1])
        nt.links.new(Math.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_003.outputs[0], Math_002.inputs[0])
        nt.links.new(Separate_Color.outputs[1], Math_003.inputs[0])
        nt.links.new(Separate_Color_001.outputs[1], Math_003.inputs[1])
        nt.links.new(GroupInput.outputs[3], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[2], Mix_001.inputs[6])
        nt.links.new(Mix_003.outputs[2], Mix_002.inputs[7])
        nt.links.new(Mix_001.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[1], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix_002.inputs[0])
        nt.links.new(Separate_Color.outputs[2], Math_004.inputs[0])
        nt.links.new(Separate_Color_001.outputs[2], Math_004.inputs[1])
        nt.links.new(Math_004.outputs[0], Math_005.inputs[0])
        nt.links.new(GroupInput.outputs[0], Reroute_004.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix_003.inputs[6])
        nt.links.new(Combine_Color.outputs[0], Mix_003.inputs[7])
        nt.links.new(Reroute_004.outputs[0], Mix_003.inputs[0])
        nt.links.new(Math_006.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Math_007.outputs[0], Combine_Color.inputs[1])
        nt.links.new(Math_008.outputs[0], Combine_Color.inputs[2])
        nt.links.new(Math_001.outputs[0], Math_006.inputs[0])
        nt.links.new(Math_002.outputs[0], Math_007.inputs[0])
        nt.links.new(Math_005.outputs[0], Math_008.inputs[0])

        # Set default values
        Mix_001.inputs[0].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5
        Math_003.inputs[2].default_value = 0.5
        Math_004.inputs[2].default_value = 0.5
        Math_006.inputs[1].default_value = 255.0
        Math_006.inputs[2].default_value = 0.5
        Math_007.inputs[1].default_value = 255.0
        Math_007.inputs[2].default_value = 0.5
        Math_008.inputs[1].default_value = 255.0
        Math_008.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 2.0
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 2.0
        Math_002.inputs[2].default_value = 0.5
        Math_005.inputs[1].default_value = 2.0
        Math_005.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
