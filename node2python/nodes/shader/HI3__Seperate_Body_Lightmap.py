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


class ShaderNodeHI3__Seperate_Body_Lightmap(ShaderNode):
    bl_idname = 'ShaderNodeHI3__Seperate_Body_Lightmap'
    bl_label = "HI3: Seperate Body Lightmap"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Lightmap"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'HI3: Seperate Body Lightmap'

        # Create output sockets
        nt.interface.new_socket('Metal', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Shadow', in_out='OUTPUT', socket_type='NodeSocketFloat')

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

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (192.9788360595703, -231.83816528320312)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (403.8800964355469, -228.09619140625)
        Math_002.name = "Math.002"
        Math_002.operation = 'GREATER_THAN'

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group.inputs[0])
        nt.links.new(Group.outputs[1], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Math_002.inputs[0])
        nt.links.new(Math_002.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Group.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Math_001.inputs[1].default_value = 10.0
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 0.019999999552965164
        Math_002.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
