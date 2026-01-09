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


class ShaderNodeSimple_Back_Toon_Dot(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Back_Toon_Dot'
    bl_label = "Simple Back Toon Dot"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Back Toon Dot'

        # Create output sockets
        nt.interface.new_socket('NdotL', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
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

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (-126.9410400390625, 152.14682006835938)
        Attribute.name = "Attribute"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (90.24742889404297, 34.880393981933594)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Group_003 = nt.nodes.new('ShaderNodeGroup')
        Group_003.location = (262.8182067871094, 262.01055908203125)
        Group_003.name = "Group.003"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-291.5524597167969, -49.616004943847656)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'DISTANCE'

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-104.94308471679688, 2.429431915283203)
        Geometry.name = "Geometry"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-103.17842102050781, -56.677162170410156)
        Math_001.name = "Math.001"
        Math_001.operation = 'GREATER_THAN'

        # Create internal links
        nt.links.new(Mix.outputs[1], Group_003.inputs[3])
        nt.links.new(Attribute.outputs[1], Group_003.inputs[1])
        nt.links.new(Group_003.outputs[1], GroupOutput.inputs[0])
        nt.links.new(Vector_Math.outputs[1], Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Geometry.outputs[1], Mix.inputs[4])
        nt.links.new(Math_001.outputs[0], Mix.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[5])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_003.inputs[0].default_value = False
        Group_003.inputs[2].default_value = 0.0
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Math_001.inputs[1].default_value = 0.0
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
