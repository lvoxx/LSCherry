import bpy
from ..utils import ShaderNode


class ShaderNodeNumberExtract(ShaderNode):
    bl_label = "Number Extract"
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
        Compressed_socket.min_value = -3.402820018375656e+38
        Compressed_socket.max_value = 3.4028234663852886e+38
        Compressed_socket.subtype = "NONE"
            Extracted_socket = nt.interface.new_socket(
                name="Extracted",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Extracted_socket.default_value = 0.0
        Extracted_socket.min_value = -3.4028234663852886e+38
        Extracted_socket.max_value = 3.4028234663852886e+38
        Extracted_socket.subtype = "NONE"

        # Input sockets
            Compressed_socket = nt.interface.new_socket(
                name="Compressed",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Compressed_socket.default_value = 0.5
        Compressed_socket.min_value = -10000.0
        Compressed_socket.max_value = 10000.0
        Compressed_socket.subtype = "NONE"

        # Create nodes
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-191.08358764648438, 110.0589599609375)
        Math.operation = "DIVIDE"
        Math.inputs["Value"].default_value = 10000.0
        Math.inputs["Value"].default_value = 0.5
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-502.9610290527344, -134.17071533203125)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1170.10595703125, 0.0)
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (14.976840019226074, 42.01896667480469)
        Math_004.operation = "TRUNC"
        Math_004.inputs["Value"].default_value = 0.5
        Math_004.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (198.36959838867188, 19.103342056274414)
        Math_001.operation = "MULTIPLY"
        Math_001.inputs["Value"].default_value = 10000.0
        Math_001.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (620.7932739257812, -160.2606964111328)
        Math_003.operation = "DIVIDE"
        Math_003.inputs["Value"].default_value = 1000.0
        Math_003.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (399.6169738769531, -91.07628631591797)
        Math_002.operation = "SUBTRACT"
        Math_002.inputs["Value"].default_value = 0.5
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (393.67376708984375, 215.65560913085938)
        # Create links
        nt.links.new(Group_Input.outputs["Compressed"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Compressed"])
        nt.links.new(Math_004.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Group_Input.outputs["Compressed"], Math_002.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Group_Output.inputs["Extracted"])
        nt.links.new(Math_001.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Math_004.inputs["Value"])
        nt.links.new(Math_002.outputs["Value"], Math_003.inputs["Value"])