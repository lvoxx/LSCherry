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


class ShaderNodeSST1__Red_Spots(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Red_Spots'
    bl_label = "SST1: Red Spots"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Builder"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Red Color"].default_value = (0.800000011920929, 0.17122192680835724, 0.12063717842102051, 1.0)
        self.inputs["Scale"].default_value = 1.0
        self.inputs["Strength"].default_value = 1.0
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Red Spots'

        # Create output sockets
        nt.interface.new_socket('Builder', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Builder', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Red Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.17122192680835724, 0.12063717842102051, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
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

        Noise_Texture = nt.nodes.new('ShaderNodeTexNoise')
        Noise_Texture.location = (46.086669921875, 265.0802001953125)
        Noise_Texture.name = "Noise Texture"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (573.16357421875, 216.23831176757812)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-178.39503479003906, 309.87493896484375)
        Mapping.name = "Mapping"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (764.7683715820312, 177.51364135742188)
        Mix.name = "Mix"
        Mix.blend_type = 'SOFT_LIGHT'

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (218.72705078125, 261.156494140625)
        ColorRamp.name = "ColorRamp"

        # Create internal links
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Noise_Texture.outputs[1], ColorRamp.inputs[0])
        nt.links.new(Mapping.outputs[0], Noise_Texture.inputs[0])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[2], Noise_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[4], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[3], Math.inputs[1])
        nt.links.new(GroupInput.outputs[4], GroupOutput.inputs[1])

        # Set default values
        Noise_Texture.inputs[1].default_value = 0.0
        Noise_Texture.inputs[3].default_value = 5.0
        Noise_Texture.inputs[4].default_value = 0.5
        Noise_Texture.inputs[5].default_value = 2.0
        Noise_Texture.inputs[6].default_value = 0.0
        Noise_Texture.inputs[7].default_value = 1.0
        Noise_Texture.inputs[8].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping.inputs[3].default_value = Vector((30.0, 30.0, 90.0))
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
