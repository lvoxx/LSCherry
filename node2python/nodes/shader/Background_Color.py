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


class ShaderNodeBackground_Color(ShaderNode):
    bl_idname = 'ShaderNodeBackground_Color'
    bl_label = "Background Color"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Background Color'

        # Create output sockets
        nt.interface.new_socket('Base', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Stylized', in_out='OUTPUT', socket_type='NodeSocketColor')

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

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-592.207763671875, -77.2547836303711)
        Combine_XYZ.name = "Combine XYZ"

        Combine_XYZ_001 = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ_001.location = (-592.207763671875, -220.91233825683594)
        Combine_XYZ_001.name = "Combine XYZ.001"

        Diffuse_BSDF = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF.location = (-397.21221923828125, -71.87067413330078)
        Diffuse_BSDF.name = "Diffuse BSDF"

        Diffuse_BSDF_001 = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF_001.location = (-397.21221923828125, -212.16127014160156)
        Diffuse_BSDF_001.name = "Diffuse BSDF.001"

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (-208.99351501464844, -84.22755432128906)
        Shader_to_RGB.name = "Shader to RGB"

        Shader_to_RGB_001 = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB_001.location = (-208.99351501464844, -224.5181884765625)
        Shader_to_RGB_001.name = "Shader to RGB.001"

        Separate_Color = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color.location = (-27.5794677734375, -126.18666076660156)
        Separate_Color.name = "Separate Color"

        Separate_Color_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_001.location = (-27.5794677734375, -231.56495666503906)
        Separate_Color_001.name = "Separate Color.001"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (179.62258911132812, -101.06237030029297)
        Math.name = "Math"
        Math.operation = 'MINIMUM'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (179.62258911132812, -143.71072387695312)
        Math_001.name = "Math.001"
        Math_001.operation = 'MINIMUM'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (179.62258911132812, -188.60374450683594)
        Math_002.name = "Math.002"
        Math_002.operation = 'MINIMUM'

        Combine_Color = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color.location = (361.7730407714844, -52.476741790771484)
        Combine_Color.name = "Combine Color"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (605.2196044921875, -276.1846008300781)
        Map_Range.name = "Map Range"

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (605.2196044921875, -532.6231689453125)
        Math_003.name = "Math.003"
        Math_003.operation = 'MINIMUM'

        Separate_Color_002 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_Color_002.location = (355.5788879394531, -220.2870330810547)
        Separate_Color_002.name = "Separate Color.002"

        Combine_Color_001 = nt.nodes.new('ShaderNodeCombineColor')
        Combine_Color_001.location = (875.0000610351562, -174.893798828125)
        Combine_Color_001.name = "Combine Color.001"

        # Create internal links
        nt.links.new(Combine_XYZ.outputs[0], Diffuse_BSDF.inputs[2])
        nt.links.new(Combine_XYZ_001.outputs[0], Diffuse_BSDF_001.inputs[2])
        nt.links.new(Diffuse_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Diffuse_BSDF_001.outputs[0], Shader_to_RGB_001.inputs[0])
        nt.links.new(Shader_to_RGB.outputs[0], Separate_Color.inputs[0])
        nt.links.new(Shader_to_RGB_001.outputs[0], Separate_Color_001.inputs[0])
        nt.links.new(Separate_Color.outputs[0], Math.inputs[0])
        nt.links.new(Separate_Color_001.outputs[0], Math.inputs[1])
        nt.links.new(Separate_Color.outputs[1], Math_001.inputs[0])
        nt.links.new(Separate_Color_001.outputs[1], Math_001.inputs[1])
        nt.links.new(Separate_Color.outputs[2], Math_002.inputs[0])
        nt.links.new(Separate_Color_001.outputs[2], Math_002.inputs[1])
        nt.links.new(Combine_Color.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Math.outputs[0], Combine_Color.inputs[0])
        nt.links.new(Math_001.outputs[0], Combine_Color.inputs[1])
        nt.links.new(Math_002.outputs[0], Combine_Color.inputs[2])
        nt.links.new(Combine_Color.outputs[0], Separate_Color_002.inputs[0])
        nt.links.new(Separate_Color_002.outputs[1], Map_Range.inputs[0])
        nt.links.new(Map_Range.outputs[0], Combine_Color_001.inputs[1])
        nt.links.new(Separate_Color_002.outputs[0], Combine_Color_001.inputs[0])
        nt.links.new(Separate_Color_002.outputs[2], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Combine_Color_001.inputs[2])
        nt.links.new(Combine_Color_001.outputs[0], GroupOutput.inputs[1])

        # Set default values
        Combine_XYZ.inputs[0].default_value = 0.0
        Combine_XYZ.inputs[1].default_value = 0.0
        Combine_XYZ.inputs[2].default_value = 1.0
        Combine_XYZ_001.inputs[0].default_value = 0.0
        Combine_XYZ_001.inputs[1].default_value = 0.0
        Combine_XYZ_001.inputs[2].default_value = -1.0
        Diffuse_BSDF.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF.inputs[1].default_value = 0.0
        Diffuse_BSDF.inputs[3].default_value = 0.0
        Diffuse_BSDF_001.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF_001.inputs[1].default_value = 0.0
        Diffuse_BSDF_001.inputs[3].default_value = 0.0
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[2].default_value = 0.5
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.5
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Math_003.inputs[1].default_value = 0.9200000166893005
        Math_003.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
