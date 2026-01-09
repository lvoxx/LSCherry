import bpy
from ..utils import ShaderNode


class ShaderNodeFromAToB(ShaderNode):
    bl_label = "FROM A TO B"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Boolean_socket = nt.interface.new_socket(
                name="Boolean",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Boolean_socket.default_value = 0.0
        Boolean_socket.min_value = -3.4028234663852886e+38
        Boolean_socket.max_value = 3.4028234663852886e+38
        Boolean_socket.subtype = "NONE"

        # Input sockets
            A_socket = nt.interface.new_socket(
                name="A",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        A_socket.default_value = 0.5
        A_socket.min_value = -10000.0
        A_socket.max_value = 10000.0
        A_socket.subtype = "NONE"
            B_socket = nt.interface.new_socket(
                name="B",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        B_socket.default_value = 0.5
        B_socket.min_value = -10000.0
        B_socket.max_value = 10000.0
        B_socket.subtype = "NONE"
            Input_socket = nt.interface.new_socket(
                name="Input",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Input_socket.default_value = 0.5
        Input_socket.min_value = -10000.0
        Input_socket.max_value = 10000.0
        Input_socket.subtype = "NONE"

        # Create nodes
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-448.70111083984375, 317.9954833984375)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-332.9420166015625, 71.32112121582031)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-332.9420166015625, -24.881412506103516)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-332.9420166015625, -100.09429931640625)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-212.33914184570312, 6.1656036376953125)
        Math_001.operation = "LESS_THAN"
        Math_001.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (217.9914093017578, 20.9896240234375)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-716.4229736328125, 54.661312103271484)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-213.4344482421875, 186.92666625976562)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.5
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (-5.354795455932617, 85.49458312988281)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (-22.77294921875, 323.034912109375)
        # Create links
        nt.links.new(Group_Input.outputs["B"], Math_001.inputs["Value"])
        nt.links.new(Group_Input.outputs["A"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Input"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Reroute.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Group_001.inputs["B"])
        nt.links.new(Math.outputs["Value"], Group_001.inputs["A"])
        nt.links.new(Group_001.outputs["O"], Group_Output.inputs["Boolean"])