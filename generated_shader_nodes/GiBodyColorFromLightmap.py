import bpy
from ..utils import ShaderNode


class ShaderNodeGiBodyColorFromLightmap(ShaderNode):
    bl_label = "GI: Body Color From Lightmap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Color_Map_socket = nt.interface.new_socket(
                name="Color Map",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_Map_socket.default_value = (0.0, 0.0, 0.0, 0.0)

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
            Map_0_socket = nt.interface.new_socket(
                name="Map 0",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_0_socket.default_value = (0.0, 0.0, 0.0, 1.0)
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
            Map_5_socket = nt.interface.new_socket(
                name="Map 5",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_5_socket.default_value = (0.0, 0.0, 0.0, 1.0)
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
            Range_4_socket = nt.interface.new_socket(
                name="Range 4",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_4_socket.default_value = 0.6200000047683716
        Range_4_socket.min_value = 0.0
        Range_4_socket.max_value = 1.0
        Range_4_socket.subtype = "FACTOR"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-200.0, -54.313480377197266)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-60.10417175292969, 114.16680908203125)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-49.89276123046875, 213.3140411376953)
        # Create links
        nt.links.new(Group_Input.outputs["Lighmap Alpha"], Group_001.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input.outputs["Map 1"], Group_001.inputs["Map 1"])
        nt.links.new(Group_Input.outputs["Map 2"], Group_001.inputs["Map 2"])
        nt.links.new(Group_Input.outputs["Map 3"], Group_001.inputs["Map 3"])
        nt.links.new(Group_Input.outputs["Map 4"], Group_001.inputs["Map 4"])
        nt.links.new(Group_Input.outputs["Range 1"], Group_001.inputs["Range 1"])
        nt.links.new(Group_Input.outputs["Range 2"], Group_001.inputs["Range 2"])
        nt.links.new(Group_Input.outputs["Range 3"], Group_001.inputs["Range 3"])
        nt.links.new(Group_001.outputs["Color Map"], Group_Output.inputs["Color Map"])
        nt.links.new(Group_Input.outputs["Range 4"], Group_001.inputs["Range 4"])
        nt.links.new(Group_Input.outputs["Map 5"], Group_001.inputs["Map 5"])
        nt.links.new(Group_Input.outputs["Map 0"], Group_001.inputs["Map 0"])