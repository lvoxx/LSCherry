import bpy
from ..utils import ShaderNode


class ShaderNodeGiAddOutlineFromLightmap(ShaderNode):
    bl_label = "GI: Add Outline From Lightmap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Outline_socket = nt.interface.new_socket(
                name="Outline",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Lighmap_Alpha_socket = nt.interface.new_socket(
                name="Lighmap Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Lighmap_Alpha_socket.default_value = 0.0
        Lighmap_Alpha_socket.min_value = 0.0
        Lighmap_Alpha_socket.max_value = 1.0
        Lighmap_Alpha_socket.subtype = "NONE"
            Map_1_socket = nt.interface.new_socket(
                name="Map 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_1_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_2_socket = nt.interface.new_socket(
                name="Map 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_2_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_3_socket = nt.interface.new_socket(
                name="Map 3",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_3_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Map_4_socket = nt.interface.new_socket(
                name="Map 4",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_4_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Range_1_socket = nt.interface.new_socket(
                name="Range 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_1_socket.default_value = 0.10000000149011612
        Range_1_socket.min_value = 0.0
        Range_1_socket.max_value = 1.0
        Range_1_socket.subtype = "FACTOR"
            Range_2_socket = nt.interface.new_socket(
                name="Range 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_2_socket.default_value = 0.30000001192092896
        Range_2_socket.min_value = 0.0
        Range_2_socket.max_value = 1.0
        Range_2_socket.subtype = "FACTOR"
            Range_3_socket = nt.interface.new_socket(
                name="Range 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_3_socket.default_value = 0.44999998807907104
        Range_3_socket.min_value = 0.0
        Range_3_socket.max_value = 1.0
        Range_3_socket.subtype = "FACTOR"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (329.360107421875, 146.60858154296875)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (139.360107421875, 146.60858154296875)
        Group.inputs["Alpha"].default_value = 1.0
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-116.9987564086914, 92.27113342285156)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (75.12033081054688, 247.3756561279297)
        # Create links
        nt.links.new(Group_Input.outputs["Lighmap Alpha"], Group.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input.outputs["Map 1"], Group.inputs["Map 1"])
        nt.links.new(Group_Input.outputs["Map 2"], Group.inputs["Map 2"])
        nt.links.new(Group_Input.outputs["Map 3"], Group.inputs["Map 3"])
        nt.links.new(Group_Input.outputs["Map 4"], Group.inputs["Map 4"])
        nt.links.new(Group_Input.outputs["Range 1"], Group.inputs["Range 1"])
        nt.links.new(Group_Input.outputs["Range 2"], Group.inputs["Range 2"])
        nt.links.new(Group_Input.outputs["Range 3"], Group.inputs["Range 3"])
        nt.links.new(Group.outputs["Outline"], Group_Output.inputs["Outline"])
        nt.links.new(Group_Input.outputs["Range 3"], Group.inputs["Range 4"])
        nt.links.new(Group_Input.outputs["Map 4"], Group.inputs["Map 5"])