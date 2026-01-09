import bpy
from ..utils import ShaderNode


class ShaderNodeFesGiCombineSmbeAndScene(ShaderNode):
    bl_label = "FES_GI: Combine SMBE and Scene"
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
            SMBE_socket = nt.interface.new_socket(
                name="SMBE",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Scene_socket = nt.interface.new_socket(
                name="Scene",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Lightmap_socket = nt.interface.new_socket(
                name="Lightmap",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            Emission_Strength_socket = nt.interface.new_socket(
                name="Emission Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Emission_Strength_socket.default_value = 85.0
        Emission_Strength_socket.min_value = 0.0
        Emission_Strength_socket.max_value = 200.0
        Emission_Strength_socket.subtype = "NONE"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-469.64630126953125, -61.62812805175781)
        Hue/Saturation/Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value.location = (-232.69863891601562, -94.54873657226562)
        Hue/Saturation/Value.inputs["Hue"].default_value = 0.5199999809265137
        Hue/Saturation/Value.inputs["Saturation"].default_value = 1.0
        Hue/Saturation/Value.inputs["Value"].default_value = 1.0
        Hue/Saturation/Value.inputs["Fac"].default_value = 1.0
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (84.0018310546875, 16.318572998046875)
        Emission.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (-223.17481994628906, 85.97417449951172)
        Mix_Shader.inputs["Fac"].default_value = 0.15800000727176666
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (528.1820678710938, 109.43952178955078)
        Add_Shader = nt.nodes.new("ShaderNodeAddShader")
        Add_Shader.location = (258.75457763671875, 139.43801879882812)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-204.37994384765625, 196.3922882080078)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Hue/Saturation/Value.inputs["Color"])
        nt.links.new(Group_Input.outputs["SMBE"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input.outputs["Scene"], Mix_Shader.inputs["Shader"])
        nt.links.new(Hue/Saturation/Value.outputs["Color"], Emission.inputs["Color"])
        nt.links.new(Group_Input.outputs["Emission Strength"], Emission.inputs["Strength"])
        nt.links.new(Mix_Shader.outputs["Shader"], Add_Shader.inputs["Shader"])
        nt.links.new(Emission.outputs["Emission"], Add_Shader.inputs["Shader"])
        nt.links.new(Add_Shader.outputs["Shader"], Group_Output.inputs["Shader"])