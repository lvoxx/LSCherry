import bpy
from ..utils import ShaderNode


class ShaderNodeSpecularCore(ShaderNode):
    bl_label = "Specular Core"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Specular_socket = nt.interface.new_socket(
                name="Specular",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Specular_socket.default_value = 0.0
        Specular_socket.min_value = -3.4028234663852886e+38
        Specular_socket.max_value = 3.4028234663852886e+38
        Specular_socket.subtype = "NONE"

        # Input sockets
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
        Group_Output.location = (386.22210693359375, 55.425628662109375)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-255.95297241210938, 4.76322078704834)
        Glossy_BSDF = nt.nodes.new("ShaderNodeBsdfAnisotropic")
        Glossy_BSDF.location = (-45.0989990234375, 102.41868591308594)
        Glossy_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Glossy_BSDF.inputs["Anisotropy"].default_value = 0.0
        Glossy_BSDF.inputs["Rotation"].default_value = 0.0
        Glossy_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs["Weight"].default_value = 0.0
        Shader_to_RGB_001 = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB_001.location = (201.10281372070312, 21.341293334960938)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-82.29158020019531, 280.3753662109375)
        # Create links
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Shader_to_RGB_001.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Normal"], Glossy_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Roughness"], Glossy_BSDF.inputs["Roughness"])
        nt.links.new(Shader_to_RGB_001.outputs["Color"], Group_Output.inputs["Specular"])