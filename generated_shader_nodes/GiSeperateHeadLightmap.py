import bpy
from ..utils import ShaderNode


class ShaderNodeGiSeperateHeadLightmap(ShaderNode):
    bl_label = "GI: Seperate Head Lightmap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Shadow_socket = nt.interface.new_socket(
                name="Shadow",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_socket.default_value = 0.0
        Shadow_socket.min_value = -3.4028234663852886e+38
        Shadow_socket.max_value = 3.4028234663852886e+38
        Shadow_socket.subtype = "NONE"
            See-Through_socket = nt.interface.new_socket(
                name="See-Through",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        See-Through_socket.default_value = 0.0
        See-Through_socket.min_value = -3.4028234663852886e+38
        See-Through_socket.max_value = 3.4028234663852886e+38
        See-Through_socket.subtype = "NONE"

        # Input sockets
            Lightmap_socket = nt.interface.new_socket(
                name="Lightmap",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-249.63360595703125, -95.09207153320312)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (0.0, 0.0)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (412.5861511230469, -98.85681915283203)
        Invert_Color.inputs["Fac"].default_value = 0.0
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (807.1785888671875, -1.3199604749679565)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (338.00994873046875, 141.1890411376953)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Group.inputs["Lightmap"])
        nt.links.new(Group.outputs["Metal"], Group_Output.inputs["See-Through"])
        nt.links.new(Invert_Color.outputs["Color"], Group_Output.inputs["Shadow"])
        nt.links.new(Group.outputs["Diffuse"], Invert_Color.inputs["Color"])