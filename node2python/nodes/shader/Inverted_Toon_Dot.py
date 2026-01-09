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


class ShaderNodeInverted_Toon_Dot(ShaderNode):
    bl_idname = 'ShaderNodeInverted_Toon_Dot'
    bl_label = "Inverted Toon Dot"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Light Dir"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Mix Light and View"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Inverted Toon Dot'

        # Create output sockets
        nt.interface.new_socket('NdotV', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('NdotInvL', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Mix InvL and V', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Main Inv Light Vector', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Face To X', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Face To Y', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Light Dir', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Mix Light and View', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
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

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-31.3594970703125, 1157.6689453125)
        Frame_001.label = "Diffuse by view"
        Frame_001.name = "Frame.001"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-31.3594970703125, 265.5730895996094)
        Frame.label = "Diffuse by dot()"
        Frame.name = "Frame"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (264.9783935546875, 898.517578125)
        Frame_002.label = "NdotV mix NdotL"
        Frame_002.name = "Frame.002"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (1023.7857055664062, 90.56810760498047)
        Reroute_011.name = "Reroute.011"

        Vector_Math_004 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_004.location = (126.94804382324219, -402.45391845703125)
        Vector_Math_004.name = "Vector Math.004"
        Vector_Math_004.operation = 'NORMALIZE'

        Vector_Rotate = nt.nodes.new('ShaderNodeVectorRotate')
        Vector_Rotate.location = (-95.94075012207031, -324.20428466796875)
        Vector_Rotate.name = "Vector Rotate"

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (126.94804382324219, -128.33355712890625)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'NORMALIZE'

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (126.94804382324219, -265.80462646484375)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'NORMALIZE'

        Vector_Math_003 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_003.location = (430.491455078125, -430.894775390625)
        Vector_Math_003.name = "Vector Math.003"
        Vector_Math_003.operation = 'DOT_PRODUCT'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (320.49688720703125, -163.7908935546875)
        Reroute.name = "Reroute"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (321.83795166015625, -438.22857666015625)
        Reroute_004.name = "Reroute.004"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (320.49688720703125, -533.698974609375)
        Reroute_002.name = "Reroute.002"

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (361.0902404785156, -160.74398803710938)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'DOT_PRODUCT'

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (1023.7857055664062, 691.8231201171875)
        Reroute_010.name = "Reroute.010"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (478.1412353515625, -442.7287902832031)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (700.9149169921875, 691.8231201171875)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (435.9365234375, -575.040771484375)
        Reroute_014.name = "Reroute.014"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (965.470703125, 46.36805725097656)
        Reroute_012.name = "Reroute.012"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (965.470703125, 420.6535339355469)
        Reroute_015.name = "Reroute.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (699.0987548828125, 67.21537780761719)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (434.120361328125, -597.2357788085938)
        Reroute_017.name = "Reroute.017"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (1020.4728393554688, -34.185333251953125)
        Reroute_009.name = "Reroute.009"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-410.48394775390625, -353.64141845703125)
        Combine_XYZ.label = "If your light is Sun, do not make change this"
        Combine_XYZ.name = "Combine XYZ"

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-54.156494140625, -452.8433837890625)
        Geometry.name = "Geometry"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (320.49688720703125, -244.2223663330078)
        Reroute_001.name = "Reroute.001"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (321.83795166015625, -299.7584228515625)
        Reroute_007.name = "Reroute.007"

        Vector_Math_005 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_005.location = (361.0902404785156, -352.47833251953125)
        Vector_Math_005.name = "Vector Math.005"
        Vector_Math_005.operation = 'DOT_PRODUCT'

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (124.3516845703125, -420.5538024902344)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Vector_Math_006 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_006.location = (361.0902404785156, -479.261962890625)
        Vector_Math_006.name = "Vector Math.006"
        Vector_Math_006.operation = 'DOT_PRODUCT'

        Combine_XYZ_002 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_002.location = (124.3516845703125, -555.48779296875)
        Combine_XYZ_002.name = "Combine XYZ.002"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (610.9039916992188, -96.54696655273438)
        Math.name = "Math"
        Math.operation = 'LESS_THAN'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (610.9039916992188, -254.17007446289062)
        Math_001.name = "Math.001"
        Math_001.operation = 'LESS_THAN'

        # Create internal links
        nt.links.new(Vector_Rotate.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Vector_Rotate.inputs[0])
        nt.links.new(Geometry.outputs[4], Vector_Math_004.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Vector_Math_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Vector_Math_003.inputs[1])
        nt.links.new(Vector_Math_004.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Vector_Math_003.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_009.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Reroute_013.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute_012.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Vector_Math_002.outputs[1], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Vector_Math_002.inputs[1])
        nt.links.new(Vector_Math_003.outputs[1], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Mix.inputs[2])
        nt.links.new(Mix.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Mix.inputs[3])
        nt.links.new(GroupInput.outputs[0], Vector_Rotate.inputs[4])
        nt.links.new(GroupInput.outputs[2], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Vector_Math_005.inputs[0])
        nt.links.new(Combine_XYZ_001.outputs[0], Vector_Math_005.inputs[1])
        nt.links.new(Vector_Math.outputs[0], Vector_Math_006.inputs[0])
        nt.links.new(Combine_XYZ_002.outputs[0], Vector_Math_006.inputs[1])
        nt.links.new(Vector_Math_005.outputs[1], Math.inputs[0])
        nt.links.new(Vector_Math_006.outputs[1], Math_001.inputs[0])
        nt.links.new(Math.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Math_001.outputs[0], GroupOutput.inputs[5])

        # Set default values
        Vector_Math_004.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[3].default_value = 1.0
        Vector_Rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate.inputs[2].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate.inputs[3].default_value = 0.0
        Vector_Math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Vector_Math_003.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs[3].default_value = 1.0
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[3].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Combine_XYZ.inputs[0].default_value = 0.0
        Combine_XYZ.inputs[1].default_value = 0.0
        Combine_XYZ.inputs[2].default_value = -1.0
        Vector_Math_005.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs[3].default_value = 1.0
        Combine_XYZ_001.inputs[0].default_value = 1.0
        Combine_XYZ_001.inputs[1].default_value = 0.0
        Combine_XYZ_001.inputs[2].default_value = 0.0
        Vector_Math_006.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs[3].default_value = 1.0
        Combine_XYZ_002.inputs[0].default_value = 0.0
        Combine_XYZ_002.inputs[1].default_value = 1.0
        Combine_XYZ_002.inputs[2].default_value = 0.0
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 0.0
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
