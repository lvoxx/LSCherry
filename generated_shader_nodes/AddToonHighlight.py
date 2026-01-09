import bpy
from ..utils import ShaderNode


class ShaderNodeAddToonHighlight(ShaderNode):
    bl_label = "Add Toon Highlight"
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
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = 0.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "FACTOR"
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
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (714.9384765625, 212.96292114257812)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-97.67365264892578, 231.18692016601562)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (352.43609619140625, 238.9521942138672)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (232.86660766601562, 384.1142578125)
        # Create links
        nt.links.new(Group_001.outputs["Combined"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_002.outputs["Combined"], Group_001.inputs["Combined"])
        nt.links.new(Group_Input_002.outputs["Shading"], Group_001.inputs["Shading"])
        nt.links.new(Group_Input_002.outputs["Fac"], Group_001.inputs["Fac"])
        nt.links.new(Group_Input_002.outputs["Color"], Group_001.inputs["Color"])
        nt.links.new(Group_Input_002.outputs["Pattern"], Group_001.inputs["Pattern"])