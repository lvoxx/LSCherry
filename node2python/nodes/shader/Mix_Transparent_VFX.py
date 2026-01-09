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


class ShaderNodeMix_Transparent_VFX(ShaderNode):
    bl_idname = 'ShaderNodeMix_Transparent_VFX'
    bl_label = "Mix Transparent VFX"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 2.9802322387695312e-08

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Mix Transparent VFX'

        # Create output sockets
        nt.interface.new_socket('Mask', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 2.9802322387695312e-08
        nt.interface.new_socket('Shader', in_out='INPUT', socket_type='NodeSocketShader')

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

        Fresnel = nt.nodes.new('ShaderNodeFresnel')
        Fresnel.location = (-138.7225341796875, -70.04754638671875)
        Fresnel.name = "Fresnel"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (180.1520538330078, 217.35824584960938)
        Transparent_BSDF.name = "Transparent BSDF"

        Mix_Shader_001 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_001.location = (720.4673461914062, 181.56712341308594)
        Mix_Shader_001.name = "Mix Shader.001"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (556.0906372070312, 86.7460708618164)
        Mix_Shader.name = "Mix Shader"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (403.2370300292969, -57.49848937988281)
        Emission.name = "Emission"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (75.56430053710938, 50.876869201660156)
        ColorRamp.name = "ColorRamp"

        # Create internal links
        nt.links.new(Fresnel.outputs[0], ColorRamp.inputs[0])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(ColorRamp.outputs[0], Mix_Shader.inputs[0])
        nt.links.new(Emission.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix_Shader_001.inputs[0])
        nt.links.new(Mix_Shader_001.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Mix_Shader.outputs[0], Mix_Shader_001.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_Shader_001.inputs[2])

        # Set default values
        Fresnel.inputs[0].default_value = 0.9500001668930054
        Fresnel.inputs[1].default_value = (0.0, 0.0, 0.0)
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0
        Emission.inputs[0].default_value = (0.8611106276512146, 0.8611106276512146, 0.8611106276512146, 1.0)
        Emission.inputs[1].default_value = 1.0
        Emission.inputs[2].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
