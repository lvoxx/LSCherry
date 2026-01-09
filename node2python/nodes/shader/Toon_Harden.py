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


class ShaderNodeToon_Harden(ShaderNode):
    bl_idname = 'ShaderNodeToon_Harden'
    bl_label = "Toon Harden"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Shading"].default_value = 0.0
        self.inputs["Size"].default_value = 0.8999999761581421
        self.inputs["Smooth"].default_value = 0.15000000596046448
        self.inputs["White Level"].default_value = 1.0
        self.inputs["Soft Shading Fac"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Toon Harden'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8999999761581421
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.15000000596046448
        input_socket = nt.interface.new_socket('White Level', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Soft Shading Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (145.10354614257812, -217.89096069335938)
        Math.name = "Math"
        Math.operation = 'ADD'

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-184.78570556640625, -95.95645904541016)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-220.95433044433594, -222.6627960205078)
        Reroute_004.name = "Reroute.004"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-184.78570556640625, -290.76568603515625)
        Reroute_002.name = "Reroute.002"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (682.1121826171875, 174.96876525878906)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (117.86553955078125, 235.2051544189453)
        Map_Range_001.name = "Map Range.001"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-220.95433044433594, 95.4958724975586)
        Reroute_005.name = "Reroute.005"

        Script = nt.nodes.new('ShaderNodeScript')
        Script.location = (-3692.534423828125, 49.04938888549805)
        Script.name = "Script"

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-153.56248474121094, -349.49609375)
        Math_003.name = "Math.003"
        Math_003.operation = 'MAXIMUM'

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (362.9831237792969, -4.021301746368408)
        Map_Range.name = "Map Range"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-79.26952362060547, 32.98460388183594)
        Math_001.name = "Math.001"
        Math_001.operation = 'SUBTRACT'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-79.26952362060547, -128.2460174560547)
        Math_002.name = "Math.002"
        Math_002.operation = 'SUBTRACT'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-474.0295715332031, -241.2061004638672)
        Math_004.name = "Math.004"
        Math_004.operation = 'SUBTRACT'

        # Create internal links
        nt.links.new(Map_Range_001.outputs[0], Map_Range.inputs[0])
        nt.links.new(Math.outputs[0], Map_Range.inputs[2])
        nt.links.new(Math_001.outputs[0], Map_Range_001.inputs[1])
        nt.links.new(GroupInput.outputs[3], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Math_001.inputs[1])
        nt.links.new(GroupInput.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Map_Range_001.inputs[0])
        nt.links.new(GroupInput.outputs[4], Mix.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Map_Range.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[2], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Math.inputs[1])
        nt.links.new(Math_002.outputs[0], Math.inputs[0])
        nt.links.new(Math_002.outputs[0], Map_Range.inputs[1])
        nt.links.new(GroupInput.outputs[1], Math_004.inputs[0])
        nt.links.new(Math_004.outputs[0], Math_002.inputs[1])

        # Set default values
        Math.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
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
        Math_003.inputs[1].default_value = 0.009999999776482582
        Math_003.inputs[2].default_value = 0.5
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_001.inputs[0].default_value = 1.0
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[0].default_value = 1.0
        Math_002.inputs[2].default_value = 0.5
        Math_004.inputs[1].default_value = 0.10000000149011612
        Math_004.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
