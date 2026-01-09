import bpy
from ..utils import ShaderNode


class ShaderNodeBackgroundColor(ShaderNode):
    bl_label = "Background Color"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Base_socket = nt.interface.new_socket(
                name="Base",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            Stylized_socket = nt.interface.new_socket(
                name="Stylized",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Stylized_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1049.002197265625, -55.269412994384766)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-444.8787841796875, -5.085439682006836)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-135.0023193359375, 147.5073699951172)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-592.207763671875, -77.2547836303711)
        Combine_XYZ.inputs["X"].default_value = 0.0
        Combine_XYZ.inputs["Y"].default_value = 0.0
        Combine_XYZ.inputs["Z"].default_value = 1.0
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (-592.207763671875, -220.91233825683594)
        Combine_XYZ_001.inputs["X"].default_value = 0.0
        Combine_XYZ_001.inputs["Y"].default_value = 0.0
        Combine_XYZ_001.inputs["Z"].default_value = -1.0
        Diffuse_BSDF = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF.location = (-397.21221923828125, -71.87067413330078)
        Diffuse_BSDF.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF.inputs["Weight"].default_value = 0.0
        Diffuse_BSDF_001 = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF_001.location = (-397.21221923828125, -212.16127014160156)
        Diffuse_BSDF_001.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Diffuse_BSDF_001.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF_001.inputs["Weight"].default_value = 0.0
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (-208.99351501464844, -84.22755432128906)
        Shader_to_RGB_001 = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB_001.location = (-208.99351501464844, -224.5181884765625)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-27.5794677734375, -126.18666076660156)
        Separate_Color_001 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color_001.location = (-27.5794677734375, -231.56495666503906)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (179.62258911132812, -101.06237030029297)
        Math.operation = "MINIMUM"
        Math.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (179.62258911132812, -143.71072387695312)
        Math_001.operation = "MINIMUM"
        Math_001.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (179.62258911132812, -188.60374450683594)
        Math_002.operation = "MINIMUM"
        Math_002.inputs["Value"].default_value = 0.5
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (361.7730407714844, -52.476741790771484)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (605.2196044921875, -276.1846008300781)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.0
        Map_Range.inputs["From Max"].default_value = 1.0
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.5
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (605.2196044921875, -532.6231689453125)
        Math_003.operation = "MINIMUM"
        Math_003.inputs["Value"].default_value = 0.9200000166893005
        Math_003.inputs["Value"].default_value = 0.5
        Separate_Color_002 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color_002.location = (355.5788879394531, -220.2870330810547)
        Combine_Color_001 = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color_001.location = (875.0000610351562, -174.893798828125)
        # Create links
        nt.links.new(Combine_XYZ.outputs["Vector"], Diffuse_BSDF.inputs["Normal"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Diffuse_BSDF_001.inputs["Normal"])
        nt.links.new(Diffuse_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Diffuse_BSDF_001.outputs["BSDF"], Shader_to_RGB_001.inputs["Shader"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Separate_Color.inputs["Color"])
        nt.links.new(Shader_to_RGB_001.outputs["Color"], Separate_Color_001.inputs["Color"])
        nt.links.new(Separate_Color.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Green"], Math_001.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Green"], Math_001.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_002.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Blue"], Math_002.inputs["Value"])
        nt.links.new(Combine_Color.outputs["Color"], Group_Output.inputs["Base"])
        nt.links.new(Math.outputs["Value"], Combine_Color.inputs["Red"])
        nt.links.new(Math_001.outputs["Value"], Combine_Color.inputs["Green"])
        nt.links.new(Math_002.outputs["Value"], Combine_Color.inputs["Blue"])
        nt.links.new(Combine_Color.outputs["Color"], Separate_Color_002.inputs["Color"])
        nt.links.new(Separate_Color_002.outputs["Green"], Map_Range.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Combine_Color_001.inputs["Green"])
        nt.links.new(Separate_Color_002.outputs["Red"], Combine_Color_001.inputs["Red"])
        nt.links.new(Separate_Color_002.outputs["Blue"], Math_003.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Combine_Color_001.inputs["Blue"])
        nt.links.new(Combine_Color_001.outputs["Color"], Group_Output.inputs["Stylized"])