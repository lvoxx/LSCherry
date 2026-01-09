import bpy
from ..utils import ShaderNode


class ShaderNodeFesGiGenshinpbrSmbe(ShaderNode):
    bl_label = "FES_GI: GenshinPBR - SMBE"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            BSDF_socket = nt.interface.new_socket(
                name="BSDF",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Base_socket = nt.interface.new_socket(
                name="Base",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Base_Alpha_socket = nt.interface.new_socket(
                name="Base Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Base_Alpha_socket.default_value = 1.0
        Base_Alpha_socket.min_value = 0.0
        Base_Alpha_socket.max_value = 1.0
        Base_Alpha_socket.subtype = "FACTOR"
            SMBE_socket = nt.interface.new_socket(
                name="SMBE",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        SMBE_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            SMBE_Alpha_socket = nt.interface.new_socket(
                name="SMBE Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        SMBE_Alpha_socket.default_value = 0.0
        SMBE_Alpha_socket.min_value = 0.0
        SMBE_Alpha_socket.max_value = 1.0
        SMBE_Alpha_socket.subtype = "FACTOR"
            Emission_Strength_socket = nt.interface.new_socket(
                name="Emission Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Emission_Strength_socket.default_value = 1.0
        Emission_Strength_socket.min_value = -3.4028234663852886e+38
        Emission_Strength_socket.max_value = 3.4028234663852886e+38
        Emission_Strength_socket.subtype = "FACTOR"
            Mix_Diffuse_with_Emission_socket = nt.interface.new_socket(
                name="Mix Diffuse with Emission",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_Diffuse_with_Emission_socket.default_value = 0.0
        Mix_Diffuse_with_Emission_socket.min_value = 0.0
        Mix_Diffuse_with_Emission_socket.max_value = 1.0
        Mix_Diffuse_with_Emission_socket.subtype = "FACTOR"
            Emission_Tint_socket = nt.interface.new_socket(
                name="Emission Tint",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Emission_Tint_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            0_=_OpenGL,_1_=_DirectX_socket = nt.interface.new_socket(
                name="0 = OpenGL, 1 = DirectX",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        0_=_OpenGL,_1_=_DirectX_socket.default_value = 1.0
        0_=_OpenGL,_1_=_DirectX_socket.min_value = 0.0
        0_=_OpenGL,_1_=_DirectX_socket.max_value = 1.0
        0_=_OpenGL,_1_=_DirectX_socket.subtype = "FACTOR"
            Normal_Strength_socket = nt.interface.new_socket(
                name="Normal Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Normal_Strength_socket.default_value = 1.0
        Normal_Strength_socket.min_value = 0.0
        Normal_Strength_socket.max_value = 10.0
        Normal_Strength_socket.subtype = "FACTOR"
            Height_socket = nt.interface.new_socket(
                name="Height",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Height_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Height_Strength_socket = nt.interface.new_socket(
                name="Height Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Height_Strength_socket.default_value = 1.0
        Height_Strength_socket.min_value = 0.0
        Height_Strength_socket.max_value = 1.0
        Height_Strength_socket.subtype = "FACTOR"
            Height_Distance_socket = nt.interface.new_socket(
                name="Height Distance",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Height_Distance_socket.default_value = 0.25
        Height_Distance_socket.min_value = 0.0
        Height_Distance_socket.max_value = 1000.0
        Height_Distance_socket.subtype = "NONE"
            ----------------_socket = nt.interface.new_socket(
                name="----------------",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        ----------------_socket.default_value = 0.0
        ----------------_socket.min_value = -3.4028234663852886e+38
        ----------------_socket.max_value = 3.4028234663852886e+38
        ----------------_socket.subtype = "FACTOR"
            Principled_BSDF_=_0,_Specular_BSDF_=_1_socket = nt.interface.new_socket(
                name="Principled BSDF = 0, Specular BSDF = 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Principled_BSDF_=_0,_Specular_BSDF_=_1_socket.default_value = 0.0
        Principled_BSDF_=_0,_Specular_BSDF_=_1_socket.min_value = 0.0
        Principled_BSDF_=_0,_Specular_BSDF_=_1_socket.max_value = 1.0
        Principled_BSDF_=_0,_Specular_BSDF_=_1_socket.subtype = "FACTOR"

        # Create nodes
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-644.9751586914062, 70.93974304199219)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-648.4550170898438, -191.36419677734375)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-643.0197143554688, 324.29852294921875)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (840.0362548828125, 0.0)
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (646.2061767578125, 70.25714111328125)
        Principled_BSDF = nt.nodes.new("ShaderNodeBsdfPrincipled")
        Principled_BSDF.location = (166.5567626953125, 664.8359375)
        Principled_BSDF.inputs["Metallic"].default_value = 0.0
        Principled_BSDF.inputs["IOR"].default_value = 1.4500000476837158
        Principled_BSDF.inputs["Weight"].default_value = 0.0
        Principled_BSDF.inputs["Diffuse Roughness"].default_value = 0.0
        Principled_BSDF.inputs["Subsurface Weight"].default_value = 0.0
        Principled_BSDF.inputs["Subsurface Radius"].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
        Principled_BSDF.inputs["Subsurface Scale"].default_value = 0.05000000074505806
        Principled_BSDF.inputs["Subsurface IOR"].default_value = 1.399999976158142
        Principled_BSDF.inputs["Subsurface Anisotropy"].default_value = 0.0
        Principled_BSDF.inputs["Specular Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs["Anisotropic"].default_value = 0.0
        Principled_BSDF.inputs["Anisotropic Rotation"].default_value = 0.0
        Principled_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs["Transmission Weight"].default_value = 0.0
        Principled_BSDF.inputs["Coat Weight"].default_value = 0.0
        Principled_BSDF.inputs["Coat Roughness"].default_value = 0.029999999329447746
        Principled_BSDF.inputs["Coat IOR"].default_value = 1.5
        Principled_BSDF.inputs["Coat Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs["Coat Normal"].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs["Sheen Weight"].default_value = 0.0
        Principled_BSDF.inputs["Sheen Roughness"].default_value = 0.5
        Principled_BSDF.inputs["Sheen Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs["Thin Film Thickness"].default_value = 0.0
        Principled_BSDF.inputs["Thin Film IOR"].default_value = 1.3300000429153442
        Specular_BSDF = nt.nodes.new("ShaderNodeEeveeSpecular")
        Specular_BSDF.location = (265.9041748046875, -21.532257080078125)
        Specular_BSDF.inputs["Clear Coat"].default_value = 0.0
        Specular_BSDF.inputs["Clear Coat Roughness"].default_value = 0.0
        Specular_BSDF.inputs["Clear Coat Normal"].default_value = (0.0, 0.0, 0.0)
        Specular_BSDF.inputs["Weight"].default_value = 0.0
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (91.8416748046875, 552.5823974609375)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (-212.31427001953125, 133.84725952148438)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (-190.29537963867188, 106.12901306152344)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (-192.7764892578125, -138.50494384765625)
        Invert = nt.nodes.new("ShaderNodeInvert")
        Invert.location = (-313.77777099609375, 500.6892395019531)
        Invert.inputs["Fac"].default_value = 1.0
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (-689.4768676757812, 367.7322082519531)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (-395.6708984375, 420.4356994628906)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (-397.839599609375, 531.662353515625)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-688.9718017578125, 551.521484375)
        Separate_RGB = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_RGB.location = (-1885.0413818359375, 507.4046325683594)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (-1653.15380859375, 390.3589782714844)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (-1655.025146484375, 426.0024108886719)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (-1690.544677734375, 529.8931884765625)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (-1689.365234375, 472.1393737792969)
        Reroute_024 = nt.nodes.new("NodeReroute")
        Reroute_024.location = (-1619.9151611328125, 471.4594421386719)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (-1639.67529296875, 450.108642578125)
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-1078.6842041015625, 300.11431884765625)
        Math_003.operation = "LESS_THAN"
        Math_003.inputs["Value"].default_value = 0.5
        Math_003.inputs["Value"].default_value = 0.5
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-822.3997192382812, 303.8578796386719)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (1.0, 1.0, 1.0, 1.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-1606.45458984375, 114.23965454101562)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Reroute_025 = nt.nodes.new("NodeReroute")
        Reroute_025.location = (-1624.02734375, 3.630218505859375)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (-1644.78662109375, -19.865478515625)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-1436.106689453125, 113.92031860351562)
        Math_001.operation = "DIVIDE"
        Math_001.inputs["Value"].default_value = 2.0
        Math_001.inputs["Value"].default_value = 0.5
        Reroute_027 = nt.nodes.new("NodeReroute")
        Reroute_027.location = (-898.8671875, 82.71218872070312)
        Reroute_028 = nt.nodes.new("NodeReroute")
        Reroute_028.location = (-898.0379638671875, 172.47549438476562)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-1271.536376953125, 113.92031860351562)
        Math_002.operation = "MULTIPLY"
        Math_002.inputs["Value"].default_value = 2.0
        Math_002.inputs["Value"].default_value = 0.5
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (-1642.39306640625, 183.52137756347656)
        Reroute_030 = nt.nodes.new("NodeReroute")
        Reroute_030.location = (-412.0425720214844, 463.7023010253906)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (-413.8198547363281, 294.154052734375)
        Reroute_031 = nt.nodes.new("NodeReroute")
        Reroute_031.location = (-80.07540893554688, 394.37054443359375)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-571.1637573242188, 498.6971130371094)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_032 = nt.nodes.new("NodeReroute")
        Reroute_032.location = (60.9649658203125, 463.6167297363281)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (60.20050048828125, 353.7098388671875)
        Reroute_029 = nt.nodes.new("NodeReroute")
        Reroute_029.location = (-82.55352783203125, 301.8550720214844)
        Reroute_033 = nt.nodes.new("NodeReroute")
        Reroute_033.location = (39.741943359375, -148.5732421875)
        Reroute_034 = nt.nodes.new("NodeReroute")
        Reroute_034.location = (39.699432373046875, -59.17791748046875)
        Reroute_035 = nt.nodes.new("NodeReroute")
        Reroute_035.location = (-87.72216796875, 12.127609252929688)
        Reroute_036 = nt.nodes.new("NodeReroute")
        Reroute_036.location = (128.23593139648438, 10.941986083984375)
        Reroute_037 = nt.nodes.new("NodeReroute")
        Reroute_037.location = (126.53964233398438, -102.49162292480469)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (89.44168090820312, -82.0297622680664)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (55.111236572265625, -126.69664764404297)
        Reroute_039 = nt.nodes.new("NodeReroute")
        Reroute_039.location = (-266.682861328125, 128.5651092529297)
        Reroute_040 = nt.nodes.new("NodeReroute")
        Reroute_040.location = (-269.8321533203125, -307.91131591796875)
        Reroute_038 = nt.nodes.new("NodeReroute")
        Reroute_038.location = (-266.67144775390625, 89.37290954589844)
        Reroute_041 = nt.nodes.new("NodeReroute")
        Reroute_041.location = (208.4625244140625, -267.1594543457031)
        Reroute_042 = nt.nodes.new("NodeReroute")
        Reroute_042.location = (210.52410888671875, -171.14093017578125)
        Invert_001 = nt.nodes.new("ShaderNodeInvert")
        Invert_001.location = (26.2003173828125, -230.82920837402344)
        Invert_001.inputs["Fac"].default_value = 1.0
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-121.96560668945312, -24.280853271484375)
        Vector_Math.operation = "MULTIPLY"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (-214.43165588378906, -116.34626770019531)
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (-953.6607055664062, -82.64456176757812)
        Vector_Math_001.operation = "MULTIPLY"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (-1251.4854736328125, -176.5738525390625)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Bump = nt.nodes.new("ShaderNodeBump")
        Bump.location = (-1544.9970703125, 374.8545227050781)
        Separate_RGB_001 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_RGB_001.location = (-1883.408203125, 188.9181365966797)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-497.9288330078125, 165.36170959472656)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (261.7330322265625, 751.004638671875)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (-1859.9744873046875, -192.9232177734375)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (-1553.09375, -178.70071411132812)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["A"].default_value = (1.0, 1.0, 1.0, 1.0)
        Normal_Map = nt.nodes.new("ShaderNodeNormalMap")
        Normal_Map.location = (-1889.6505126953125, 360.1208190917969)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (-2583.58544921875, -146.96011352539062)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (-2568.2626953125, -121.54046630859375)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-2819.135009765625, 585.7265625)
        Separate_XYZ = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ.location = (-2468.705322265625, 36.60798645019531)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-2126.672607421875, 40.971038818359375)
        Invert_002 = nt.nodes.new("ShaderNodeInvert")
        Invert_002.location = (-2300.2724609375, 19.94091796875)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-1154.20849609375, 700.0792846679688)
        # Create links
        nt.links.new(Group_Input_001.outputs["Principled BSDF = 0, Specular BSDF = 1"], Mix_Shader.inputs["Fac"])
        nt.links.new(Principled_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["BSDF"])
        nt.links.new(Specular_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Reroute.outputs["Output"], Principled_BSDF.inputs["Base Color"])
        nt.links.new(Reroute_001.outputs["Output"], Specular_BSDF.inputs["Base Color"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute.inputs["Input"])
        nt.links.new(Group_Input.outputs["SMBE"], Separate_RGB.inputs["Color"])
        nt.links.new(Group_Input.outputs["Base"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Mix.inputs["A"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Group_Input.outputs["Normal Strength"], Normal_Map.inputs["Strength"])
        nt.links.new(Reroute_005.outputs["Output"], Principled_BSDF.inputs["Normal"])
        nt.links.new(Normal_Map.outputs["Normal"], Bump.inputs["Normal"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_006.outputs["Output"], Specular_BSDF.inputs["Normal"])
        nt.links.new(Reroute_005.outputs["Output"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Vector_Math.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Emission Strength"], Reroute_007.inputs["Input"])
        nt.links.new(Reroute_033.outputs["Output"], Specular_BSDF.inputs["Emissive Color"])
        nt.links.new(Group_Input.outputs["SMBE Alpha"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Principled_BSDF.inputs["Emission Color"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_012.outputs["Output"], Principled_BSDF.inputs["Emission Strength"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Reroute_022.outputs["Output"], Invert.inputs["Color"])
        nt.links.new(Reroute_015.outputs["Output"], Principled_BSDF.inputs["Roughness"])
        nt.links.new(Reroute_032.outputs["Output"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Specular_BSDF.inputs["Roughness"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_016.inputs["Input"])
        nt.links.new(Separate_RGB.outputs["Red"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Separate_RGB.outputs["Blue"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_014.outputs["Output"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_025.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Reroute_023.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Reroute_017.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Reroute_024.inputs["Input"])
        nt.links.new(Reroute_024.outputs["Output"], Reroute_025.inputs["Input"])
        nt.links.new(Math.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Separate_RGB.outputs["Green"], Reroute_026.inputs["Input"])
        nt.links.new(Math_003.outputs["Value"], Mix_001.inputs["Factor"])
        nt.links.new(Reroute_028.outputs["Output"], Mix_001.inputs["A"])
        nt.links.new(Math_002.outputs["Value"], Reroute_027.inputs["Input"])
        nt.links.new(Reroute_027.outputs["Output"], Reroute_028.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Math_003.inputs["Value"])
        nt.links.new(Mix_001.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Reroute_031.outputs["Output"], Principled_BSDF.inputs["Specular IOR Level"])
        nt.links.new(Reroute_030.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Reroute_029.inputs["Input"])
        nt.links.new(Mix.outputs["Result"], Reroute_030.inputs["Input"])
        nt.links.new(Reroute_029.outputs["Output"], Reroute_031.inputs["Input"])
        nt.links.new(Invert.outputs["Color"], Reroute_032.inputs["Input"])
        nt.links.new(Reroute_037.outputs["Output"], Specular_BSDF.inputs["Specular"])
        nt.links.new(Reroute_034.outputs["Output"], Reroute_033.inputs["Input"])
        nt.links.new(Vector_Math.outputs["Vector"], Reroute_034.inputs["Input"])
        nt.links.new(Reroute_029.outputs["Output"], Reroute_035.inputs["Input"])
        nt.links.new(Reroute_035.outputs["Output"], Reroute_036.inputs["Input"])
        nt.links.new(Reroute_036.outputs["Output"], Reroute_037.inputs["Input"])
        nt.links.new(Reroute_038.outputs["Output"], Principled_BSDF.inputs["Alpha"])
        nt.links.new(Reroute_039.outputs["Output"], Reroute_038.inputs["Input"])
        nt.links.new(Group_Input_002.outputs["Base Alpha"], Reroute_039.inputs["Input"])
        nt.links.new(Reroute_040.outputs["Output"], Invert_001.inputs["Color"])
        nt.links.new(Reroute_038.outputs["Output"], Reroute_040.inputs["Input"])
        nt.links.new(Reroute_042.outputs["Output"], Specular_BSDF.inputs["Transparency"])
        nt.links.new(Invert_001.outputs["Color"], Reroute_041.inputs["Input"])
        nt.links.new(Reroute_041.outputs["Output"], Reroute_042.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Vector_Math.inputs["Vector"])
        nt.links.new(Reroute_008.outputs["Output"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Vector_Math_001.outputs["Vector"], Reroute_009.inputs["Input"])
        nt.links.new(Group_Input_003.outputs["Emission Tint"], Mix_002.inputs["B"])
        nt.links.new(Mix_002.outputs["Result"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Bump.outputs["Normal"], Reroute_004.inputs["Input"])
        nt.links.new(Group_Input.outputs["Height Distance"], Bump.inputs["Distance"])
        nt.links.new(Group_Input.outputs["Height Strength"], Bump.inputs["Strength"])
        nt.links.new(Separate_RGB_001.outputs["Red"], Bump.inputs["Height"])
        nt.links.new(Group_Input.outputs["Height"], Separate_RGB_001.inputs["Color"])
        nt.links.new(Group_Input_003.outputs["Base"], Mix_003.inputs["B"])
        nt.links.new(Group_Input_003.outputs["Mix Diffuse with Emission"], Mix_003.inputs["Factor"])
        nt.links.new(Mix_003.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Group_Input.outputs["Normal"], Separate_XYZ.inputs["Vector"])
        nt.links.new(Separate_XYZ.outputs["Y"], Invert_002.inputs["Color"])
        nt.links.new(Separate_XYZ.outputs["X"], Combine_XYZ.inputs["X"])
        nt.links.new(Invert_002.outputs["Color"], Combine_XYZ.inputs["Y"])
        nt.links.new(Separate_XYZ.outputs["Z"], Combine_XYZ.inputs["Z"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Normal_Map.inputs["Color"])
        nt.links.new(Group_Input.outputs["0 = OpenGL, 1 = DirectX"], Invert_002.inputs["Fac"])