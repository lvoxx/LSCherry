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


class ShaderNodeBuild_Nose_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeBuild_Nose_Ramp'
    bl_label = "Build Nose Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Face Ramp (Required)"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Face Value"].default_value = 0.5
        self.inputs["Face Map"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Build Nose Ramp'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Face Ramp (Required)', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
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

        Group_005 = nt.nodes.new('ShaderNodeGroup')
        Group_005.location = (0.0, 0.0)
        Group_005.name = "Group.005"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (390.765869140625, 294.1714782714844)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (211.45297241210938, 47.657386779785156)
        Invert_Color.name = "Invert Color"

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Group_005.inputs[0])
        nt.links.new(GroupInput.outputs[2], Group_005.inputs[1])
        nt.links.new(Invert_Color.outputs[0], Mix.inputs[7])
        nt.links.new(Group_005.outputs[0], Invert_Color.inputs[1])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_Color.inputs[0].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
