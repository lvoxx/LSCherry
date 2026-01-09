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


class ShaderNodeToonify_PBR_Colors(ShaderNode):
    bl_idname = 'ShaderNodeToonify_PBR_Colors'
    bl_label = "Toonify PBR Colors"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        self.inputs["Saturation"].default_value = 0.8500000238418579
        self.inputs["Gamma"].default_value = 0.75
        self.inputs["Bright"].default_value = 0.10000000149011612
        self.inputs["Contrast"].default_value = 0.15000000596046448

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Toonify PBR Colors'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        input_socket = nt.interface.new_socket('Saturation', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8500000238418579
        input_socket = nt.interface.new_socket('Gamma', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.75
        input_socket = nt.interface.new_socket('Bright', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Contrast', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.15000000596046448

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

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (-179.62716674804688, 13.2052001953125)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Gamma = nt.nodes.new('ShaderNodeGamma')
        Gamma.location = (9.562591552734375, -13.2052001953125)
        Gamma.name = "Gamma"

        Brightness_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Brightness_Contrast.location = (179.627197265625, -12.23052978515625)
        Brightness_Contrast.name = "Brightness/Contrast"

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-264.99334716796875, -88.86517333984375)
        Separate_Color.name = "Separate Color"

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (194.30886840820312, -57.297119140625)
        Combine_Color.name = "Combine Color"

        RGB_Curves = nt.nodes.new('ShaderNodeRGBCurve')
        RGB_Curves.location = (-99.4940185546875, -173.23776245117188)
        RGB_Curves.name = "RGB Curves"

        RGB_Curves_001 = nt.nodes.new('ShaderNodeRGBCurve')
        RGB_Curves_001.location = (-220.81796264648438, -48.17718505859375)
        RGB_Curves_001.name = "RGB Curves.001"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-471.0701904296875, -360.5313415527344)
        Frame_001.name = "Frame.001"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (-43.4908447265625, -388.5313415527344)
        Frame_002.name = "Frame.002"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (16.534133911132812, -47.09332275390625)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (253.10829162597656, -47.09332275390625)
        Reroute_001.name = "Reroute.001"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (44.07353210449219, -28.859375)
        Frame_003.label = "Toonify PBR Colors"
        Frame_003.name = "Frame.003"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (549.5283813476562, -370.5313415527344)
        Frame_004.name = "Frame.004"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (-17.58428955078125, -186.18270874023438)
        Frame_005.label = "Because PBR colors are more complex than Toon, I recommend"
        Frame_005.name = "Frame.005"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (-17.58428955078125, -252.2303466796875)
        Frame_006.label = "using additional color converters to achieve the best results."
        Frame_006.name = "Frame.006"

        # Create internal links
        nt.links.new(Gamma.outputs[0], Brightness_Contrast.inputs[0])
        nt.links.new(Hue_Saturation_Value.outputs[0], Gamma.inputs[0])
        nt.links.new(GroupInput.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(Brightness_Contrast.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Hue_Saturation_Value.inputs[1])
        nt.links.new(GroupInput.outputs[2], Gamma.inputs[1])
        nt.links.new(GroupInput.outputs[3], Brightness_Contrast.inputs[1])
        nt.links.new(GroupInput.outputs[4], Brightness_Contrast.inputs[2])
        nt.links.new(Separate_Color.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Separate_Color.outputs[1], Combine_Color.inputs[1])
        nt.links.new(RGB_Curves.outputs[0], Combine_Color.inputs[2])
        nt.links.new(Separate_Color.outputs[2], RGB_Curves.inputs[1])
        nt.links.new(Combine_Color.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute_001.outputs[0], RGB_Curves_001.inputs[1])

        # Set default values
        Hue_Saturation_Value.inputs[0].default_value = 0.5
        Hue_Saturation_Value.inputs[2].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Separate_Color.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        RGB_Curves.inputs[0].default_value = 1.0
        RGB_Curves_001.inputs[0].default_value = 1.0
        Reroute_001.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
