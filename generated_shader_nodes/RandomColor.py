import bpy
from ..utils import ShaderNode


class ShaderNodeRandomColor(ShaderNode):
    bl_label = "Random Color"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "NONE"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (772.4732666015625, 8.411381721496582)
        Hue/Saturation/Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value.location = (541.9999389648438, 10.383028984069824)
        Hue/Saturation/Value.inputs["Hue"].default_value = 0.5
        Hue/Saturation/Value.inputs["Saturation"].default_value = 1.0
        Hue/Saturation/Value.inputs["Value"].default_value = 1.5
        Hue/Saturation/Value.inputs["Fac"].default_value = 1.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-317.05877685546875, 0.0)
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (-102.65557861328125, -21.80877685546875)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Scale"].default_value = 12.09999942779541
        Noise_Texture.inputs["Detail"].default_value = 0.0
        Noise_Texture.inputs["Roughness"].default_value = 0.0
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 1.2999999523162842
        Texture_Coordinate = nt.nodes.new("ShaderNodeTexCoord")
        Texture_Coordinate.location = (-588.892578125, -25.754043579101562)
        Color_Ramp = nt.nodes.new("ShaderNodeValToRGB")
        Color_Ramp.location = (222.058837890625, 34.6854248046875)
        Color_Ramp.color_ramp.color_mode = "RGB"
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (21.1109619140625, 214.92861938476562)
        # Create links
        nt.links.new(Hue/Saturation/Value.outputs["Color"], Group_Output.inputs["Color"])
        nt.links.new(Color_Ramp.outputs["Color"], Hue/Saturation/Value.inputs["Color"])
        nt.links.new(Noise_Texture.outputs["Fac"], Color_Ramp.inputs["Fac"])
        nt.links.new(Texture_Coordinate.outputs["UV"], Noise_Texture.inputs["Vector"])