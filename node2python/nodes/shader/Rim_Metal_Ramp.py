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


class ShaderNodeRim_Metal_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeRim_Metal_Ramp'
    bl_label = "Rim Metal Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Roughness"].default_value = 0.10000000149011612
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Mix 1"].default_value = 0.699999988079071
        self.inputs["Mix 2"].default_value = 0.8500000238418579
        self.inputs["Mix 3"].default_value = 0.949999988079071
        self.inputs["Lv 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Lv 2"].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        self.inputs["Lv 3"].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        self.inputs["Lv 4"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Rim Metal Ramp'

        # Create output sockets
        nt.interface.new_socket('Metal Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Mix 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.699999988079071
        input_socket = nt.interface.new_socket('Mix 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8500000238418579
        input_socket = nt.interface.new_socket('Mix 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.949999988079071
        input_socket = nt.interface.new_socket('Lv 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Lv 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        input_socket = nt.interface.new_socket('Lv 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        input_socket = nt.interface.new_socket('Lv 4', in_out='INPUT', socket_type='NodeSocketColor')
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

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (-33.31854248046875, -150.17013549804688)
        Group_001.name = "Group.001"

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (-176.43560791015625, 150.170166015625)
        Group_002.name = "Group.002"

        Bright_or_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Bright_or_Contrast.location = (-172.010986328125, 43.83245849609375)
        Bright_or_Contrast.name = "Bright or Contrast"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-478.858154296875, 82.16242218017578)
        Group.name = "Group"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (151.62652587890625, 128.42034912109375)
        Map_Range.name = "Map Range"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (349.1401672363281, 6.087677001953125)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (-14.69964599609375, 30.186492919921875)
        Invert_Color.name = "Invert Color"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-280.15411376953125, 44.17274475097656)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-280.15411376953125, -379.3769836425781)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-336.71673583984375, -40.138771057128906)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-336.71673583984375, -100.54105377197266)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (108.24241638183594, -100.54105377197266)
        Reroute_004.name = "Reroute.004"

        # Create internal links
        nt.links.new(Invert_Color.outputs[0], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute.outputs[0], Group_002.inputs[3])
        nt.links.new(Group_001.outputs[0], Mix_001.inputs[6])
        nt.links.new(Bright_or_Contrast.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Group_002.outputs[2], Bright_or_Contrast.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[0])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[2], Group_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Group_001.inputs[1])
        nt.links.new(GroupInput.outputs[4], Group_001.inputs[2])
        nt.links.new(GroupInput.outputs[5], Group_001.inputs[3])
        nt.links.new(GroupInput.outputs[6], Group_001.inputs[4])
        nt.links.new(GroupInput.outputs[7], Group_001.inputs[5])
        nt.links.new(GroupInput.outputs[8], Group_001.inputs[6])
        nt.links.new(Group.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Group_001.inputs[7])
        nt.links.new(GroupInput.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Bright_or_Contrast.inputs[1])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Map_Range.inputs[2])

        # Set default values
        Group_002.inputs[0].default_value = False
        Group_002.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Group_002.inputs[2].default_value = 0.0
        Bright_or_Contrast.inputs[2].default_value = 0.0
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[3].default_value = 1.0
        Map_Range.inputs[4].default_value = 0.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_Color.inputs[0].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
