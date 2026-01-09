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


class ShaderNodeSST1__Pores_Dirt(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Pores_Dirt'
    bl_label = "SST1: Pores Dirt"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Builder"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Pores (require)"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Dirt Color"].default_value = (0.05000000074505806, 0.01831624284386635, 0.0050119939260184765, 1.0)
        self.inputs["Dirt Strength"].default_value = 0.25

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Pores Dirt'

        # Create output sockets
        nt.interface.new_socket('Builder', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Builder', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Pores (require)', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Dirt Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.05000000074505806, 0.01831624284386635, 0.0050119939260184765, 1.0)
        input_socket = nt.interface.new_socket('Dirt Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.25

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

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (-363.3407287597656, 270.3984680175781)
        ColorRamp.name = "ColorRamp"

        Invert = nt.nodes.new('ShaderNodeInvert')
        Invert.location = (-43.308040618896484, 182.9916229248047)
        Invert.name = "Invert"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (396.7427673339844, 56.03672409057617)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (189.79107666015625, 204.44126892089844)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        # Create internal links
        nt.links.new(GroupInput.outputs[1], ColorRamp.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[6])
        nt.links.new(Mix.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[3], Math.inputs[1])
        nt.links.new(Math.outputs[0], Mix.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Invert.inputs[1])
        nt.links.new(Invert.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix.inputs[7])

        # Set default values
        Invert.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
