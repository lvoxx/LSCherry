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


class ShaderNodeBuild_Face_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeBuild_Face_Ramp'
    bl_label = "Build Face Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Face Value"].default_value = 0.5
        self.inputs["Face Map"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Build Face Ramp'

        # Create output sockets
        nt.interface.new_socket('Custom Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Face Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Face Map', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (229.33355712890625, 59.68492889404297)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (1481.3741455078125, -41.60562515258789)
        Reroute.name = "Reroute"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (175.45269775390625, -70.42658996582031)
        Reroute_006.name = "Reroute.006"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (175.45269775390625, -48.3992919921875)
        Reroute_003.name = "Reroute.003"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (437.1700744628906, -41.60562515258789)
        Reroute_001.name = "Reroute.001"

        # Create internal links
        nt.links.new(Reroute_006.outputs[0], Math.inputs[0])
        nt.links.new(Reroute.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_006.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Math.inputs[1])
        nt.links.new(GroupInput.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Math.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute.inputs[0])

        # Set default values
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
