import bpy
from ..utils import ShaderNode


class ShaderNodeAddOutlineFromLightmap(ShaderNode):
    bl_label = "Add Outline From Lightmap"
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
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 1.0
        Alpha_socket.min_value = 0.0
        Alpha_socket.max_value = 1.0
        Alpha_socket.subtype = "FACTOR"
            Map_1_socket = nt.interface.new_socket(
                name="Map 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_1_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            Map_2_socket = nt.interface.new_socket(
                name="Map 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Map_2_socket.default_value = (0.5, 0.5, 0.5, 1.0)
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
        
        Range_1_socket.default_value = 0.125
        Range_1_socket.min_value = 0.0
        Range_1_socket.max_value = 1.0
        Range_1_socket.subtype = "FACTOR"
            Range_2_socket = nt.interface.new_socket(
                name="Range 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_2_socket.default_value = 0.25
        Range_2_socket.min_value = 0.0
        Range_2_socket.max_value = 1.0
        Range_2_socket.subtype = "FACTOR"
            Range_3_socket = nt.interface.new_socket(
                name="Range 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Range_3_socket.default_value = 0.375
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
        Group_Output.location = (320.6649169921875, 0.0)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (-130.66490173339844, -6.945831298828125)
        Group_001.inputs["Map 0"].default_value = (0.0, 0.0, 0.0, 1.0)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (130.66490173339844, 6.945831298828125)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-391.8161926269531, -74.04216003417969)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-149.544189453125, 152.8770294189453)
        # Create links
        nt.links.new(Group_001.outputs["Color Map"], Group.inputs["Outline Color"])
        nt.links.new(Group_Input.outputs["Lighmap Alpha"], Group_001.inputs["Lighmap Alpha"])
        nt.links.new(Group_Input.outputs["Map 1"], Group_001.inputs["Map 1"])
        nt.links.new(Group_Input.outputs["Map 2"], Group_001.inputs["Map 2"])
        nt.links.new(Group_Input.outputs["Map 3"], Group_001.inputs["Map 3"])
        nt.links.new(Group_Input.outputs["Map 4"], Group_001.inputs["Map 4"])
        nt.links.new(Group_Input.outputs["Map 5"], Group_001.inputs["Map 5"])
        nt.links.new(Group_Input.outputs["Range 1"], Group_001.inputs["Range 1"])
        nt.links.new(Group_Input.outputs["Range 2"], Group_001.inputs["Range 2"])
        nt.links.new(Group_Input.outputs["Range 3"], Group_001.inputs["Range 3"])
        nt.links.new(Group_Input.outputs["Range 4"], Group_001.inputs["Range 4"])
        nt.links.new(Group.outputs["Outline"], Group_Output.inputs["Outline"])
        nt.links.new(Group_Input.outputs["Alpha"], Group.inputs["Alpha"])