import bpy
from ..utils import ShaderNode


class ShaderNodeConvert0255To01(ShaderNode):
    bl_label = "Convert [0, 255] to [0,1]"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            [0,_1]_socket = nt.interface.new_socket(
                name="[0, 1]",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        [0,_1]_socket.default_value = 0.0
        [0,_1]_socket.min_value = -3.4028234663852886e+38
        [0,_1]_socket.max_value = 3.4028234663852886e+38
        [0,_1]_socket.subtype = "NONE"

        # Input sockets
            [0,_255]_socket = nt.interface.new_socket(
                name="[0, 255]",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        [0,_255]_socket.default_value = 0.0
        [0,_255]_socket.min_value = -10000.0
        [0,_255]_socket.max_value = 10000.0
        [0,_255]_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.91796875, -4.8596906661987305)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-264.88372802734375, -57.8938102722168)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (-55.72362518310547, 30.07027816772461)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.0
        Map_Range.inputs["From Max"].default_value = 255.0
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-49.42486572265625, 164.65509033203125)
        # Create links
        nt.links.new(Group_Input.outputs["[0, 255]"], Map_Range.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Group_Output.inputs["[0, 1]"])