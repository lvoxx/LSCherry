import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Build(ShaderNode):
    bl_label = "SST1: Build"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (292.879638671875, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-336.0129699707031, -18.350139617919922)
        Hue_Saturation_Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue_Saturation_Value.location = (-102.879638671875, -106.84799194335938)
        Hue_Saturation_Value.inputs["Hue"].default_value = 0.44999998807907104
        Hue_Saturation_Value.inputs["Saturation"].default_value = 1.5
        Hue_Saturation_Value.inputs["Value"].default_value = 1.0
        Hue_Saturation_Value.inputs["Fac"].default_value = 1.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (102.879638671875, 106.8480224609375)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = 0.009999999776482582
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-6.201507568359375, 212.72119140625)
        # Create links
        nt.links.new(Hue_Saturation_Value.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Color"], Hue_Saturation_Value.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Color"])