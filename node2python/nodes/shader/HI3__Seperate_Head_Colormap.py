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


class ShaderNodeHI3__Seperate_Head_Colormap(ShaderNode):
    bl_idname = 'ShaderNodeHI3__Seperate_Head_Colormap'
    bl_label = "HI3: Seperate Head Colormap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lightmap"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HI3: Seperate Head Colormap'

        # Create output sockets
        nt.interface.new_socket('Blush', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Mood Down', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Lightmap', in_out='INPUT', socket_type='NodeSocketColor')
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

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (0.0, 0.0)
        Group.name = "Group"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(Group.outputs[1], GroupOutput.inputs[1])
        nt.links.new(Group.outputs[0], GroupOutput.inputs[0])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
