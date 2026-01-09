import bpy
from ..utils import ShaderNode


class ShaderNodeAddFrequentHairHighlight(ShaderNode):
    bl_label = "Add Frequent Hair Highlight"
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
            Fac_socket = nt.interface.new_socket(
                name="Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fac_socket.default_value = 1.0
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Toon_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Mix_High_And_Low_Frequent_socket = nt.interface.new_socket(
                name="Mix High And Low Frequent",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_High_And_Low_Frequent_socket.default_value = 0.5
        Mix_High_And_Low_Frequent_socket.min_value = -10.0
        Mix_High_And_Low_Frequent_socket.max_value = 10.0
        Mix_High_And_Low_Frequent_socket.subtype = "FACTOR"
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 0.0
        Size_socket.min_value = -10.0
        Size_socket.max_value = 10.0
        Size_socket.subtype = "FACTOR"
            Frequency_socket = nt.interface.new_socket(
                name="Frequency",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Frequency_socket.default_value = 1.0
        Frequency_socket.min_value = -10.0
        Frequency_socket.max_value = 10.0
        Frequency_socket.subtype = "NONE"
            Fill_Gap_socket = nt.interface.new_socket(
                name="Fill Gap",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fill_Gap_socket.default_value = 0.0
        Fill_Gap_socket.min_value = -1.0
        Fill_Gap_socket.max_value = 1.0
        Fill_Gap_socket.subtype = "FACTOR"
            Offset-Z_socket = nt.interface.new_socket(
                name="Offset-Z",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Offset-Z_socket.default_value = 0.0
        Offset-Z_socket.min_value = -10.0
        Offset-Z_socket.max_value = 10.0
        Offset-Z_socket.subtype = "FACTOR"
            Z-View_Instensity_socket = nt.interface.new_socket(
                name="Z-View Instensity",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Z-View_Instensity_socket.default_value = 0.0
        Z-View_Instensity_socket.min_value = 0.0
        Z-View_Instensity_socket.max_value = 1.0
        Z-View_Instensity_socket.subtype = "FACTOR"
            Z-limit_-_top_socket = nt.interface.new_socket(
                name="Z-limit - top",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Z-limit_-_top_socket.default_value = 0.4000000059604645
        Z-limit_-_top_socket.min_value = 0.0
        Z-limit_-_top_socket.max_value = 1.0
        Z-limit_-_top_socket.subtype = "FACTOR"
            Z-limit-_bot_socket = nt.interface.new_socket(
                name="Z-limit- bot",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Z-limit-_bot_socket.default_value = 0.6000000238418579
        Z-limit-_bot_socket.min_value = 0.0
        Z-limit-_bot_socket.max_value = 1.0
        Z-limit-_bot_socket.subtype = "FACTOR"
            Planar_UV_socket = nt.interface.new_socket(
                name="Planar UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Planar_UV_socket.default_value = (0.0, 0.0, 0.0)
        Planar_UV_socket.subtype = "NONE"

        # Create nodes
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (67.27474975585938, -90.52102661132812)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (2401.167724609375, 214.02178955078125)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (1178.237060546875, 68.4765625)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (1937.5301513671875, 552.9666748046875)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (319.7497863769531, 402.4115905761719)
        Separate_XYZ_001 = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ_001.location = (91.67711639404297, -97.78819274902344)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (316.1763000488281, -63.783966064453125)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 0.5
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-901.0721435546875, -395.74884033203125)
        Combine_XYZ.inputs["Y"].default_value = 1.0
        Combine_XYZ.inputs["Z"].default_value = 1.0
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (672.839599609375, 10.947555541992188)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (892.839599609375, 6.9261474609375)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "ADD"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (3758.053466796875, 415.5412902832031)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (453.143310546875, -5.1380157470703125)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (750.570556640625, 52.86041259765625)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Map_Range_001 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_001.location = (191.312255859375, -176.08584594726562)
        Map_Range_001.data_type = "FLOAT"
        Map_Range_001.interpolation_type = "LINEAR"
        Map_Range_001.inputs["To Min"].default_value = 1.0
        Map_Range_001.inputs["To Max"].default_value = 0.0
        Map_Range_001.inputs["Steps"].default_value = 4.0
        Map_Range_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Math_005 = nt.nodes.new("ShaderNodeMath")
        Math_005.location = (-22.70556640625, -414.4844970703125)
        Math_005.operation = "ADD"
        Math_005.inputs["Value"].default_value = 0.10000000149011612
        Math_005.inputs["Value"].default_value = 0.5
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (411.16314697265625, 25.117401123046875)
        Math_004.operation = "MINIMUM"
        Math_004.inputs["Value"].default_value = 0.5
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (191.312255859375, 91.26068115234375)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-136.16873168945312, -241.92381286621094)
        Math_003.operation = "SUBTRACT"
        Math_003.inputs["Value"].default_value = 0.5
        Math_003.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (107.3121337890625, -314.4951171875)
        Math_002.operation = "ADD"
        Math_002.inputs["Value"].default_value = 0.5
        Bright/Contrast = nt.nodes.new("ShaderNodeBrightContrast")
        Bright/Contrast.location = (-332.8984069824219, -232.31329345703125)
        Bright/Contrast.inputs["Bright"].default_value = 0.0
        Noise_Texture_001 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_001.location = (-576.3134765625, 241.05685424804688)
        Noise_Texture_001.inputs["W"].default_value = 0.0
        Noise_Texture_001.inputs["Scale"].default_value = 19.299999237060547
        Noise_Texture_001.inputs["Detail"].default_value = 0.0
        Noise_Texture_001.inputs["Roughness"].default_value = 0.5416666865348816
        Noise_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_001.inputs["Offset"].default_value = 0.0
        Noise_Texture_001.inputs["Gain"].default_value = 1.0
        Noise_Texture_001.inputs["Distortion"].default_value = 0.0
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (-576.3134765625, -188.19239807128906)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Scale"].default_value = 19.299999237060547
        Noise_Texture.inputs["Detail"].default_value = 0.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5416666865348816
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        Bright/Contrast_001 = nt.nodes.new("ShaderNodeBrightContrast")
        Bright/Contrast_001.location = (-332.8984069824219, 144.63406372070312)
        Bright/Contrast_001.inputs["Contrast"].default_value = 10.0
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (-901.0721435546875, -249.64097595214844)
        Combine_XYZ_001.inputs["X"].default_value = 0.0
        Combine_XYZ_001.inputs["Z"].default_value = 0.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1315.73828125, -166.83926391601562)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (217.406005859375, -328.24664306640625)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-6.943103790283203, -228.60220336914062)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-579.94970703125, -78.72930908203125)
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-690.157958984375, -50.762939453125)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Separate_XYZ = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ.location = (-491.17547607421875, 24.411346435546875)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (-234.0723876953125, -261.3712463378906)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (-19.554443359375, -102.7694091796875)
        Mix_004.data_type = "FLOAT"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_004.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-312.0650634765625, -321.73260498046875)
        Vector_Math.operation = "MULTIPLY"
        Vector_Math.inputs["Vector"].default_value = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (-128.3623504638672, -147.65667724609375)
        Vector_Math_001.operation = "ADD"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Vector_Transform_001 = nt.nodes.new("ShaderNodeVectorTransform")
        Vector_Transform_001.location = (-505.9357604980469, -305.82958984375)
        Vector_Transform_001.vector_type = "VECTOR"
        Vector_Transform_001.convert_from = "WORLD"
        Vector_Transform_001.convert_to = "WORLD"
        Vector_Transform_001.inputs["Vector"].default_value = (0.0, 0.0, 1.0)
        Vector_Transform = nt.nodes.new("ShaderNodeVectorTransform")
        Vector_Transform.location = (-348.9312438964844, -74.17208862304688)
        Vector_Transform.vector_type = "VECTOR"
        Vector_Transform.convert_from = "WORLD"
        Vector_Transform.convert_to = "CAMERA"
        Vector_Transform.inputs["Vector"].default_value = (0.0, 0.0, 1.0)
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (-93.420166015625, 38.51716613769531)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (-4.795166015625, 190.06027221679688)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (251.603271484375, -13.38519287109375)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        ColorRamp_002 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_002.location = (-92.369873046875, -177.6376953125)
        ColorRamp_002.color_ramp.color_mode = "HSV"
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (3514.0, 428.03900146484375)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MIX"
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_006 = nt.nodes.new("NodeGroupInput")
        Group_Input_006.location = (3166.365478515625, 567.7608032226562)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (1372.73291015625, 701.7479248046875)
        # Create links
        nt.links.new(Math_002.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Separate_XYZ_001.outputs["Z"], Math_001.inputs["Value"])
        nt.links.new(Vector_Math_001.outputs["Vector"], Separate_XYZ_001.inputs["Vector"])
        nt.links.new(Mapping.outputs["Vector"], Separate_XYZ.inputs["Vector"])
        nt.links.new(Bright/Contrast.outputs["Color"], Math_003.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Separate_XYZ.outputs["X"], Noise_Texture.inputs["Vector"])
        nt.links.new(Separate_XYZ.outputs["Y"], Math_002.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Noise_Texture.outputs["Fac"], Bright/Contrast.inputs["Color"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping.inputs["Scale"])
        nt.links.new(Group_Input.outputs["Frequency"], Combine_XYZ.inputs["X"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Mapping.inputs["Location"])
        nt.links.new(Group_Input.outputs["Offset-Z"], Combine_XYZ_001.inputs["Y"])
        nt.links.new(Map_Range.outputs["Result"], Math_004.inputs["Value"])
        nt.links.new(Map_Range_001.outputs["Result"], Math_004.inputs["Value"])
        nt.links.new(Group_Input_002.outputs["Z-View Instensity"], Math_001.inputs["Value"])
        nt.links.new(Group_Input_003.outputs["Z-limit - top"], Map_Range.inputs["From Min"])
        nt.links.new(Group_Input_003.outputs["Z-limit- bot"], Map_Range_001.inputs["From Max"])
        nt.links.new(Group_Input_003.outputs["Z-limit - top"], Math_005.inputs["Value"])
        nt.links.new(Math_005.outputs["Value"], Map_Range.inputs["From Max"])
        nt.links.new(Math_005.outputs["Value"], Map_Range_001.inputs["From Min"])
        nt.links.new(Mix_003.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Mix_005.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input_004.outputs["Color"], Mix_001.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Group_Input_004.outputs["Combined"], Mix_002.inputs["B"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix_003.inputs["A"])
        nt.links.new(ColorRamp_002.outputs["Color"], Mix_003.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Size"], Bright/Contrast.inputs["Contrast"])
        nt.links.new(Noise_Texture_001.outputs["Fac"], Bright/Contrast_001.inputs["Color"])
        nt.links.new(Separate_XYZ.outputs["X"], Noise_Texture_001.inputs["Vector"])
        nt.links.new(Bright/Contrast_001.outputs["Color"], Mix_004.inputs["Factor"])
        nt.links.new(Math.outputs["Value"], Map_Range.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Map_Range_001.inputs["Value"])
        nt.links.new(Math_004.outputs["Value"], Mix_004.inputs["A"])
        nt.links.new(Mix_004.outputs["Result"], ColorRamp_001.inputs["Fac"])
        nt.links.new(Mix_004.outputs["Result"], ColorRamp_002.inputs["Fac"])
        nt.links.new(Group_Input_001.outputs["Fill Gap"], Bright/Contrast_001.inputs["Bright"])
        nt.links.new(Group_Input.outputs["Planar UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input_005.outputs["Toon"], Mix.inputs["Factor"])
        nt.links.new(Vector_Transform_001.outputs["Vector"], Vector_Math.inputs["Vector"])
        nt.links.new(Vector_Transform.outputs["Vector"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Vector_Math.outputs["Vector"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Group_Input_004.outputs["Mix High And Low Frequent"], Mix_003.inputs["Factor"])
        nt.links.new(Group_Input_006.outputs["Fac"], Mix_005.inputs["Factor"])
        nt.links.new(Group_Input_004.outputs["Combined"], Mix_005.inputs["A"])
        nt.links.new(Mix_002.outputs["Result"], Mix_005.inputs["B"])