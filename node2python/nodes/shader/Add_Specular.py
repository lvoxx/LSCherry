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


class ShaderNodeAdd_Specular(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Specular'
    bl_label = "Add Specular"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Factor"].default_value = 1.0
        self.inputs["Combined"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Use Dot"].default_value = False
        self.inputs["Roughness"].default_value = 0.10000000149011612
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Specular'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Use Dot', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
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

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (-89.34616088867188, -39.845542907714844)
        Group_003.name = "Group.003"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (462.1734924316406, 25.004531860351562)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'ADD'

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (695.7699584960938, 207.0552978515625)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'ADD'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (870.9095458984375, 404.9409484863281)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MIX'

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-672.9998779296875, -131.88177490234375)
        Group.name = "Group"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (-131.51766967773438, -231.34349060058594)
        Group_004.name = "Group.004"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (-480.6791076660156, -290.3297119140625)
        Attribute.name = "Attribute"

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (226.27517700195312, -209.3500518798828)
        Map_Range_001.name = "Map Range.001"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-117.0727767944336, -353.33642578125)
        Math.name = "Math"
        Math.operation = 'SUBTRACT'

        # Create internal links
        nt.links.new(GroupInput.outputs[4], Group_003.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix_002.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_004.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix_004.inputs[7])
        nt.links.new(Mix_005.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_005.inputs[6])
        nt.links.new(Mix_004.outputs[2], Mix_005.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_005.inputs[0])
        nt.links.new(Mix_002.outputs[0], Mix_004.inputs[0])
        nt.links.new(Group_003.outputs[0], Mix_002.inputs[2])
        nt.links.new(GroupInput.outputs[5], Group.inputs[0])
        nt.links.new(Group.outputs[0], Group_003.inputs[1])
        nt.links.new(Attribute.outputs[1], Group_004.inputs[0])
        nt.links.new(Math.outputs[0], Map_Range_001.inputs[1])
        nt.links.new(Group_004.outputs[0], Map_Range_001.inputs[0])
        nt.links.new(Group.outputs[0], Group_004.inputs[1])
        nt.links.new(GroupInput.outputs[4], Math.inputs[1])
        nt.links.new(Map_Range_001.outputs[0], Mix_002.inputs[3])

        # Set default values
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_002.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
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
        Math.inputs[0].default_value = 1.0
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
