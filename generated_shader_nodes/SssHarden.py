import bpy
from ..utils import ShaderNode


class ShaderNodeSssHarden(ShaderNode):
    bl_label = "SSS Harden"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 0.0
        Shading_socket.min_value = 0.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"

        # Input sockets
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 0.0
        Shading_socket.min_value = -3.4028234663852886e+38
        Shading_socket.max_value = 3.4028234663852886e+38
        Shading_socket.subtype = "NONE"
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 0.8999999761581421
        Size_socket.min_value = 0.0
        Size_socket.max_value = 1.0
        Size_socket.subtype = "NONE"
            Smooth_socket = nt.interface.new_socket(
                name="Smooth",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Smooth_socket.default_value = 0.15000000596046448
        Smooth_socket.min_value = 0.0
        Smooth_socket.max_value = 1.0
        Smooth_socket.subtype = "NONE"

        # Create nodes
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (145.10354614257812, -260.87188720703125)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Script = nt.nodes.new("ShaderNodeScript")
        Script.location = (-3692.534423828125, 49.04938888549805)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-438.609375, -246.67654418945312)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-527.3643798828125, -222.6627960205078)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-527.3643798828125, 95.4958724975586)
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-153.56248474121094, -349.49609375)
        Math_003.operation = "MAXIMUM"
        Math_003.inputs["Value"].default_value = 0.009999999776482582
        Math_003.inputs["Value"].default_value = 0.5
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-889.881103515625, -184.79843139648438)
        Map_Range_001 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_001.location = (117.86553955078125, 235.2051544189453)
        Map_Range_001.data_type = "FLOAT"
        Map_Range_001.interpolation_type = "LINEAR"
        Map_Range_001.inputs["From Min"].default_value = -0.009999999776482582
        Map_Range_001.inputs["From Max"].default_value = 1.0
        Map_Range_001.inputs["To Min"].default_value = 0.0
        Map_Range_001.inputs["To Max"].default_value = 1.0
        Map_Range_001.inputs["Steps"].default_value = 4.0
        Map_Range_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-79.26952362060547, -128.2460174560547)
        Math_002.operation = "SUBTRACT"
        Math_002.inputs["Value"].default_value = 1.0
        Math_002.inputs["Value"].default_value = 0.5
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (362.9831237792969, -4.021301746368408)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (940.903564453125, 91.37847900390625)
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (-346.3614807128906, -132.76296997070312)
        Math_004.operation = "SUBTRACT"
        Math_004.inputs["Value"].default_value = 0.009999999776482582
        Math_004.inputs["Value"].default_value = 0.5
        # Create links
        nt.links.new(Map_Range_001.outputs["Result"], Map_Range.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Map_Range.inputs["From Max"])
        nt.links.new(Math_002.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Map_Range.inputs["From Min"])
        nt.links.new(Math_004.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Group_Input.outputs["Shading"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Map_Range_001.inputs["Value"])
        nt.links.new(Group_Input.outputs["Smooth"], Math_003.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Group_Output.inputs["Shading"])
        nt.links.new(Group_Input.outputs["Size"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Math_004.inputs["Value"])