import bpy
from ..utils import ShaderNode


class ShaderNodeSst1Pores(ShaderNode):
    bl_label = "SST1: Pores"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Pores_socket = nt.interface.new_socket(
                name="Pores",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Pores_socket.default_value = (0.0, 0.0, 0.0, 0.0)
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Input sockets
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
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Create nodes
        Voronoi_Texture_001 = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture_001.location = (-68.9775390625, 171.57217407226562)
        Voronoi_Texture_001.inputs["W"].default_value = 0.0
        Voronoi_Texture_001.inputs["Scale"].default_value = 800.0
        Voronoi_Texture_001.inputs["Detail"].default_value = 0.0
        Voronoi_Texture_001.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture_001.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture_001.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture_001.inputs["Randomness"].default_value = 0.6000000238418579
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (150.834228515625, 209.84768676757812)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-290.802490234375, -209.84765625)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 1.5707963705062866)
        Mapping_002 = nt.nodes.new("ShaderNodeMapping")
        Mapping_002.location = (-295.344482421875, 169.09503173828125)
        Mapping_002.vector_type = "POINT"
        Mapping_002.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping_002.inputs["Rotation"].default_value = (0.0, 0.0, 0.7853981852531433)
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (155.376220703125, -169.0950927734375)
        ColorRamp.color_ramp.color_mode = "RGB"
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-993.4130859375, -210.604736328125)
        Voronoi_Texture = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture.location = (-64.435546875, -207.37060546875)
        Voronoi_Texture.inputs["W"].default_value = 0.0
        Voronoi_Texture.inputs["Scale"].default_value = 1000.0
        Voronoi_Texture.inputs["Detail"].default_value = 0.0
        Voronoi_Texture.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture.inputs["Randomness"].default_value = 0.6000000238418579
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1244.4354248046875, 11.449897766113281)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (475.344482421875, 15.2484130859375)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (849.596923828125, 142.86874389648438)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (612.0170288085938, 133.4027557373047)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-643.5103759765625, -309.8591613769531)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (321.23974609375, 312.2937316894531)
        # Create links
        nt.links.new(Mapping.outputs["Vector"], Voronoi_Texture.inputs["Vector"])
        nt.links.new(Voronoi_Texture.outputs["Distance"], ColorRamp.inputs["Fac"])
        nt.links.new(Mapping_002.outputs["Vector"], Voronoi_Texture_001.inputs["Vector"])
        nt.links.new(Voronoi_Texture_001.outputs["Distance"], ColorRamp_001.inputs["Fac"])
        nt.links.new(ColorRamp.outputs["Color"], Mix.inputs["A"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Pores"])
        nt.links.new(Group_Input_001.outputs["Factor"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["X"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping.inputs["Scale"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping_002.inputs["Scale"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["Y"])
        nt.links.new(Group_Input.outputs["Scale"], Combine_XYZ.inputs["Z"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_002.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Group_Output.inputs["UV"])