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


class GeometryNodeCore_LSCherryProvider(GeometryNode):
    bl_idname = 'GeometryNodeCore_LSCherryProvider'
    bl_label = "Core.LSCherryProvider"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Blend Mode"].default_value = 1
        self.inputs["Value Enhance"].default_value = 0.10000000149011612
        self.inputs["World Value Enhance"].default_value = 0.0
        self.inputs["World Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'GeometryNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Core.LSCherryProvider'

        # Create output sockets
        nt.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')

        # Create input sockets
        nt.interface.new_socket('Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
        nt.interface.new_socket('Main Light Dot', in_out='INPUT', socket_type='NodeSocketObject')
        nt.interface.new_socket('Back Light Dot', in_out='INPUT', socket_type='NodeSocketObject')
        nt.interface.new_socket('Main Head', in_out='INPUT', socket_type='NodeSocketObject')
        nt.interface.new_socket('Sub Head-X', in_out='INPUT', socket_type='NodeSocketObject')
        nt.interface.new_socket('Sub Head-Y', in_out='INPUT', socket_type='NodeSocketObject')
        input_socket = nt.interface.new_socket('Blend Mode', in_out='INPUT', socket_type='NodeSocketInt')
        input_socket.default_value = 1
        input_socket = nt.interface.new_socket('Value Enhance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('World Value Enhance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('World Color', in_out='INPUT', socket_type='NodeSocketColor')
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

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (-44.084930419921875, -866.5917358398438)
        Frame_003.label = "Head Pivot Rotation"
        Frame_003.name = "Frame.003"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (-44.084930419921875, -964.4878540039062)
        Frame_004.label = "Pivot - X"
        Frame_004.name = "Frame.004"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-44.084930419921875, -770.003662109375)
        Frame_001.label = "Back Light Rotation"
        Frame_001.name = "Frame.001"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-292.775634765625, -624.1180419921875)
        Frame.label = "Main Light Rotation"
        Frame.name = "Frame"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (-44.084930419921875, -1060.579345703125)
        Frame_005.label = "Pivot- Y"
        Frame_005.name = "Frame.005"

        Object_Info_004 = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info_004.location = (-285.623779296875, 19.949951171875)
        Object_Info_004.label = "headPivot"
        Object_Info_004.name = "Object Info.004"

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (-1.61822509765625, -1000.0729370117188)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'SUBTRACT'

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-1.61822509765625, -948.6768188476562)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'SUBTRACT'

        Object_Info = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info.location = (-35.386810302734375, -19.10809326171875)
        Object_Info.label = "mainLightDir"
        Object_Info.name = "Object Info"

        Object_Info_003 = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info_003.location = (-285.623779296875, 19.949951171875)
        Object_Info_003.label = "headPivot"
        Object_Info_003.name = "Object Info.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-93.96699523925781, -865.6597290039062)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-93.96699523925781, -984.9590454101562)
        Reroute_005.name = "Reroute.005"

        Object_Info_001 = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info_001.location = (-285.623779296875, 26.43206787109375)
        Object_Info_001.label = "backLightDir"
        Object_Info_001.name = "Object Info.001"

        Object_Info_005 = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info_005.location = (-285.623779296875, 18.8675537109375)
        Object_Info_005.label = "headPivot"
        Object_Info_005.name = "Object Info.005"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-246.38876342773438, -1471.0672607421875)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-246.38876342773438, -1513.703125)
        Reroute_003.name = "Reroute.003"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-246.38876342773438, -1448.7413330078125)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-246.38876342773438, -1492.8048095703125)
        Reroute_007.name = "Reroute.007"

        Store_Named_Attribute = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute.location = (226.21620178222656, -707.6113891601562)
        Store_Named_Attribute.name = "Store Named Attribute"

        Store_Named_Attribute_001 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_001.location = (425.84619140625, -707.6113891601562)
        Store_Named_Attribute_001.name = "Store Named Attribute.001"

        Store_Named_Attribute_002 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_002.location = (599.692626953125, -707.6113891601562)
        Store_Named_Attribute_002.name = "Store Named Attribute.002"

        Store_Named_Attribute_003 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_003.location = (785.8021240234375, -707.6113891601562)
        Store_Named_Attribute_003.name = "Store Named Attribute.003"

        Store_Named_Attribute_004 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_004.location = (242.26673889160156, -1132.627685546875)
        Store_Named_Attribute_004.name = "Store Named Attribute.004"

        Store_Named_Attribute_005 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_005.location = (425.84619140625, -1132.627685546875)
        Store_Named_Attribute_005.name = "Store Named Attribute.005"

        Store_Named_Attribute_006 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_006.location = (599.692626953125, -1132.627685546875)
        Store_Named_Attribute_006.name = "Store Named Attribute.006"

        Store_Named_Attribute_007 = nt.nodes.new('GeometryNodeStoreNamedAttribute')
        Store_Named_Attribute_007.location = (785.8021240234375, -1132.627685546875)
        Store_Named_Attribute_007.name = "Store Named Attribute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (334.58453369140625, -1471.0672607421875)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (715.1287841796875, -1513.703125)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (135.50979614257812, -1448.7413330078125)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (522.8252563476562, -1492.8048095703125)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (977.8539428710938, -743.05126953125)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (977.8539428710938, -1106.108154296875)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (218.11917114257812, -1106.108154296875)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (218.11917114257812, -1242.759765625)
        Reroute_015.name = "Reroute.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (1015.7730102539062, -1168.2269287109375)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (1015.7730102539062, -840.5847778320312)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (544.8914794921875, -959.9219970703125)
        Reroute_018.name = "Reroute.018"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (387.369140625, -883.3795166015625)
        Reroute_020.name = "Reroute.020"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (-615.0892333984375, -818.817138671875)
        Reroute_022.name = "Reroute.022"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (-615.0892333984375, -556.5671997070312)
        Reroute_023.name = "Reroute.023"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (192.9830322265625, -556.5671997070312)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (192.9830322265625, -815.695068359375)
        Reroute_025.name = "Reroute.025"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (130.58355712890625, -884.3795776367188)
        Reroute_026.name = "Reroute.026"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (672.06103515625, -1009.3407592773438)
        Reroute_027.name = "Reroute.027"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (130.58355712890625, -660.89013671875)
        Reroute_028.name = "Reroute.028"

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Object_Info.inputs[0])
        nt.links.new(GroupInput.outputs[2], Object_Info_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Object_Info_003.inputs[0])
        nt.links.new(GroupInput.outputs[4], Object_Info_004.inputs[0])
        nt.links.new(GroupInput.outputs[5], Object_Info_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Vector_Math.inputs[1])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Object_Info_004.outputs[1], Vector_Math.inputs[0])
        nt.links.new(Object_Info_003.outputs[1], Reroute_004.inputs[0])
        nt.links.new(Object_Info_005.outputs[1], Vector_Math_001.inputs[1])
        nt.links.new(Reroute_005.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[9], Reroute_003.inputs[0])
        nt.links.new(GroupInput.outputs[7], Reroute_002.inputs[0])
        nt.links.new(GroupInput.outputs[6], Reroute_006.inputs[0])
        nt.links.new(GroupInput.outputs[8], Reroute_007.inputs[0])
        nt.links.new(Store_Named_Attribute.outputs[0], Store_Named_Attribute_001.inputs[0])
        nt.links.new(Store_Named_Attribute_001.outputs[0], Store_Named_Attribute_002.inputs[0])
        nt.links.new(Store_Named_Attribute_002.outputs[0], Store_Named_Attribute_003.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Store_Named_Attribute_002.inputs[3])
        nt.links.new(Reroute_027.outputs[0], Store_Named_Attribute_003.inputs[3])
        nt.links.new(Reroute_020.outputs[0], Store_Named_Attribute_001.inputs[3])
        nt.links.new(Store_Named_Attribute_004.outputs[0], Store_Named_Attribute_005.inputs[0])
        nt.links.new(Store_Named_Attribute_005.outputs[0], Store_Named_Attribute_006.inputs[0])
        nt.links.new(Store_Named_Attribute_006.outputs[0], Store_Named_Attribute_007.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Store_Named_Attribute_004.inputs[3])
        nt.links.new(Reroute_002.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Store_Named_Attribute_005.inputs[3])
        nt.links.new(Reroute_007.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Store_Named_Attribute_006.inputs[3])
        nt.links.new(Reroute_009.outputs[0], Store_Named_Attribute_007.inputs[3])
        nt.links.new(Store_Named_Attribute_003.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Store_Named_Attribute_004.inputs[0])
        nt.links.new(Store_Named_Attribute_007.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Reroute_018.inputs[0])
        nt.links.new(GroupInput.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Store_Named_Attribute.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Store_Named_Attribute.inputs[3])
        nt.links.new(Vector_Math_001.outputs[0], Reroute_027.inputs[0])
        nt.links.new(Object_Info_001.outputs[2], Reroute_020.inputs[0])
        nt.links.new(Object_Info.outputs[2], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Reroute_026.inputs[0])

        # Set default values
        Object_Info_004.inputs[1].default_value = False
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Object_Info.inputs[1].default_value = False
        Object_Info_003.inputs[1].default_value = False
        Object_Info_001.inputs[1].default_value = False
        Object_Info_005.inputs[1].default_value = False
        Store_Named_Attribute.inputs[1].default_value = True
        Store_Named_Attribute.inputs[2].default_value = 'm'
        Store_Named_Attribute_001.inputs[1].default_value = True
        Store_Named_Attribute_001.inputs[2].default_value = 'b'
        Store_Named_Attribute_002.inputs[1].default_value = True
        Store_Named_Attribute_002.inputs[2].default_value = 'fx'
        Store_Named_Attribute_003.inputs[1].default_value = True
        Store_Named_Attribute_003.inputs[2].default_value = 'fy'
        Store_Named_Attribute_004.inputs[1].default_value = True
        Store_Named_Attribute_004.inputs[2].default_value = 'blendM'
        Store_Named_Attribute_005.inputs[1].default_value = True
        Store_Named_Attribute_005.inputs[2].default_value = 'valEnh'
        Store_Named_Attribute_006.inputs[1].default_value = True
        Store_Named_Attribute_006.inputs[2].default_value = 'wValEnh'
        Store_Named_Attribute_007.inputs[1].default_value = True
        Store_Named_Attribute_007.inputs[2].default_value = 'wCol'

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
