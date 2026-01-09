import bpy
from ..utils import ShaderNode


class ShaderNodeAddHighlight(ShaderNode):
    bl_label = "Add Highlight"
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
        
        Combined_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = 0.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Pattern_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (319.3514099121094, 194.54754638671875)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-59.91670227050781, -58.99342346191406)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-188.16824340820312, -65.71331787109375)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-31.17645263671875, -62.74810791015625)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "ADD"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (639.4234008789062, 141.6680145263672)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (-42.00877380371094, -54.46623992919922)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (56.424354553222656, -37.779579162597656)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-577.090576171875, 16.47336769104004)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (461.833984375, 379.9659423828125)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (9.704864501953125, 360.41473388671875)
        # Create links
        nt.links.new(Group_Input.outputs["Shading"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Pattern"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Combined"], Mix_001.inputs["A"])
        nt.links.new(Group_Input.outputs["Color"], Mix_002.inputs["B"])
        nt.links.new(Group_Input.outputs["Shading"], Mix_002.inputs["A"])
        nt.links.new(Mix_002.outputs["Result"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Combined"], Mix_003.inputs["A"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_003.inputs["Factor"])
        nt.links.new(Mix_001.outputs["Result"], Mix_003.inputs["B"])
        nt.links.new(Mix_003.outputs["Result"], Group_Output.inputs["Combined"])