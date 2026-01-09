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


class ShaderNodeGI__Seperate_Hair_Lightmap(ShaderNode):
    bl_idname = 'ShaderNodeGI__Seperate_Hair_Lightmap'
    bl_label = "GI: Seperate Hair Lightmap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lightmap"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GI: Seperate Hair Lightmap'

        # Create output sockets
        nt.interface.new_socket('Shadow', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Highlight', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Metal', in_out='OUTPUT', socket_type='NodeSocketFloat')

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

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (292.4388732910156, 37.34421157836914)
        Map_Range.name = "Map Range"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(Group.outputs[2], GroupOutput.inputs[1])
        nt.links.new(Group.outputs[1], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group.outputs[0], GroupOutput.inputs[2])

        # Set default values
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 0.20999999344348907
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
