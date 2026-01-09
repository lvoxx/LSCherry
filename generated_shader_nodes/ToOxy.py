import bpy
from ..utils import ShaderNode


class ShaderNodeToOxy(ShaderNode):
    bl_label = "To Oxy"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            Oxy_socket = nt.interface.new_socket(
                name="Oxy",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Oxy_socket.default_value = (0.0, 0.0, 0.0)
        Oxy_socket.subtype = "NONE"

        # Input sockets
            Oxyz_socket = nt.interface.new_socket(
                name="Oxyz",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Oxyz_socket.default_value = (0.0, 0.0, 0.0)
        Oxyz_socket.subtype = "NONE"

        # Create nodes
        Separate_XYZ = nt.nodes.new("ShaderNodeSeparateXYZ")
        Separate_XYZ.location = (-96.49684143066406, -2.9728546142578125)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (96.49684143066406, 2.9728546142578125)
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (286.4968566894531, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-296.496826171875, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-8.088760375976562, 178.3916015625)
        # Create links
        nt.links.new(Separate_XYZ.outputs["Y"], Combine_XYZ.inputs["Y"])
        nt.links.new(Separate_XYZ.outputs["X"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input.outputs["Oxyz"], Separate_XYZ.inputs["Vector"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Group_Output.inputs["Oxy"])