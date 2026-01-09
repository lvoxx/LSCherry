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


class ShaderNodeAdd_Fake_Bright_Color(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Fake_Bright_Color'
    bl_label = "Add Fake Bright Color"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Original Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Factor"].default_value = 0.0
        self.inputs["Bright Mask"].default_value = 0.0
        self.inputs["Bright Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Fake Bright Color'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Original Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Bright Mask', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Bright Color', in_out='INPUT', socket_type='NodeSocketColor')
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

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (105.35580444335938, 125.22613525390625)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-105.35580444335938, -125.22610473632812)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        # Create internal links
        nt.links.new(GroupInput.outputs[2], Mix.inputs[0])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])

        # Set default values
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
