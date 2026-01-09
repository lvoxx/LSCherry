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


class ShaderNodeBuild_Ramp_From_Map(ShaderNode):
    bl_idname = 'ShaderNodeBuild_Ramp_From_Map'
    bl_label = "Build Ramp From Map"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Toon"].default_value = 0.0
        self.inputs["Ramp Size"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Build Ramp From Map'

        # Create output sockets
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Toon', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Ramp Size', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-249.54733276367188, 9.415594100952148)
        Combine_XYZ.name = "Combine XYZ"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-463.28900146484375, 70.53758239746094)
        Map_Range.name = "Map Range"

        # Create internal links
        nt.links.new(Combine_XYZ.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[1], Map_Range.inputs[2])

        # Set default values
        Combine_XYZ.inputs[1].default_value = 1.0
        Combine_XYZ.inputs[2].default_value = 0.0
        Map_Range.inputs[1].default_value = -1.0
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
