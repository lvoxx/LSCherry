import bpy
from ..utils import ShaderNode


class ShaderNodeNumberCompress(ShaderNode):
    bl_label = "Number Compress"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Compressed_socket = nt.interface.new_socket(
                name="Compressed",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Compressed_socket.default_value = 0.0
        Compressed_socket.min_value = -3.4028234663852886e+38
        Compressed_socket.max_value = 3.4028234663852886e+38
        Compressed_socket.subtype = "NONE"

        # Input sockets
            MAX_2_SEQUENCES_socket = nt.interface.new_socket(
                name="MAX 2 SEQUENCES",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            Sequence_1_socket = nt.interface.new_socket(
                name="Sequence 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Sequence_1_socket.default_value = 0.5
        Sequence_1_socket.min_value = -10000.0
        Sequence_1_socket.max_value = 10000.0
        Sequence_1_socket.subtype = "NONE"
            Sequence_2_socket = nt.interface.new_socket(
                name="Sequence 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Sequence_2_socket.default_value = 1000.0
        Sequence_2_socket.min_value = -10000.0
        Sequence_2_socket.max_value = 10000.0
        Sequence_2_socket.subtype = "NONE"

        # Create nodes
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (287.2575988769531, -10.637981414794922)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (70.97384643554688, 62.3270263671875)
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (8.62823486328125, -99.06138610839844)
        Math_004.operation = "ADD"
        Math_004.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-39.44537353515625, 7.616203308105469)
        Math_002.operation = "MULTIPLY"
        Math_002.inputs["Value"].default_value = 10000.0
        Math_002.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (584.335693359375, 35.423583984375)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-407.6225280761719, -3.5251736640930176)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (70.46086120605469, 226.48410034179688)
        # Create links
        nt.links.new(Math_002.outputs["Value"], Math_004.inputs["Value"])
        nt.links.new(Math_004.outputs["Value"], Group_Output.inputs["Compressed"])
        nt.links.new(Group_Input.outputs["Sequence 1"], Math_002.inputs["Value"])
        nt.links.new(Group_Input.outputs["Sequence 2"], Math_004.inputs["Value"])