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


class ShaderNodeAdd_Invert_Tint_V_Body(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Invert_Tint_V_Body'
    bl_label = "Add Invert Tint V-Body"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 0.0
        self.inputs["Combine"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Low Color"].default_value = (1.0, 0.7686304450035095, 0.7463362216949463, 1.0)
        self.inputs["Mid Color"].default_value = (0.6780416965484619, 0.2375265657901764, 0.18046948313713074, 1.0)
        self.inputs["High Color"].default_value = (0.7339583039283752, 0.19292114675045013, 0.14441092312335968, 1.0)
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Invert Tint V-Body'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Combine', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Low Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.7686304450035095, 0.7463362216949463, 1.0)
        input_socket = nt.interface.new_socket('Mid Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.6780416965484619, 0.2375265657901764, 0.18046948313713074, 1.0)
        input_socket = nt.interface.new_socket('High Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.7339583039283752, 0.19292114675045013, 0.14441092312335968, 1.0)
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

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (464.0, 41.781463623046875)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MULTIPLY'

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (647.0053100585938, -154.46824645996094)
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MULTIPLY'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (850.166259765625, 110.67061614990234)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1038.4705810546875, 349.002685546875)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (604.56298828125, 262.93072509765625)
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MULTIPLY'

        Layer_Weight = nt.nodes.new('ShaderNodeLayerWeight')
        Layer_Weight.location = (-384.64544677734375, 272.345703125)
        Layer_Weight.name = "Layer Weight"

        Invert = nt.nodes.new('ShaderNodeInvert')
        Invert.location = (-169.94845581054688, 285.9302978515625)
        Invert.name = "Invert"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (18.744552612304688, 394.985595703125)
        ColorRamp.name = "ColorRamp"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (472.081298828125, -424.84942626953125)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-66.61239624023438, -594.340087890625)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Invert_002 = nt.nodes.new('ShaderNodeInvert')
        Invert_002.location = (-443.4919738769531, -586.1895141601562)
        Invert_002.name = "Invert.002"

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (-129.74241638183594, 65.16404724121094)
        ColorRamp_001.name = "ColorRamp.001"

        Layer_Weight_001 = nt.nodes.new('ShaderNodeLayerWeight')
        Layer_Weight_001.location = (-498.4541015625, -23.90289306640625)
        Layer_Weight_001.name = "Layer Weight.001"

        Invert_001 = nt.nodes.new('ShaderNodeInvert')
        Invert_001.location = (-321.8406982421875, -33.68381118774414)
        Invert_001.name = "Invert.001"

        Layer_Weight_002 = nt.nodes.new('ShaderNodeLayerWeight')
        Layer_Weight_002.location = (-644.3169555664062, -593.8218994140625)
        Layer_Weight_002.name = "Layer Weight.002"

        ColorRamp_002 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_002.location = (-169.03936767578125, -373.980224609375)
        ColorRamp_002.name = "ColorRamp.002"

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (1762.955078125, 659.1505737304688)
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'BURN'

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (1295.1007080078125, 684.57763671875)
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MIX'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (1503.1953125, 682.2168579101562)
        Math_001.name = "Math.001"
        Math_001.operation = 'POWER'

        # Create internal links
        nt.links.new(Layer_Weight_002.outputs[1], Invert_002.inputs[1])
        nt.links.new(Layer_Weight_001.outputs[1], Invert_001.inputs[1])
        nt.links.new(Layer_Weight.outputs[1], Invert.inputs[1])
        nt.links.new(Invert_002.outputs[0], ColorRamp_002.inputs[0])
        nt.links.new(Invert.outputs[0], ColorRamp.inputs[0])
        nt.links.new(Invert_001.outputs[0], ColorRamp_001.inputs[0])
        nt.links.new(Invert_002.outputs[0], Math.inputs[0])
        nt.links.new(ColorRamp_002.outputs[0], Mix.inputs[6])
        nt.links.new(Math.outputs[0], Mix.inputs[7])
        nt.links.new(Mix_003.outputs[2], Mix_001.inputs[6])
        nt.links.new(Mix_004.outputs[2], Mix_002.inputs[6])
        nt.links.new(Mix_001.outputs[2], Mix_002.inputs[7])
        nt.links.new(Mix_005.outputs[2], Mix_001.inputs[7])
        nt.links.new(ColorRamp_001.outputs[0], Mix_003.inputs[6])
        nt.links.new(ColorRamp.outputs[0], Mix_004.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_005.inputs[6])
        nt.links.new(GroupInput.outputs[4], Mix_004.inputs[7])
        nt.links.new(Mix_002.outputs[2], Mix_006.inputs[2])
        nt.links.new(Mix_006.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_006.inputs[6])
        nt.links.new(Mix_002.outputs[2], Mix_006.inputs[7])
        nt.links.new(GroupInput.outputs[3], Mix_004.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[5], Mix_003.inputs[7])
        nt.links.new(GroupInput.outputs[3], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[6], Mix_005.inputs[7])
        nt.links.new(GroupInput.outputs[3], Mix_005.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_007.inputs[3])
        nt.links.new(GroupInput.outputs[2], Mix_007.inputs[0])
        nt.links.new(Mix_007.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix_006.inputs[0])
        nt.links.new(GroupInput.outputs[7], Layer_Weight.inputs[1])
        nt.links.new(GroupInput.outputs[7], Layer_Weight_001.inputs[1])
        nt.links.new(GroupInput.outputs[7], Layer_Weight_002.inputs[1])

        # Set default values
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[0].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[0].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Layer_Weight.inputs[0].default_value = 0.8999999761581421
        Invert.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 0.9000000953674316
        Math.inputs[2].default_value = 0.5
        Invert_002.inputs[0].default_value = 1.0
        Layer_Weight_001.inputs[0].default_value = 0.7000000476837158
        Invert_001.inputs[0].default_value = 1.0
        Layer_Weight_002.inputs[0].default_value = 0.40000009536743164
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[3].default_value = 0.0
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_007.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_001.inputs[1].default_value = 1.5
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
