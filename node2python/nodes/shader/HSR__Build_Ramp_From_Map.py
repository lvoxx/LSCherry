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


class ShaderNodeHSR__Build_Ramp_From_Map(ShaderNode):
    bl_idname = 'ShaderNodeHSR__Build_Ramp_From_Map'
    bl_label = "HSR: Build Ramp From Map"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Shadow Factor"].default_value = 1.0
        self.inputs["Toon"].default_value = 0.0
        self.inputs["Shadow Mask"].default_value = 0.0
        self.inputs["Ramp Size"].default_value = 0.800000011920929
        self.inputs["Value Enhance"].default_value = 0.10000000149011612

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HSR: Build Ramp From Map'

        # Create output sockets
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Shadow Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Toon', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow Mask', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Ramp Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.800000011920929
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

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-112.73562622070312, -19.041732788085938)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (112.73562622070312, 19.041732788085938)
        Group_009.name = "Group.009"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-346.350830078125, -129.3411865234375)
        Math.name = "Math"
        Math.operation = 'ADD'

        # Create internal links
        nt.links.new(Mix.outputs[2], Group_009.inputs[0])
        nt.links.new(Group_009.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Math.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[1], Math.inputs[0])
        nt.links.new(GroupInput.outputs[4], Math.inputs[1])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_009.inputs[1].default_value = 0.5
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
