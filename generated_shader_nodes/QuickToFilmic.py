import bpy
from ..utils import ShaderNode


class ShaderNodeQuickToFilmic(ShaderNode):
    bl_label = "Quick To Filmic"
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
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Gamma = nt.nodes.new("ShaderNodeGamma")
        Gamma.location = (0.0, 0.0)
        Gamma.inputs["Gamma"].default_value = 2.200000047683716
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-200.0, -25.864898681640625)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-33.02581787109375, 141.14651489257812)
        # Create links
        nt.links.new(Gamma.outputs["Color"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input.outputs["Combined"], Gamma.inputs["Color"])