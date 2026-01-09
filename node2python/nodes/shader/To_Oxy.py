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


class ShaderNodeTo_Oxy(ShaderNode):
    bl_idname = 'ShaderNodeTo_Oxy'
    bl_label = "To Oxy"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Oxyz"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'To Oxy'

        # Create output sockets
        nt.interface.new_socket('Oxy', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Oxyz', in_out='INPUT', socket_type='NodeSocketVector')
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

        Separate_XYZ = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ.location = (-96.49684143066406, -2.9728546142578125)
        Separate_XYZ.name = "Separate XYZ"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (96.49684143066406, 2.9728546142578125)
        Combine_XYZ.name = "Combine XYZ"

        # Create internal links
        nt.links.new(Separate_XYZ.outputs[1], Combine_XYZ.inputs[1])
        nt.links.new(Separate_XYZ.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[0], Separate_XYZ.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Combine_XYZ.inputs[2].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
