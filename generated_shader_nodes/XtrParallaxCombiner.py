import bpy
from ..utils import ShaderNode


class ShaderNodeXtrParallaxCombiner(ShaderNode):
    bl_label = "XTR: Parallax Combiner"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Parallax_socket = nt.interface.new_socket(
                name="Parallax",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Parallax_socket.default_value = 0.0
        Parallax_socket.min_value = -3.4028234663852886e+38
        Parallax_socket.max_value = 3.4028234663852886e+38
        Parallax_socket.subtype = "NONE"

        # Input sockets
            Layer_A_socket = nt.interface.new_socket(
                name="Layer A",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Layer_A_socket.default_value = 1.0
        Layer_A_socket.min_value = -10000.0
        Layer_A_socket.max_value = 10000.0
        Layer_A_socket.subtype = "NONE"
            Layer_B_socket = nt.interface.new_socket(
                name="Layer B",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Layer_B_socket.default_value = 0.8500000238418579
        Layer_B_socket.min_value = -10000.0
        Layer_B_socket.max_value = 10000.0
        Layer_B_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-252.4765625, -55.0050048828125)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (0.0, 0.0)
        Math_002.operation = "MAXIMUM"
        Math_002.inputs["Value"].default_value = 0.004999999888241291
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-27.253082275390625, 118.24844360351562)
        # Create links
        nt.links.new(Group_Input.outputs["Layer A"], Math_002.inputs["Value"])
        nt.links.new(Group_Input.outputs["Layer B"], Math_002.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Group_Output.inputs["Parallax"])