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


class ShaderNodeGI__Build_Head_Package(ShaderNode):
    bl_idname = 'ShaderNodeGI__Build_Head_Package'
    bl_label = "GI: Build Head Package"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Head Base Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Head Lightmap Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Head Colormap Texture"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Fake Shadow Factor"].default_value = 0.0
        self.inputs["Fake Shadow Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Blush Factor"].default_value = 0.0
        self.inputs["Bright Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Mood Down Factor"].default_value = 0.0
        self.inputs["Mood Down Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GI: Build Head Package'

        # Create output sockets
        nt.interface.new_socket('Base Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Head Base Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Head Lightmap Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Head Colormap Texture', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Fake Shadow Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Fake Shadow Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Blush Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Bright Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Mood Down Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Mood Down Color', in_out='INPUT', socket_type='NodeSocketColor')
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

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (390.28594970703125, -108.94723510742188)
        Group_014.name = "Group.014"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (99.45367431640625, 10.870697021484375)
        Group_013.name = "Group.013"

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (-111.14820098876953, 159.07786560058594)
        Group_011.name = "Group.011"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-377.0361328125, 55.30039596557617)
        Group.name = "Group"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (-290.36572265625, -248.8246307373047)
        Group_012.name = "Group.012"

        # Create internal links
        nt.links.new(Group_013.outputs[0], Group_014.inputs[0])
        nt.links.new(Group_012.outputs[1], Group_014.inputs[2])
        nt.links.new(Group_011.outputs[0], Group_013.inputs[0])
        nt.links.new(Group_012.outputs[0], Group_013.inputs[2])
        nt.links.new(GroupInput.outputs[0], Group_011.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[0])
        nt.links.new(Group.outputs[0], Group_011.inputs[2])
        nt.links.new(GroupInput.outputs[2], Group_012.inputs[0])
        nt.links.new(GroupInput.outputs[3], Group_011.inputs[1])
        nt.links.new(GroupInput.outputs[4], Group_011.inputs[3])
        nt.links.new(GroupInput.outputs[5], Group_013.inputs[1])
        nt.links.new(GroupInput.outputs[6], Group_013.inputs[3])
        nt.links.new(Group_014.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[7], Group_014.inputs[1])
        nt.links.new(GroupInput.outputs[8], Group_014.inputs[3])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
