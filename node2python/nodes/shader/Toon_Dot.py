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


class ShaderNodeToon_Dot(ShaderNode):
    bl_idname = 'ShaderNodeToon_Dot'
    bl_label = "Toon Dot"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Invert MLight"].default_value = False
        self.inputs["Light Dir"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Mix Light and View"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Toon Dot'

        # Create output sockets
        nt.interface.new_socket('NdotV', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('NdotL', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('VcrsNcrsL', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Mix L and V', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Main Light Vector', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Face To X', in_out='OUTPUT', socket_type='NodeSocketBool')
        nt.interface.new_socket('Face To Y', in_out='OUTPUT', socket_type='NodeSocketBool')

        # Create input sockets
        input_socket = nt.interface.new_socket('Invert MLight', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
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
        Reroute_011.location = (1213.926025390625, 89.26538848876953)
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
        Reroute.location = (297.0549621582031, -163.7908935546875)
        Reroute.name = "Reroute"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (355.698486328125, -438.22857666015625)
        Reroute_004.name = "Reroute.004"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (297.0549621582031, -533.698974609375)
        Reroute_002.name = "Reroute.002"

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (397.5554504394531, -160.74398803710938)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'DOT_PRODUCT'

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (1213.926025390625, 691.8231201171875)
        Reroute_010.name = "Reroute.010"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (478.1412353515625, -442.7287902832031)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (656.6358032226562, 691.8231201171875)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (391.65740966796875, -575.040771484375)
        Reroute_014.name = "Reroute.014"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (1155.611083984375, 26.827266693115234)
        Reroute_012.name = "Reroute.012"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (1155.611083984375, 420.6535339355469)
        Reroute_015.name = "Reroute.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (699.0987548828125, 67.21537780761719)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (434.120361328125, -597.2357788085938)
        Reroute_017.name = "Reroute.017"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-410.48394775390625, -353.64141845703125)
        Combine_XYZ.label = "If your light is Sun, do not make change this"
        Combine_XYZ.name = "Combine XYZ"

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-54.156494140625, -452.8433837890625)
        Geometry.name = "Geometry"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (297.0549621582031, -244.2223663330078)
        Reroute_001.name = "Reroute.001"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (321.83795166015625, -299.7584228515625)
        Reroute_007.name = "Reroute.007"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (1210.61328125, -34.185333251953125)
        Reroute_009.name = "Reroute.009"

        Vector_Math_005 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_005.location = (361.0902404785156, -419.984375)
        Vector_Math_005.name = "Vector Math.005"
        Vector_Math_005.operation = 'CROSS_PRODUCT'

        Vector_Math_006 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_006.location = (562.9507446289062, -319.67523193359375)
        Vector_Math_006.name = "Vector Math.006"
        Vector_Math_006.operation = 'CROSS_PRODUCT'

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (355.698486328125, -400.71527099609375)
        Reroute_005.name = "Reroute.005"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (321.83795166015625, -527.7340087890625)
        Reroute_008.name = "Reroute.008"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (297.0549621582031, -506.0687255859375)
        Reroute_003.name = "Reroute.003"

        Vector_Math_007 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_007.location = (751.1427001953125, -325.10028076171875)
        Vector_Math_007.name = "Vector Math.007"
        Vector_Math_007.operation = 'LENGTH'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (948.2926025390625, -327.5105285644531)
        Invert_Color.name = "Invert Color"

        Vector_Math_008 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_008.location = (384.3673095703125, -361.69512939453125)
        Vector_Math_008.name = "Vector Math.008"
        Vector_Math_008.operation = 'DOT_PRODUCT'

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (147.62876892089844, -429.7706298828125)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Vector_Math_009 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_009.location = (384.3673095703125, -488.478759765625)
        Vector_Math_009.name = "Vector Math.009"
        Vector_Math_009.operation = 'DOT_PRODUCT'

        Combine_XYZ_002 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_002.location = (147.62876892089844, -564.70458984375)
        Combine_XYZ_002.name = "Combine XYZ.002"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (665.54052734375, -371.33685302734375)
        Math.name = "Math"
        Math.operation = 'LESS_THAN'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (665.54052734375, -528.9599609375)
        Math_001.name = "Math.001"
        Math_001.operation = 'LESS_THAN'

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (290.47845458984375, -374.2950744628906)
        Reroute_018.name = "Reroute.018"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (1153.4193115234375, -407.2030029296875)
        Reroute_019.name = "Reroute.019"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (1179.7286376953125, -566.2504272460938)
        Reroute_020.name = "Reroute.020"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (-691.4459228515625, -330.23748779296875)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

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
        nt.links.new(Reroute_013.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute_012.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Vector_Math_002.outputs[1], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Vector_Math_003.outputs[1], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Mix.inputs[2])
        nt.links.new(Mix.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Mix.inputs[3])
        nt.links.new(GroupInput.outputs[1], Vector_Rotate.inputs[4])
        nt.links.new(Reroute_007.outputs[0], Vector_Math_002.inputs[1])
        nt.links.new(Reroute_007.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], GroupOutput.inputs[4])
        nt.links.new(GroupInput.outputs[3], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math_005.outputs[0], Vector_Math_006.inputs[1])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Vector_Math_005.inputs[1])
        nt.links.new(Reroute_001.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Vector_Math_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Vector_Math_006.inputs[0])
        nt.links.new(Vector_Math_006.outputs[0], Vector_Math_007.inputs[0])
        nt.links.new(Invert_Color.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Vector_Math_007.outputs[1], Invert_Color.inputs[1])
        nt.links.new(Combine_XYZ_001.outputs[0], Vector_Math_008.inputs[1])
        nt.links.new(Combine_XYZ_002.outputs[0], Vector_Math_009.inputs[1])
        nt.links.new(Vector_Math_008.outputs[1], Math.inputs[0])
        nt.links.new(Vector_Math_009.outputs[1], Math_001.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Vector_Math_008.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Vector_Math_009.inputs[0])
        nt.links.new(Math.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Math_001.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_019.outputs[0], GroupOutput.inputs[5])
        nt.links.new(Reroute_020.outputs[0], GroupOutput.inputs[6])
        nt.links.new(Mix_001.outputs[0], Combine_XYZ.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])

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
        Vector_Math_005.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs[3].default_value = 1.0
        Vector_Math_006.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs[3].default_value = 1.0
        Vector_Math_007.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs[3].default_value = 1.0
        Invert_Color.inputs[0].default_value = 1.0
        Vector_Math_008.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_008.inputs[3].default_value = 1.0
        Combine_XYZ_001.inputs[0].default_value = 1.0
        Combine_XYZ_001.inputs[1].default_value = 0.0
        Combine_XYZ_001.inputs[2].default_value = 0.0
        Vector_Math_009.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_009.inputs[3].default_value = 1.0
        Combine_XYZ_002.inputs[0].default_value = 0.0
        Combine_XYZ_002.inputs[1].default_value = 1.0
        Combine_XYZ_002.inputs[2].default_value = 0.0
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 0.0
        Math_001.inputs[2].default_value = 0.5
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 1.0
        Mix_001.inputs[3].default_value = -1.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
