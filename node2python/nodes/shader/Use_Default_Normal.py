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


class ShaderNodeUse_Default_Normal(ShaderNode):
    bl_idname = 'ShaderNodeUse_Default_Normal'
    bl_label = "Use Default Normal"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Use Default Normal'

        # Create output sockets
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)

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

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-144.440185546875, 16.198043823242188)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'DISTANCE'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (36.21836853027344, -17.059417724609375)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (35.09747314453125, -55.27488708496094)
        Geometry.name = "Geometry"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (200.5790557861328, 32.153717041015625)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        # Create internal links
        nt.links.new(Vector_Math.outputs[1], Math.inputs[0])
        nt.links.new(Geometry.outputs[1], Mix.inputs[4])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[0], Vector_Math.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[5])
        nt.links.new(Mix.outputs[1], GroupOutput.inputs[0])

        # Set default values
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Math.inputs[1].default_value = 0.5
        Math.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
