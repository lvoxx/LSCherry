import bpy
from ..utils import ShaderNode


class ShaderNodeStackNextToon(ShaderNode):
    bl_label = "Stack Next Toon"
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
        
        Shading_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Stack_socket = nt.interface.new_socket(
                name="Stack",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Stack_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Shading_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 0.0, 0.002265453338623047, 1.0)
            Stack_socket = nt.interface.new_socket(
                name="Stack",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Stack_socket.default_value = (0.0, 1.0, 0.018648559227585793, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 1.0
        Size_socket.min_value = 0.20000000298023224
        Size_socket.max_value = 1.0
        Size_socket.subtype = "FACTOR"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 0.05000000074505806
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "FACTOR"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (933.211181640625, 41.072174072265625)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-276.0687561035156, -12.879579544067383)
        Group_015 = nt.nodes.new("ShaderNodeGroup")
        Group_015.location = (-86.64947509765625, 69.92706298828125)
        Group_015.inputs["Disable Toon Style"].default_value = False
        Group_015.inputs["Fresnel (Required)"].default_value = 0.0
        Group_015.inputs["Toon Style"].default_value = (0.0, 0.0, 0.0)
        Group_015.inputs["Soft Shading Fac"].default_value = 0.0
        Group_015.inputs["Mix With Fresnel"].default_value = 0.0
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (753.0, -66.18302917480469)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "MIX"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (274.8832092285156, 47.685333251953125)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MULTIPLY"
        Mix_005.inputs["Factor"].default_value = 1.0
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (72.07156372070312, -114.37761688232422)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (142.769287109375, -229.2503204345703)
        # Create links
        nt.links.new(Group_Input.outputs["Shading"], Group_015.inputs["Shading"])
        nt.links.new(Group_Input_001.outputs["Color"], Mix_005.inputs["B"])
        nt.links.new(Mix_005.outputs["Result"], Mix_004.inputs["B"])
        nt.links.new(Group_015.outputs["Shading"], Mix_004.inputs["Factor"])
        nt.links.new(Group_015.outputs["Shading"], Mix_005.inputs["A"])
        nt.links.new(Group_Input.outputs["Size"], Group_015.inputs["Size"])
        nt.links.new(Group_Input.outputs["Smooth"], Group_015.inputs["Smooth"])
        nt.links.new(Group_Input_002.outputs["Stack"], Mix_004.inputs["A"])
        nt.links.new(Group_Input.outputs["Shading"], Group_Output.inputs["Shading"])
        nt.links.new(Mix_004.outputs["Result"], Group_Output.inputs["Stack"])