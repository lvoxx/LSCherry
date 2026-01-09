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


class ShaderNodeAdd_Fake_Shadow_Color(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Fake_Shadow_Color'
    bl_label = "Add Fake Shadow Color"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Original Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Factor"].default_value = 0.0
        self.inputs["Shadow Mask"].default_value = 0.0
        self.inputs["Shadow Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Fake Shadow Color'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Original Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow Mask', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow Color', in_out='INPUT', socket_type='NodeSocketColor')
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
        Mix_001.location = (93.79545593261719, 60.5994873046875)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-158.3504638671875, 77.71369934082031)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-169.3253936767578, -214.0353546142578)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (-418.74639892578125, -93.11418151855469)
        Invert_Color.name = "Invert Color"

        # Create internal links
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[3], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[1], Math.inputs[0])
        nt.links.new(Math.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[2], Invert_Color.inputs[1])
        nt.links.new(Invert_Color.outputs[0], Math.inputs[1])
        nt.links.new(Invert_Color.outputs[0], Mix.inputs[0])

        # Set default values
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_Color.inputs[0].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
