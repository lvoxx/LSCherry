import bpy
from ..utils import ShaderNode


class ShaderNodeNumberToSequence(ShaderNode):
    bl_label = "Number To Sequence"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Sequence_socket = nt.interface.new_socket(
                name="Sequence",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Sequence_socket.default_value = 0.0
        Sequence_socket.min_value = -3.4028234663852886e+38
        Sequence_socket.max_value = 3.4028234663852886e+38
        Sequence_socket.subtype = "NONE"

        # Input sockets
            Number_socket = nt.interface.new_socket(
                name="Number",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Number_socket.default_value = 0.5
        Number_socket.min_value = -10000.0
        Number_socket.max_value = 10000.0
        Number_socket.subtype = "NONE"

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-270.7940368652344, -77.692138671875)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (0.0, 0.0)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 1000.0
        Math_001.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-69.14718627929688, 114.63056182861328)
        # Create links
        nt.links.new(Group_Input.outputs["Number"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Group_Output.inputs["Sequence"])