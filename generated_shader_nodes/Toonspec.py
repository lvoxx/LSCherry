import bpy
from ..utils import ShaderNode


class ShaderNodeToonspec(ShaderNode):
    bl_label = "ToonSpec"
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
            Tangent_socket = nt.interface.new_socket(
                name="Tangent",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Tangent_socket.default_value = (0.0, 0.0, 0.0)
        Tangent_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (331.1458740234375, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-773.8687744140625, -9.363410949707031)
        Glossy_BSDF = nt.nodes.new("ShaderNodeBsdfAnisotropic")
        Glossy_BSDF.location = (-141.14588928222656, 112.11140441894531)
        Glossy_BSDF.inputs["Anisotropy"].default_value = 0.0
        Glossy_BSDF.inputs["Rotation"].default_value = 0.0
        Glossy_BSDF.inputs["Weight"].default_value = 0.0
        Toon_BSDF = nt.nodes.new("ShaderNodeBsdfToon")
        Toon_BSDF.location = (-141.14588928222656, -112.11140441894531)
        Toon_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (103.6272201538086, 23.878311157226562)
        Mix_Shader.inputs["Fac"].default_value = 0.800000011920929
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-583.9517822265625, -143.54417419433594)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.3330000042915344
        Math.inputs["Value"].default_value = 0.5
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (-365.0149230957031, -187.68978881835938)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.0
        Map_Range.inputs["From Max"].default_value = 1.3300000429153442
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-277.71685791015625, 237.98529052734375)
        # Create links
        nt.links.new(Toon_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Color"], Glossy_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Toon_BSDF.inputs["Color"])
        nt.links.new(Group_Input.outputs["Roughness"], Glossy_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Size"], Math.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Toon_BSDF.inputs["Size"])
        nt.links.new(Group_Input.outputs["Smooth"], Toon_BSDF.inputs["Smooth"])
        nt.links.new(Group_Input.outputs["Normal"], Glossy_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Toon_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Tangent"], Glossy_BSDF.inputs["Tangent"])
        nt.links.new(Math.outputs["Value"], Map_Range.inputs["Value"])
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])