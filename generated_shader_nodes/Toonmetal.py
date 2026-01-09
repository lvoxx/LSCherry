import bpy
from ..utils import ShaderNode


class ShaderNodeToonmetal(ShaderNode):
    bl_label = "ToonMetal"
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
            Edge_Tint_socket = nt.interface.new_socket(
                name="Edge Tint",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Edge_Tint_socket.default_value = (0.7699999809265137, 0.7699999809265137, 0.7699999809265137, 1.0)
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
            Tangent_socket = nt.interface.new_socket(
                name="Tangent",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Tangent_socket.default_value = (0.0, 0.0, 0.0)
        Tangent_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (369.73284912109375, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-564.6365966796875, -38.57564163208008)
        Toon_BSDF = nt.nodes.new("ShaderNodeBsdfToon")
        Toon_BSDF.location = (-87.8956298828125, -133.12738037109375)
        Toon_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (179.73284912109375, -24.94872283935547)
        Mix_Shader.inputs["Fac"].default_value = 0.800000011920929
        Metallic_BSDF = nt.nodes.new("ShaderNodeBsdfMetallic")
        Metallic_BSDF.location = (-179.73287963867188, 133.12738037109375)
        Metallic_BSDF.inputs["IOR"].default_value = (2.756999969482422, 2.513000011444092, 2.2309999465942383)
        Metallic_BSDF.inputs["Extinction"].default_value = (3.867000102996826, 3.4040000438690186, 3.009000062942505)
        Metallic_BSDF.inputs["Anisotropy"].default_value = 0.0
        Metallic_BSDF.inputs["Rotation"].default_value = 0.0
        Metallic_BSDF.inputs["Weight"].default_value = 0.0
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-158.30242919921875, 268.9317626953125)
        # Create links
        nt.links.new(Toon_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Metallic_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Color"], Toon_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Metallic_BSDF.inputs["Base Color"])
        nt.links.new(Group_Input.outputs["Edge Tint"], Metallic_BSDF.inputs["Edge Tint"])
        nt.links.new(Group_Input.outputs["Roughness"], Metallic_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Size"], Toon_BSDF.inputs["Size"])
        nt.links.new(Group_Input.outputs["Smooth"], Toon_BSDF.inputs["Smooth"])
        nt.links.new(Group_Input.outputs["Normal"], Metallic_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Toon_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Tangent"], Metallic_BSDF.inputs["Tangent"])