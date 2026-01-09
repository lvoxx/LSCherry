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


class ShaderNodeSimple_Pantyhose(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Pantyhose'
    bl_label = "Simple Pantyhose"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Enable Dot"].default_value = False
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Base Color"].default_value = (0.685835599899292, 0.685835599899292, 0.685835599899292, 1.0)
        self.inputs["Highlight Color"].default_value = (1.0, 0.6242283582687378, 0.5513602495193481, 1.0)
        self.inputs["Size"].default_value = 8.0
        self.inputs["Roughness"].default_value = 0.20000000298023224

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Pantyhose'

        # Create output sockets
        nt.interface.new_socket('Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Pattern', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        nt.interface.new_socket('-- DEPRECATED --', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Enable Dot', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.685835599899292, 0.685835599899292, 0.685835599899292, 1.0)
        input_socket = nt.interface.new_socket('Highlight Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.6242283582687378, 0.5513602495193481, 1.0)
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 8.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.20000000298023224

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

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (-283.23663330078125, 318.64459228515625)
        Voronoi_Texture.name = "Voronoi Texture"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-561.6070556640625, 323.682861328125)
        Mapping.name = "Mapping"

        Voronoi_Texture_001 = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture_001.location = (-283.23663330078125, -51.00897216796875)
        Voronoi_Texture_001.name = "Voronoi Texture.001"

        Mapping_001 = nt.nodes.new('ShaderNodeMapping')
        Mapping_001.location = (-561.6070556640625, -25.392303466796875)
        Mapping_001.name = "Mapping.001"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (10.09716796875, 253.45834350585938)
        Mix.name = "Mix"
        Mix.blend_type = 'DARKEN'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-980.0739135742188, -105.99383544921875)
        Math.name = "Math"
        Math.operation = 'MULTIPLY'

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-779.8394775390625, -30.49593734741211)
        Combine_XYZ.name = "Combine XYZ"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-559.0631103515625, -323.682861328125)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Color_Ramp = nt.nodes.new('ShaderNodeValToRGB')
        Color_Ramp.location = (226.18603515625, 246.9811248779297)
        Color_Ramp.name = "Color Ramp"

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (556.9907836914062, 241.77159118652344)
        Bump.name = "Bump"

        Specular_BSDF = nt.nodes.new('ShaderNodeEeveeSpecular')
        Specular_BSDF.location = (792.5206909179688, 317.7504577636719)
        Specular_BSDF.name = "Specular BSDF"

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (980.0739135742188, 297.0311584472656)
        Shader_to_RGB.name = "Shader to RGB"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (1282.4886474609375, -20.238998413085938)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'DODGE'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (756.4066772460938, 380.5945129394531)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (1478.68359375, 380.5945129394531)
        Reroute_001.name = "Reroute.001"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-182.685546875, 457.8871765136719)
        Frame.label = "Deprecated: Use Simple Pantyhose Type 2 instead"
        Frame.name = "Frame"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (798.9196166992188, 18.010482788085938)
        Group.name = "Group"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (600.055419921875, -7.453155517578125)
        Attribute.name = "Attribute"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (1282.4886474609375, 216.66436767578125)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (993.73095703125, 20.206893920898438)
        Math_002.name = "Math.002"
        Math_002.operation = 'ADD'

        # Create internal links
        nt.links.new(Mapping_001.outputs[0], Voronoi_Texture_001.inputs[0])
        nt.links.new(Bump.outputs[0], Specular_BSDF.inputs[5])
        nt.links.new(Math_001.outputs[0], Voronoi_Texture_001.inputs[2])
        nt.links.new(Math.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(Specular_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Math.outputs[0], Math_001.inputs[0])
        nt.links.new(Color_Ramp.outputs[0], Bump.inputs[2])
        nt.links.new(Combine_XYZ.outputs[0], Mapping_001.inputs[3])
        nt.links.new(Voronoi_Texture_001.outputs[0], Mix.inputs[7])
        nt.links.new(Combine_XYZ.outputs[0], Mapping.inputs[3])
        nt.links.new(Mix.outputs[2], Color_Ramp.inputs[0])
        nt.links.new(Voronoi_Texture.outputs[0], Mix.inputs[6])
        nt.links.new(Mapping.outputs[0], Voronoi_Texture.inputs[0])
        nt.links.new(Math_001.outputs[0], Voronoi_Texture.inputs[2])
        nt.links.new(GroupInput.outputs[2], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mapping_001.inputs[0])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[5], Math.inputs[0])
        nt.links.new(Shader_to_RGB.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Mix_001.inputs[6])
        nt.links.new(GroupInput.outputs[4], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[6], Specular_BSDF.inputs[2])
        nt.links.new(Bump.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], GroupOutput.inputs[2])
        nt.links.new(Attribute.outputs[2], Group.inputs[0])
        nt.links.new(Bump.outputs[0], Group.inputs[1])
        nt.links.new(GroupInput.outputs[1], Mix_002.inputs[0])
        nt.links.new(Math_002.outputs[0], Mix_002.inputs[7])
        nt.links.new(Shader_to_RGB.outputs[0], Mix_002.inputs[6])
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[1])
        nt.links.new(Group.outputs[0], Math_002.inputs[0])

        # Set default values
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[3].default_value = 0.0
        Voronoi_Texture.inputs[4].default_value = 0.5
        Voronoi_Texture.inputs[5].default_value = 2.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Voronoi_Texture.inputs[8].default_value = 1.0
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Voronoi_Texture_001.inputs[1].default_value = 0.0
        Voronoi_Texture_001.inputs[3].default_value = 0.0
        Voronoi_Texture_001.inputs[4].default_value = 0.5
        Voronoi_Texture_001.inputs[5].default_value = 2.0
        Voronoi_Texture_001.inputs[6].default_value = 1.0
        Voronoi_Texture_001.inputs[7].default_value = 0.5
        Voronoi_Texture_001.inputs[8].default_value = 1.0
        Mapping_001.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_001.inputs[2].default_value = Euler((0.0, 0.0, 1.5707963705062866), 'XYZ')
        Mix.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 10.0
        Math.inputs[2].default_value = 0.5
        Combine_XYZ.inputs[1].default_value = 1.0
        Combine_XYZ.inputs[2].default_value = 1.0
        Math_001.inputs[1].default_value = 100.0
        Math_001.inputs[2].default_value = 0.5
        Bump.inputs[0].default_value = 0.25
        Bump.inputs[1].default_value = 1.0
        Bump.inputs[3].default_value = (0.0, 0.0, 0.0)
        Specular_BSDF.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
        Specular_BSDF.inputs[1].default_value = (0.14003700017929077, 0.14003700017929077, 0.14003700017929077, 1.0)
        Specular_BSDF.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
        Specular_BSDF.inputs[4].default_value = 0.0
        Specular_BSDF.inputs[6].default_value = 0.0
        Specular_BSDF.inputs[7].default_value = 0.0
        Specular_BSDF.inputs[8].default_value = (0.0, 0.0, 0.0)
        Specular_BSDF.inputs[9].default_value = 0.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math_002.inputs[1].default_value = 0.10000000149011612
        Math_002.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
