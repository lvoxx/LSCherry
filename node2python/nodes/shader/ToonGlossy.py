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


class ShaderNodeToonGlossy(ShaderNode):
    bl_idname = 'ShaderNodeToonGlossy'
    bl_label = "ToonGlossy"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Size"].default_value = 0.8999999761581421
        self.inputs["Smooth"].default_value = 0.10000000149011612
        self.inputs["Roughness"].default_value = 0.5
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'ToonGlossy'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8999999761581421
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
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

        Toon_BSDF = nt.nodes.new('ShaderNodeBsdfToon')
        Toon_BSDF.location = (-141.1240692138672, -108.997314453125)
        Toon_BSDF.name = "Toon BSDF"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (126.50444030761719, -0.8186416625976562)
        Mix_Shader.name = "Mix Shader"

        Glossy_BSDF = nt.nodes.new('ShaderNodeBsdfAnisotropic')
        Glossy_BSDF.location = (-138.9541015625, 108.99728393554688)
        Glossy_BSDF.name = "Glossy BSDF"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Toon_BSDF.inputs[0])
        nt.links.new(GroupInput.outputs[0], Glossy_BSDF.inputs[0])
        nt.links.new(GroupInput.outputs[1], Toon_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[2], Toon_BSDF.inputs[2])
        nt.links.new(GroupInput.outputs[3], Glossy_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[4], Toon_BSDF.inputs[3])
        nt.links.new(GroupInput.outputs[4], Glossy_BSDF.inputs[4])
        nt.links.new(Glossy_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Toon_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Toon_BSDF.inputs[4].default_value = 0.0
        Mix_Shader.inputs[0].default_value = 0.800000011920929
        Glossy_BSDF.inputs[2].default_value = 0.0
        Glossy_BSDF.inputs[3].default_value = 0.0
        Glossy_BSDF.inputs[5].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs[6].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
