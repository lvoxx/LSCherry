import bpy
from ..utils import ShaderNode


class ShaderNodeToonifyPbrColors(ShaderNode):
    bl_label = "Toonify PBR Colors"
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
            Saturation_socket = nt.interface.new_socket(
                name="Saturation",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Saturation_socket.default_value = 0.8500000238418579
        Saturation_socket.min_value = 0.0
        Saturation_socket.max_value = 2.0
        Saturation_socket.subtype = "NONE"
            Gamma_socket = nt.interface.new_socket(
                name="Gamma",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Gamma_socket.default_value = 0.75
        Gamma_socket.min_value = 0.0010000000474974513
        Gamma_socket.max_value = 10.0
        Gamma_socket.subtype = "NONE"
            Bright_socket = nt.interface.new_socket(
                name="Bright",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Bright_socket.default_value = 0.10000000149011612
        Bright_socket.min_value = -100.0
        Bright_socket.max_value = 100.0
        Bright_socket.subtype = "NONE"
            Contrast_socket = nt.interface.new_socket(
                name="Contrast",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Contrast_socket.default_value = 0.15000000596046448
        Contrast_socket.min_value = -100.0
        Contrast_socket.max_value = 100.0
        Contrast_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (372.1709289550781, -53.45722198486328)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-500.453857421875, 5.0911641120910645)
        Hue/Saturation/Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value.location = (-179.62716674804688, 13.2052001953125)
        Hue/Saturation/Value.inputs["Hue"].default_value = 0.5
        Hue/Saturation/Value.inputs["Value"].default_value = 1.0
        Hue/Saturation/Value.inputs["Fac"].default_value = 1.0
        Gamma = nt.nodes.new("ShaderNodeGamma")
        Gamma.location = (9.562591552734375, -13.2052001953125)
        Brightness/Contrast = nt.nodes.new("ShaderNodeBrightContrast")
        Brightness/Contrast.location = (179.627197265625, -12.23052978515625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-18.010330200195312, 162.14474487304688)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-264.99334716796875, -88.86517333984375)
        Separate_Color.inputs["Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (194.30886840820312, -57.297119140625)
        RGB_Curves = nt.nodes.new("ShaderNodeRGBCurve")
        RGB_Curves.location = (-99.4940185546875, -173.23776245117188)
        RGB_Curves.inputs["Fac"].default_value = 1.0
        RGB_Curves_001 = nt.nodes.new("ShaderNodeRGBCurve")
        RGB_Curves_001.location = (-220.81796264648438, -48.17718505859375)
        RGB_Curves_001.inputs["Fac"].default_value = 1.0
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-471.0701904296875, -360.5313415527344)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-43.4908447265625, -388.5313415527344)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (16.534133911132812, -47.09332275390625)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (253.10829162597656, -47.09332275390625)
        Reroute_001.inputs["Input"].default_value = (0.0, 0.0, 0.0, 1.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (44.07353210449219, -28.859375)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (549.5283813476562, -370.5313415527344)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (-17.58428955078125, -186.18270874023438)
        Frame_006 = nt.nodes.new("NodeFrame")
        Frame_006.location = (-17.58428955078125, -252.2303466796875)
        # Create links
        nt.links.new(Gamma.outputs["Color"], Brightness/Contrast.inputs["Color"])
        nt.links.new(Hue/Saturation/Value.outputs["Color"], Gamma.inputs["Color"])
        nt.links.new(Group_Input.outputs["Color"], Hue/Saturation/Value.inputs["Color"])
        nt.links.new(Brightness/Contrast.outputs["Color"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Saturation"], Hue/Saturation/Value.inputs["Saturation"])
        nt.links.new(Group_Input.outputs["Gamma"], Gamma.inputs["Gamma"])
        nt.links.new(Group_Input.outputs["Bright"], Brightness/Contrast.inputs["Bright"])
        nt.links.new(Group_Input.outputs["Contrast"], Brightness/Contrast.inputs["Contrast"])
        nt.links.new(Separate_Color.outputs["Red"], Combine_Color.inputs["Red"])
        nt.links.new(Separate_Color.outputs["Green"], Combine_Color.inputs["Green"])
        nt.links.new(RGB_Curves.outputs["Color"], Combine_Color.inputs["Blue"])
        nt.links.new(Separate_Color.outputs["Blue"], RGB_Curves.inputs["Color"])
        nt.links.new(Combine_Color.outputs["Color"], Reroute.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], RGB_Curves_001.inputs["Color"])