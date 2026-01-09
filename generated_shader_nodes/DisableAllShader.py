import bpy
from ..utils import ShaderNode


class ShaderNodeDisableAllShader(ShaderNode):
    bl_label = "Disable All Shader"
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
            Fac_socket = nt.interface.new_socket(
                name="Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fac_socket.default_value = 0.0
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Shader_socket = nt.interface.new_socket(
                name="Shader",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (305.50872802734375, 0.0)
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (115.50872802734375, 53.576416015625)
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (-115.50869750976562, -53.576416015625)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-315.5086975097656, 28.38391876220703)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (8.535415649414062, 221.83009338378906)
        # Create links
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Shader"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_Shader.inputs["Fac"])