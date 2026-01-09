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


class ShaderNodeFace_Ramp_Builder(ShaderNode):
    bl_idname = 'ShaderNodeFace_Ramp_Builder'
    bl_label = "Face Ramp Builder"
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
        nt.description = 'Face Ramp Builder'

        # Create output sockets
        nt.interface.new_socket('Face Value', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Face GS-Vector', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
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
        Frame_002.location = (-43.1673583984375, 25.653594970703125)
        Frame_002.label = "Flip FaceMap If Opposite Site"
        Frame_002.name = "Frame.002"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (122.04266357421875, 511.54351806640625)
        Frame_001.label = "Map Value Limit"
        Frame_001.name = "Frame.001"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-436.7603759765625, 303.8605041503906)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'NORMALIZE'

        Vector_Math_004 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_004.location = (-33.008544921875, -7.8170166015625)
        Vector_Math_004.name = "Vector Math.004"
        Vector_Math_004.operation = 'DOT_PRODUCT'

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (415.8372497558594, 366.1020812988281)
        Reroute_010.name = "Reroute.010"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (789.5553588867188, 166.19171142578125)
        Mapping.name = "Mapping"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-184.5743408203125, 268.5618591308594)
        Reroute.name = "Reroute"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (537.69580078125, -36.428680419921875)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (-614.2136840820312, 303.8605041503906)
        Group_002.name = "Group.002"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-250.7588348388672, -73.22085571289062)
        Reroute_002.name = "Reroute.002"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-184.5743408203125, -65.05874633789062)
        Reroute_006.name = "Reroute.006"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-213.39797973632812, -51.35321044921875)
        Reroute_005.name = "Reroute.005"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-184.5743408203125, 138.08108520507812)
        Reroute_001.name = "Reroute.001"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-250.7588348388672, 116.20392608642578)
        Reroute_004.name = "Reroute.004"

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (274.46282958984375, -103.37098693847656)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (274.46282958984375, -68.40756225585938)
        Combine_XYZ.name = "Combine XYZ"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (42.38671112060547, -110.4229736328125)
        Map_Range.name = "Map Range"

        Vector_Math_003 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_003.location = (-196.08633422851562, -288.5357360839844)
        Vector_Math_003.name = "Vector Math.003"
        Vector_Math_003.operation = 'DOT_PRODUCT'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (150.931396484375, -25.15631103515625)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (-793.5289916992188, 329.8482971191406)
        Group_001.name = "Group.001"

        Attribute_002 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_002.location = (-1074.020263671875, 238.6177215576172)
        Attribute_002.name = "Attribute.002"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (-1.090179443359375, 579.9298706054688)
        Frame_003.label = "Changed to \"Face Ramp Builder\""
        Frame_003.name = "Frame.003"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (407.5379333496094, 138.11953735351562)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (450.7052917480469, -71.38351440429688)
        Reroute_008.name = "Reroute.008"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (699.2705078125, -22.6007080078125)
        Reroute_015.name = "Reroute.015"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (699.2705078125, 143.70297241210938)
        Reroute_018.name = "Reroute.018"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (967.9348754882812, 156.50965881347656)
        Reroute_025.name = "Reroute.025"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (967.9348754882812, 278.0309753417969)
        Reroute_026.name = "Reroute.026"

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-1073.031005859375, 100.34602355957031)
        Geometry.name = "Geometry"

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (42.878692626953125, -363.50543212890625)
        Math_003.name = "Math.003"
        Math_003.operation = 'GREATER_THAN'

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-576.6366577148438, -16.496978759765625)
        Group.name = "Group"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-213.39797973632812, -89.3150634765625)
        Reroute_009.name = "Reroute.009"

        # Create internal links
        nt.links.new(Reroute_004.outputs[0], Vector_Math_003.inputs[1])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Reroute.inputs[0])
        nt.links.new(Group_002.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Group_001.outputs[4], Group_002.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Vector_Math_004.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Vector_Math_003.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mix.inputs[4])
        nt.links.new(Map_Range.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Group.outputs[1], Reroute_002.inputs[0])
        nt.links.new(Attribute_002.outputs[1], Group_001.inputs[1])
        nt.links.new(GroupInput.outputs[1], Map_Range.inputs[1])
        nt.links.new(GroupInput.outputs[2], Map_Range.inputs[2])
        nt.links.new(GroupInput.outputs[4], Combine_XYZ_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Combine_XYZ.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Mix.outputs[1], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Mapping.inputs[3])
        nt.links.new(Reroute_025.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Geometry.outputs[1], Group_001.inputs[3])
        nt.links.new(Reroute_010.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Mapping.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Combine_XYZ_001.outputs[0], Mix.inputs[5])
        nt.links.new(Math_003.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Vector_Math_004.outputs[1], Math.inputs[0])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(Group.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Vector_Math_004.inputs[1])
        nt.links.new(Vector_Math_003.outputs[1], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], Math_003.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mapping.inputs[0])

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
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Group_001.inputs[0].default_value = False
        Group_001.inputs[2].default_value = 0.0
        Math_003.inputs[1].default_value = 0.0
        Math_003.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
