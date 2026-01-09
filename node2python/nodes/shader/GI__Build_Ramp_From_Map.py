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


class ShaderNodeGI__Build_Ramp_From_Map(ShaderNode):
    bl_idname = 'ShaderNodeGI__Build_Ramp_From_Map'
    bl_label = "GI: Build Ramp From Map"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Toon"].default_value = 0.0
        self.inputs["Shadow Factor"].default_value = 1.0
        self.inputs["Shadow Mask"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'GI: Build Ramp From Map'

        # Create output sockets
        nt.interface.new_socket('Hot-UV1', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Hot-UV2', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Hot-UV3', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Hot-UV4', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Hot-UV5', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Cold-UV1', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Cold-UV2', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Cold-UV3', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Cold-UV4', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Cold-UV5', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Toon', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Shadow Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Shadow Mask', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-112.73562622070312, -19.041732788085938)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (110.99164581298828, 14.680463790893555)
        Group_009.name = "Group.009"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (9.757568359375, -58.710289001464844)
        Mapping.name = "Mapping"

        Value = nt.nodes.new('ShaderNodeValue')
        Value.location = (113.41205596923828, -121.33500671386719)
        Value.name = "Value"

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (9.757568359375, -92.29483032226562)
        Mapping_001.name = "Mapping.001"

        Mapping_002 = nt.nodes.new('ShaderNodeMapping')
        Mapping_002.location = (9.757568359375, -131.1036376953125)
        Mapping_002.name = "Mapping.002"

        Mapping_003 = nt.nodes.new('ShaderNodeMapping')
        Mapping_003.location = (9.757568359375, -167.6734619140625)
        Mapping_003.name = "Mapping.003"

        Mapping_004 = nt.nodes.new('ShaderNodeMapping')
        Mapping_004.location = (9.757568359375, -205.7359619140625)
        Mapping_004.name = "Mapping.004"

        Value_001 = nt.nodes.new('ShaderNodeValue')
        Value_001.location = (113.41205596923828, -156.1265411376953)
        Value_001.name = "Value.001"

        Value_002 = nt.nodes.new('ShaderNodeValue')
        Value_002.location = (113.41205596923828, -190.33822631835938)
        Value_002.name = "Value.002"

        Value_003 = nt.nodes.new('ShaderNodeValue')
        Value_003.location = (108.45938110351562, -227.64901733398438)
        Value_003.name = "Value.003"

        Value_004 = nt.nodes.new('ShaderNodeValue')
        Value_004.location = (108.45939636230469, -258.38153076171875)
        Value_004.name = "Value.004"

        Mapping_005 = nt.nodes.new('ShaderNodeMapping')
        Mapping_005.location = (6.929473876953125, -58.506622314453125)
        Mapping_005.name = "Mapping.005"

        Value_005 = nt.nodes.new('ShaderNodeValue')
        Value_005.location = (113.41205596923828, 184.49720764160156)
        Value_005.name = "Value.005"

        Mapping_006 = nt.nodes.new('ShaderNodeMapping')
        Mapping_006.location = (6.929473876953125, -92.0911865234375)
        Mapping_006.name = "Mapping.006"

        Mapping_007 = nt.nodes.new('ShaderNodeMapping')
        Mapping_007.location = (6.929473876953125, -130.89999389648438)
        Mapping_007.name = "Mapping.007"

        Mapping_008 = nt.nodes.new('ShaderNodeMapping')
        Mapping_008.location = (6.929473876953125, -167.46981811523438)
        Mapping_008.name = "Mapping.008"

        Mapping_009 = nt.nodes.new('ShaderNodeMapping')
        Mapping_009.location = (6.929473876953125, -205.5323028564453)
        Mapping_009.name = "Mapping.009"

        Value_006 = nt.nodes.new('ShaderNodeValue')
        Value_006.location = (113.41205596923828, 149.70567321777344)
        Value_006.name = "Value.006"

        Value_007 = nt.nodes.new('ShaderNodeValue')
        Value_007.location = (113.41205596923828, 115.49398803710938)
        Value_007.name = "Value.007"

        Value_008 = nt.nodes.new('ShaderNodeValue')
        Value_008.location = (113.41205596923828, 83.31179809570312)
        Value_008.name = "Value.008"

        Value_009 = nt.nodes.new('ShaderNodeValue')
        Value_009.location = (113.41205596923828, 52.57928466796875)
        Value_009.name = "Value.009"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (698.57861328125, -24.5408935546875)
        Frame.label = "Cold"
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (701.57861328125, 292.301513671875)
        Frame_001.label = "Hot"
        Frame_001.name = "Frame.001"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (384.42578125, -626.47314453125)
        Combine_XYZ.name = "Combine XYZ"

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (385.53460693359375, -503.95599365234375)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Combine_XYZ_002 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_002.location = (383.31707763671875, -368.67242431640625)
        Combine_XYZ_002.name = "Combine XYZ.002"

        Combine_XYZ_003 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_003.location = (383.31707763671875, -234.4977569580078)
        Combine_XYZ_003.name = "Combine XYZ.003"

        Combine_XYZ_004 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_004.location = (383.31707763671875, -103.49919891357422)
        Combine_XYZ_004.name = "Combine XYZ.004"

        Combine_XYZ_005 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_005.location = (384.42578125, 159.09683227539062)
        Combine_XYZ_005.name = "Combine XYZ.005"

        Combine_XYZ_006 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_006.location = (385.53460693359375, 281.6139831542969)
        Combine_XYZ_006.name = "Combine XYZ.006"

        Combine_XYZ_007 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_007.location = (383.31707763671875, 416.8975524902344)
        Combine_XYZ_007.name = "Combine XYZ.007"

        Combine_XYZ_008 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_008.location = (383.31707763671875, 551.072265625)
        Combine_XYZ_008.name = "Combine XYZ.008"

        Combine_XYZ_009 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_009.location = (383.31707763671875, 682.07080078125)
        Combine_XYZ_009.name = "Combine XYZ.009"

        # Create internal links
        nt.links.new(Mix.outputs[2], Group_009.inputs[0])
        nt.links.new(Mapping.outputs[0], GroupOutput.inputs[5])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[0])
        nt.links.new(Group_009.outputs[0], Mapping.inputs[0])
        nt.links.new(Combine_XYZ_004.outputs[0], Mapping.inputs[1])
        nt.links.new(Group_009.outputs[0], Mapping_001.inputs[0])
        nt.links.new(Combine_XYZ_003.outputs[0], Mapping_001.inputs[1])
        nt.links.new(Combine_XYZ_002.outputs[0], Mapping_002.inputs[1])
        nt.links.new(Group_009.outputs[0], Mapping_002.inputs[0])
        nt.links.new(Group_009.outputs[0], Mapping_003.inputs[0])
        nt.links.new(Combine_XYZ_001.outputs[0], Mapping_003.inputs[1])
        nt.links.new(Combine_XYZ.outputs[0], Mapping_004.inputs[1])
        nt.links.new(Group_009.outputs[0], Mapping_004.inputs[0])
        nt.links.new(Mapping_001.outputs[0], GroupOutput.inputs[6])
        nt.links.new(Mapping_002.outputs[0], GroupOutput.inputs[7])
        nt.links.new(Mapping_003.outputs[0], GroupOutput.inputs[8])
        nt.links.new(Mapping_004.outputs[0], GroupOutput.inputs[9])
        nt.links.new(Group_009.outputs[0], Mapping_005.inputs[0])
        nt.links.new(Group_009.outputs[0], Mapping_006.inputs[0])
        nt.links.new(Group_009.outputs[0], Mapping_008.inputs[0])
        nt.links.new(Group_009.outputs[0], Mapping_009.inputs[0])
        nt.links.new(Mapping_006.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Mapping_007.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Mapping_008.outputs[0], GroupOutput.inputs[3])
        nt.links.new(Mapping_009.outputs[0], GroupOutput.inputs[4])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(Mapping_005.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Value_004.outputs[0], Combine_XYZ.inputs[1])
        nt.links.new(Value_003.outputs[0], Combine_XYZ_001.inputs[1])
        nt.links.new(Value_002.outputs[0], Combine_XYZ_002.inputs[1])
        nt.links.new(Value_001.outputs[0], Combine_XYZ_003.inputs[1])
        nt.links.new(Value.outputs[0], Combine_XYZ_004.inputs[1])
        nt.links.new(Value_009.outputs[0], Combine_XYZ_005.inputs[1])
        nt.links.new(Combine_XYZ_005.outputs[0], Mapping_009.inputs[1])
        nt.links.new(Value_008.outputs[0], Combine_XYZ_006.inputs[1])
        nt.links.new(Combine_XYZ_006.outputs[0], Mapping_008.inputs[1])
        nt.links.new(Value_007.outputs[0], Combine_XYZ_007.inputs[1])
        nt.links.new(Combine_XYZ_007.outputs[0], Mapping_007.inputs[1])
        nt.links.new(Value_006.outputs[0], Combine_XYZ_008.inputs[1])
        nt.links.new(Combine_XYZ_008.outputs[0], Mapping_006.inputs[1])
        nt.links.new(Value_005.outputs[0], Combine_XYZ_009.inputs[1])
        nt.links.new(Combine_XYZ_009.outputs[0], Mapping_005.inputs[1])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_009.inputs[1].default_value = 0.10000000149011612
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_001.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_001.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_002.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_002.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_003.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_003.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_004.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_004.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_005.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_005.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_006.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_006.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_007.inputs[0].default_value = (0.0, 0.0, 0.0)
        Mapping_007.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_007.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_008.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_008.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Mapping_009.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping_009.inputs[3].default_value = Vector((1.0, 0.10000000149011612, 1.0))
        Combine_XYZ.inputs[0].default_value = 0.0
        Combine_XYZ.inputs[2].default_value = 0.0
        Combine_XYZ_001.inputs[0].default_value = 0.0
        Combine_XYZ_001.inputs[2].default_value = 0.0
        Combine_XYZ_002.inputs[0].default_value = 0.0
        Combine_XYZ_002.inputs[2].default_value = 0.0
        Combine_XYZ_003.inputs[0].default_value = 0.0
        Combine_XYZ_003.inputs[2].default_value = 0.0
        Combine_XYZ_004.inputs[0].default_value = 0.0
        Combine_XYZ_004.inputs[2].default_value = 0.0
        Combine_XYZ_005.inputs[0].default_value = 0.0
        Combine_XYZ_005.inputs[2].default_value = 0.0
        Combine_XYZ_006.inputs[0].default_value = 0.0
        Combine_XYZ_006.inputs[2].default_value = 0.0
        Combine_XYZ_007.inputs[0].default_value = 0.0
        Combine_XYZ_007.inputs[2].default_value = 0.0
        Combine_XYZ_008.inputs[0].default_value = 0.0
        Combine_XYZ_008.inputs[2].default_value = 0.0
        Combine_XYZ_009.inputs[0].default_value = 0.0
        Combine_XYZ_009.inputs[2].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
