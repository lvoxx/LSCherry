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


class ShaderNodeNAND(ShaderNode):
    bl_idname = 'ShaderNodeNAND'
    bl_label = "NAND"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["A"].default_value = 0.0
        self.inputs["B"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'NAND'

        # Create output sockets
        nt.interface.new_socket('O', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('A', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('B', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0

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

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-380.0, 60.0)
        Math_002.name = "Math.002"
        Math_002.operation = 'CEIL'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-380.0, -80.0)
        Math_003.name = "Math.003"
        Math_003.operation = 'CEIL'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-200.0, 60.0)
        Math_004.name = "Math.004"
        Math_004.operation = 'ADD'

        Math_006 = nt.nodes.new('ShaderNodeMath')
        Math_006.location = (-20.0, 60.0)
        Math_006.name = "Math.006"
        Math_006.operation = 'LESS_THAN'

        # Create internal links
        nt.links.new(Math_002.outputs[0], Math_004.inputs[0])
        nt.links.new(Math_003.outputs[0], Math_004.inputs[1])
        nt.links.new(GroupInput.outputs[0], Math_002.inputs[0])
        nt.links.new(GroupInput.outputs[1], Math_003.inputs[0])
        nt.links.new(Math_004.outputs[0], Math_006.inputs[0])
        nt.links.new(Math_006.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Math_002.inputs[1].default_value = 7.0
        Math_002.inputs[2].default_value = 0.5
        Math_003.inputs[1].default_value = 7.0
        Math_003.inputs[2].default_value = 0.5
        Math_004.inputs[2].default_value = 0.5
        Math_006.inputs[1].default_value = 2.0
        Math_006.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
