import bpy
from ..utils import ShaderNode


class ShaderNodeHi3BuildRampFromMap(ShaderNode):
    bl_label = "HI3: Build Ramp From Map"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Input sockets
            Shadow_Factor_socket = nt.interface.new_socket(
                name="Shadow Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Factor_socket.default_value = 1.0
        Shadow_Factor_socket.min_value = 0.0
        Shadow_Factor_socket.max_value = 1.0
        Shadow_Factor_socket.subtype = "FACTOR"
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Toon_socket.default_value = 0.0
        Toon_socket.min_value = 0.0
        Toon_socket.max_value = 1.0
        Toon_socket.subtype = "NONE"
            Shadow_Mask_socket = nt.interface.new_socket(
                name="Shadow Mask",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Mask_socket.default_value = 0.0
        Shadow_Mask_socket.min_value = 0.0
        Shadow_Mask_socket.max_value = 1.0
        Shadow_Mask_socket.subtype = "NONE"
            Ramp_Size_socket = nt.interface.new_socket(
                name="Ramp Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Ramp_Size_socket.default_value = 0.800000011920929
        Ramp_Size_socket.min_value = 0.0
        Ramp_Size_socket.max_value = 1.0
        Ramp_Size_socket.subtype = "FACTOR"
            Value_Enhance_socket = nt.interface.new_socket(
                name="Value Enhance",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Value_Enhance_socket.default_value = 0.10000000149011612
        Value_Enhance_socket.min_value = 0.0
        Value_Enhance_socket.max_value = 1.0
        Value_Enhance_socket.subtype = "FACTOR"

        # Create nodes
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-112.73562622070312, -19.041732788085938)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (338.5034484863281, 25.050386428833008)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (112.73562622070312, 19.041732788085938)
        Group_009.inputs["Ramp Size"].default_value = 0.5
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-346.350830078125, -129.3411865234375)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-590.9628295898438, -61.165870666503906)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-212.16744995117188, 139.50607299804688)
        # Create links
        nt.links.new(Mix.outputs["Result"], Group_009.inputs["Toon"])
        nt.links.new(Group_009.outputs["UV"], Group_Output.inputs["UV"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Shadow Mask"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Shadow Factor"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Toon"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Value Enhance"], Math.inputs["Value"])