import bpy
from ..utils import ShaderNode


class ShaderNodeWorldColor(ShaderNode):
    bl_label = "World Color"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            WorldColor_socket = nt.interface.new_socket(
                name="WorldColor",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        WorldColor_socket.default_value = (0.5, 0.5, 0.5, 1.0)

        # Input sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Strength_socket = nt.interface.new_socket(
                name="Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Strength_socket.default_value = 0.0
        Strength_socket.min_value = 0.0
        Strength_socket.max_value = 3.4028234663852886e+38
        Strength_socket.subtype = "NONE"

        # Create nodes
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (172.00001525878906, 8.867683410644531)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (392.1772155761719, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-444.8787841796875, -5.085439682006836)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-135.0023193359375, 147.5073699951172)
        # Create links
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["WorldColor"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Strength"], Mix.inputs["B"])