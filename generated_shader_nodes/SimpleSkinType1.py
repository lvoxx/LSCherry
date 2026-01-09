import bpy
from ..utils import ShaderNode


class ShaderNodeSimpleSkinType1(ShaderNode):
    bl_label = "Simple Skin Type 1"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Input sockets
            Skin_Color_socket = nt.interface.new_socket(
                name="Skin Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Skin_Color_socket.default_value = (0.949999988079071, 0.6191033124923706, 0.5204554796218872, 1.0)
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"
            --_Blemishes_--_socket = nt.interface.new_socket(
                name="-- Blemishes --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Red_Color_socket = nt.interface.new_socket(
                name="Red Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Red_Color_socket.default_value = (0.8999999761581421, 0.19262465834617615, 0.13571682572364807, 1.0)
            Blue_Color_socket = nt.interface.new_socket(
                name="Blue Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Blue_Color_socket.default_value = (0.3672824203968048, 0.24802467226982117, 0.8999999761581421, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 1.100000023841858
        Size_socket.min_value = 0.0
        Size_socket.max_value = 100.0
        Size_socket.subtype = "NONE"
            Strength_socket = nt.interface.new_socket(
                name="Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Strength_socket.default_value = 1.0
        Strength_socket.min_value = 0.0
        Strength_socket.max_value = 100.0
        Strength_socket.subtype = "NONE"
            --_Red_Spots_--_socket = nt.interface.new_socket(
                name="-- Red Spots --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Red_Spots_Red_Color_socket = nt.interface.new_socket(
                name="Red Spots Red Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Red_Spots_Red_Color_socket.default_value = (0.800000011920929, 0.17122192680835724, 0.12063717842102051, 1.0)
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 1.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 100.0
        Scale_socket.subtype = "NONE"
            Strength_socket = nt.interface.new_socket(
                name="Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Strength_socket.default_value = 1.0
        Strength_socket.min_value = 0.0
        Strength_socket.max_value = 100.0
        Strength_socket.subtype = "NONE"
            --_Veins_--_socket = nt.interface.new_socket(
                name="-- Veins --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Blue_Color_socket = nt.interface.new_socket(
                name="Blue Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Blue_Color_socket.default_value = (0.35572776198387146, 0.082790806889534, 0.800000011920929, 1.0)
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 1.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 100.0
        Scale_socket.subtype = "NONE"
            Mask_Scale_socket = nt.interface.new_socket(
                name="Mask Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mask_Scale_socket.default_value = 7.0
        Mask_Scale_socket.min_value = 0.0
        Mask_Scale_socket.max_value = 100.0
        Mask_Scale_socket.subtype = "NONE"
            Strength_socket = nt.interface.new_socket(
                name="Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Strength_socket.default_value = 1.0
        Strength_socket.min_value = 0.0
        Strength_socket.max_value = 100.0
        Strength_socket.subtype = "NONE"
            --_Moles_--_socket = nt.interface.new_socket(
                name="-- Moles --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Red_Color_socket = nt.interface.new_socket(
                name="Red Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Red_Color_socket.default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 75.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 1000.0999755859375
        Scale_socket.subtype = "NONE"
            Threadhold_socket = nt.interface.new_socket(
                name="Threadhold",
                in_out="INPUT",
                socket_type="NodeSocketInt"
            )
        
        Threadhold_socket.default_value = 0
        Threadhold_socket.min_value = 0
        Threadhold_socket.max_value = 1000
        Threadhold_socket.subtype = "NONE"
            --_Freckles_--_socket = nt.interface.new_socket(
                name="-- Freckles --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 0.0
        Factor_socket.min_value = 0.0
        Factor_socket.max_value = 1.0
        Factor_socket.subtype = "FACTOR"
            Red_Color_socket = nt.interface.new_socket(
                name="Red Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Red_Color_socket.default_value = (0.800000011920929, 0.35005807876586914, 0.20150570571422577, 1.0)
            Intensity_socket = nt.interface.new_socket(
                name="Intensity",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Intensity_socket.default_value = 0.5
        Intensity_socket.min_value = 0.0
        Intensity_socket.max_value = 1.0
        Intensity_socket.subtype = "FACTOR"
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 1.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 1000.0
        Scale_socket.subtype = "NONE"
            Scale_Small_socket = nt.interface.new_socket(
                name="Scale Small",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_Small_socket.default_value = 2000.0
        Scale_Small_socket.min_value = 0.0
        Scale_Small_socket.max_value = 1000.0
        Scale_Small_socket.subtype = "NONE"
            Scale_Big_socket = nt.interface.new_socket(
                name="Scale Big",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_Big_socket.default_value = 1100.0
        Scale_Big_socket.min_value = 0.0
        Scale_Big_socket.max_value = 1000.0
        Scale_Big_socket.subtype = "NONE"
            --_Pores_--_socket = nt.interface.new_socket(
                name="-- Pores --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 0.0
        Factor_socket.min_value = 0.0
        Factor_socket.max_value = 1.0
        Factor_socket.subtype = "FACTOR"
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 1.5
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 1000.0
        Scale_socket.subtype = "NONE"
            Dirt_Color_socket = nt.interface.new_socket(
                name="Dirt Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Dirt_Color_socket.default_value = (0.05000000074505806, 0.01831624284386635, 0.0050119939260184765, 1.0)
            Dirt_Strength_socket = nt.interface.new_socket(
                name="Dirt Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Dirt_Strength_socket.default_value = 0.25
        Dirt_Strength_socket.min_value = 0.0
        Dirt_Strength_socket.max_value = 1.0
        Dirt_Strength_socket.subtype = "NONE"
            --_Skin_Bump_--_socket = nt.interface.new_socket(
                name="-- Skin Bump --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Goose_Bumps_socket = nt.interface.new_socket(
                name="Goose Bumps",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Goose_Bumps_socket.default_value = 0.0
        Goose_Bumps_socket.min_value = 0.0
        Goose_Bumps_socket.max_value = 1.0
        Goose_Bumps_socket.subtype = "FACTOR"
            Details_socket = nt.interface.new_socket(
                name="Details",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Details_socket.default_value = 0.30000001192092896
        Details_socket.min_value = 0.0
        Details_socket.max_value = 1.0
        Details_socket.subtype = "FACTOR"
            Skin_Scale_socket = nt.interface.new_socket(
                name="Skin Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Skin_Scale_socket.default_value = 9.0
        Skin_Scale_socket.min_value = 0.0
        Skin_Scale_socket.max_value = 1000.0
        Skin_Scale_socket.subtype = "NONE"
            Noise_Scale_socket = nt.interface.new_socket(
                name="Noise Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Noise_Scale_socket.default_value = 50.0
        Noise_Scale_socket.min_value = 0.0
        Noise_Scale_socket.max_value = 1000.0
        Noise_Scale_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1115.218994140625, 50.788414001464844)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1271.6390380859375, -99.3969497680664)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (-1036.21142578125, -34.53603744506836)
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (923.5552978515625, 98.5340576171875)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (-823.240234375, -34.53603744506836)
        Group_005 = nt.nodes.new("ShaderNodeGroup")
        Group_005.location = (-586.589599609375, -34.53603744506836)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (-345.0238342285156, -34.53603744506836)
        Group_006 = nt.nodes.new("ShaderNodeGroup")
        Group_006.location = (-97.11336517333984, -22.38582420349121)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (706.9749755859375, 98.5340576171875)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (413.081298828125, 2.5635623931884766)
        Group_007 = nt.nodes.new("ShaderNodeGroup")
        Group_007.location = (706.9749755859375, -88.40463256835938)
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (198.76678466796875, 98.5340576171875)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-1036.2178955078125, -187.77566528320312)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-822.5975952148438, -276.2513732910156)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (-584.9447021484375, -276.2513732910156)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (-348.9307861328125, -276.2513732910156)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (-97.11336517333984, -262.81256103515625)
        Group_Input_006 = nt.nodes.new("NodeGroupInput")
        Group_Input_006.location = (193.92648315429688, -262.81256103515625)
        Group_Input_007 = nt.nodes.new("NodeGroupInput")
        Group_Input_007.location = (510.9499206542969, -262.81256103515625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-60.65336608886719, 245.64385986328125)
        # Create links
        nt.links.new(Group_008.outputs["Builder"], Group_012.inputs["Color"])
        nt.links.new(Group_006.outputs["UV"], Group_014.inputs["UV"])
        nt.links.new(Group_013.outputs["Builder"], Group_005.inputs["Builder"])
        nt.links.new(Group_011.outputs["UV"], Group_013.inputs["UV"])
        nt.links.new(Group_013.outputs["UV"], Group_005.inputs["UV"])
        nt.links.new(Group_014.outputs["UV"], Group_010.inputs["UV"])
        nt.links.new(Group_011.outputs["Builder"], Group_013.inputs["Builder"])
        nt.links.new(Group_005.outputs["Builder"], Group_004.inputs["Builder"])
        nt.links.new(Group_010.outputs["Pores"], Group_007.inputs["Pores (require)"])
        nt.links.new(Group_005.outputs["UV"], Group_004.inputs["UV"])
        nt.links.new(Group_004.outputs["Builder"], Group_006.inputs["Builder"])
        nt.links.new(Group_010.outputs["Pores"], Group_008.inputs["Pores (require)"])
        nt.links.new(Group_006.outputs["Builder"], Group_014.inputs["Builder"])
        nt.links.new(Group_014.outputs["Builder"], Group_008.inputs["Builder"])
        nt.links.new(Group_004.outputs["UV"], Group_006.inputs["UV"])
        nt.links.new(Group_Input.outputs["UV"], Group_011.inputs["UV"])
        nt.links.new(Group_012.outputs["Color"], Group_Output.inputs["Color"])
        nt.links.new(Group_007.outputs["Normal"], Group_Output.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Skin Color"], Group_011.inputs["Skin Color"])
        nt.links.new(Group_010.outputs["UV"], Group_007.inputs["UV"])
        nt.links.new(Group_Input_001.outputs["Red Color"], Group_013.inputs["Red Color"])
        nt.links.new(Group_Input_001.outputs["Blue Color"], Group_013.inputs["Blue Color"])
        nt.links.new(Group_Input_001.outputs["Size"], Group_013.inputs["Size"])
        nt.links.new(Group_Input_001.outputs["Strength"], Group_013.inputs["Strength"])
        nt.links.new(Group_Input_002.outputs["Red Spots Red Color"], Group_005.inputs["Red Color"])
        nt.links.new(Group_Input_002.outputs["Scale"], Group_005.inputs["Scale"])
        nt.links.new(Group_Input_002.outputs["Strength"], Group_005.inputs["Strength"])
        nt.links.new(Group_Input_003.outputs["Blue Color"], Group_004.inputs["Blue Color"])
        nt.links.new(Group_Input_003.outputs["Scale"], Group_004.inputs["Scale"])
        nt.links.new(Group_Input_003.outputs["Mask Scale"], Group_004.inputs["Mask Scale"])
        nt.links.new(Group_Input_003.outputs["Strength"], Group_004.inputs["Strength"])
        nt.links.new(Group_Input_004.outputs["Red Color"], Group_006.inputs["Red Color"])
        nt.links.new(Group_Input_004.outputs["Scale"], Group_006.inputs["Scale"])
        nt.links.new(Group_Input_004.outputs["Threadhold"], Group_006.inputs["Threadhold"])
        nt.links.new(Group_Input_005.outputs["Factor"], Group_014.inputs["Factor"])
        nt.links.new(Group_Input_005.outputs["Red Color"], Group_014.inputs["Red Color"])
        nt.links.new(Group_Input_005.outputs["Intensity"], Group_014.inputs["Intensity"])
        nt.links.new(Group_Input_005.outputs["Scale"], Group_014.inputs["Scale"])
        nt.links.new(Group_Input_005.outputs["Scale Small"], Group_014.inputs["Scale Small"])
        nt.links.new(Group_Input_005.outputs["Scale Big"], Group_014.inputs["Scale Big"])
        nt.links.new(Group_Input_006.outputs["Factor"], Group_010.inputs["Factor"])
        nt.links.new(Group_Input_006.outputs["Scale"], Group_010.inputs["Scale"])
        nt.links.new(Group_Input_006.outputs["Dirt Color"], Group_008.inputs["Dirt Color"])
        nt.links.new(Group_Input_006.outputs["Dirt Strength"], Group_008.inputs["Dirt Strength"])
        nt.links.new(Group_Input_007.outputs["Goose Bumps"], Group_007.inputs["Goose Bumps"])
        nt.links.new(Group_Input_007.outputs["Details"], Group_007.inputs["Details"])
        nt.links.new(Group_Input_007.outputs["Skin Scale"], Group_007.inputs["Skin Scale"])
        nt.links.new(Group_Input_007.outputs["Noise Scale"], Group_007.inputs["Noise Scale"])