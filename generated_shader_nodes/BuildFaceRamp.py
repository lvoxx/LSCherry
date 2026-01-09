import bpy
from ..utils import ShaderNode


class ShaderNodeBuildFaceRamp(ShaderNode):
    bl_label = "Build Face Ramp"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Custom_Ramp_socket = nt.interface.new_socket(
                name="Custom Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Custom_Ramp_socket.default_value = (0.0, 0.0, 0.0, 1.0)

        # Input sockets
            Face_Value_socket = nt.interface.new_socket(
                name="Face Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Value_socket.default_value = 0.5
        Face_Value_socket.min_value = -10000.0
        Face_Value_socket.max_value = 10000.0
        Face_Value_socket.subtype = "NONE"
            Face_Map_socket = nt.interface.new_socket(
                name="Face Map",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Map_socket.default_value = 0.5
        Face_Map_socket.min_value = -10000.0
        Face_Map_socket.max_value = 10000.0
        Face_Map_socket.subtype = "NONE"

        # Create nodes
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (229.33355712890625, 59.68492889404297)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1624.7054443359375, 14.525022506713867)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (6.51812744140625, -12.794715881347656)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (1064.32861328125, 217.2521209716797)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (1481.3741455078125, -41.60562515258789)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (175.45269775390625, -70.42658996582031)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (175.45269775390625, -48.3992919921875)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (437.1700744628906, -41.60562515258789)
        # Create links
        nt.links.new(Reroute_006.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Reroute.outputs["Output"], Group_Output.inputs["Custom Ramp"])
        nt.links.new(Group_Input.outputs["Face Map"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Face Value"], Reroute_003.inputs["Input"])
        nt.links.new(Math.outputs["Value"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute.inputs["Input"])