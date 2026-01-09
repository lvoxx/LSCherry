import bpy
from ..utils import ShaderNode


class ShaderNodeStylizedFresnel(ShaderNode):
    bl_label = "Stylized Fresnel"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Fresnel_socket = nt.interface.new_socket(
                name="Fresnel",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fresnel_socket.default_value = 0.0
        Fresnel_socket.min_value = -1.0
        Fresnel_socket.max_value = 1.0
        Fresnel_socket.subtype = "NONE"

        # Input sockets
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.0
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (36.82098388671875, -101.02154541015625)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (4.189537048339844, 344.4308776855469)
        Fresnel = nt.nodes.new("ShaderNodeFresnel")
        Fresnel.location = (516.5775146484375, 0.0)
        Geometry_001 = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry_001.location = (-94.75682830810547, -270.8712158203125)
        Bump = nt.nodes.new("ShaderNodeBump")
        Bump.location = (-92.44503021240234, -89.64186096191406)
        Bump.inputs["Strength"].default_value = 0.0
        Bump.inputs["Distance"].default_value = 0.10000000149011612
        Bump.inputs["Height"].default_value = 1.0
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (177.30618286132812, -47.9111328125)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (693.9759521484375, 0.0)
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-57.642555236816406, -39.89361572265625)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (179.46578979492188, -55.05224609375)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-17.78949546813965, -254.08999633789062)
        Math.operation = "DIVIDE"
        Math.inputs["Value"].default_value = 1.0
        Math.inputs["Value"].default_value = 0.5
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-737.181396484375, 151.6472930908203)
        Value = nt.nodes.new("ShaderNodeValue")
        Value.location = (-512.1998901367188, 244.6036834716797)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (81.5069580078125, 491.5982971191406)
        # Create links
        nt.links.new(Fresnel.outputs["Fac"], Group_Output.inputs["Fresnel"])
        nt.links.new(Geometry.outputs["Backfacing"], Mix.inputs["Factor"])
        nt.links.new(Mix.outputs["Result"], Fresnel.inputs["IOR"])
        nt.links.new(Bump.outputs["Normal"], Mix_001.inputs["A"])
        nt.links.new(Geometry_001.outputs["Incoming"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Roughness"], Mix_001.inputs["Factor"])
        nt.links.new(Mix_001.outputs["Result"], Fresnel.inputs["Normal"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["B"])
        nt.links.new(Value.outputs["Value"], Mix.inputs["A"])
        nt.links.new(Value.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Normal"], Bump.inputs["Normal"])