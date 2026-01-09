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


class ShaderNodeLimit_Color_Value(ShaderNode):
    bl_idname = 'ShaderNodeLimit_Color_Value'
    bl_label = "Limit Color Value"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Target Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Limit Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Limit Value"].default_value = 0.8899999856948853

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Limit Color Value'

        # Create output sockets
        nt.interface.new_socket('Limited Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Target Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Limit Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Limit Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8899999856948853

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

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (207.2974395751953, 66.01544189453125)
        Combine_Color.name = "Combine Color"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (46.77466583251953, -126.66946411132812)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-161.3773956298828, -64.03618621826172)
        Math_001.name = "Math.001"
        Math_001.operation = 'GREATER_THAN'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-355.7034912109375, -133.75070190429688)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Separate_Color_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_001.location = (-544.141845703125, -102.017822265625)
        Separate_Color_001.name = "Separate Color.001"

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-544.141845703125, 107.83062744140625)
        Separate_Color.name = "Separate Color"

        # Create internal links
        nt.links.new(Separate_Color.outputs[1], Combine_Color.inputs[1])
        nt.links.new(Separate_Color.outputs[0], Combine_Color.inputs[0])
        nt.links.new(GroupInput.outputs[0], Separate_Color.inputs[0])
        nt.links.new(Combine_Color.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[2], Math.inputs[1])
        nt.links.new(GroupInput.outputs[1], Separate_Color_001.inputs[0])
        nt.links.new(Separate_Color_001.outputs[2], Math.inputs[0])
        nt.links.new(Math.outputs[0], Math_001.inputs[1])
        nt.links.new(Separate_Color.outputs[2], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix.inputs[0])
        nt.links.new(Math.outputs[0], Mix.inputs[3])
        nt.links.new(Separate_Color.outputs[2], Mix.inputs[2])
        nt.links.new(Mix.outputs[0], Combine_Color.inputs[2])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_001.inputs[2].default_value = 0.5
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
