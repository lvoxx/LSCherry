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


class ShaderNodeHI3__Add_Shadow_From_Lightmap(ShaderNode):
    bl_idname = 'ShaderNodeHI3__Add_Shadow_From_Lightmap'
    bl_label = "HI3: Add Shadow From Lightmap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Original Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Factor"].default_value = 0.0
        self.inputs["Shadow"].default_value = 0.0
        self.inputs["Shadow Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HI3: Add Shadow From Lightmap'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Original Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (0.0, 0.0)
        Group.name = "Group"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(GroupInput.outputs[2], Group.inputs[2])
        nt.links.new(GroupInput.outputs[3], Group.inputs[3])
        nt.links.new(Group.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[1])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
