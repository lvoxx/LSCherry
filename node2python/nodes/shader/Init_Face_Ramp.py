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


class ShaderNodeInit_Face_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeInit_Face_Ramp'
    bl_label = "Init Face Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Min Dot Value"].default_value = -0.5
        self.inputs["Max  Dot Value"].default_value = 0.5
        self.inputs["Default UV"].default_value = -1.0
        self.inputs["Flip UV"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Init Face Ramp'

        # Create output sockets
        nt.interface.new_socket('Face Value', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Face Vector', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Is X Side', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        nt.interface.new_socket('Deprecated', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Min Dot Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = -0.5
        input_socket = nt.interface.new_socket('Max  Dot Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Default UV', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = -1.0
        input_socket = nt.interface.new_socket('Flip UV', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (97.22677612304688, -255.40377807617188)
        Frame_002.label = "Flip FaceMap If Opposite Site"
        Frame_002.name = "Frame.002"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (261.4367980957031, 511.54351806640625)
        Frame_001.label = "Map Value Limit"
        Frame_001.name = "Frame.001"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-618.3001098632812, 88.67147827148438)
        Frame.label = "Face Pivot"
        Frame.name = "Frame"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-436.7603759765625, 303.8605041503906)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'NORMALIZE'

        Vector_Math_004 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_004.location = (-33.008544921875, -7.8170166015625)
        Vector_Math_004.name = "Vector Math.004"
        Vector_Math_004.operation = 'DOT_PRODUCT'

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (423.24176025390625, -185.3865966796875)
        Reroute_008.name = "Reroute.008"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (844.465087890625, 347.05712890625)
        Reroute_010.name = "Reroute.010"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (977.9639282226562, 54.206703186035156)
        Mapping.name = "Mapping"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-169.753173828125, 268.5618591308594)
        Reroute.name = "Reroute"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (485.61187744140625, -44.27337646484375)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (813.0778198242188, -336.0631408691406)
        Reroute_011.name = "Reroute.011"

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (-614.2136840820312, 303.8605041503906)
        Group_002.name = "Group.002"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-129.55636596679688, -28.63583755493164)
        Reroute_002.name = "Reroute.002"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-169.753173828125, -352.84197998046875)
        Reroute_006.name = "Reroute.006"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-251.4383544921875, -375.2464904785156)
        Reroute_005.name = "Reroute.005"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-169.753173828125, 132.0079345703125)
        Reroute_001.name = "Reroute.001"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-129.55636596679688, 106.93687438964844)
        Reroute_004.name = "Reroute.004"

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (288.5528259277344, -325.3872985839844)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (288.5528259277344, -194.30615234375)
        Combine_XYZ.name = "Combine XYZ"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (42.38671112060547, -110.4229736328125)
        Map_Range.name = "Map Range"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (423.2417297363281, -32.905548095703125)
        Reroute_007.name = "Reroute.007"

        Vector_Math_003 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_003.location = (-196.08633422851562, -288.5357360839844)
        Vector_Math_003.name = "Vector Math.003"
        Vector_Math_003.operation = 'DOT_PRODUCT'

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-251.4383544921875, -197.71432495117188)
        Reroute_003.name = "Reroute.003"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (-14.38739013671875, -251.07644653320312)
        Group_004.name = "Group.004"

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (-14.38739013671875, -80.17926025390625)
        Group_003.name = "Group.003"

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (162.78460693359375, -251.07644653320312)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'NORMALIZE'

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (162.78460693359375, -80.17926025390625)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'NORMALIZE'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (166.67138671875, 2.3528900146484375)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (-793.5289916992188, 329.8482971191406)
        Group_001.name = "Group.001"

        Attribute_001 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_001.location = (-1074.020263671875, -181.37783813476562)
        Attribute_001.name = "Attribute.001"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (-1074.020263671875, -59.146995544433594)
        Attribute.name = "Attribute"

        Normal_Map = nt.nodes.new('ShaderNodeNormalMap')
        Normal_Map.location = (-1072.22021484375, 109.19798278808594)
        Normal_Map.name = "Normal Map"

        Attribute_002 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_002.location = (-1074.020263671875, 238.6177215576172)
        Attribute_002.name = "Attribute.002"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (-1.090179443359375, 579.9298706054688)
        Frame_003.label = "Changed to \"Face Ramp Builder\""
        Frame_003.name = "Frame.003"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (520.468505859375, 259.1134338378906)
        Reroute_009.name = "Reroute.009"

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (794.4168701171875, 300.3866271972656)
        Invert_Color.name = "Invert Color"

        # Create internal links
        nt.links.new(Group_004.outputs[0], Vector_Math_002.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Vector_Math_003.inputs[1])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Group_003.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Mix.inputs[0])
        nt.links.new(Math.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Group_002.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Vector_Math_003.outputs[1], Map_Range.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Vector_Math_004.outputs[1], Math.inputs[0])
        nt.links.new(Group_001.outputs[4], Group_002.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Vector_Math_004.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_010.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mapping.inputs[0])
        nt.links.new(Mapping.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Reroute_001.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Vector_Math_003.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Vector_Math_004.inputs[1])
        nt.links.new(Reroute_011.outputs[0], Mapping.inputs[3])
        nt.links.new(Mix.outputs[1], Reroute_011.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mix.inputs[4])
        nt.links.new(Combine_XYZ_001.outputs[0], Mix.inputs[5])
        nt.links.new(GroupInput.outputs[4], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[5], Combine_XYZ_001.inputs[0])
        nt.links.new(GroupInput.outputs[2], Map_Range.inputs[1])
        nt.links.new(GroupInput.outputs[3], Map_Range.inputs[2])
        nt.links.new(Map_Range.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Vector_Math_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Normal_Map.outputs[0], Group_001.inputs[3])
        nt.links.new(Attribute.outputs[1], Group_003.inputs[0])
        nt.links.new(Attribute_001.outputs[1], Group_004.inputs[0])
        nt.links.new(Attribute_002.outputs[1], Group_001.inputs[1])
        nt.links.new(Reroute_007.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Invert_Color.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Reroute_009.outputs[0], Invert_Color.inputs[1])

        # Set default values
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Vector_Math_004.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs[3].default_value = 1.0
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Combine_XYZ_001.inputs[1].default_value = 1.0
        Combine_XYZ_001.inputs[2].default_value = 1.0
        Combine_XYZ.inputs[1].default_value = 1.0
        Combine_XYZ.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Vector_Math_003.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs[3].default_value = 1.0
        Vector_Math_002.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[3].default_value = 1.0
        Vector_Math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Group_001.inputs[0].default_value = False
        Group_001.inputs[2].default_value = 0.0
        Normal_Map.inputs[0].default_value = 1.0
        Normal_Map.inputs[1].default_value = (0.5, 0.5, 1.0, 1.0)
        Invert_Color.inputs[0].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
