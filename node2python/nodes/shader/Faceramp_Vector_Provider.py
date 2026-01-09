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


class ShaderNodeFaceramp_Vector_Provider(ShaderNode):
    bl_idname = 'ShaderNodeFaceramp_Vector_Provider'
    bl_label = "Faceramp Vector Provider"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Faceramp Vector Provider'

        # Create output sockets
        nt.interface.new_socket('Fx', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Fy', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('X(-1, 0, 0)', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('X(1, 0, 0)', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets

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

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (275.03240966796875, 266.2572326660156)
        Group_004.name = "Group.004"

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (278.46209716796875, 34.254512786865234)
        Group_003.name = "Group.003"

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (275.03240966796875, 231.08343505859375)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'NORMALIZE'

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (278.46209716796875, -3.0510311126708984)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'NORMALIZE'

        Attribute_001 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_001.location = (275.03240966796875, 382.68988037109375)
        Attribute_001.name = "Attribute.001"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (278.46209716796875, 153.4551544189453)
        Attribute.name = "Attribute"

        Combine_XYZ_002 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_002.location = (275.65203857421875, -242.83462524414062)
        Combine_XYZ_002.name = "Combine XYZ.002"

        Combine_XYZ_003 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_003.location = (275.65203857421875, -108.6993408203125)
        Combine_XYZ_003.name = "Combine XYZ.003"

        # Create internal links
        nt.links.new(Attribute_001.outputs[1], Group_004.inputs[0])
        nt.links.new(Group_003.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Attribute.outputs[1], Group_003.inputs[0])
        nt.links.new(Group_004.outputs[0], Vector_Math_002.inputs[0])
        nt.links.new(Vector_Math_002.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Combine_XYZ_002.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Combine_XYZ_003.outputs[0], GroupOutput.inputs[2])

        # Set default values
        Vector_Math_002.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[3].default_value = 1.0
        Vector_Math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Combine_XYZ_002.inputs[0].default_value = 1.0
        Combine_XYZ_002.inputs[1].default_value = 0.0
        Combine_XYZ_002.inputs[2].default_value = 0.0
        Combine_XYZ_003.inputs[0].default_value = -1.0
        Combine_XYZ_003.inputs[1].default_value = 0.0
        Combine_XYZ_003.inputs[2].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
