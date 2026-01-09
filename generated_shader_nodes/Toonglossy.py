import bpy
from ..utils import ShaderNode


class ShaderNodeToonglossy(ShaderNode):
    bl_label = "ToonGlossy"
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
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 0.8999999761581421
        Size_socket.min_value = 0.0
        Size_socket.max_value = 1.0
        Size_socket.subtype = "FACTOR"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 0.10000000149011612
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "FACTOR"
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.5
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (331.1458740234375, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-490.26641845703125, -17.383657455444336)
        Toon_BSDF = nt.nodes.new("ShaderNodeBsdfToon")
        Toon_BSDF.location = (-141.1240692138672, -108.997314453125)
        Toon_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (126.50444030761719, -0.8186416625976562)
        Mix_Shader.inputs["Fac"].default_value = 0.800000011920929
        Glossy_BSDF = nt.nodes.new("ShaderNodeBsdfAnisotropic")
        Glossy_BSDF.location = (-138.9541015625, 108.99728393554688)
        Glossy_BSDF.inputs["Anisotropy"].default_value = 0.0
        Glossy_BSDF.inputs["Rotation"].default_value = 0.0
        Glossy_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs["Weight"].default_value = 0.0
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-228.50509643554688, 315.0162353515625)
        # Create links
        nt.links.new(Group_Input.outputs["Color"], Toon_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Glossy_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Size"], Toon_BSDF.inputs["Size"])
        nt.links.new(Group_Input.outputs["Smooth"], Toon_BSDF.inputs["Smooth"])
        nt.links.new(Group_Input.outputs["Roughness"], Glossy_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Normal"], Toon_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Glossy_BSDF.inputs["Normal"])
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Toon_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])