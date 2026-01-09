import bpy
from ..utils import ShaderNode


class ShaderNodeToonCore(ShaderNode):
    bl_label = "Toon Core"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Toon_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            AO_Fac_socket = nt.interface.new_socket(
                name="AO Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        AO_Fac_socket.default_value = 1.0
        AO_Fac_socket.min_value = 0.0
        AO_Fac_socket.max_value = 1.0
        AO_Fac_socket.subtype = "FACTOR"
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.0
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (138.1495361328125, 102.3504638671875)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (60.67625427246094, -398.3809814453125)
        Diffuse_BSDF = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF.location = (-199.08876037597656, -44.15856170654297)
        Diffuse_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Diffuse_BSDF.inputs["Weight"].default_value = 0.0
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (-5.5664825439453125, -50.39952850341797)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-321.73590087890625, -480.62371826171875)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (277.157958984375, -480.62371826171875)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-321.7359313964844, 2.2898635864257812)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-366.1334228515625, -354.88592529296875)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (507.2261657714844, 100.90921020507812)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "DARKEN"
        Mix_001.inputs["Factor"].default_value = 1.0
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-366.1334228515625, -42.12685012817383)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (668.8276977539062, 96.53599548339844)
        Ambient_Occlusion = nt.nodes.new("ShaderNodeAmbientOcclusion")
        Ambient_Occlusion.location = (-225.97164916992188, 248.52731323242188)
        Ambient_Occlusion.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Ambient_Occlusion.inputs["Distance"].default_value = 1.0
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (-45.820945739746094, 242.20018005371094)
        ColorRamp.color_ramp.color_mode = "RGB"
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (251.40228271484375, 225.54747009277344)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (1.0, 1.0, 1.0, 1.0)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (216.48170471191406, 61.402801513671875)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-761.1728515625, 37.70774841308594)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (63.59220886230469, 241.99301147460938)
        # Create links
        nt.links.new(Diffuse_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Toon"])
        nt.links.new(Ambient_Occlusion.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(ColorRamp.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Mix_001.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Roughness"], Diffuse_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["AO Fac"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Reroute_004.outputs["Output"], Diffuse_BSDF.inputs["Normal"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Ambient_Occlusion.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Reroute_004.inputs["Input"])