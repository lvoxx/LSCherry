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


class ShaderNodeSST1__Freckles(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Freckles'
    bl_label = "SST1: Freckles"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Builder"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Factor"].default_value = 1.0
        self.inputs["Red Color"].default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
        self.inputs["Intensity"].default_value = 0.5
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Scale Small"].default_value = 2000.0
        self.inputs["Scale Big"].default_value = 1100.0
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Freckles'

        # Create output sockets
        nt.interface.new_socket('Builder', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Builder', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
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
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
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

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (-89.63232421875, 271.0816650390625)
        ColorRamp_001.name = "ColorRamp.001"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-484.948486328125, 163.66796875)
        Mapping.name = "Mapping"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (-87.31494140625, 16.7813720703125)
        ColorRamp.name = "ColorRamp"

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (-273.95166015625, 20.8126220703125)
        Noise_Texture.name = "Noise Texture"

        Noise_Texture_001 = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture_001.location = (-274.65576171875, 277.53857421875)
        Noise_Texture_001.name = "Noise Texture.001"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (262.88037109375, 87.5010986328125)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'ADD'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (904.4683837890625, 65.1212387084961)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (687.060302734375, 124.13150787353516)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MULTIPLY'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (500.6427917480469, -80.82946014404297)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-708.9114379882812, -96.78730010986328)
        Combine_XYZ.name = "Combine XYZ"

        # Create internal links
        nt.links.new(Combine_XYZ.outputs[0], Mapping.inputs[3])
        nt.links.new(GroupInput.outputs[5], Noise_Texture_001.inputs[2])
        nt.links.new(Noise_Texture.outputs[1], ColorRamp.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix_001.inputs[6])
        nt.links.new(Noise_Texture_001.outputs[1], ColorRamp_001.inputs[0])
        nt.links.new(ColorRamp_001.outputs[0], Mix_001.inputs[7])
        nt.links.new(Mix_001.outputs[2], Math.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture_001.inputs[0])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Math.outputs[0], Mix_003.inputs[7])
        nt.links.new(Mix_003.outputs[2], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_003.inputs[6])
        nt.links.new(GroupInput.outputs[4], Combine_XYZ.inputs[0])
        nt.links.new(GroupInput.outputs[4], Combine_XYZ.inputs[1])
        nt.links.new(GroupInput.outputs[4], Combine_XYZ.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[7], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[6], Noise_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[3], Math.inputs[1])
        nt.links.new(GroupInput.outputs[7], GroupOutput.inputs[1])

        # Set default values
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[3].default_value = 2.0
        Noise_Texture.inputs[4].default_value = 0.5
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Noise_Texture_001.inputs[1].default_value = 0.0
        Noise_Texture_001.inputs[3].default_value = 2.0
        Noise_Texture_001.inputs[4].default_value = 0.5
        Noise_Texture_001.inputs[5].default_value = 2.0
        Noise_Texture_001.inputs[6].default_value = 0.0
        Noise_Texture_001.inputs[7].default_value = 1.0
        Noise_Texture_001.inputs[8].default_value = 0.0
        Mix_001.inputs[0].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[0].default_value = 1.0
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
