import bpy
from ..utils import ShaderNode


class ShaderNodeToonray(ShaderNode):
    bl_label = "ToonRay"
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
        
        Roughness_socket.default_value = 0.0
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
        Group_Output.location = (309.0787353515625, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-319.0787048339844, 0.0)
        Diffuse_BSDF = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF.location = (-119.07870483398438, 67.40975952148438)
        Diffuse_BSDF.inputs["Weight"].default_value = 0.0
        Toon_BSDF = nt.nodes.new("ShaderNodeBsdfToon")
        Toon_BSDF.location = (-119.07870483398438, -67.40974426269531)
        Toon_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (121.82398986816406, 10.719467163085938)
        Mix_Shader.inputs["Fac"].default_value = 0.800000011920929
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-91.19808959960938, 225.47369384765625)
        # Create links
        nt.links.new(Toon_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Roughness"], Diffuse_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Color"], Diffuse_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Toon_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Size"], Toon_BSDF.inputs["Size"])
        nt.links.new(Group_Input.outputs["Smooth"], Toon_BSDF.inputs["Smooth"])
        nt.links.new(Group_Input.outputs["Normal"], Diffuse_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Toon_BSDF.inputs["Normal"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Diffuse_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])