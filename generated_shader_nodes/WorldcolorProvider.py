import bpy
from ..utils import ShaderNode


class ShaderNodeWorldcolorProvider(ShaderNode):
    bl_label = "WorldColor Provider"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Enable_WorldColor_socket = nt.interface.new_socket(
                name="Enable WorldColor",
                in_out="OUTPUT",
                socket_type="NodeSocketInt"
            )
        
        Enable_WorldColor_socket.default_value = 1
        Enable_WorldColor_socket.min_value = 0
        Enable_WorldColor_socket.max_value = 1
        Enable_WorldColor_socket.subtype = "NONE"
            WorldColor_socket = nt.interface.new_socket(
                name="WorldColor",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        WorldColor_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets
            Saturation_socket = nt.interface.new_socket(
                name="Saturation",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Saturation_socket.default_value = 1.2000000476837158
        Saturation_socket.min_value = 0.0
        Saturation_socket.max_value = 2.0
        Saturation_socket.subtype = "NONE"
            Value_socket = nt.interface.new_socket(
                name="Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Value_socket.default_value = 1.5
        Value_socket.min_value = 0.0
        Value_socket.max_value = 2.0
        Value_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (784.05322265625, 230.3676300048828)
        Group_Output.inputs["Enable WorldColor"].default_value = 1
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (173.9503173828125, 176.29747009277344)
        Diffuse_BSDF = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF.location = (84.53228759765625, 63.373985290527344)
        Diffuse_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Diffuse_BSDF.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF.inputs["Weight"].default_value = 0.0
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (284.64068603515625, 54.18236541748047)
        Hue/Saturation/Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value.location = (478.91204833984375, 176.95895385742188)
        Hue/Saturation/Value.inputs["Hue"].default_value = 0.5
        Hue/Saturation/Value.inputs["Fac"].default_value = 1.0
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (439.3619384765625, 375.8868408203125)
        # Create links
        nt.links.new(Diffuse_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Hue/Saturation/Value.outputs["Color"], Group_Output.inputs["WorldColor"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Hue/Saturation/Value.inputs["Color"])
        nt.links.new(Group_Input.outputs["Saturation"], Hue/Saturation/Value.inputs["Saturation"])
        nt.links.new(Group_Input.outputs["Value"], Hue/Saturation/Value.inputs["Value"])