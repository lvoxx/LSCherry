import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Freckles(ShaderNode):
    bl_label = "SST1: Freckles"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Input sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 1.0
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
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (-89.63232421875, 271.0816650390625)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-484.948486328125, 163.66796875)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (-87.31494140625, 16.7813720703125)
        ColorRamp.color_ramp.color_mode = "RGB"
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (-273.95166015625, 20.8126220703125)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Detail"].default_value = 2.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        Noise_Texture_001 = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture_001.location = (-274.65576171875, 277.53857421875)
        Noise_Texture_001.inputs["W"].default_value = 0.0
        Noise_Texture_001.inputs["Detail"].default_value = 2.0
        Noise_Texture_001.inputs["Roughness"].default_value = 0.5
        Noise_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture_001.inputs["Offset"].default_value = 0.0
        Noise_Texture_001.inputs["Gain"].default_value = 1.0
        Noise_Texture_001.inputs["Distortion"].default_value = 0.0
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1141.6102294921875, 35.50736999511719)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (262.88037109375, 87.5010986328125)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "ADD"
        Mix_001.inputs["Factor"].default_value = 1.0
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (904.4683837890625, 65.1212387084961)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1042.2847900390625, -3.0976333618164062)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (687.060302734375, 124.13150787353516)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MULTIPLY"
        Mix_003.inputs["Factor"].default_value = 1.0
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (509.4871826171875, -12.657180786132812)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (500.6427917480469, -80.82946014404297)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-708.9114379882812, -96.78730010986328)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (686.4815063476562, -112.39985656738281)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (-487.8265380859375, -149.1704864501953)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (265.968994140625, -198.3126678466797)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (77.4271240234375, 369.846923828125)
        # Create links
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping.inputs["Scale"])
        nt.links.new(Group_Input.outputs["Scale Small"], Noise_Texture_001.inputs["Scale"])
        nt.links.new(Noise_Texture.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture.inputs["Vector"])
        nt.links.new(ColorRamp.outputs["Color"], Mix_001.inputs["A"])
        nt.links.new(Noise_Texture_001.outputs["Color"], ColorRamp_001.inputs["Fac"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix_001.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture_001.inputs["Vector"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Builder"])
        nt.links.new(Math.outputs["Value"], Mix_003.inputs["B"])
        nt.links.new(Mix_003.outputs["Result"], Mix.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Factor"], Mix_003.inputs["A"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["Y"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["Z"])
        nt.links.new(Group_Input_002.outputs["Builder"], Mix.inputs["A"])
        nt.links.new(Group_Input_002.outputs["Red Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input_003.outputs["Scale Big"], Noise_Texture.inputs["Scale"])
        nt.links.new(Group_Input_004.outputs["Intensity"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])