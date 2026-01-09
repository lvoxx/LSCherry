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


class ShaderNodeSimple_Skin_Type_1(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Skin_Type_1'
    bl_label = "Simple Skin Type 1"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Skin Color"].default_value = (0.949999988079071, 0.6191033124923706, 0.5204554796218872, 1.0)
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Red Color"].default_value = (0.8999999761581421, 0.19262465834617615, 0.13571682572364807, 1.0)
        self.inputs["Blue Color"].default_value = (0.3672824203968048, 0.24802467226982117, 0.8999999761581421, 1.0)
        self.inputs["Size"].default_value = 1.100000023841858
        self.inputs["Strength"].default_value = 1.0
        self.inputs["Red Spots Red Color"].default_value = (0.800000011920929, 0.17122192680835724, 0.12063717842102051, 1.0)
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Strength"].default_value = 1.0
        self.inputs["Blue Color"].default_value = (0.35572776198387146, 0.082790806889534, 0.800000011920929, 1.0)
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Mask Scale"].default_value = 7.0
        self.inputs["Strength"].default_value = 1.0
        self.inputs["Red Color"].default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        self.inputs["Scale"].default_value = 75.0
        self.inputs["Threadhold"].default_value = 0
        self.inputs["Factor"].default_value = 0.0
        self.inputs["Red Color"].default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        self.inputs["Intensity"].default_value = 0.5
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Scale Small"].default_value = 2000.0
        self.inputs["Scale Big"].default_value = 1100.0
        self.inputs["Factor"].default_value = 0.0
        self.inputs["Scale"].default_value = 1.5
        self.inputs["Dirt Color"].default_value = (0.05000000074505806, 0.01831624284386635, 0.0050119939260184765, 1.0)
        self.inputs["Dirt Strength"].default_value = 0.25
        self.inputs["Goose Bumps"].default_value = 0.0
        self.inputs["Details"].default_value = 0.30000001192092896
        self.inputs["Skin Scale"].default_value = 9.0
        self.inputs["Noise Scale"].default_value = 50.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Skin Type 1'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Skin Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.949999988079071, 0.6191033124923706, 0.5204554796218872, 1.0)
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        nt.interface.new_socket('-- Blemishes --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.8999999761581421, 0.19262465834617615, 0.13571682572364807, 1.0)
        input_socket = nt.interface.new_socket('Blue Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.3672824203968048, 0.24802467226982117, 0.8999999761581421, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.100000023841858
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        nt.interface.new_socket('-- Red Spots --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Red Spots Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.17122192680835724, 0.12063717842102051, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        nt.interface.new_socket('-- Veins --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Blue Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.35572776198387146, 0.082790806889534, 0.800000011920929, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Mask Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 7.0
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        nt.interface.new_socket('-- Moles --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 75.0
        input_socket = nt.interface.new_socket('Threadhold', in_out='INPUT', socket_type='NodeSocketInt')
        input_socket.default_value = 0
        nt.interface.new_socket('-- Freckles --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        input_socket = nt.interface.new_socket('Intensity', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Scale Small', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2000.0
        input_socket = nt.interface.new_socket('Scale Big', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1100.0
        nt.interface.new_socket('-- Pores --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.5
        input_socket = nt.interface.new_socket('Dirt Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.05000000074505806, 0.01831624284386635, 0.0050119939260184765, 1.0)
        input_socket = nt.interface.new_socket('Dirt Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.25
        nt.interface.new_socket('-- Skin Bump --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Goose Bumps', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Details', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Skin Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 9.0
        input_socket = nt.interface.new_socket('Noise Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 50.0

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

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (-1036.21142578125, -34.53603744506836)
        Group_011.name = "Group.011"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (923.5552978515625, 98.5340576171875)
        Group_012.name = "Group.012"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-823.240234375, -34.53603744506836)
        Group_013.name = "Group.013"

        Group_005 = nt.nodes.new('ShaderNodeGroup')
        Group_005.location = (-586.589599609375, -34.53603744506836)
        Group_005.name = "Group.005"

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (-345.0238342285156, -34.53603744506836)
        Group_004.name = "Group.004"

        Group_006 = nt.nodes.new('ShaderNodeGroup')
        Group_006.location = (-97.11336517333984, -22.38582420349121)
        Group_006.name = "Group.006"

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (706.9749755859375, 98.5340576171875)
        Group_008.name = "Group.008"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (413.081298828125, 2.5635623931884766)
        Group_010.name = "Group.010"

        Group_007 = nt.nodes.new('ShaderNodeGroup')
        Group_007.location = (706.9749755859375, -88.40463256835938)
        Group_007.name = "Group.007"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (198.76678466796875, 98.5340576171875)
        Group_014.name = "Group.014"

        # Create internal links
        nt.links.new(Group_008.outputs[0], Group_012.inputs[0])
        nt.links.new(Group_006.outputs[1], Group_014.inputs[7])
        nt.links.new(Group_013.outputs[0], Group_005.inputs[0])
        nt.links.new(Group_011.outputs[1], Group_013.inputs[5])
        nt.links.new(Group_013.outputs[1], Group_005.inputs[4])
        nt.links.new(Group_014.outputs[1], Group_010.inputs[2])
        nt.links.new(Group_011.outputs[0], Group_013.inputs[0])
        nt.links.new(Group_005.outputs[0], Group_004.inputs[0])
        nt.links.new(Group_010.outputs[0], Group_007.inputs[0])
        nt.links.new(Group_005.outputs[1], Group_004.inputs[5])
        nt.links.new(Group_004.outputs[0], Group_006.inputs[0])
        nt.links.new(Group_010.outputs[0], Group_008.inputs[1])
        nt.links.new(Group_006.outputs[0], Group_014.inputs[0])
        nt.links.new(Group_014.outputs[0], Group_008.inputs[0])
        nt.links.new(Group_004.outputs[1], Group_006.inputs[4])
        nt.links.new(GroupInput.outputs[1], Group_011.inputs[1])
        nt.links.new(Group_012.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_007.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[0], Group_011.inputs[0])
        nt.links.new(Group_010.outputs[1], Group_007.inputs[5])
        nt.links.new(GroupInput.outputs[3], Group_013.inputs[1])
        nt.links.new(GroupInput.outputs[4], Group_013.inputs[2])
        nt.links.new(GroupInput.outputs[5], Group_013.inputs[3])
        nt.links.new(GroupInput.outputs[6], Group_013.inputs[4])
        nt.links.new(GroupInput.outputs[8], Group_005.inputs[1])
        nt.links.new(GroupInput.outputs[9], Group_005.inputs[2])
        nt.links.new(GroupInput.outputs[10], Group_005.inputs[3])
        nt.links.new(GroupInput.outputs[12], Group_004.inputs[1])
        nt.links.new(GroupInput.outputs[13], Group_004.inputs[2])
        nt.links.new(GroupInput.outputs[14], Group_004.inputs[3])
        nt.links.new(GroupInput.outputs[15], Group_004.inputs[4])
        nt.links.new(GroupInput.outputs[17], Group_006.inputs[1])
        nt.links.new(GroupInput.outputs[18], Group_006.inputs[2])
        nt.links.new(GroupInput.outputs[19], Group_006.inputs[3])
        nt.links.new(GroupInput.outputs[21], Group_014.inputs[1])
        nt.links.new(GroupInput.outputs[22], Group_014.inputs[2])
        nt.links.new(GroupInput.outputs[23], Group_014.inputs[3])
        nt.links.new(GroupInput.outputs[24], Group_014.inputs[4])
        nt.links.new(GroupInput.outputs[25], Group_014.inputs[5])
        nt.links.new(GroupInput.outputs[26], Group_014.inputs[6])
        nt.links.new(GroupInput.outputs[28], Group_010.inputs[0])
        nt.links.new(GroupInput.outputs[29], Group_010.inputs[1])
        nt.links.new(GroupInput.outputs[30], Group_008.inputs[2])
        nt.links.new(GroupInput.outputs[31], Group_008.inputs[3])
        nt.links.new(GroupInput.outputs[33], Group_007.inputs[1])
        nt.links.new(GroupInput.outputs[34], Group_007.inputs[2])
        nt.links.new(GroupInput.outputs[35], Group_007.inputs[3])
        nt.links.new(GroupInput.outputs[36], Group_007.inputs[4])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
