import bpy
from ..utils import ShaderNode


class ShaderNodeHsrSeperateBodyLightmap(ShaderNode):
    bl_label = "HSR: Seperate Body Lightmap"
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
        Group_Input.location = (-677.0464477539062, -98.66634368896484)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-410.74688720703125, -17.871360778808594)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1149.495849609375, -25.543529510498047)
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (154.398681640625, 317.74566650390625)
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
        Map_Range_001 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_001.location = (143.47811889648438, -268.27618408203125)
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
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (388.5966796875, 181.65969848632812)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["B"].default_value = 1.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (609.0000610351562, 158.89093017578125)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 10.0
        Math_001.inputs["Value"].default_value = 0.5
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (882.7385864257812, 77.95582580566406)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (330.1296691894531, -271.1135559082031)
        Math_002.operation = "MULTIPLY"
        Math_002.inputs["Value"].default_value = 10.0
        Math_002.inputs["Value"].default_value = 0.5
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (762.283203125, -50.005741119384766)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (555.8516845703125, -271.85675048828125)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.10000000149011612
        Math.inputs["Value"].default_value = 0.5
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (326.8624267578125, 477.7340393066406)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Group.inputs["Lightmap"])
        nt.links.new(Map_Range.outputs["Result"], Mix.inputs["Factor"])
        nt.links.new(Invert_Color.outputs["Color"], Group_Output.inputs["Shadow"])
        nt.links.new(Group.outputs["Metal"], Map_Range.inputs["Value"])
        nt.links.new(Group.outputs["Metal"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Invert_Color.inputs["Color"])
        nt.links.new(Group.outputs["Highlight"], Map_Range_001.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Map_Range_001.outputs["Result"], Math_002.inputs["Value"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Metal"])
        nt.links.new(Math.outputs["Value"], Mix_001.inputs["Factor"])
        nt.links.new(Math_002.outputs["Value"], Mix_001.inputs["B"])