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


class ShaderNodeAVR__Metal_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeAVR__Metal_Ramp'
    bl_label = "AVR: Metal Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Use Dot"].default_value = False
        self.inputs["Roughness"].default_value = 0.3919999897480011
        self.inputs["Scale"].default_value = 4.010000228881836
        self.inputs["Distortion"].default_value = 1.0
        self.inputs["Value Enhance"].default_value = 0.10000000149011612
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'AVR: Metal Ramp'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Use Dot', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.3919999897480011
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 4.010000228881836
        input_socket = nt.interface.new_socket('Distortion', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Value Enhance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
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

        Texture_Coordinate = nt.nodes.new('ShaderNodeTexCoord')
        Texture_Coordinate.location = (-59.0645751953125, -107.30476379394531)
        Texture_Coordinate.name = "Texture Coordinate"

        Vector_Transform = nt.nodes.new('ShaderNodeVectorTransform')
        Vector_Transform.location = (-58.850982666015625, -139.39349365234375)
        Vector_Transform.name = "Vector Transform"
        Vector_Transform.convert_to = 'CAMERA'

        Magic_Texture = nt.nodes.new('ShaderNodeTexMagic')
        Magic_Texture.location = (128.21871948242188, -97.2367935180664)
        Magic_Texture.name = "Magic Texture"

        Brightness_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Brightness_Contrast.location = (315.77288818359375, -107.52403259277344)
        Brightness_Contrast.name = "Brightness/Contrast"

        RGB = nt.nodes.new('ShaderNodeRGB')
        RGB.location = (311.60113525390625, 87.25995635986328)
        RGB.name = "RGB"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (505.5378723144531, 27.774192810058594)
        Mix.name = "Mix"
        Mix.blend_type = 'LINEAR_LIGHT'

        Glossy_BSDF = nt.nodes.new('ShaderNodeBsdfAnisotropic')
        Glossy_BSDF.location = (785.1636962890625, 134.77391052246094)
        Glossy_BSDF.name = "Glossy BSDF"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (500.9324035644531, -219.11923217773438)
        Group.name = "Group"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (313.784423828125, -243.6303253173828)
        Attribute.name = "Attribute"

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (985.3834228515625, 114.62686157226562)
        Shader_to_RGB.name = "Shader to RGB"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (1180.79248046875, 147.2022247314453)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (785.7068481445312, -96.95433044433594)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (67.48004150390625, -414.9092102050781)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (312.6501159667969, -360.6098327636719)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Normal_Map = nt.nodes.new('ShaderNodeNormalMap')
        Normal_Map.location = (65.7913818359375, -453.1343688964844)
        Normal_Map.name = "Normal Map"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (1184.102294921875, -86.27543640136719)
        Mix_Shader.name = "Mix Shader"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (1361.0, 209.443115234375)
        Math_001.name = "Math.001"
        Math_001.operation = 'ADD'

        # Create internal links
        nt.links.new(Vector_Transform.outputs[0], Magic_Texture.inputs[0])
        nt.links.new(Texture_Coordinate.outputs[1], Vector_Transform.inputs[0])
        nt.links.new(RGB.outputs[0], Mix.inputs[6])
        nt.links.new(Brightness_Contrast.outputs[0], Mix.inputs[7])
        nt.links.new(Mix.outputs[2], Glossy_BSDF.inputs[0])
        nt.links.new(Attribute.outputs[1], Group.inputs[0])
        nt.links.new(Glossy_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Shader_to_RGB.outputs[0], Mix_001.inputs[6])
        nt.links.new(Math_001.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Mix_002.outputs[2], Mix_001.inputs[7])
        nt.links.new(Group.outputs[0], Mix_002.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_002.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[5], Glossy_BSDF.inputs[4])
        nt.links.new(GroupInput.outputs[5], Math.inputs[0])
        nt.links.new(Math.outputs[0], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[5], Mix_003.inputs[5])
        nt.links.new(Normal_Map.outputs[0], Mix_003.inputs[4])
        nt.links.new(Mix_003.outputs[1], Group.inputs[1])
        nt.links.new(GroupInput.outputs[2], Magic_Texture.inputs[1])
        nt.links.new(GroupInput.outputs[3], Magic_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[1], Glossy_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[0], Mix_Shader.inputs[0])
        nt.links.new(Glossy_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Mix_002.outputs[2], Mix_Shader.inputs[2])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Magic_Texture.outputs[1], Brightness_Contrast.inputs[0])
        nt.links.new(Mix_001.outputs[2], Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[4], Math_001.inputs[1])

        # Set default values
        Brightness_Contrast.inputs[1].default_value = 0.0
        Brightness_Contrast.inputs[2].default_value = 2.0
        Mix.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Glossy_BSDF.inputs[2].default_value = 0.0
        Glossy_BSDF.inputs[3].default_value = 0.0
        Glossy_BSDF.inputs[5].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs[6].default_value = 0.0
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
        Math.inputs[1].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Normal_Map.inputs[0].default_value = 1.0
        Normal_Map.inputs[1].default_value = (0.5, 0.5, 1.0, 1.0)
        Math_001.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
