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


class ShaderNodeMMD__MatCapUV(ShaderNode):
    bl_idname = 'ShaderNodeMMD__MatCapUV'
    bl_label = "MMD: MatCapUV"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'MMD: MatCapUV'

        # Create output sockets
        nt.interface.new_socket('ToonUV', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('SphereUV', in_out='OUTPUT', socket_type='NodeSocketVector')

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

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (-175.29501342773438, 1.52587890625e-05)
        Texture_Coordinate.name = "Texture Coordinate"

        Vector_Transform = nt.nodes.new('ShaderNodeVectorTransform')
        Vector_Transform.location = (-8.140594482421875, -5.4357452392578125)
        Vector_Transform.name = "Vector Transform"
        Vector_Transform.convert_to = 'CAMERA'

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (175.2949981689453, 5.4357452392578125)
        Mapping.name = "Mapping"

        # Create internal links
        nt.links.new(Vector_Transform.outputs[0], Mapping.inputs[0])
        nt.links.new(Texture_Coordinate.outputs[1], Vector_Transform.inputs[0])
        nt.links.new(Mapping.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Mapping.outputs[0], GroupOutput.inputs[1])

        # Set default values
        Mapping.inputs[1].default_value = Vector((0.5, 0.5, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping.inputs[3].default_value = Vector((0.5, 0.5, 1.0))

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
