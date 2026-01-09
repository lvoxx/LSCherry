import bpy
from ..utils import ShaderNode


class ShaderNodeHsrSeperateHairLightmap(ShaderNode):
    bl_label = "HSR: Seperate Hair Lightmap"
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
            Highlight_socket = nt.interface.new_socket(
                name="Highlight",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Highlight_socket.default_value = 0.0
        Highlight_socket.min_value = -3.4028234663852886e+38
        Highlight_socket.max_value = 3.4028234663852886e+38
        Highlight_socket.subtype = "NONE"

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
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1248.55908203125, -14.913078308105469)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (0.0, 0.0)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (331.0364074707031, 185.4125213623047)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.0
        Map_Range.inputs["From Max"].default_value = 0.20999999344348907
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (250.95291137695312, 314.023193359375)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Group.inputs["Lightmap"])
        nt.links.new(Group.outputs["Highlight"], Group_Output.inputs["Highlight"])
        nt.links.new(Group.outputs["Metal"], Map_Range.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Group_Output.inputs["Shadow"])