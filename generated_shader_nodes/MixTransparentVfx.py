import bpy
from ..utils import ShaderNode


class ShaderNodeMixTransparentVfx(ShaderNode):
    bl_label = "Mix Transparent VFX"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Mask_socket = nt.interface.new_socket(
                name="Mask",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Fac_socket = nt.interface.new_socket(
                name="Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fac_socket.default_value = 2.9802322387695312e-08
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Shader_socket = nt.interface.new_socket(
                name="Shader",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        

        # Create nodes
        Fresnel = nt.nodes.new("ShaderNodeFresnel")
        Fresnel.location = (-138.7225341796875, -70.04754638671875)
        Fresnel.inputs["IOR"].default_value = 0.9500001668930054
        Fresnel.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (180.1520538330078, 217.35824584960938)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader_001 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_001.location = (720.4673461914062, 181.56712341308594)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (933.0806274414062, 158.39202880859375)
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (556.0906372070312, 86.7460708618164)
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (403.2370300292969, -57.49848937988281)
        Emission.inputs["Color"].default_value = (0.8611106276512146, 0.8611106276512146, 0.8611106276512146, 1.0)
        Emission.inputs["Strength"].default_value = 1.0
        Emission.inputs["Weight"].default_value = 0.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-313.88702392578125, 123.08967590332031)
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (75.56430053710938, 50.876869201660156)
        ColorRamp.color_ramp.color_mode = "RGB"
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (347.4512939453125, 391.6933898925781)
        # Create links
        nt.links.new(Fresnel.outputs["Fac"], ColorRamp.inputs["Fac"])
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(ColorRamp.outputs["Color"], Mix_Shader.inputs["Fac"])
        nt.links.new(Emission.outputs["Emission"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_Shader_001.inputs["Fac"])
        nt.links.new(Mix_Shader_001.outputs["Shader"], Group_Output.inputs["Mask"])
        nt.links.new(Mix_Shader.outputs["Shader"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Shader"], Mix_Shader_001.inputs["Shader"])