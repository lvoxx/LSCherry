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


class ShaderNodeSimple_Pantyhose_Type_1(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Pantyhose_Type_1'
    bl_label = "Simple Pantyhose Type 1"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Combined"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Color"].default_value = (0.5, 0.5, 0.5, 1.0)
        self.inputs["Factor"].default_value = 1.0
        self.inputs["Scale"].default_value = 50.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Pantyhose Type 1'

        # Create output sockets
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Pattern', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.5, 0.5, 0.5, 1.0)
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 50.0

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

        Brick_Texture = nt.nodes.new('ShaderNodeTexBrick')
        Brick_Texture.location = (0.9044647216796875, 217.58111572265625)
        Brick_Texture.name = "Brick Texture"

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (230.46725463867188, 70.99293518066406)
        Invert_Color.name = "Invert Color"

        Invert_Color_001 = nt.nodes.new('ShaderNodeInvert')
        Invert_Color_001.location = (230.46725463867188, -119.0087890625)
        Invert_Color_001.name = "Invert Color.001"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-215.34666442871094, 145.64297485351562)
        Mapping.name = "Mapping"

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-234.94956970214844, -182.9010467529297)
        Geometry.name = "Geometry"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-239.86407470703125, -262.2213134765625)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (0.8156051635742188, -169.9659881591797)
        Voronoi_Texture.name = "Voronoi Texture"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (450.9528503417969, 96.89138793945312)
        Mix.name = "Mix"
        Mix.blend_type = 'SUBTRACT'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (1267.336669921875, 581.9349975585938)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MULTIPLY'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1081.6785888671875, 391.4034729003906)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Color_Ramp = nt.nodes.new('ShaderNodeValToRGB')
        Color_Ramp.location = (656.121826171875, 154.5895538330078)
        Color_Ramp.name = "Color Ramp"

        # Create internal links
        nt.links.new(Brick_Texture.outputs[1], Invert_Color.inputs[1])
        nt.links.new(Invert_Color_001.outputs[0], Mix.inputs[7])
        nt.links.new(Invert_Color.outputs[0], Mix.inputs[6])
        nt.links.new(Geometry.outputs[4], Voronoi_Texture.inputs[0])
        nt.links.new(Voronoi_Texture.outputs[0], Invert_Color_001.inputs[1])
        nt.links.new(Mapping.outputs[0], Brick_Texture.inputs[0])
        nt.links.new(Mix_002.outputs[2], Mix_001.inputs[7])
        nt.links.new(Math.outputs[0], Voronoi_Texture.inputs[2])
        nt.links.new(Mix.outputs[2], Color_Ramp.inputs[0])
        nt.links.new(Color_Ramp.outputs[0], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[0], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[4], Math.inputs[0])
        nt.links.new(GroupInput.outputs[4], Brick_Texture.inputs[4])
        nt.links.new(Color_Ramp.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix_002.inputs[7])
        nt.links.new(GroupInput.outputs[1], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[3], Mix_001.inputs[0])

        # Set default values
        Brick_Texture.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
        Brick_Texture.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
        Brick_Texture.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
        Brick_Texture.inputs[5].default_value = 0.10000000149011612
        Brick_Texture.inputs[6].default_value = 1.0
        Brick_Texture.inputs[7].default_value = 0.0
        Brick_Texture.inputs[8].default_value = 0.30000001192092896
        Brick_Texture.inputs[9].default_value = 0.10000000149011612
        Invert_Color.inputs[0].default_value = 1.0
        Invert_Color_001.inputs[0].default_value = 0.0
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mapping.inputs[3].default_value = Vector((1.0, 1.0, 1.0))
        Math.inputs[1].default_value = 3.0
        Math.inputs[2].default_value = 0.5
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[3].default_value = 0.0
        Voronoi_Texture.inputs[4].default_value = 0.5
        Voronoi_Texture.inputs[5].default_value = 2.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Voronoi_Texture.inputs[8].default_value = 0.0
        Mix.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
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

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
