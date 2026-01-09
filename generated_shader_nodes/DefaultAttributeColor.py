import bpy
from ..utils import ShaderNode


class ShaderNodeDefaultAttributeColor(ShaderNode):
    bl_label = "Default Attribute: Color"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Result_socket = nt.interface.new_socket(
                name="Result",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Result_socket.default_value = (0.0, 0.0, 0.0, 1.0)
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
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Default_socket = nt.interface.new_socket(
                name="Default",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Default_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (304.9979248046875, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-651.058349609375, -95.36563873291016)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-304.3564147949219, 61.88203430175781)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-21.92888641357422, -113.94464111328125)
        Math.operation = "COMPARE"
        Math.inputs["Value"].default_value = 0.0
        # Create links
        nt.links.new(Group_Input.outputs["Default"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Compare"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Default"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Default"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Result"])
        nt.links.new(Mix.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Default"], Math.inputs["Value"])