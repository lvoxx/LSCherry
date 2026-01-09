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


class ShaderNodeSpecular_Core(ShaderNode):
    bl_idname = 'ShaderNodeSpecular_Core'
    bl_label = "Specular Core"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Specular Core'

        # Create output sockets
        nt.interface.new_socket('Specular', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
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
        Glossy_BSDF.location = (-45.0989990234375, 102.41868591308594)
        Glossy_BSDF.name = "Glossy BSDF"

        Shader_to_RGB_001 = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB_001.location = (201.10281372070312, 21.341293334960938)
        Shader_to_RGB_001.name = "Shader to RGB.001"

        # Create internal links
        nt.links.new(Glossy_BSDF.outputs[0], Shader_to_RGB_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Glossy_BSDF.inputs[4])
        nt.links.new(GroupInput.outputs[0], Glossy_BSDF.inputs[1])
        nt.links.new(Shader_to_RGB_001.outputs[0], GroupOutput.inputs[0])

        # Set default values
        Glossy_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Glossy_BSDF.inputs[2].default_value = 0.0
        Glossy_BSDF.inputs[3].default_value = 0.0
        Glossy_BSDF.inputs[5].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs[6].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
