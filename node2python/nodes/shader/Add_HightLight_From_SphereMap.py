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


class ShaderNodeAdd_HightLight_From_SphereMap(ShaderNode):
    bl_idname = 'ShaderNodeAdd_HightLight_From_SphereMap'
    bl_label = "Add HightLight From SphereMap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 1.0
        self.inputs["Combined"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["SphereMap"].default_value = 0.0
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add HightLight From SphereMap'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Result', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('SphereMap', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
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

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (0.0, 0.0)
        Mix.name = "Mix"
        Mix.blend_type = 'ADD'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (200.5462646484375, 201.74594116210938)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        # Create internal links
        nt.links.new(GroupInput.outputs[2], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[6])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_001.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[1])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
