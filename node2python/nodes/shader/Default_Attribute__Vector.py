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


class ShaderNodeDefault_Attribute__Vector(ShaderNode):
    bl_idname = 'ShaderNodeDefault_Attribute__Vector'
    bl_label = "Default Attribute: Vector"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Default"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Default Attribute: Vector'

        # Create output sockets
        nt.interface.new_socket('Result', in_out='OUTPUT', socket_type='NodeSocketVector')
        nt.interface.new_socket('Compare', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('Vector', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Default', in_out='INPUT', socket_type='NodeSocketVector')
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

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-118.84967803955078, -131.5231475830078)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (105.66834259033203, -142.41546630859375)
        Math.name = "Math"
        Math.operation = 'COMPARE'

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-391.99237060546875, -56.42120361328125)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'LENGTH'

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-389.460693359375, -90.3770523071289)
        Group.name = "Group"

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (-118.77096557617188, -217.74578857421875)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'LENGTH'

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (-118.77096557617188, -253.0888671875)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'LENGTH'

        # Create internal links
        nt.links.new(GroupInput.outputs[1], Mix.inputs[2])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[3])
        nt.links.new(Math.outputs[0], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[0], Vector_Math.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix.inputs[5])
        nt.links.new(GroupInput.outputs[1], Mix.inputs[4])
        nt.links.new(Vector_Math.outputs[1], Group.inputs[0])
        nt.links.new(Group.outputs[0], Mix.inputs[0])
        nt.links.new(Vector_Math_001.outputs[1], Math.inputs[0])
        nt.links.new(GroupInput.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Vector_Math_002.inputs[0])
        nt.links.new(Vector_Math_002.outputs[1], Math.inputs[1])
        nt.links.new(Mix.outputs[1], GroupOutput.inputs[0])

        # Set default values
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.0
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Group.inputs[1].default_value = 0.0
        Vector_Math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Vector_Math_002.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[3].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
