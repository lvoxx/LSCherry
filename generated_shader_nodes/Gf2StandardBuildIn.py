import bpy
from ..utils import ShaderNode


class ShaderNodeGf2StandardBuildIn(ShaderNode):
    bl_label = "GF2: Standard Build-in"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = "Standard GF2 materials build-in"

        # Output sockets
            Diffuse_Texture_socket = nt.interface.new_socket(
                name="Diffuse Texture",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Diffuse_Texture_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 0.0
        Alpha_socket.min_value = 0.0
        Alpha_socket.max_value = 1.0
        Alpha_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"
            Specular_Color_socket = nt.interface.new_socket(
                name="Specular Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Specular_Color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            Specular_Tint_socket = nt.interface.new_socket(
                name="Specular Tint",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Specular_Tint_socket.default_value = 0.0
        Specular_Tint_socket.min_value = -3.4028234663852886e+38
        Specular_Tint_socket.max_value = 3.4028234663852886e+38
        Specular_Tint_socket.subtype = "NONE"
            Metal_Ramp_socket = nt.interface.new_socket(
                name="Metal Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Metal_Ramp_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            Blend_Metal_Ramp_socket = nt.interface.new_socket(
                name="Blend Metal Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Blend_Metal_Ramp_socket.default_value = 0.0
        Blend_Metal_Ramp_socket.min_value = -3.4028234663852886e+38
        Blend_Metal_Ramp_socket.max_value = 3.4028234663852886e+38
        Blend_Metal_Ramp_socket.subtype = "NONE"

        # Input sockets
            Diffuse_Texture_socket = nt.interface.new_socket(
                name="Diffuse Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Diffuse_Texture_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 1.0
        Alpha_socket.min_value = 0.0
        Alpha_socket.max_value = 1.0
        Alpha_socket.subtype = "NONE"
            Spec_Texture_socket = nt.interface.new_socket(
                name="Spec Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Spec_Texture_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Normal_Texture_socket = nt.interface.new_socket(
                name="Normal Texture",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_Texture_socket.default_value = (0.0, 0.0, 0.0)
        Normal_Texture_socket.subtype = "NONE"
            Anisotropic_socket = nt.interface.new_socket(
                name="Anisotropic",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Anisotropic_socket.default_value = 0.0
        Anisotropic_socket.min_value = 0.0
        Anisotropic_socket.max_value = 1.0
        Anisotropic_socket.subtype = "FACTOR"
            AO_socket = nt.interface.new_socket(
                name="AO",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        AO_socket.default_value = 1.0
        AO_socket.min_value = 0.0
        AO_socket.max_value = 1.0
        AO_socket.subtype = "FACTOR"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1362.3076171875, 120.27081298828125)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-382.0918884277344, 124.48867797851562)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-141.62542724609375, 75.1331787109375)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (89.5264663696289, 7.390474319458008)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.20000000298023224
        Map_Range.inputs["From Max"].default_value = 1.0
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (577.2362060546875, -222.5399169921875)
        Group.inputs["Use Dot"].default_value = True
        Group.inputs["Scale"].default_value = 4.010000228881836
        Group.inputs["Distortion"].default_value = 1.0
        Group.inputs["Value Enhance"].default_value = 0.10000000149011612
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (577.2362060546875, -159.46548461914062)
        Group_001.inputs["Mix 1"].default_value = 0.8999999761581421
        Group_001.inputs["Mix 2"].default_value = 0.9399999976158142
        Group_001.inputs["Mix 3"].default_value = 0.9800000190734863
        Group_001.inputs["Lv 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_001.inputs["Lv 2"].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        Group_001.inputs["Lv 3"].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        Group_001.inputs["Lv 4"].default_value = (1.0, 1.0, 1.0, 1.0)
        Group_001.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (791.058837890625, -99.7928695678711)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (377.9173583984375, -124.38348388671875)
        Math.operation = "SUBTRACT"
        Math.inputs["Value"].default_value = 1.0
        Math.inputs["Value"].default_value = 0.5
        Group_002 = nt.nodes.new("ShaderNodeGroup")
        Group_002.location = (-146.75616455078125, -113.14131164550781)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (575.6005249023438, 264.1119689941406)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (151.82542419433594, -78.43937683105469)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Hue/Saturation/Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value.location = (368.2861022949219, 9.572591781616211)
        Hue/Saturation/Value.inputs["Hue"].default_value = 0.5
        Hue/Saturation/Value.inputs["Saturation"].default_value = 0.5
        Hue/Saturation/Value.inputs["Value"].default_value = 1.0
        Hue/Saturation/Value.inputs["Fac"].default_value = 1.0
        Hue/Saturation/Value_001 = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value_001.location = (1044.7650146484375, -160.9136962890625)
        Hue/Saturation/Value_001.inputs["Hue"].default_value = 0.5
        Hue/Saturation/Value_001.inputs["Saturation"].default_value = 0.20000000298023224
        Hue/Saturation/Value_001.inputs["Value"].default_value = 1.5
        Hue/Saturation/Value_001.inputs["Fac"].default_value = 1.0
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (1096.2611083984375, 67.11038208007812)
        Math_001.operation = "DIVIDE"
        Math_001.inputs["Value"].default_value = 10.0
        Math_001.inputs["Value"].default_value = 0.5
        # Create links
        nt.links.new(Separate_Color.outputs["Green"], Map_Range.inputs["Value"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Diffuse Texture"])
        nt.links.new(Group_Input.outputs["Spec Texture"], Separate_Color.inputs["Color"])
        nt.links.new(Group_001.outputs["Custom Ramp"], Mix.inputs["A"])
        nt.links.new(Group.outputs["Ramp"], Mix.inputs["B"])
        nt.links.new(Map_Range.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Anisotropic"], Mix.inputs["Factor"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Metal Ramp"])
        nt.links.new(Group_Input.outputs["Normal Texture"], Group_002.inputs["Normal"])
        nt.links.new(Group_002.outputs["Normal"], Group.inputs["Normal"])
        nt.links.new(Group_002.outputs["Normal"], Group_Output.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Diffuse Texture"], Mix_001.inputs["A"])
        nt.links.new(Hue/Saturation/Value.outputs["Color"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["AO"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Alpha"], Group_Output.inputs["Alpha"])
        nt.links.new(Map_Range.outputs["Result"], Group_Output.inputs["Blend Metal Ramp"])
        nt.links.new(Math_001.outputs["Value"], Group_Output.inputs["Specular Tint"])
        nt.links.new(Separate_Color.outputs["Blue"], Mix_002.inputs["A"])
        nt.links.new(Group_Input.outputs["AO"], Mix_002.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Diffuse Texture"], Mix_002.inputs["B"])
        nt.links.new(Mix_002.outputs["Result"], Hue/Saturation/Value.inputs["Color"])
        nt.links.new(Mix_001.outputs["Result"], Hue/Saturation/Value_001.inputs["Color"])
        nt.links.new(Hue/Saturation/Value_001.outputs["Color"], Group_Output.inputs["Specular Color"])
        nt.links.new(Separate_Color.outputs["Red"], Math_001.inputs["Value"])