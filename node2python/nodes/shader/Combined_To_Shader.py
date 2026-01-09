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


class ShaderNodeCombined_To_Shader(ShaderNode):
    bl_idname = 'ShaderNodeCombined_To_Shader'
    bl_label = "Combined To Shader"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Combined"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Alpha"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Combined To Shader'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('To AgX', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Combined', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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

        Light_Path = nt.nodes.new('ShaderNodeLightPath')
        Light_Path.location = (-80.0, -16.71942138671875)
        Light_Path.name = "Light Path"

        Diffuse_BSDF = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF.location = (-82.93646240234375, -78.18234252929688)
        Diffuse_BSDF.name = "Diffuse BSDF"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (1006.1566772460938, -240.0)
        Emission.name = "Emission"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (1206.15673828125, -107.67730712890625)
        Mix_Shader.name = "Mix Shader"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-291.4339599609375, -272.70123291015625)
        Reroute.name = "Reroute"

        Brightness_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Brightness_Contrast.location = (-47.81293487548828, -411.03436279296875)
        Brightness_Contrast.name = "Brightness/Contrast"

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (128.25906372070312, -419.6368713378906)
        Separate_Color.name = "Separate Color"

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (638.796875, -406.7232666015625)
        Combine_Color.name = "Combine Color"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (401.1755065917969, -339.4941711425781)
        Math.name = "Math"
        Math.operation = 'POWER'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (401.1755065917969, -396.31781005859375)
        Math_001.name = "Math.001"
        Math_001.operation = 'POWER'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (401.1755065917969, -455.41436767578125)
        Math_002.name = "Math.002"
        Math_002.operation = 'POWER'

        Value = nt.nodes.new('ShaderNodeValue')
        Value.location = (-52.81246566772461, -539.0415649414062)
        Value.name = "Value"

        Gamma_001 = nt.nodes.new('ShaderNodeGamma')
        Gamma_001.location = (-227.9216766357422, -359.40374755859375)
        Gamma_001.name = "Gamma.001"

        Emission_001 = nt.nodes.new('ShaderNodeEmission')
        Emission_001.location = (1006.1566772460938, -376.60821533203125)
        Emission_001.name = "Emission.001"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (1206.8447265625, -3.847503662109375)
        Transparent_BSDF.name = "Transparent BSDF"

        Mix_Shader_001 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_001.location = (1419.8065185546875, -107.67730712890625)
        Mix_Shader_001.name = "Mix Shader.001"

        Mix_Shader_002 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_002.location = (1419.8065185546875, -259.1390380859375)
        Mix_Shader_002.name = "Mix Shader.002"

        # Create internal links
        nt.links.new(Light_Path.outputs[0], Mix_Shader.inputs[0])
        nt.links.new(Diffuse_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Emission.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Mix_Shader_001.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute.outputs[0], Diffuse_BSDF.inputs[0])
        nt.links.new(Gamma_001.outputs[0], Brightness_Contrast.inputs[0])
        nt.links.new(Brightness_Contrast.outputs[0], Separate_Color.inputs[0])
        nt.links.new(Math.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Math_001.outputs[0], Combine_Color.inputs[1])
        nt.links.new(Math_002.outputs[0], Combine_Color.inputs[2])
        nt.links.new(Separate_Color.outputs[0], Math.inputs[0])
        nt.links.new(Separate_Color.outputs[1], Math_001.inputs[0])
        nt.links.new(Value.outputs[0], Math.inputs[1])
        nt.links.new(Value.outputs[0], Math_002.inputs[1])
        nt.links.new(Value.outputs[0], Math_001.inputs[1])
        nt.links.new(Separate_Color.outputs[2], Math_002.inputs[0])
        nt.links.new(Reroute.outputs[0], Gamma_001.inputs[0])
        nt.links.new(Reroute.outputs[0], Emission.inputs[0])
        nt.links.new(GroupInput.outputs[0], Reroute.inputs[0])
        nt.links.new(Combine_Color.outputs[0], Emission_001.inputs[0])
        nt.links.new(Mix_Shader_002.outputs[0], GroupOutput.inputs[1])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader_001.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], Mix_Shader_001.inputs[2])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader_002.inputs[1])
        nt.links.new(Emission_001.outputs[0], Mix_Shader_002.inputs[2])
        nt.links.new(GroupInput.outputs[1], Mix_Shader_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Mix_Shader_002.inputs[0])

        # Set default values
        Diffuse_BSDF.inputs[1].default_value = 0.0
        Diffuse_BSDF.inputs[2].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF.inputs[3].default_value = 0.0
        Emission.inputs[1].default_value = 1.0
        Emission.inputs[2].default_value = 0.0
        Brightness_Contrast.inputs[1].default_value = 0.0
        Brightness_Contrast.inputs[2].default_value = -0.15000000596046448
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[2].default_value = 0.5
        Gamma_001.inputs[1].default_value = 1.149999976158142
        Emission_001.inputs[1].default_value = 1.0
        Emission_001.inputs[2].default_value = 0.0
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
