import bpy
from ..utils import ShaderNode


class ShaderNodeBuildStackedToon(ShaderNode):
    bl_label = "Build Stacked Toon"
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
        
            To_AgX_socket = nt.interface.new_socket(
                name="To AgX",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Stack_socket = nt.interface.new_socket(
                name="Stack",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Stack_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 1.0
        Alpha_socket.min_value = 0.0
        Alpha_socket.max_value = 1.0
        Alpha_socket.subtype = "FACTOR"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (328.5899658203125, -14.88987922668457)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-341.0716552734375, 0.0)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (-141.0716552734375, -43.58099365234375)
        Group_013.inputs["Alpha"].default_value = 1.0
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (-141.0716552734375, 43.5809326171875)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (141.0716552734375, -21.1348876953125)
        Mix_Shader_001 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_001.location = (141.0716552734375, -143.97640991210938)
        # Create links
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_013.outputs["Shader"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Stack"], Group_013.inputs["Combined"])
        nt.links.new(Group_Input.outputs["Alpha"], Mix_Shader.inputs["Fac"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Group_013.outputs["To AgX"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Alpha"], Mix_Shader_001.inputs["Fac"])
        nt.links.new(Mix_Shader_001.outputs["Shader"], Group_Output.inputs["To AgX"])