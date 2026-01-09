import bpy
from ..utils import ShaderNode


class ShaderNodeStackedToonBuilder(ShaderNode):
    bl_label = "Stacked Toon Builder"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Shading_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Pattern_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Enable_Dot_socket = nt.interface.new_socket(
                name="Enable Dot",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Enable_Dot_socket.default_value = False
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (722.85595703125, 88.46595764160156)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (338.7626037597656, 204.41661071777344)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (112.65667724609375, 207.96243286132812)
        Group_013.inputs["AO Fac"].default_value = 1.0
        Group_013.inputs["Roughness"].default_value = 0.0
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (112.65667724609375, 59.0443115234375)
        Group_014.inputs["Invert MLight"].default_value = False
        Group_014.inputs["Mix Light and View"].default_value = 0.0
        Group_015 = nt.nodes.new("ShaderNodeGroup")
        Group_015.location = (-169.65121459960938, -197.87451171875)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (50.4844970703125, -207.96240234375)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (50.4844970703125, -152.8009033203125)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (50.4844970703125, 83.60595703125)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (112.65667724609375, -179.28424072265625)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (338.7626037597656, 146.1382598876953)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (522.3208618164062, 144.94757080078125)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (338.7626037597656, -85.50379943847656)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-169.65121459960938, -136.41592407226562)
        # Create links
        nt.links.new(Group_015.outputs["Normal"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Group_014.inputs["Normal"])
        nt.links.new(Reroute_010.outputs["Output"], Group_013.inputs["Normal"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Attribute.outputs["Vector"], Group_014.inputs["Light Dir"])
        nt.links.new(Group_013.outputs["Toon"], Mix.inputs["A"])
        nt.links.new(Group_014.outputs["NdotL"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Enable Dot"], Mix.inputs["Factor"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Shading"])
        nt.links.new(Mix.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Group_Input_001.outputs["Pattern"], Mix_002.inputs["B"])
        nt.links.new(Group_Input_002.outputs["Normal"], Group_015.inputs["Normal"])