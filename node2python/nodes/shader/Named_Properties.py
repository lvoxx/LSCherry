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


class ShaderNodeNamed_Properties(ShaderNode):
    bl_idname = 'ShaderNodeNamed_Properties'
    bl_label = "Named Properties"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Named Properties'

        # Create output sockets
        nt.interface.new_socket('Main Light Vector', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Back Light Vector', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Fx', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Fy', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Toon Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets

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

        Attribute_001 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_001.location = (0.0, -123.15982055664062)
        Attribute_001.name = "Attribute.001"

        Attribute_002 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_002.location = (0.0, 22.36132049560547)
        Attribute_002.name = "Attribute.002"

        Attribute_003 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_003.location = (0.0, -13.008338928222656)
        Attribute_003.name = "Attribute.003"

        Attribute_004 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_004.location = (0.0, -49.85173797607422)
        Attribute_004.name = "Attribute.004"

        Attribute_005 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_005.location = (0.0, -85.90742492675781)
        Attribute_005.name = "Attribute.005"

        # Create internal links
        nt.links.new(Attribute_002.outputs[1], GroupOutput.inputs[0])
        nt.links.new(Attribute_003.outputs[1], GroupOutput.inputs[1])
        nt.links.new(Attribute_004.outputs[1], GroupOutput.inputs[2])
        nt.links.new(Attribute_005.outputs[1], GroupOutput.inputs[3])
        nt.links.new(Attribute_001.outputs[1], GroupOutput.inputs[4])

        # Set default values

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
