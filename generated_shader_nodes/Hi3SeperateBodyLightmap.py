import bpy
from ..utils import ShaderNode


class ShaderNodeHi3SeperateBodyLightmap(ShaderNode):
    bl_label = "HI3: Seperate Body Lightmap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Metal_socket = nt.interface.new_socket(
                name="Metal",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Metal_socket.default_value = 0.0
        Metal_socket.min_value = -3.4028234663852886e+38
        Metal_socket.max_value = 3.4028234663852886e+38
        Metal_socket.subtype = "NONE"
            Shadow_socket = nt.interface.new_socket(
                name="Shadow",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_socket.default_value = 0.0
        Shadow_socket.min_value = -3.4028234663852886e+38
        Shadow_socket.max_value = 3.4028234663852886e+38
        Shadow_socket.subtype = "NONE"

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
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (192.9788360595703, -231.83816528320312)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 10.0
        Math_001.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (403.8800964355469, -228.09619140625)
        Math_002.operation = "GREATER_THAN"
        Math_002.inputs["Value"].default_value = 0.019999999552965164
        Math_002.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (683.0411376953125, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (295.61016845703125, 128.23895263671875)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Group.inputs["Lightmap"])
        nt.links.new(Group.outputs["Diffuse"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Group_Output.inputs["Shadow"])
        nt.links.new(Group.outputs["Metal"], Group_Output.inputs["Metal"])