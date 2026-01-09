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


class ShaderNodeNumber_Compress(ShaderNode):
    bl_idname = 'ShaderNodeNumber_Compress'
    bl_label = "Number Compress"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Sequence 1"].default_value = 0.5
        self.inputs["Sequence 2"].default_value = 1000.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Number Compress'

        # Create output sockets
        nt.interface.new_socket('Compressed', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        nt.interface.new_socket('MAX 2 SEQUENCES', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Sequence 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Sequence 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1000.0

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

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (287.2575988769531, -10.637981414794922)
        Frame_003.label = "IDDD,IDDD"
        Frame_003.name = "Frame.003"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (70.97384643554688, 62.3270263671875)
        Frame_001.label = "IDDD,0000"
        Frame_001.name = "Frame.001"

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (8.62823486328125, -99.06138610839844)
        Math_004.name = "Math.004"
        Math_004.operation = 'ADD'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-39.44537353515625, 7.616203308105469)
        Math_002.name = "Math.002"
        Math_002.operation = 'MULTIPLY'

        # Create internal links
        nt.links.new(Math_002.outputs[0], Math_004.inputs[0])
        nt.links.new(Math_004.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Math_002.inputs[0])
        nt.links.new(GroupInput.outputs[2], Math_004.inputs[1])

        # Set default values
        Math_004.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 10000.0
        Math_002.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
