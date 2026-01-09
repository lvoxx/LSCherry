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


class ShaderNodeStack_Next_Toon(ShaderNode):
    bl_idname = 'ShaderNodeStack_Next_Toon'
    bl_label = "Stack Next Toon"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Shading"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Color"].default_value = (1.0, 0.0, 0.002265453338623047, 1.0)
        self.inputs["Stack"].default_value = (0.0, 1.0, 0.018648559227585793, 1.0)
        self.inputs["Size"].default_value = 1.0
        self.inputs["Smooth"].default_value = 0.05000000074505806

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Stack Next Toon'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Stack', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.0, 0.002265453338623047, 1.0)
        input_socket = nt.interface.new_socket('Stack', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 1.0, 0.018648559227585793, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806

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

        Group_015 = nt.nodes.new('ShaderNodeGroup')
        Group_015.location = (-86.64947509765625, 69.92706298828125)
        Group_015.name = "Group.015"

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (753.0, -66.18302917480469)
        Mix_004.label = "Add Base Color"
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MIX'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (274.8832092285156, 47.685333251953125)
        Mix_005.label = "Add Shadow Color"
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MULTIPLY'

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group_015.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_005.inputs[7])
        nt.links.new(Mix_005.outputs[2], Mix_004.inputs[7])
        nt.links.new(Group_015.outputs[0], Mix_004.inputs[0])
        nt.links.new(Group_015.outputs[0], Mix_005.inputs[6])
        nt.links.new(GroupInput.outputs[3], Group_015.inputs[4])
        nt.links.new(GroupInput.outputs[4], Group_015.inputs[5])
        nt.links.new(GroupInput.outputs[2], Mix_004.inputs[6])
        nt.links.new(GroupInput.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Mix_004.outputs[2], GroupOutput.inputs[1])

        # Set default values
        Group_015.inputs[0].default_value = False
        Group_015.inputs[2].default_value = 0.0
        Group_015.inputs[3].default_value = Vector((0.0, 0.0, 0.0))
        Group_015.inputs[6].default_value = 0.0
        Group_015.inputs[7].default_value = 0.0
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[0].default_value = 1.0
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
