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


class ShaderNodeFROM_A_TO_B(ShaderNode):
    bl_idname = 'ShaderNodeFROM_A_TO_B'
    bl_label = "FROM A TO B"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["A"].default_value = 0.5
        self.inputs["B"].default_value = 0.5
        self.inputs["Input"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'FROM A TO B'

        # Create output sockets
        nt.interface.new_socket('Boolean', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('A', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('B', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Input', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5

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

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-448.70111083984375, 317.9954833984375)
        Frame.name = "Frame"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-332.9420166015625, 71.32112121582031)
        Reroute_001.name = "Reroute.001"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-332.9420166015625, -24.881412506103516)
        Reroute.name = "Reroute"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-332.9420166015625, -100.09429931640625)
        Reroute_002.name = "Reroute.002"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-212.33914184570312, 6.1656036376953125)
        Math_001.label = "Value <= B"
        Math_001.name = "Math.001"
        Math_001.operation = 'LESS_THAN'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-213.4344482421875, 186.92666625976562)
        Math.label = "A <= Value"
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (-5.354795455932617, 85.49458312988281)
        Group_001.name = "Group.001"

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Math_001.inputs[1])
        nt.links.new(GroupInput.outputs[0], Math.inputs[1])
        nt.links.new(GroupInput.outputs[2], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Math.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Group_001.inputs[1])
        nt.links.new(Math.outputs[0], Group_001.inputs[0])
        nt.links.new(Group_001.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Math_001.inputs[2].default_value = 0.5
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
