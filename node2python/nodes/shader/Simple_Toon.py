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


class ShaderNodeSimple_Toon(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Toon'
    bl_label = "Simple Toon"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["AO Fac"].default_value = 1.0
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Use Diffuse"].default_value = True
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Toon'

        # Create output sockets
        nt.interface.new_socket('Toon', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('AO Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Use Diffuse', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = True
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

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (324.4455871582031, -74.18356323242188)
        Group_008.name = "Group.008"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (327.2247619628906, 111.55999755859375)
        Group_010.name = "Group.010"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (319.92144775390625, 276.4154357910156)
        Math_001.name = "Math.001"
        Math_001.operation = 'GREATER_THAN'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (577.43115234375, 78.74671936035156)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-72.2286376953125, 444.8995361328125)
        Frame.label = "FIX: Add an input enable default normal to Toon Core"
        Frame.name = "Frame"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-44.9328498840332, -53.439727783203125)
        Group.name = "Group"

        # Create internal links
        nt.links.new(GroupInput.outputs[0], Group_010.inputs[0])
        nt.links.new(GroupInput.outputs[3], Group_008.inputs[0])
        nt.links.new(GroupInput.outputs[1], Group_010.inputs[1])
        nt.links.new(GroupInput.outputs[2], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Mix_001.inputs[0])
        nt.links.new(Group_008.outputs[0], Mix_001.inputs[2])
        nt.links.new(Group_010.outputs[0], Mix_001.inputs[3])
        nt.links.new(Group_010.outputs[0], Mix_001.inputs[7])
        nt.links.new(Group_008.outputs[0], Mix_001.inputs[6])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Group.outputs[0], Group_010.inputs[2])
        nt.links.new(GroupInput.outputs[3], Group.inputs[0])

        # Set default values
        Math_001.inputs[1].default_value = 0.0
        Math_001.inputs[2].default_value = 0.5
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
