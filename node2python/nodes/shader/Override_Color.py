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


class ShaderNodeOverride_Color(ShaderNode):
    bl_idname = 'ShaderNodeOverride_Color'
    bl_label = "Override Color"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Condition "].default_value = 0.0
        self.inputs["Color"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["Override Color"].default_value = (0.0, 0.0, 0.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Override Color'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Condition ', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('Override Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)

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
        Mix.location = (292.4040222167969, 121.61607360839844)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-167.44644165039062, 138.94482421875)
        Separate_Color.name = "Separate Color"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (59.84764099121094, 165.4730224609375)
        Math_002.name = "Math.002"
        Math_002.operation = 'GREATER_THAN'

        # Create internal links
        nt.links.new(Math_002.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[7])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Separate_Color.inputs[0])
        nt.links.new(Separate_Color.outputs[2], Math_002.inputs[0])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_002.inputs[1].default_value = 0.0
        Math_002.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
