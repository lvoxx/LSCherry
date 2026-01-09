import bpy
from ..utils import ShaderNode


class ShaderNodeHsrBuildHeadPackage(ShaderNode):
    bl_label = "HSR: Build Head Package"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Head_Base_Texture_socket = nt.interface.new_socket(
                name="Head Base Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Head_Base_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Head_Lightmap_Texture_socket = nt.interface.new_socket(
                name="Head Lightmap Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Head_Lightmap_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Head_Colormap_Texture_socket = nt.interface.new_socket(
                name="Head Colormap Texture",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Head_Colormap_Texture_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Fake_Shadow_Factor_socket = nt.interface.new_socket(
                name="Fake Shadow Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fake_Shadow_Factor_socket.default_value = 0.0
        Fake_Shadow_Factor_socket.min_value = 0.0
        Fake_Shadow_Factor_socket.max_value = 1.0
        Fake_Shadow_Factor_socket.subtype = "NONE"
            Fake_Shadow_Color_socket = nt.interface.new_socket(
                name="Fake Shadow Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Fake_Shadow_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Blush_Factor_socket = nt.interface.new_socket(
                name="Blush Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Blush_Factor_socket.default_value = 0.0
        Blush_Factor_socket.min_value = 0.0
        Blush_Factor_socket.max_value = 1.0
        Blush_Factor_socket.subtype = "FACTOR"
            Bright_Color_socket = nt.interface.new_socket(
                name="Bright Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Bright_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Mood_Down_Factor_socket = nt.interface.new_socket(
                name="Mood Down Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mood_Down_Factor_socket.default_value = 0.0
        Mood_Down_Factor_socket.min_value = 0.0
        Mood_Down_Factor_socket.max_value = 1.0
        Mood_Down_Factor_socket.subtype = "FACTOR"
            Mood_Down_Color_socket = nt.interface.new_socket(
                name="Mood Down Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Mood_Down_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_014 = nt.nodes.new("ShaderNodeGroup")
        Group_014.location = (390.28594970703125, -108.94723510742188)
        Group_013 = nt.nodes.new("ShaderNodeGroup")
        Group_013.location = (99.45367431640625, 10.870697021484375)
        Group_011 = nt.nodes.new("ShaderNodeGroup")
        Group_011.location = (-111.14820098876953, 159.07786560058594)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-377.0361328125, 55.30039596557617)
        Group_012 = nt.nodes.new("ShaderNodeGroup")
        Group_012.location = (-290.36572265625, -248.8246307373047)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (699.5655517578125, -132.42022705078125)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-252.84938049316406, -96.61878204345703)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-696.4589233398438, 79.21564483642578)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (74.70637512207031, -325.0809631347656)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-157.81549072265625, 284.3533020019531)
        # Create links
        nt.links.new(Group_013.outputs["Color"], Group_014.inputs["Original Color"])
        nt.links.new(Group_012.outputs["Mood Down"], Group_014.inputs["Bright Mask"])
        nt.links.new(Group_011.outputs["Color"], Group_013.inputs["Original Color"])
        nt.links.new(Group_012.outputs["Blush"], Group_013.inputs["Bright Mask"])
        nt.links.new(Group_Input.outputs["Head Base Texture"], Group_011.inputs["Original Color"])
        nt.links.new(Group_Input.outputs["Head Lightmap Texture"], Group.inputs["Lightmap"])
        nt.links.new(Group.outputs["Shadow"], Group_011.inputs["Shadow Mask"])
        nt.links.new(Group_Input.outputs["Head Colormap Texture"], Group_012.inputs["Lightmap"])
        nt.links.new(Group_Input.outputs["Fake Shadow Factor"], Group_011.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Fake Shadow Color"], Group_011.inputs["Shadow Color"])
        nt.links.new(Group_Input_001.outputs["Blush Factor"], Group_013.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Bright Color"], Group_013.inputs["Bright Color"])
        nt.links.new(Group_014.outputs["Color"], Group_Output.inputs["Base Color"])
        nt.links.new(Group_Input_002.outputs["Mood Down Factor"], Group_014.inputs["Factor"])
        nt.links.new(Group_Input_002.outputs["Mood Down Color"], Group_014.inputs["Bright Color"])