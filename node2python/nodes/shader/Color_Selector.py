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


class ShaderNodeColor_Selector(ShaderNode):
    bl_idname = 'ShaderNodeColor_Selector'
    bl_label = "Color Selector"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Case Number"].default_value = 1
        self.inputs["Color 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 2"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 3"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 4"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 5"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 6"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 7"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 8"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 9"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color 10"].default_value = (0.0, 0.0, 0.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Color Selector'

        # Create output sockets
        nt.interface.new_socket('Selected Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Case Number', in_out='INPUT', socket_type='NodeSocketInt')
        input_socket.default_value = 1
        input_socket = nt.interface.new_socket('Color 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 5', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 6', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 7', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 8', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 9', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color 10', in_out='INPUT', socket_type='NodeSocketColor')
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
        Mix_001.location = (-481.2478942871094, -153.72579956054688)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (-743.9290771484375, -400.3948974609375)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (-1177.1661376953125, -829.6622924804688)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (-1683.350341796875, -1194.5777587890625)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MIX'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (-952.0189208984375, -621.5968627929688)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (-1405.95263671875, -1012.6511840820312)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MIX'

        Math_005 = nt.nodes.new('ShaderNodeMath')
        Math_005.location = (-1871.8441162109375, -975.42578125)
        Math_005.name = "Math.005"
        Math_005.operation = 'GREATER_THAN'

        Math_006 = nt.nodes.new('ShaderNodeMath')
        Math_006.location = (-2148.79443359375, -1110.295654296875)
        Math_006.name = "Math.006"
        Math_006.operation = 'GREATER_THAN'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-1674.364013671875, -812.9003295898438)
        Math_004.name = "Math.004"
        Math_004.operation = 'GREATER_THAN'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-1489.7413330078125, -655.294189453125)
        Math_003.name = "Math.003"
        Math_003.operation = 'GREATER_THAN'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-1346.8056640625, -449.7989807128906)
        Math_002.name = "Math.002"
        Math_002.operation = 'GREATER_THAN'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-1209.071533203125, -264.5382385253906)
        Math_001.name = "Math.001"
        Math_001.operation = 'GREATER_THAN'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-1194.1641845703125, -35.95575714111328)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-260.5355529785156, 144.94393920898438)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math_007 = nt.nodes.new('ShaderNodeMath')
        Math_007.location = (-2465.22705078125, -1235.902099609375)
        Math_007.name = "Math.007"
        Math_007.operation = 'GREATER_THAN'

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (-1982.593017578125, -1387.9356689453125)
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MIX'

        Math_008 = nt.nodes.new('ShaderNodeMath')
        Math_008.location = (-2671.56005859375, -1450.7152099609375)
        Math_008.name = "Math.008"
        Math_008.operation = 'GREATER_THAN'

        Mix_008 = nt.nodes.new('ShaderNodeMix')
        Mix_008.location = (-2188.926025390625, -1602.748779296875)
        Mix_008.name = "Mix.008"
        Mix_008.blend_type = 'MIX'

        Math_009 = nt.nodes.new('ShaderNodeMath')
        Math_009.location = (-2922.989501953125, -1574.5716552734375)
        Math_009.name = "Math.009"
        Math_009.operation = 'GREATER_THAN'

        Mix_009 = nt.nodes.new('ShaderNodeMix')
        Mix_009.location = (-2433.908447265625, -1810.46630859375)
        Mix_009.name = "Mix.009"
        Mix_009.blend_type = 'MIX'

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix_001.inputs[6])
        nt.links.new(Mix_001.outputs[2], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[3], Mix_002.inputs[6])
        nt.links.new(Mix_002.outputs[2], Mix_001.inputs[7])
        nt.links.new(Mix_003.outputs[2], Mix_002.inputs[7])
        nt.links.new(Mix_004.outputs[2], Mix_003.inputs[7])
        nt.links.new(Mix_005.outputs[2], Mix_004.inputs[7])
        nt.links.new(GroupInput.outputs[4], Mix_003.inputs[6])
        nt.links.new(GroupInput.outputs[5], Mix_004.inputs[6])
        nt.links.new(GroupInput.outputs[6], Mix_005.inputs[6])
        nt.links.new(GroupInput.outputs[7], Mix_006.inputs[6])
        nt.links.new(GroupInput.outputs[8], Mix_007.inputs[6])
        nt.links.new(Mix_007.outputs[2], Mix_006.inputs[7])
        nt.links.new(GroupInput.outputs[0], Math.inputs[0])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_002.inputs[0])
        nt.links.new(Math_002.outputs[0], Mix_002.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Mix_003.inputs[0])
        nt.links.new(Mix_006.outputs[2], Mix_005.inputs[7])
        nt.links.new(GroupInput.outputs[0], Math_007.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_006.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_005.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_004.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Math_004.outputs[0], Mix_004.inputs[0])
        nt.links.new(Math_005.outputs[0], Mix_005.inputs[0])
        nt.links.new(Math_006.outputs[0], Mix_006.inputs[0])
        nt.links.new(Math_007.outputs[0], Mix_007.inputs[0])
        nt.links.new(Math_008.outputs[0], Mix_008.inputs[0])
        nt.links.new(Mix_008.outputs[2], Mix_007.inputs[7])
        nt.links.new(GroupInput.outputs[9], Mix_008.inputs[6])
        nt.links.new(GroupInput.outputs[0], Math_008.inputs[0])
        nt.links.new(Math_009.outputs[0], Mix_009.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_009.inputs[0])
        nt.links.new(GroupInput.outputs[10], Mix_009.inputs[6])
        nt.links.new(Mix_009.outputs[2], Mix_008.inputs[7])

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
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[2].default_value = 0.0
        Mix_006.inputs[3].default_value = 0.0
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_005.inputs[1].default_value = 6.099999904632568
        Math_005.inputs[2].default_value = 0.5
        Math_006.inputs[1].default_value = 7.099999904632568
        Math_006.inputs[2].default_value = 0.5
        Math_004.inputs[1].default_value = 5.099999904632568
        Math_004.inputs[2].default_value = 0.5
        Math_003.inputs[1].default_value = 4.099999904632568
        Math_003.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 3.0999999046325684
        Math_002.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 2.0999999046325684
        Math_001.inputs[2].default_value = 0.5
        Math.inputs[1].default_value = 1.100000023841858
        Math.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_007.inputs[1].default_value = 8.100000381469727
        Math_007.inputs[2].default_value = 0.5
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[3].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_008.inputs[1].default_value = 9.100000381469727
        Math_008.inputs[2].default_value = 0.5
        Mix_008.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_008.inputs[2].default_value = 0.0
        Mix_008.inputs[3].default_value = 0.0
        Mix_008.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_008.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_009.inputs[1].default_value = 10.100000381469727
        Math_009.inputs[2].default_value = 0.5
        Mix_009.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_009.inputs[2].default_value = 0.0
        Mix_009.inputs[3].default_value = 0.0
        Mix_009.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_009.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_009.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
