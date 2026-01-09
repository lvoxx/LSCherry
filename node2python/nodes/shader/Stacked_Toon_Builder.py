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


class ShaderNodeStacked_Toon_Builder(ShaderNode):
    bl_idname = 'ShaderNodeStacked_Toon_Builder'
    bl_label = "Stacked Toon Builder"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Enable Dot"].default_value = False
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Stacked Toon Builder'

        # Create output sockets
        nt.interface.new_socket('Shading', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Enable Dot', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
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

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (112.65667724609375, 207.96243286132812)
        Group_013.name = "Group.013"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (112.65667724609375, 59.0443115234375)
        Group_014.name = "Group.014"

        Group_015 = nt.nodes.new('ShaderNodeGroup')
        Group_015.location = (-169.65121459960938, -197.87451171875)
        Group_015.name = "Group.015"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (50.4844970703125, -207.96240234375)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (50.4844970703125, -152.8009033203125)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (50.4844970703125, 83.60595703125)
        Reroute_010.name = "Reroute.010"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (112.65667724609375, -179.28424072265625)
        Attribute.name = "Attribute"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (338.7626037597656, 146.1382598876953)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (522.3208618164062, 144.94757080078125)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        # Create internal links
        nt.links.new(Group_015.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Group_014.inputs[3])
        nt.links.new(Reroute_010.outputs[0], Group_013.inputs[2])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Attribute.outputs[1], Group_014.inputs[1])
        nt.links.new(Group_013.outputs[0], Mix.inputs[6])
        nt.links.new(Group_014.outputs[1], Mix.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[0])
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Mix.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[0], Mix_002.inputs[7])
        nt.links.new(GroupInput.outputs[2], Group_015.inputs[0])

        # Set default values
        Group_013.inputs[0].default_value = 1.0
        Group_013.inputs[1].default_value = 0.0
        Group_014.inputs[0].default_value = False
        Group_014.inputs[2].default_value = 0.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[0].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
