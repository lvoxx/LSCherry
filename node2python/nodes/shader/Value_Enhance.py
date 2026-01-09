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


class ShaderNodeValue_Enhance(ShaderNode):
    bl_idname = 'ShaderNodeValue_Enhance'
    bl_label = "Value Enhance"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Value Enhance"].default_value = 0.10000000149011612

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Value Enhance'

        # Create output sockets
        nt.interface.new_socket('Enhanced Shading', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Value Enhance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612

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
        Math.location = (-64.39303588867188, -0.6713714599609375)
        Math.name = "Math"
        Math.operation = 'ADD'

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[1], Math.inputs[1])
        nt.links.new(Math.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
