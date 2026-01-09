import bpy
from ..utils import ShaderNode


class ShaderNodeDefaultAttributeAlpha(ShaderNode):
    bl_label = "Default Attribute: Alpha"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Result_socket = nt.interface.new_socket(
                name="Result",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Result_socket.default_value = 0.0
        Result_socket.min_value = -3.4028234663852886e+38
        Result_socket.max_value = 3.4028234663852886e+38
        Result_socket.subtype = "NONE"
            Compare_socket = nt.interface.new_socket(
                name="Compare",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Compare_socket.default_value = 0.0
        Compare_socket.min_value = -3.4028234663852886e+38
        Compare_socket.max_value = 3.4028234663852886e+38
        Compare_socket.subtype = "NONE"

        # Input sockets
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 0.0
        Alpha_socket.min_value = -10000.0
        Alpha_socket.max_value = 10000.0
        Alpha_socket.subtype = "NONE"
            Default_socket = nt.interface.new_socket(
                name="Default",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Default_socket.default_value = 0.0
        Default_socket.min_value = -10000.0
        Default_socket.max_value = 10000.0
        Default_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (304.9979248046875, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-426.32611083984375, -95.36563873291016)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-50.93915939331055, 0.0)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (128.2432098388672, -57.98484802246094)
        Math.operation = "COMPARE"
        Math.inputs["Value"].default_value = 0.0
        # Create links
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Result"])
        nt.links.new(Group_Input.outputs["Alpha"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Default"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Alpha"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Compare"])
        nt.links.new(Group_Input.outputs["Default"], Math.inputs["Value"])