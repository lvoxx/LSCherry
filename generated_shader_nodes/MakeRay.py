import bpy
from ..utils import ShaderNode


class ShaderNodeMakeRay(ShaderNode):
    bl_label = "Make Ray"
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
            ―【CORE】―_socket = nt.interface.new_socket(
                name="―【CORE】―",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (1.0, 0.0, 0.0, 1.0)
            Specular_Color_socket = nt.interface.new_socket(
                name="Specular Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Specular_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Edge_Tint_socket = nt.interface.new_socket(
                name="Edge Tint",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Edge_Tint_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            ―【GENERAL】―_socket = nt.interface.new_socket(
                name="―【GENERAL】―",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 0.8999999761581421
        Size_socket.min_value = 0.0
        Size_socket.max_value = 1.0
        Size_socket.subtype = "FACTOR"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 0.10000000149011612
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "FACTOR"
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.0
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Metal_socket = nt.interface.new_socket(
                name="Metal",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metal_socket.default_value = 0.0
        Metal_socket.min_value = 0.0
        Metal_socket.max_value = 1.0
        Metal_socket.subtype = "FACTOR"
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 1.0
        Alpha_socket.min_value = 0.0
        Alpha_socket.max_value = 1.0
        Alpha_socket.subtype = "NONE"
            Emission_Color_socket = nt.interface.new_socket(
                name="Emission Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Emission_Color_socket.default_value = (0.049706313759088516, 0.006048834882676601, 0.0, 1.0)
            Emission_Strength_socket = nt.interface.new_socket(
                name="Emission Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Emission_Strength_socket.default_value = 0.0
        Emission_Strength_socket.min_value = 0.0
        Emission_Strength_socket.max_value = 1000000.0
        Emission_Strength_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"
            Tangent_socket = nt.interface.new_socket(
                name="Tangent",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Tangent_socket.default_value = (0.0, 0.0, 0.0)
        Tangent_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1033.1141357421875, 185.59979248046875)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-711.2731323242188, -162.93984985351562)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (-313.228759765625, 153.92971801757812)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (-313.228759765625, -47.740570068359375)
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (-52.30828094482422, 105.36119079589844)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (-313.228759765625, 279.9310607910156)
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (418.5204162597656, -13.192481994628906)
        Emission.inputs["Weight"].default_value = 0.0
        Add_Shader = nt.nodes.new("ShaderNodeAddShader")
        Add_Shader.location = (644.9150390625, 83.19893646240234)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-313.228759765625, 358.6959228515625)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (418.5204162597656, -114.09021759033203)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-461.08612060546875, -266.0368957519531)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-440.595703125, -287.8684997558594)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-416.90802001953125, -309.8193359375)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (-387.371337890625, -332.50982666015625)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-461.08612060546875, -151.65081787109375)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-461.08612060546875, 50.359310150146484)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-440.595703125, -171.08148193359375)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (-440.595703125, 30.761253356933594)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (-416.90802001953125, -194.12335205078125)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (-416.90802001953125, 7.00199031829834)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (-387.371337890625, -216.81240844726562)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (-461.08612060546875, -427.91943359375)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (-440.595703125, -449.4589538574219)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (-416.90802001953125, -472.3288879394531)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (-387.371337890625, -494.3876647949219)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (-387.371337890625, -14.748672485351562)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (-516.3226318359375, -198.2943572998047)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (-516.3226318359375, 74.75299072265625)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (-516.3226318359375, -383.21392822265625)
        Mix_Shader_001 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_001.location = (418.5204162597656, 110.16600799560547)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (-53.2172966003418, 162.23062133789062)
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (640.0816650390625, 184.20404052734375)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader_002 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_002.location = (855.1224975585938, 186.701416015625)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (639.3588256835938, 240.26922607421875)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (-313.228759765625, -304.36077880859375)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (-366.1617126464844, -353.7314147949219)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (-366.1617126464844, -239.83929443359375)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (-366.1617126464844, -516.983642578125)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (164.727783203125, 346.49560546875)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.0
        Map_Range.inputs["From Max"].default_value = 1.0
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 0.800000011920929
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Reroute_022 = nt.nodes.new("NodeReroute")
        Reroute_022.location = (-497.20660400390625, -220.6082000732422)
        Reroute_023 = nt.nodes.new("NodeReroute")
        Reroute_023.location = (-497.20660400390625, -129.75897216796875)
        Reroute_024 = nt.nodes.new("NodeReroute")
        Reroute_024.location = (-482.86956787109375, -242.9220428466797)
        Reroute_025 = nt.nodes.new("NodeReroute")
        Reroute_025.location = (-482.86956787109375, -406.291259765625)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (247.0649871826172, -339.34967041015625)
        Reroute_027 = nt.nodes.new("NodeReroute")
        Reroute_027.location = (247.0649871826172, 4.1244049072265625)
        Reroute_028 = nt.nodes.new("NodeReroute")
        Reroute_028.location = (247.0649871826172, 68.67523193359375)
        Reroute_029 = nt.nodes.new("NodeReroute")
        Reroute_029.location = (247.0649871826172, 29.625961303710938)
        # Create links
        nt.links.new(Emission.outputs["Emission"], Add_Shader.inputs["Shader"])
        nt.links.new(Group_008.outputs["Shader"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_009.outputs["Shader"], Mix_Shader.inputs["Shader"])
        nt.links.new(Group_Input_001.outputs["Normal"], Group_010.inputs["Normal"])
        nt.links.new(Group_Input_001.outputs["Roughness"], Group_010.inputs["Roughness"])
        nt.links.new(Group_Input_002.outputs["Emission Color"], Emission.inputs["Color"])
        nt.links.new(Group_Input_002.outputs["Emission Strength"], Emission.inputs["Strength"])
        nt.links.new(Group_Input.outputs["Size"], Reroute.inputs["Input"])
        nt.links.new(Group_Input.outputs["Smooth"], Reroute_001.inputs["Input"])
        nt.links.new(Group_Input.outputs["Normal"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Group_008.inputs["Size"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_006.outputs["Output"], Group_009.inputs["Smooth"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_007.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Group_008.inputs["Smooth"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Group_009.inputs["Roughness"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Group_008.inputs["Roughness"])
        nt.links.new(Reroute_003.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Group_009.inputs["Normal"])
        nt.links.new(Reroute.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Group_Input.outputs["Roughness"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Group_008.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Base Color"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Group_008.inputs["Color"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Map_Range.outputs["Result"], Mix_Shader_001.inputs["Fac"])
        nt.links.new(Mix_Shader_001.outputs["Shader"], Add_Shader.inputs["Shader"])
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader_002.inputs["Shader"])
        nt.links.new(Add_Shader.outputs["Shader"], Mix_Shader_002.inputs["Shader"])
        nt.links.new(Group_Input_004.outputs["Alpha"], Mix_Shader_002.inputs["Fac"])
        nt.links.new(Mix_Shader_002.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Reroute_004.outputs["Output"], Group_009.inputs["Size"])
        nt.links.new(Group_010.outputs["Fresnel"], Mix_Shader.inputs["Fac"])
        nt.links.new(Reroute_018.outputs["Output"], Group_001.inputs["Color"])
        nt.links.new(Reroute_011.outputs["Output"], Group_001.inputs["Size"])
        nt.links.new(Reroute_012.outputs["Output"], Group_001.inputs["Smooth"])
        nt.links.new(Reroute_013.outputs["Output"], Group_001.inputs["Roughness"])
        nt.links.new(Reroute_014.outputs["Output"], Group_001.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Tangent"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Group_009.inputs["Tangent"])
        nt.links.new(Reroute_021.outputs["Output"], Group_001.inputs["Tangent"])
        nt.links.new(Reroute_019.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Group_Input_003.outputs["Metal"], Map_Range.inputs["Value"])
        nt.links.new(Group_Input.outputs["Specular Color"], Reroute_022.inputs["Input"])
        nt.links.new(Reroute_022.outputs["Output"], Reroute_023.inputs["Input"])
        nt.links.new(Reroute_023.outputs["Output"], Group_009.inputs["Color"])
        nt.links.new(Group_Input.outputs["Edge Tint"], Reroute_024.inputs["Input"])
        nt.links.new(Reroute_024.outputs["Output"], Reroute_025.inputs["Input"])
        nt.links.new(Reroute_025.outputs["Output"], Group_001.inputs["Edge Tint"])
        nt.links.new(Group_001.outputs["Shader"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Reroute_027.inputs["Input"])
        nt.links.new(Reroute_027.outputs["Output"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Reroute_028.inputs["Input"])
        nt.links.new(Reroute_028.outputs["Output"], Reroute_029.inputs["Input"])
        nt.links.new(Reroute_029.outputs["Output"], Mix_Shader_001.inputs["Shader"])