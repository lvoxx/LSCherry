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


class ShaderNodeToonMetal(ShaderNode):
    bl_idname = 'ShaderNodeToonMetal'
    bl_label = "ToonMetal"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Edge Tint"].default_value = (0.7699999809265137, 0.7699999809265137, 0.7699999809265137, 1.0)
        self.inputs["Size"].default_value = 0.8999999761581421
        self.inputs["Smooth"].default_value = 0.10000000149011612
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'ToonMetal'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Edge Tint', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.7699999809265137, 0.7699999809265137, 0.7699999809265137, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8999999761581421
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Tangent', in_out='INPUT', socket_type='NodeSocketVector')
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
        Toon_BSDF.location = (-87.8956298828125, -133.12738037109375)
        Toon_BSDF.name = "Toon BSDF"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (179.73284912109375, -24.94872283935547)
        Mix_Shader.name = "Mix Shader"

        Metallic_BSDF = nt.nodes.new('ShaderNodeBsdfMetallic')
        Metallic_BSDF.location = (-179.73287963867188, 133.12738037109375)
        Metallic_BSDF.name = "Metallic BSDF"

        # Create internal links
        nt.links.new(Toon_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Metallic_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Toon_BSDF.inputs[0])
        nt.links.new(GroupInput.outputs[0], Metallic_BSDF.inputs[0])
        nt.links.new(GroupInput.outputs[1], Metallic_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[4], Metallic_BSDF.inputs[4])
        nt.links.new(GroupInput.outputs[2], Toon_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[3], Toon_BSDF.inputs[2])
        nt.links.new(GroupInput.outputs[5], Metallic_BSDF.inputs[7])
        nt.links.new(GroupInput.outputs[5], Toon_BSDF.inputs[3])
        nt.links.new(GroupInput.outputs[6], Metallic_BSDF.inputs[8])

        # Set default values
        Toon_BSDF.inputs[4].default_value = 0.0
        Mix_Shader.inputs[0].default_value = 0.800000011920929
        Metallic_BSDF.inputs[2].default_value = (2.756999969482422, 2.513000011444092, 2.2309999465942383)
        Metallic_BSDF.inputs[3].default_value = (3.867000102996826, 3.4040000438690186, 3.009000062942505)
        Metallic_BSDF.inputs[5].default_value = 0.0
        Metallic_BSDF.inputs[6].default_value = 0.0
        Metallic_BSDF.inputs[9].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
