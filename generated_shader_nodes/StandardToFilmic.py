import bpy
from ..utils import ShaderNode


class ShaderNodeStandardToFilmic(ShaderNode):
    bl_label = "Standard To Filmic"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Bright/Contrast = nt.nodes.new("ShaderNodeBrightContrast")
        Bright/Contrast.location = (-326.51068115234375, -148.99867248535156)
        Bright/Contrast.inputs["Bright"].default_value = 0.0
        Bright/Contrast.inputs["Contrast"].default_value = 0.009999999776482582
        RGB_Curves = nt.nodes.new("ShaderNodeRGBCurve")
        RGB_Curves.location = (16.555625915527344, -20.7540340423584)
        RGB_Curves.inputs["Fac"].default_value = 1.0
        Hue_Saturation_Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue_Saturation_Value.location = (657.0335693359375, -15.053702354431152)
        Hue_Saturation_Value.inputs["Hue"].default_value = 0.5
        Hue_Saturation_Value.inputs["Saturation"].default_value = 1.0099999904632568
        Hue_Saturation_Value.inputs["Value"].default_value = 1.0
        Hue_Saturation_Value.inputs["Fac"].default_value = 0.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (837.4287719726562, 191.5542755126953)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1110.2022705078125, 161.25424194335938)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-767.1213989257812, 47.59791564941406)
        Gamma = nt.nodes.new("ShaderNodeGamma")
        Gamma.location = (-547.0000610351562, -89.43470764160156)
        Gamma.inputs["Gamma"].default_value = 1.5
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-65.6805419921875, 192.40020751953125)
        # Create links
        nt.links.new(Bright/Contrast.outputs["Color"], RGB_Curves.inputs["Color"])
        nt.links.new(Gamma.outputs["Color"], Bright/Contrast.inputs["Color"])
        nt.links.new(RGB_Curves.outputs["Color"], Hue_Saturation_Value.inputs["Color"])
        nt.links.new(Group_Input.outputs["Combined"], Mix.inputs["A"])
        nt.links.new(Hue_Saturation_Value.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input.outputs["Combined"], Gamma.inputs["Color"])