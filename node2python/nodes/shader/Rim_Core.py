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


class ShaderNodeRim_Core(ShaderNode):
    bl_idname = 'ShaderNodeRim_Core'
    bl_label = "Rim Core"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Rim Strength"].default_value = 0.0
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Rim Core'

        # Create output sockets
        nt.interface.new_socket('Rim', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Rim Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
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

        Glossy_BSDF = nt.nodes.new('ShaderNodeBsdfAnisotropic')
        Glossy_BSDF.location = (-2.3977508544921875, 12.53759765625)
        Glossy_BSDF.name = "Glossy BSDF"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-192.8369140625, 46.86745834350586)
        Math_001.label = "Scale Ramp up"
        Math_001.name = "Math.001"
        Math_001.operation = 'ADD'

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (196.9232177734375, -12.537567138671875)
        Shader_to_RGB.name = "Shader to RGB"

        Bright_or_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Bright_or_Contrast.location = (417.0, 1.7748947143554688)
        Bright_or_Contrast.name = "Bright or Contrast"

        # Create internal links
        nt.links.new(Glossy_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Math_001.outputs[0], Glossy_BSDF.inputs[1])
        nt.links.new(Bright_or_Contrast.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Math_001.inputs[0])
        nt.links.new(Shader_to_RGB.outputs[0], Bright_or_Contrast.inputs[0])
        nt.links.new(GroupInput.outputs[0], Bright_or_Contrast.inputs[1])
        nt.links.new(GroupInput.outputs[2], Glossy_BSDF.inputs[4])

        # Set default values
        Glossy_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Glossy_BSDF.inputs[2].default_value = 0.0
        Glossy_BSDF.inputs[3].default_value = 0.0
        Glossy_BSDF.inputs[5].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs[6].default_value = 0.0
        Math_001.inputs[1].default_value = 0.5
        Math_001.inputs[2].default_value = 0.5
        Bright_or_Contrast.inputs[2].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
