import bpy
from ..utils import ShaderNode


class ShaderNodeGiSeperateBodyLightmap(ShaderNode):
    bl_label = "GI: Seperate Body Lightmap"
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
            Metal_socket = nt.interface.new_socket(
                name="Metal",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metal_socket.default_value = 0.0
        Metal_socket.min_value = -3.4028234663852886e+38
        Metal_socket.max_value = 3.4028234663852886e+38
        Metal_socket.subtype = "NONE"

        # Input sockets
            Lightmap_socket = nt.interface.new_socket(
                name="Lightmap",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-501.6336669921875, -95.09207153320312)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-251.99998474121094, 0.0)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (187.8311004638672, -235.7021484375)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 10.0
        Math_001.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (403.8800964355469, -228.09619140625)
        Math_002.operation = "GREATER_THAN"
        Math_002.inputs["Value"].default_value = 0.10000000149011612
        Math_002.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (904.45751953125, -22.636503219604492)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (21.196884155273438, 194.7568817138672)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.8999999761581421
        Map_Range.inputs["From Max"].default_value = 1.0
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (243.0, 181.30575561523438)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["B"].default_value = 1.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (464.0, 95.79544067382812)
        Math_003.operation = "MULTIPLY"
        Math_003.inputs["Value"].default_value = 10.0
        Math_003.inputs["Value"].default_value = 0.5
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (684.0001220703125, 69.20967102050781)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (623.9999389648438, -111.06930541992188)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Map_Range_001 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_001.location = (-4.974416732788086, -156.86618041992188)
        Map_Range_001.data_type = "FLOAT"
        Map_Range_001.interpolation_type = "LINEAR"
        Map_Range_001.inputs["From Min"].default_value = 0.009999999776482582
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
        Map_Range_002 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_002.location = (-4.974416732788086, -420.8045654296875)
        Map_Range_002.data_type = "FLOAT"
        Map_Range_002.interpolation_type = "LINEAR"
        Map_Range_002.inputs["From Min"].default_value = 0.0
        Map_Range_002.inputs["From Max"].default_value = 0.20999999344348907
        Map_Range_002.inputs["To Min"].default_value = 0.0
        Map_Range_002.inputs["To Max"].default_value = 1.0
        Map_Range_002.inputs["Steps"].default_value = 4.0
        Map_Range_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_002.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_002.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_002.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Map_Range_003 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_003.location = (21.18216323852539, 472.1224670410156)
        Map_Range_003.data_type = "FLOAT"
        Map_Range_003.interpolation_type = "LINEAR"
        Map_Range_003.inputs["From Min"].default_value = 0.20999999344348907
        Map_Range_003.inputs["From Max"].default_value = 1.0
        Map_Range_003.inputs["To Min"].default_value = 0.0
        Map_Range_003.inputs["To Max"].default_value = 1.0
        Map_Range_003.inputs["Steps"].default_value = 4.0
        Map_Range_003.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_003.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_003.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_003.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (268.7588195800781, 629.1688232421875)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Group.inputs["Lightmap"])
        nt.links.new(Map_Range_001.outputs["Result"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Group.outputs["Metal"], Map_Range.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Mix.inputs["Factor"])
        nt.links.new(Group.outputs["Metal"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Math_003.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Invert_Color.inputs["Color"])
        nt.links.new(Math_002.outputs["Value"], Mix_001.inputs["Factor"])
        nt.links.new(Group.outputs["Highlight"], Map_Range_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Mix_001.inputs["B"])
        nt.links.new(Group.outputs["Diffuse"], Map_Range_002.inputs["Value"])
        nt.links.new(Map_Range_002.outputs["Result"], Group_Output.inputs["Shadow"])
        nt.links.new(Group.outputs["Metal"], Map_Range_003.inputs["Value"])
        nt.links.new(Map_Range_003.outputs["Result"], Group_Output.inputs["Metal"])