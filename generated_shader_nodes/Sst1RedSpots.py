import bpy
from ..utils import ShaderNode


class ShaderNodeSst1RedSpots(ShaderNode):
    bl_label = "SST1: Red Spots"
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
            Red_Color_socket = nt.interface.new_socket(
                name="Red Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Red_Color_socket.default_value = (0.800000011920929, 0.17122192680835724, 0.12063717842102051, 1.0)
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
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        Noise_Texture = nt.nodes.new("ShaderNodeTexNoise")
        Noise_Texture.location = (46.086669921875, 265.0802001953125)
        Noise_Texture.inputs["W"].default_value = 0.0
        Noise_Texture.inputs["Detail"].default_value = 5.0
        Noise_Texture.inputs["Roughness"].default_value = 0.5
        Noise_Texture.inputs["Lacunarity"].default_value = 2.0
        Noise_Texture.inputs["Offset"].default_value = 0.0
        Noise_Texture.inputs["Gain"].default_value = 1.0
        Noise_Texture.inputs["Distortion"].default_value = 0.0
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (993.7029418945312, 140.7958984375)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (573.16357421875, 216.23831176757812)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-178.39503479003906, 309.87493896484375)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Scale"].default_value = (30.0, 30.0, 90.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (764.7683715820312, 177.51364135742188)
        Mix.data_type = "RGBA"
        Mix.blend_type = "SOFT_LIGHT"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (218.72705078125, 261.156494140625)
        ColorRamp.color_ramp.color_mode = "RGB"
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-508.80126953125, 132.2281951904297)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (302.87969970703125, 32.742733001708984)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (378.9102783203125, 397.6151428222656)
        # Create links
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Builder"])
        nt.links.new(Noise_Texture.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(Mapping.outputs["Vector"], Noise_Texture.inputs["Vector"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(ColorRamp.outputs["Color"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Scale"], Noise_Texture.inputs["Scale"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input_002.outputs["Builder"], Mix.inputs["A"])
        nt.links.new(Group_Input_002.outputs["Red Color"], Mix.inputs["B"])
        nt.links.new(Group_Input_002.outputs["Strength"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])