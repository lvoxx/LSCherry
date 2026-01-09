import bpy
from ..utils import ShaderNode


class ShaderNodeBuildNoseRamp(ShaderNode):
    bl_label = "Build Nose Ramp"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 0.0
        Shading_socket.min_value = -3.4028234663852886e+38
        Shading_socket.max_value = 3.4028234663852886e+38
        Shading_socket.subtype = "NONE"

        # Input sockets
            Face_Ramp_(Required)_socket = nt.interface.new_socket(
                name="Face Ramp (Required)",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Face_Ramp_(Required)_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Face_Value_socket = nt.interface.new_socket(
                name="Face Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Value_socket.default_value = 0.5
        Face_Value_socket.min_value = -10000.0
        Face_Value_socket.max_value = 10000.0
        Face_Value_socket.subtype = "NONE"
            Face_Map_socket = nt.interface.new_socket(
                name="Face Map",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Map_socket.default_value = 0.5
        Face_Map_socket.min_value = -10000.0
        Face_Map_socket.max_value = 10000.0
        Face_Map_socket.subtype = "NONE"

        # Create nodes
        Group_005 = nt.nodes.new("ShaderNodeGroup")
        Group_005.location = (0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-255.17320251464844, -22.679298400878906)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (589.21484375, 146.9224395751953)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (390.765869140625, 294.1714782714844)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (211.45297241210938, 47.657386779785156)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (183.55177307128906, 415.6323547363281)
        # Create links
        nt.links.new(Group_Input.outputs["Face Value"], Group_005.inputs["Face Value"])
        nt.links.new(Group_Input.outputs["Face Map"], Group_005.inputs["Face Map"])
        nt.links.new(Invert_Color.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Group_005.outputs["Custom Ramp"], Invert_Color.inputs["Color"])
        nt.links.new(Group_Input.outputs["Face Ramp (Required)"], Mix.inputs["Factor"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Shading"])