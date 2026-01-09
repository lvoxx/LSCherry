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


class ShaderNodeNumber_Extract(ShaderNode):
    bl_idname = 'ShaderNodeNumber_Extract'
    bl_label = "Number Extract"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Compressed"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Number Extract'

        # Create output sockets
        nt.interface.new_socket('Compressed', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Extracted', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Compressed', in_out='INPUT', socket_type='NodeSocketFloat')
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
        Math.location = (-191.08358764648438, 110.0589599609375)
        Math.name = "Math"
        Math.operation = 'DIVIDE'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (14.976840019226074, 42.01896667480469)
        Math_004.name = "Math.004"
        Math_004.operation = 'TRUNC'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (198.36959838867188, 19.103342056274414)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (620.7932739257812, -160.2606964111328)
        Math_003.name = "Math.003"
        Math_003.operation = 'DIVIDE'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (399.6169738769531, -91.07628631591797)
        Math_002.name = "Math.002"
        Math_002.operation = 'SUBTRACT'

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Math.inputs[0])
        nt.links.new(Math.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Math_004.outputs[0], Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math_002.inputs[0])
        nt.links.new(Math_003.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Math_001.outputs[0], Math_002.inputs[1])
        nt.links.new(Math.outputs[0], Math_004.inputs[0])
        nt.links.new(Math_002.outputs[0], Math_003.inputs[0])

        # Set default values
        Math.inputs[1].default_value = 10000.0
        Math.inputs[2].default_value = 0.5
        Math_004.inputs[1].default_value = 0.5
        Math_004.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 10000.0
        Math_001.inputs[2].default_value = 0.5
        Math_003.inputs[1].default_value = 1000.0
        Math_003.inputs[2].default_value = 0.5
        Math_002.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
