import bpy
import sys
from pathlib import Path

# Import utils (handle both relative and absolute imports)
try:
    from ..utils import GeometryNode
except ImportError:
    # Fallback for direct execution
    import importlib.util
    utils_path = Path(__file__).parent.parent / 'utils.py'
    spec = importlib.util.spec_from_file_location('utils', utils_path)
    utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utils)
    GeometryNode = utils.GeometryNode


class GeometryNodeCore_PrincipleProvider(GeometryNode):
    bl_idname = 'GeometryNodeCore_PrincipleProvider'
    bl_label = "Core.PrincipleProvider"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Size"].default_value = 1.0
        self.inputs["Smooth"].default_value = 0.10000000149011612

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'GeometryNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Core.PrincipleProvider'

        # Create output sockets
        nt.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')

        # Create input sockets
        nt.interface.new_socket('Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612

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

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-189.80538940429688, 342.42706298828125)
        Frame.label = "Author: 夜雀的3D小店 (bilibili)"
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-189.80538940429688, 277.9440002441406)
        Frame_001.label = "Maintainer: Lvoxx"
        Frame_001.name = "Frame.001"

        Named_Attribute = nt.nodes.new('GeometryNodeInputNamedAttribute')
        Named_Attribute.location = (-965.681640625, -203.23504638671875)
        Named_Attribute.name = "Named Attribute"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-383.7811584472656, -145.04098510742188)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'DOT_PRODUCT'

        Normal = nt.nodes.new('GeometryNodeInputNormal')
        Normal.location = (-744.147216796875, -263.9705505371094)
        Normal.name = "Normal"

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (515.5654296875, -5.884620666503906)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'NORMALIZE'

        Store_Named_Attribute = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute.location = (811.883056640625, 144.68338012695312)
        Store_Named_Attribute.name = "Store Named Attribute"

        Vector_Rotate = nt.nodes.new('ShaderNodeVectorRotate')
        Vector_Rotate.location = (-746.88134765625, -21.312271118164062)
        Vector_Rotate.name = "Vector Rotate"

        Vector = nt.nodes.new('FunctionNodeInputVector')
        Vector.location = (-960.361328125, -74.47088623046875)
        Vector.name = "Vector"

        Vector_Math_004 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_004.location = (335.9999694824219, -12.707561492919922)
        Vector_Math_004.name = "Vector Math.004"
        Vector_Math_004.operation = 'ADD'

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (129.651123046875, -121.24305725097656)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'SCALE'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-116.25619506835938, -223.967529296875)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-535.3798217773438, -57.42656707763672)
        Reroute.name = "Reroute"

        # Create internal links
        nt.links.new(Normal.outputs[0], Vector_Math.inputs[1])
        nt.links.new(Vector_Math_002.outputs[0], Store_Named_Attribute.inputs[3])
        nt.links.new(Store_Named_Attribute.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Store_Named_Attribute.inputs[0])
        nt.links.new(Vector.outputs[0], Vector_Rotate.inputs[0])
        nt.links.new(Named_Attribute.outputs[0], Vector_Rotate.inputs[4])
        nt.links.new(Vector_Math_001.outputs[0], Vector_Math_004.inputs[1])
        nt.links.new(Vector_Math.outputs[1], Math.inputs[0])
        nt.links.new(Math.outputs[0], Vector_Math_001.inputs[3])
        nt.links.new(Reroute.outputs[0], Vector_Math_004.inputs[0])
        nt.links.new(Vector_Math_004.outputs[0], Vector_Math_002.inputs[0])
        nt.links.new(Vector_Rotate.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Reroute.outputs[0], Vector_Math.inputs[0])

        # Set default values
        Named_Attribute.inputs[0].default_value = 'm'
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Vector_Math_002.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[3].default_value = 1.0
        Store_Named_Attribute.inputs[1].default_value = True
        Store_Named_Attribute.inputs[2].default_value = 'tn'
        Vector_Rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate.inputs[2].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate.inputs[3].default_value = 0.0
        Vector_Math_004.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[3].default_value = 1.0
        Vector_Math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Math.inputs[1].default_value = 5.0
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
