import bpy
from ..utils import ShaderNode


class ShaderNodeEmissionMask(ShaderNode):
    bl_label = "Emission Mask"
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
            Mask_socket = nt.interface.new_socket(
                name="Mask",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mask_socket.default_value = 0.5
        Mask_socket.min_value = 0.0
        Mask_socket.max_value = 1.0
        Mask_socket.subtype = "FACTOR"
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 1.0
        Scale_socket.min_value = 1.0
        Scale_socket.max_value = 1000.0
        Scale_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (459.1246337890625, 102.02742767333984)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-579.6181640625, 103.91682434082031)
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (-33.60517883300781, 69.78109741210938)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (-33.0797119140625, -13.705078125)
        Emission.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (249.29244995117188, 90.21170043945312)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-258.4811096191406, -90.21173095703125)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-63.015960693359375, 239.5391845703125)
        # Create links
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Emission.outputs["Emission"], Mix_Shader.inputs["Shader"])
        nt.links.new(Math.outputs["Value"], Emission.inputs["Strength"])
        nt.links.new(Group_Input.outputs["Mask"], Mix_Shader.inputs["Fac"])
        nt.links.new(Group_Input.outputs["Color"], Emission.inputs["Color"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Mask"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Scale"], Math.inputs["Value"])