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


class ShaderNodeSpecular_Dot(ShaderNode):
    bl_idname = 'ShaderNodeSpecular_Dot'
    bl_label = "Specular Dot"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Light Dir"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Specular Dot'

        # Create output sockets
        nt.interface.new_socket('Specular', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Light Dir', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
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

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-774.6715698242188, -102.4208984375)
        Geometry.name = "Geometry"

        Vector_Math_004 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_004.location = (-594.3843994140625, -64.6788330078125)
        Vector_Math_004.name = "Vector Math.004"
        Vector_Math_004.operation = 'NORMALIZE'

        Vector_Math_005 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_005.location = (-362.0174560546875, 51.208518981933594)
        Vector_Math_005.name = "Vector Math.005"
        Vector_Math_005.operation = 'DOT_PRODUCT'

        Vector_Rotate = nt.nodes.new('ShaderNodeVectorRotate')
        Vector_Rotate.location = (-955.6923828125, 116.63909149169922)
        Vector_Rotate.name = "Vector Rotate"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-1316.3924560546875, 135.5072784423828)
        Combine_XYZ.label = "If your light is Sun, do not make change this"
        Combine_XYZ.name = "Combine XYZ"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (401.16302490234375, 34.977012634277344)
        Math.name = "Math"
        Math.operation = 'POWER'

        Vector_Math_006 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_006.location = (-568.5167236328125, 57.11375427246094)
        Vector_Math_006.name = "Vector Math.006"
        Vector_Math_006.operation = 'NORMALIZE'

        Vector_Math_010 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_010.location = (-761.449462890625, 77.2073974609375)
        Vector_Math_010.name = "Vector Math.010"
        Vector_Math_010.operation = 'REFLECT'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-1.6712188720703125, 237.70672607421875)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Vector_Math_012 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_012.location = (-465.1744384765625, 312.0865783691406)
        Vector_Math_012.name = "Vector Math.012"
        Vector_Math_012.operation = 'DOT_PRODUCT'

        Vector_Math_007 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_007.location = (-285.43194580078125, 276.3628234863281)
        Vector_Math_007.name = "Vector Math.007"
        Vector_Math_007.operation = 'NORMALIZE'

        Vector_Rotate_001 = nt.nodes.new('ShaderNodeVectorRotate')
        Vector_Rotate_001.location = (-843.6282958984375, 465.81817626953125)
        Vector_Rotate_001.name = "Vector Rotate.001"

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (-1204.328369140625, 484.68634033203125)
        Combine_XYZ_001.label = "If your light is Sun, do not make change this"
        Combine_XYZ_001.name = "Combine XYZ.001"

        # Create internal links
        nt.links.new(Geometry.outputs[4], Vector_Math_004.inputs[0])
        nt.links.new(Vector_Math_006.outputs[0], Vector_Math_005.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Vector_Rotate.inputs[0])
        nt.links.new(GroupInput.outputs[0], Vector_Rotate.inputs[4])
        nt.links.new(Math.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Vector_Math_010.inputs[1])
        nt.links.new(Vector_Math_007.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[4])
        nt.links.new(Vector_Math_004.outputs[0], Mix.inputs[5])
        nt.links.new(Vector_Math_012.outputs[1], Vector_Math_007.inputs[0])
        nt.links.new(Vector_Math_004.outputs[0], Vector_Math_005.inputs[1])
        nt.links.new(Vector_Math_012.outputs[1], Mix.inputs[2])
        nt.links.new(Mix.outputs[0], Math.inputs[0])
        nt.links.new(Vector_Math_005.outputs[1], Mix.inputs[3])
        nt.links.new(Vector_Rotate.outputs[0], Vector_Math_010.inputs[0])
        nt.links.new(Combine_XYZ_001.outputs[0], Vector_Rotate_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Vector_Rotate_001.inputs[4])
        nt.links.new(Vector_Rotate_001.outputs[0], Vector_Math_012.inputs[0])
        nt.links.new(GroupInput.outputs[1], Vector_Math_012.inputs[1])
        nt.links.new(Vector_Math_010.outputs[0], Vector_Math_006.inputs[0])

        # Set default values
        Vector_Math_004.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[3].default_value = 1.0
        Vector_Math_005.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs[3].default_value = 1.0
        Vector_Rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate.inputs[2].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate.inputs[3].default_value = 0.0
        Combine_XYZ.inputs[0].default_value = 0.0
        Combine_XYZ.inputs[1].default_value = 0.0
        Combine_XYZ.inputs[2].default_value = -1.0
        Math.inputs[1].default_value = 0.5
        Math.inputs[2].default_value = 0.5
        Vector_Math_006.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs[3].default_value = 1.0
        Vector_Math_010.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_010.inputs[3].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Vector_Math_012.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_012.inputs[3].default_value = 1.0
        Vector_Math_007.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs[3].default_value = 1.0
        Vector_Rotate_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate_001.inputs[2].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate_001.inputs[3].default_value = 0.0
        Combine_XYZ_001.inputs[0].default_value = 0.0
        Combine_XYZ_001.inputs[1].default_value = 0.0
        Combine_XYZ_001.inputs[2].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
