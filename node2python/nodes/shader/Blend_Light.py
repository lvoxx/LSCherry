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


class ShaderNodeBlend_Light(ShaderNode):
    bl_idname = 'ShaderNodeBlend_Light'
    bl_label = "Blend Light"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Factor"].default_value = 1.0
        self.inputs["Mix Add And Blend"].default_value = 0.0
        self.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Blend Color"].default_value = (0.0, 0.0, 0.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Blend Light'

        # Create output sockets
        nt.interface.new_socket('Blended Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Mix Add And Blend', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
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
        Mix_001.blend_type = 'ADD'

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-668.17138671875, 476.02691650390625)
        Reroute_001.name = "Reroute.001"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-668.17138671875, 59.636253356933594)
        Reroute.name = "Reroute"

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-568.0955200195312, -25.37151336669922)
        Separate_Color.name = "Separate Color"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (738.197509765625, 476.02691650390625)
        Reroute_002.name = "Reroute.002"

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (587.3651123046875, -43.149192810058594)
        Combine_Color.name = "Combine Color"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (807.7364501953125, 180.3450927734375)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (738.197509765625, 28.1114501953125)
        Reroute_003.name = "Reroute.003"

        Separate_Color_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_001.location = (-568.0955200195312, -209.38037109375)
        Separate_Color_001.name = "Separate Color.001"

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-184.5499725341797, -188.0381622314453)
        Math_004.name = "Math.004"
        Math_004.operation = 'ADD'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-184.5499725341797, -17.24056625366211)
        Math_003.name = "Math.003"
        Math_003.operation = 'ADD'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-184.5499725341797, 150.09715270996094)
        Math.name = "Math"
        Math.operation = 'ADD'

        Math_005 = nt.nodes.new('ShaderNodeMath')
        Math_005.location = (51.67621612548828, -188.0381622314453)
        Math_005.name = "Math.005"
        Math_005.operation = 'DIVIDE'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (51.67621612548828, -17.24056625366211)
        Math_002.name = "Math.002"
        Math_002.operation = 'DIVIDE'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (51.67621612548828, 150.09715270996094)
        Math_001.name = "Math.001"
        Math_001.operation = 'DIVIDE'

        Math_007 = nt.nodes.new('ShaderNodeMath')
        Math_007.location = (289.21795654296875, -17.24056625366211)
        Math_007.name = "Math.007"
        Math_007.operation = 'SUBTRACT'

        Math_006 = nt.nodes.new('ShaderNodeMath')
        Math_006.location = (289.21795654296875, 150.09715270996094)
        Math_006.name = "Math.006"
        Math_006.operation = 'SUBTRACT'

        Math_008 = nt.nodes.new('ShaderNodeMath')
        Math_008.location = (289.21795654296875, -188.0381622314453)
        Math_008.name = "Math.008"
        Math_008.operation = 'SUBTRACT'

        # Create internal links
        nt.links.new(GroupInput.outputs[2], Separate_Color.inputs[0])
        nt.links.new(GroupInput.outputs[3], Separate_Color_001.inputs[0])
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Separate_Color.outputs[0], Math.inputs[0])
        nt.links.new(Separate_Color_001.outputs[0], Math.inputs[1])
        nt.links.new(Math_006.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Separate_Color.outputs[1], Math_003.inputs[0])
        nt.links.new(Separate_Color_001.outputs[1], Math_003.inputs[1])
        nt.links.new(GroupInput.outputs[3], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[2], Mix_001.inputs[6])
        nt.links.new(Combine_Color.outputs[0], Mix_002.inputs[7])
        nt.links.new(Mix_001.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[1], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix_002.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])
        nt.links.new(Math.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_003.outputs[0], Math_002.inputs[0])
        nt.links.new(Math_007.outputs[0], Combine_Color.inputs[1])
        nt.links.new(Math_004.outputs[0], Math_005.inputs[0])
        nt.links.new(Separate_Color.outputs[2], Math_004.inputs[0])
        nt.links.new(Separate_Color_001.outputs[2], Math_004.inputs[1])
        nt.links.new(Math_008.outputs[0], Combine_Color.inputs[2])
        nt.links.new(Math_002.outputs[0], Math_007.inputs[1])
        nt.links.new(Math_001.outputs[0], Math_006.inputs[1])
        nt.links.new(Math_005.outputs[0], Math_008.inputs[1])

        # Set default values
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
        Math_004.inputs[2].default_value = 0.5
        Math_003.inputs[2].default_value = 0.5
        Math.inputs[2].default_value = 0.5
        Math_005.inputs[1].default_value = 2.0
        Math_005.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 2.0
        Math_002.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 2.0
        Math_001.inputs[2].default_value = 0.5
        Math_007.inputs[0].default_value = 1.0
        Math_007.inputs[2].default_value = 0.5
        Math_006.inputs[0].default_value = 1.0
        Math_006.inputs[2].default_value = 0.5
        Math_008.inputs[0].default_value = 1.0
        Math_008.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
