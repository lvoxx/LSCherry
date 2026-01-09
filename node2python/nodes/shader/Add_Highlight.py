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


class ShaderNodeAdd_Highlight(ShaderNode):
    bl_idname = 'ShaderNodeAdd_Highlight'
    bl_label = "Add Highlight"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Fac"].default_value = 1.0
        self.inputs["Combined"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["Shading"].default_value = 1.0
        self.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Add Highlight'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('Shading', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
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

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (319.3514099121094, 194.54754638671875)
        Frame_002.label = "Combine With Base"
        Frame_002.name = "Frame.002"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-59.91670227050781, -58.99342346191406)
        Frame.label = "Add Pattern"
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-188.16824340820312, -65.71331787109375)
        Frame_001.label = "Add Highlight Color"
        Frame_001.name = "Frame.001"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (-31.17645263671875, -62.74810791015625)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'ADD'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (-42.00877380371094, -54.46623992919922)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (56.424354553222656, -37.779579162597656)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (461.833984375, 379.9659423828125)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        # Create internal links
        nt.links.new(GroupInput.outputs[2], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[4], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[3], Mix_002.inputs[7])
        nt.links.new(GroupInput.outputs[2], Mix_002.inputs[6])
        nt.links.new(Mix_002.outputs[2], Mix.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix_003.inputs[6])
        nt.links.new(GroupInput.outputs[0], Mix_003.inputs[0])
        nt.links.new(Mix_001.outputs[2], Mix_003.inputs[7])
        nt.links.new(Mix_003.outputs[2], GroupOutput.inputs[0])

        # Set default values
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
        Mix.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
