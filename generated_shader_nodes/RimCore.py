import bpy
from ..utils import ShaderNode


class ShaderNodeRimCore(ShaderNode):
    bl_label = "Rim Core"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Rim_socket = nt.interface.new_socket(
                name="Rim",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Rim_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Rim_Strength_socket = nt.interface.new_socket(
                name="Rim Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Rim_Strength_socket.default_value = 0.0
        Rim_Strength_socket.min_value = 0.0
        Rim_Strength_socket.max_value = 10.0
        Rim_Strength_socket.subtype = "NONE"
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.0
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Glossy_BSDF = nt.nodes.new("ShaderNodeBsdfAnisotropic")
        Glossy_BSDF.location = (-2.3977508544921875, 12.53759765625)
        Glossy_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Glossy_BSDF.inputs["Anisotropy"].default_value = 0.0
        Glossy_BSDF.inputs["Rotation"].default_value = 0.0
        Glossy_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs["Weight"].default_value = 0.0
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-192.8369140625, 46.86745834350586)
        Math_001.operation = "ADD"
        Math_001.inputs["Value"].default_value = 0.5
        Math_001.inputs["Value"].default_value = 0.5
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (196.9232177734375, -12.537567138671875)
        Bright/Contrast = nt.nodes.new("ShaderNodeBrightContrast")
        Bright/Contrast.location = (417.0, 1.7748947143554688)
        Bright/Contrast.inputs["Contrast"].default_value = 0.0
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (636.95166015625, 5.522380352020264)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-576.7027587890625, -171.70443725585938)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-49.94342041015625, 155.17494201660156)
        # Create links
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Math_001.outputs["Value"], Glossy_BSDF.inputs["Roughness"])
        nt.links.new(Bright/Contrast.outputs["Color"], Group_Output.inputs["Rim"])
        nt.links.new(Group_Input.outputs["Roughness"], Math_001.inputs["Value"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Bright/Contrast.inputs["Color"])
        nt.links.new(Group_Input.outputs["Rim Strength"], Bright/Contrast.inputs["Bright"])
        nt.links.new(Group_Input.outputs["Normal"], Glossy_BSDF.inputs["Normal"])