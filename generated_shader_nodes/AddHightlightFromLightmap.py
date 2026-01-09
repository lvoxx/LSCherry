import bpy
from ..utils import ShaderNode


class ShaderNodeAddHightlightFromLightmap(ShaderNode):
    bl_label = "Add HightLight From LightMap"
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
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)

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
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Toon_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            LightMap_socket = nt.interface.new_socket(
                name="LightMap",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        LightMap_socket.default_value = 1.0
        LightMap_socket.min_value = 0.0
        LightMap_socket.max_value = 1.0
        LightMap_socket.subtype = "NONE"
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Pattern_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (148.7164764404297, 93.66732788085938)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (856.4722900390625, 90.6350326538086)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (600.846435546875, 39.98954772949219)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (355.73150634765625, 68.42402648925781)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-7.785976409912109, -60.4461669921875)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-250.4407958984375, -208.58468627929688)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (336.9267578125, -104.95816040039062)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (198.70159912109375, 224.86952209472656)
        # Create links
        nt.links.new(Group_Input_002.outputs["Color"], Mix_001.inputs["B"])
        nt.links.new(Group_Input_002.outputs["LightMap"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Combined"], Group.inputs["Combined"])
        nt.links.new(Mix_001.outputs["Result"], Group.inputs["Color"])
        nt.links.new(Group.outputs["Combined"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_001.outputs["Pattern"], Group.inputs["Pattern"])
        nt.links.new(Group_Input.outputs["Toon"], Group.inputs["Shading"])
        nt.links.new(Group_Input_001.outputs["Fac"], Group.inputs["Fac"])