import bpy
from ..utils import ShaderNode


class ShaderNodeSimpleToon(ShaderNode):
    bl_label = "Simple Toon"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Toon_socket.default_value = (0.0, 0.0, 0.0, 1.0)

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
            Use_Diffuse_socket = nt.interface.new_socket(
                name="Use Diffuse",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Use_Diffuse_socket.default_value = True
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (762.533447265625, 7.119321823120117)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-404.57110595703125, -1.3030028343200684)
        Group_008 = nt.nodes.new("ShaderNodeGroup")
        Group_008.location = (324.4455871582031, -74.18356323242188)
        Group_010 = nt.nodes.new("ShaderNodeGroup")
        Group_010.location = (327.2247619628906, 111.55999755859375)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (319.92144775390625, 276.4154357910156)
        Math_001.operation = "GREATER_THAN"
        Math_001.inputs["Value"].default_value = 0.0
        Math_001.inputs["Value"].default_value = 0.5
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (577.43115234375, 78.74671936035156)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-72.2286376953125, 444.8995361328125)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-44.9328498840332, -53.439727783203125)
        # Create links
        nt.links.new(Group_Input.outputs["AO Fac"], Group_010.inputs["AO Fac"])
        nt.links.new(Group_Input.outputs["Normal"], Group_008.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Roughness"], Group_010.inputs["Roughness"])
        nt.links.new(Group_Input.outputs["Use Diffuse"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Mix_001.inputs["Factor"])
        nt.links.new(Group_008.outputs["NdotL"], Mix_001.inputs["A"])
        nt.links.new(Group_010.outputs["Toon"], Mix_001.inputs["B"])
        nt.links.new(Group_010.outputs["Toon"], Mix_001.inputs["B"])
        nt.links.new(Group_008.outputs["NdotL"], Mix_001.inputs["A"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Toon"])
        nt.links.new(Group.outputs["Normal"], Group_010.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Group.inputs["Normal"])