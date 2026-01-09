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


class ShaderNodeDefault_Attribute__Alpha(ShaderNode):
    bl_idname = 'ShaderNodeDefault_Attribute__Alpha'
    bl_label = "Default Attribute: Alpha"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Alpha"].default_value = 0.0
        self.inputs["Default"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Default Attribute: Alpha'

        # Create output sockets
        nt.interface.new_socket('Result', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Compare', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Default', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-50.93915939331055, 0.0)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (128.2432098388672, -57.98484802246094)
        Math.name = "Math"
        Math.operation = 'COMPARE'

        # Create internal links
        nt.links.new(Mix.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[3])
        nt.links.new(Mix.outputs[0], Math.inputs[0])
        nt.links.new(Math.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[1], Math.inputs[1])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
