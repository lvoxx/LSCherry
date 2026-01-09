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


class ShaderNodeToonSpec(ShaderNode):
    bl_idname = 'ShaderNodeToonSpec'
    bl_label = "ToonSpec"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Size"].default_value = 0.8999999761581421
        self.inputs["Smooth"].default_value = 0.10000000149011612
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'ToonSpec'

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

        Glossy_BSDF = nt.nodes.new('ShaderNodeBsdfAnisotropic')
        Glossy_BSDF.location = (-141.14588928222656, 112.11140441894531)
        Glossy_BSDF.name = "Glossy BSDF"

        Toon_BSDF = nt.nodes.new('ShaderNodeBsdfToon')
        Toon_BSDF.location = (-141.14588928222656, -112.11140441894531)
        Toon_BSDF.name = "Toon BSDF"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (103.6272201538086, 23.878311157226562)
        Mix_Shader.name = "Mix Shader"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-583.9517822265625, -143.54417419433594)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-365.0149230957031, -187.68978881835938)
        Map_Range.name = "Map Range"

        # Create internal links
        nt.links.new(Toon_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(GroupInput.outputs[0], Glossy_BSDF.inputs[0])
        nt.links.new(GroupInput.outputs[0], Toon_BSDF.inputs[0])
        nt.links.new(GroupInput.outputs[3], Glossy_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[1], Math.inputs[0])
        nt.links.new(Map_Range.outputs[0], Toon_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[2], Toon_BSDF.inputs[2])
        nt.links.new(GroupInput.outputs[4], Glossy_BSDF.inputs[4])
        nt.links.new(GroupInput.outputs[4], Toon_BSDF.inputs[3])
        nt.links.new(GroupInput.outputs[5], Glossy_BSDF.inputs[5])
        nt.links.new(Math.outputs[0], Map_Range.inputs[0])
        nt.links.new(Glossy_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Glossy_BSDF.inputs[2].default_value = 0.0
        Glossy_BSDF.inputs[3].default_value = 0.0
        Glossy_BSDF.inputs[6].default_value = 0.0
        Toon_BSDF.inputs[4].default_value = 0.0
        Mix_Shader.inputs[0].default_value = 0.800000011920929
        Math.inputs[1].default_value = 0.3330000042915344
        Math.inputs[2].default_value = 0.5
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.3300000429153442
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
