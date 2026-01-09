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


class ShaderNodeAdd_Random_Toon_Highlight(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Random_Toon_Highlight'
    bl_label = "Add Random Toon Highlight"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 1.0
        self.inputs["Combined"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Size"].default_value = 0.7000000476837158
        self.inputs["Seed"].default_value = 0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Random Toon Highlight'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.7000000476837158
        input_socket = nt.interface.new_socket('Seed', in_out='INPUT', socket_type='NodeSocketInt')
        input_socket.default_value = 0
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

        Layer_Weight = nt.nodes.new('ShaderNodeLayerWeight')
        Layer_Weight.location = (-971.7139892578125, 290.26519775390625)
        Layer_Weight.name = "Layer Weight"

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (-750.8175048828125, 282.51739501953125)
        Invert_Color.name = "Invert Color"

        Color_Ramp = nt.nodes.new('ShaderNodeValToRGB')
        Color_Ramp.location = (-514.8946533203125, 351.01373291015625)
        Color_Ramp.name = "Color Ramp"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-192.53042602539062, 247.9304962158203)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Group_004 = nt.nodes.new('ShaderNodeGroup')
        Group_004.location = (-165.87347412109375, -273.5133972167969)
        Group_004.name = "Group.004"

        Hue_Saturation_Value = nt.nodes.new('ShaderNodeHueSaturation')
        Hue_Saturation_Value.location = (68.14691162109375, -99.08222961425781)
        Hue_Saturation_Value.name = "Hue/Saturation/Value"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-753.8392333984375, -253.73004150390625)
        Map_Range.name = "Map Range"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-745.32568359375, -91.35757446289062)
        Math_001.name = "Math.001"
        Math_001.operation = 'GREATER_THAN'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-429.0243225097656, -115.80615234375)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (-753.8392333984375, -530.9930419921875)
        Map_Range_001.name = "Map Range.001"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (547.5572509765625, 319.479248046875)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (319.4386291503906, 105.1480712890625)
        Group.name = "Group"

        # Create internal links
        nt.links.new(Layer_Weight.outputs[1], Invert_Color.inputs[1])
        nt.links.new(Invert_Color.outputs[0], Color_Ramp.inputs[0])
        nt.links.new(Color_Ramp.outputs[0], Math.inputs[1])
        nt.links.new(GroupInput.outputs[2], Math.inputs[0])
        nt.links.new(Group_004.outputs[0], Hue_Saturation_Value.inputs[4])
        nt.links.new(GroupInput.outputs[5], Map_Range.inputs[0])
        nt.links.new(GroupInput.outputs[5], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[5], Map_Range_001.inputs[0])
        nt.links.new(Map_Range.outputs[0], Mix.inputs[2])
        nt.links.new(Map_Range_001.outputs[0], Mix.inputs[3])
        nt.links.new(Mix.outputs[0], Hue_Saturation_Value.inputs[0])
        nt.links.new(GroupInput.outputs[4], Layer_Weight.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_001.inputs[6])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group.inputs[1])
        nt.links.new(Math.outputs[0], Group.inputs[2])
        nt.links.new(GroupInput.outputs[3], Group.inputs[3])
        nt.links.new(Hue_Saturation_Value.outputs[0], Group.inputs[4])
        nt.links.new(Group.outputs[0], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[6], Layer_Weight.inputs[1])

        # Set default values
        Invert_Color.inputs[0].default_value = 1.0
        Math.inputs[2].default_value = 0.5
        Hue_Saturation_Value.inputs[1].default_value = 1.0
        Hue_Saturation_Value.inputs[2].default_value = 1.0
        Hue_Saturation_Value.inputs[3].default_value = 1.0
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 49.0
        Map_Range.inputs[3].default_value = 0.5
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 0.5
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_001.inputs[1].default_value = 50.0
        Math_001.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Map_Range_001.inputs[1].default_value = 50.0
        Map_Range_001.inputs[2].default_value = 100.0
        Map_Range_001.inputs[3].default_value = 0.0
        Map_Range_001.inputs[4].default_value = 0.5
        Map_Range_001.inputs[5].default_value = 1.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group.inputs[0].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
