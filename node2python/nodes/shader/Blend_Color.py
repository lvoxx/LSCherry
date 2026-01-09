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


class ShaderNodeBlend_Color(ShaderNode):
    bl_idname = 'ShaderNodeBlend_Color'
    bl_label = "Blend Color"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Mix"].default_value = 1.0
        self.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Outer Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Blend Color'

        # Create output sockets
        nt.interface.new_socket('Blend Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Mix', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Outer Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)

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

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-307.2112121582031, 71.15016174316406)
        Separate_Color.name = "Separate Color"

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (314.899658203125, 57.46061706542969)
        Combine_Color.name = "Combine Color"

        Separate_Color_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_001.location = (-307.2112121582031, -98.38943481445312)
        Separate_Color_001.name = "Separate Color.001"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-104.336181640625, 158.2195587158203)
        Math.name = "Math"
        Math.operation = 'ADD'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-104.336181640625, 2.8958587646484375)
        Math_001.name = "Math.001"
        Math_001.operation = 'ADD'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-104.336181640625, -158.21954345703125)
        Math_002.name = "Math.002"
        Math_002.operation = 'ADD'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (96.61370849609375, 158.2195587158203)
        Math_003.name = "Math.003"
        Math_003.operation = 'DIVIDE'

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (96.61370849609375, 2.369232177734375)
        Math_004.name = "Math.004"
        Math_004.operation = 'DIVIDE'

        Math_005 = nt.nodes.new('ShaderNodeMath')
        Math_005.location = (96.61370849609375, -152.4280548095703)
        Math_005.name = "Math.005"
        Math_005.operation = 'DIVIDE'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (521.6471557617188, 332.6307067871094)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (195.90890502929688, 472.49908447265625)
        Frame.label = "For more details: https://www.youtube.com/watch?v=gwLQ0cDb4cE"
        Frame.name = "Frame"

        # Create internal links
        nt.links.new(Math_002.outputs[0], Math_005.inputs[0])
        nt.links.new(Math_001.outputs[0], Math_004.inputs[0])
        nt.links.new(Math.outputs[0], Math_003.inputs[0])
        nt.links.new(Separate_Color.outputs[2], Math_002.inputs[0])
        nt.links.new(Separate_Color_001.outputs[0], Math.inputs[1])
        nt.links.new(Separate_Color.outputs[0], Math.inputs[0])
        nt.links.new(Separate_Color_001.outputs[1], Math_001.inputs[1])
        nt.links.new(Separate_Color.outputs[1], Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Separate_Color.inputs[0])
        nt.links.new(GroupInput.outputs[2], Separate_Color_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[0])
        nt.links.new(Combine_Color.outputs[0], Mix.inputs[7])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Separate_Color_001.outputs[2], Math_002.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[6])
        nt.links.new(Math_003.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Math_004.outputs[0], Combine_Color.inputs[1])
        nt.links.new(Math_005.outputs[0], Combine_Color.inputs[2])

        # Set default values
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[2].default_value = 0.5
        Math_003.inputs[1].default_value = 2.0
        Math_003.inputs[2].default_value = 0.5
        Math_004.inputs[1].default_value = 2.0
        Math_004.inputs[2].default_value = 0.5
        Math_005.inputs[1].default_value = 2.0
        Math_005.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
