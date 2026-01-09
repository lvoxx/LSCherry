import bpy
from ..utils import ShaderNode


class ShaderNodeSimplePantyhose(ShaderNode):
    bl_label = "Simple Pantyhose"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "NONE"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.8055135011672974, 0.8055135011672974, 0.8055135011672974, 1.0)
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Pattern_socket.default_value = 0.0
        Pattern_socket.min_value = -3.4028234663852886e+38
        Pattern_socket.max_value = 3.4028234663852886e+38
        Pattern_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Input sockets
            --_DEPRECATED_--_socket = nt.interface.new_socket(
                name="-- DEPRECATED --",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Enable_Dot_socket = nt.interface.new_socket(
                name="Enable Dot",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Enable_Dot_socket.default_value = False
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (0.685835599899292, 0.685835599899292, 0.685835599899292, 1.0)
            Highlight_Color_socket = nt.interface.new_socket(
                name="Highlight Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Highlight_Color_socket.default_value = (1.0, 0.6242283582687378, 0.5513602495193481, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 8.0
        Size_socket.min_value = 1.0
        Size_socket.max_value = 100.0
        Size_socket.subtype = "NONE"
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.20000000298023224
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1564.8671875, 290.7862548828125)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1259.8253173828125, 46.66898727416992)
        Voronoi_Texture = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture.location = (-283.23663330078125, 318.64459228515625)
        Voronoi_Texture.inputs["W"].default_value = 0.0
        Voronoi_Texture.inputs["Detail"].default_value = 0.0
        Voronoi_Texture.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture.inputs["Randomness"].default_value = 1.0
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-561.6070556640625, 323.682861328125)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Voronoi_Texture_001 = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture_001.location = (-283.23663330078125, -51.00897216796875)
        Voronoi_Texture_001.inputs["W"].default_value = 0.0
        Voronoi_Texture_001.inputs["Detail"].default_value = 0.0
        Voronoi_Texture_001.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture_001.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture_001.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture_001.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture_001.inputs["Randomness"].default_value = 1.0
        Mapping_001 = nt.nodes.new("ShaderNodeMapping")
        Mapping_001.location = (-561.6070556640625, -25.392303466796875)
        Mapping_001.vector_type = "POINT"
        Mapping_001.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Rotation"].default_value = (0.0, 0.0, 1.5707963705062866)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (10.09716796875, 253.45834350585938)
        Mix.data_type = "RGBA"
        Mix.blend_type = "DARKEN"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-980.0739135742188, -105.99383544921875)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 10.0
        Math.inputs["Value"].default_value = 0.5
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-779.8394775390625, -30.49593734741211)
        Combine_XYZ.inputs["Y"].default_value = 1.0
        Combine_XYZ.inputs["Z"].default_value = 1.0
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-559.0631103515625, -323.682861328125)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 100.0
        Math_001.inputs["Value"].default_value = 0.5
        Color_Ramp = nt.nodes.new("ShaderNodeValToRGB")
        Color_Ramp.location = (226.18603515625, 246.9811248779297)
        Color_Ramp.color_ramp.color_mode = "RGB"
        Bump = nt.nodes.new("ShaderNodeBump")
        Bump.location = (556.9907836914062, 241.77159118652344)
        Bump.inputs["Strength"].default_value = 0.25
        Bump.inputs["Distance"].default_value = 1.0
        Bump.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Specular_BSDF = nt.nodes.new("ShaderNodeEeveeSpecular")
        Specular_BSDF.location = (792.5206909179688, 317.7504577636719)
        Specular_BSDF.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        Specular_BSDF.inputs["Specular"].default_value = (0.14003700017929077, 0.14003700017929077, 0.14003700017929077, 1.0)
        Specular_BSDF.inputs["Emissive Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        Specular_BSDF.inputs["Transparency"].default_value = 0.0
        Specular_BSDF.inputs["Clear Coat"].default_value = 0.0
        Specular_BSDF.inputs["Clear Coat Roughness"].default_value = 0.0
        Specular_BSDF.inputs["Clear Coat Normal"].default_value = (0.0, 0.0, 0.0)
        Specular_BSDF.inputs["Weight"].default_value = 0.0
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (980.0739135742188, 297.0311584472656)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (556.96923828125, 303.726806640625)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (1282.4886474609375, -20.238998413085938)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "DODGE"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (1285.8177490234375, -244.6519775390625)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (756.4066772460938, 380.5945129394531)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (1478.68359375, 380.5945129394531)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-182.685546875, 457.8871765136719)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (798.9196166992188, 18.010482788085938)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (600.055419921875, -7.453155517578125)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1282.4886474609375, 216.66436767578125)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (982.3959350585938, 188.62124633789062)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (993.73095703125, 20.206893920898438)
        Math_002.operation = "ADD"
        Math_002.inputs["Value"].default_value = 0.10000000149011612
        Math_002.inputs["Value"].default_value = 0.5
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-181.8687744140625, 528.9346313476562)
        # Create links
        nt.links.new(Mapping_001.outputs["Vector"], Voronoi_Texture_001.inputs["Vector"])
        nt.links.new(Bump.outputs["Normal"], Specular_BSDF.inputs["Normal"])
        nt.links.new(Math_001.outputs["Value"], Voronoi_Texture_001.inputs["Scale"])
        nt.links.new(Math.outputs["Value"], Combine_XYZ.inputs["X"])
        nt.links.new(Specular_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Math.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Color_Ramp.outputs["Color"], Bump.inputs["Height"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping_001.inputs["Scale"])
        nt.links.new(Voronoi_Texture_001.outputs["Distance"], Mix.inputs["B"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping.inputs["Scale"])
        nt.links.new(Mix.outputs["Result"], Color_Ramp.inputs["Fac"])
        nt.links.new(Voronoi_Texture.outputs["Distance"], Mix.inputs["A"])
        nt.links.new(Mapping.outputs["Vector"], Voronoi_Texture.inputs["Vector"])
        nt.links.new(Math_001.outputs["Value"], Voronoi_Texture.inputs["Scale"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input.outputs["UV"], Mapping_001.inputs["Vector"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Size"], Math.inputs["Value"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input_002.outputs["Base Color"], Mix_001.inputs["A"])
        nt.links.new(Group_Input_002.outputs["Highlight Color"], Mix_001.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Roughness"], Specular_BSDF.inputs["Roughness"])
        nt.links.new(Bump.outputs["Normal"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Group_Output.inputs["Normal"])
        nt.links.new(Attribute.outputs["Fac"], Group.inputs["Light Dir"])
        nt.links.new(Bump.outputs["Normal"], Group.inputs["Normal"])
        nt.links.new(Group_Input_003.outputs["Enable Dot"], Mix_002.inputs["Factor"])
        nt.links.new(Math_002.outputs["Value"], Mix_002.inputs["B"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Mix_002.inputs["A"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Pattern"])
        nt.links.new(Group.outputs["Specular"], Math_002.inputs["Value"])