import bpy
from ..utils import ShaderNode


class ShaderNodeAddOutline(ShaderNode):
    bl_label = "Add Outline"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Outline_socket = nt.interface.new_socket(
                name="Outline",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Outline_Color_socket = nt.interface.new_socket(
                name="Outline Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Outline_Color_socket.default_value = (0.012772791087627411, 0.012772791087627411, 0.012772791087627411, 1.0)
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
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-242.52853393554688, -25.51680564880371)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (931.5992431640625, 1.0672754049301147)
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (8.618843078613281, 0.0)
        Emission.inputs["Strength"].default_value = 1.0
        Emission.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (220.51385498046875, 64.11897277832031)
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (8.618843078613281, 84.397216796875)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (8.618843078613281, 151.6417694091797)
        Mix_Shader_001 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_001.location = (571.7650146484375, 64.11897277832031)
        Transparent_BSDF_001 = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF_001.location = (220.51385498046875, -81.97634887695312)
        Transparent_BSDF_001.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF_001.inputs["Weight"].default_value = 0.0
        Light_Path = nt.nodes.new("ShaderNodeLightPath")
        Light_Path.location = (220.51385498046875, 138.98599243164062)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (285.22576904296875, 294.3856201171875)
        Mix_Shader_002 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_002.location = (752.0, 64.11897277832031)
        Transparent_BSDF_002 = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF_002.location = (564.6485595703125, -81.97634887695312)
        Transparent_BSDF_002.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF_002.inputs["Weight"].default_value = 0.0
        # Create links
        nt.links.new(Group_Input.outputs["Outline Color"], Emission.inputs["Color"])
        nt.links.new(Mix_Shader_002.outputs["Shader"], Group_Output.inputs["Outline"])
        nt.links.new(Geometry.outputs["Backfacing"], Mix_Shader.inputs["Fac"])
        nt.links.new(Transparent_BSDF_001.outputs["BSDF"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Light_Path.outputs["Is Camera Ray"], Mix_Shader_001.inputs["Fac"])
        nt.links.new(Emission.outputs["Emission"], Mix_Shader.inputs["Shader"])
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Transparent_BSDF_002.outputs["BSDF"], Mix_Shader_002.inputs["Shader"])
        nt.links.new(Mix_Shader_001.outputs["Shader"], Mix_Shader_002.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Alpha"], Mix_Shader_002.inputs["Fac"])