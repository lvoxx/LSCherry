import bpy
from ..utils import ShaderNode


class ShaderNodeReflectiveToon(ShaderNode):
    bl_label = "Reflective Toon"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Shader_socket = nt.interface.new_socket(
                name="Shader",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.0
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Emission_Strength_socket = nt.interface.new_socket(
                name="Emission Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Emission_Strength_socket.default_value = 1.0
        Emission_Strength_socket.min_value = 0.0
        Emission_Strength_socket.max_value = 1000000.0
        Emission_Strength_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (307.1024475097656, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-317.1024169921875, 0.0)
        Glossy_BSDF = nt.nodes.new("ShaderNodeBsdfAnisotropic")
        Glossy_BSDF.location = (-117.1024169921875, 111.15472412109375)
        Glossy_BSDF.inputs["Anisotropy"].default_value = 0.0
        Glossy_BSDF.inputs["Rotation"].default_value = 0.0
        Glossy_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (117.10244750976562, 60.204315185546875)
        Mix_Shader.inputs["Fac"].default_value = 0.10000000149011612
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (-117.1024169921875, -111.15475463867188)
        Emission.inputs["Weight"].default_value = 0.0
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-115.4925537109375, 213.7895965576172)
        # Create links
        nt.links.new(Emission.outputs["Emission"], Mix_Shader.inputs["Shader"])
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Color"], Glossy_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Emission.inputs["Color"])
        nt.links.new(Group_Input.outputs["Roughness"], Glossy_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Emission Strength"], Emission.inputs["Strength"])
        nt.links.new(Group_Input.outputs["Normal"], Glossy_BSDF.inputs["Normal"])