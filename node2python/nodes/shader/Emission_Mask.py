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


class ShaderNodeEmission_Mask(ShaderNode):
    bl_idname = 'ShaderNodeEmission_Mask'
    bl_label = "Emission Mask"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Mask"].default_value = 0.5
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Scale"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Emission Mask'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Mask', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (-33.60517883300781, 69.78109741210938)
        Transparent_BSDF.name = "Transparent BSDF"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (-33.0797119140625, -13.705078125)
        Emission.name = "Emission"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (249.29244995117188, 90.21170043945312)
        Mix_Shader.name = "Mix Shader"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-258.4811096191406, -90.21173095703125)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        # Create internal links
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Emission.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Math.outputs[0], Emission.inputs[1])
        nt.links.new(GroupInput.outputs[0], Mix_Shader.inputs[0])
        nt.links.new(GroupInput.outputs[1], Emission.inputs[0])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[2], Math.inputs[1])

        # Set default values
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0
        Emission.inputs[2].default_value = 0.0
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
