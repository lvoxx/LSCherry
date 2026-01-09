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


class ShaderNodeXTR__Parallax_UV(ShaderNode):
    bl_idname = 'ShaderNodeXTR__Parallax_UV'
    bl_label = "XTR: Parallax UV"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["UV Map"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Tangent UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Distance"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'XTR: Parallax UV'

        # Create output sockets
        nt.interface.new_socket('Parallax UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('UV Map', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Tangent UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Distance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0

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

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-649.3381958007812, 73.59461975097656)
        Geometry.name = "Geometry"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-369.15557861328125, -109.80319213867188)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'CROSS_PRODUCT'

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (-128.464111328125, -38.04986572265625)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'DOT_PRODUCT'

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (-128.464111328125, -75.01606750488281)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'DOT_PRODUCT'

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (62.574005126953125, -29.362245559692383)
        Combine_XYZ.name = "Combine XYZ"

        Vector_Math_003 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_003.location = (238.40826416015625, 1.087677001953125)
        Vector_Math_003.name = "Vector Math.003"
        Vector_Math_003.operation = 'TANGENT'

        Vector_Math_004 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_004.location = (429.43560791015625, -19.763751983642578)
        Vector_Math_004.name = "Vector Math.004"
        Vector_Math_004.operation = 'SCALE'

        Vector_Math_005 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_005.location = (635.0256958007812, 58.97786331176758)
        Vector_Math_005.name = "Vector Math.005"
        Vector_Math_005.operation = 'SUBTRACT'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (302.40301513671875, 68.76893615722656)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-681.0000610351562, -198.0869903564453)
        Reroute_001.name = "Reroute.001"

        # Create internal links
        nt.links.new(Geometry.outputs[4], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math_002.outputs[1], Combine_XYZ.inputs[1])
        nt.links.new(Vector_Math_001.outputs[1], Combine_XYZ.inputs[0])
        nt.links.new(Geometry.outputs[1], Vector_Math.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Vector_Math_002.inputs[1])
        nt.links.new(Vector_Math_004.outputs[0], Vector_Math_005.inputs[1])
        nt.links.new(Vector_Math_003.outputs[0], Vector_Math_004.inputs[0])
        nt.links.new(Geometry.outputs[4], Vector_Math_002.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Vector_Math_003.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Vector_Math_001.inputs[1])
        nt.links.new(Reroute.outputs[0], Vector_Math_005.inputs[0])
        nt.links.new(GroupInput.outputs[2], Vector_Math_004.inputs[3])
        nt.links.new(Vector_Math_005.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Vector_Math.inputs[1])
        nt.links.new(GroupInput.outputs[1], Reroute_001.inputs[0])

        # Set default values
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[3].default_value = 1.0
        Combine_XYZ.inputs[2].default_value = 0.0
        Vector_Math_003.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs[3].default_value = 1.0
        Vector_Math_004.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs[3].default_value = 1.159999966621399

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
