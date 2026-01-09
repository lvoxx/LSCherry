import bpy
from ..utils import ShaderNode


class ShaderNodeSimpleBackToonDot(ShaderNode):
    bl_label = "Simple Back Toon Dot"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            NdotL_socket = nt.interface.new_socket(
                name="NdotL",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        NdotL_socket.default_value = 0.0
        NdotL_socket.min_value = -3.4028234663852886e+38
        NdotL_socket.max_value = 3.4028234663852886e+38
        NdotL_socket.subtype = "NONE"

        # Input sockets
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (496.3570556640625, 239.00836181640625)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-489.3575439453125, 0.0)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (-126.9410400390625, 152.14682006835938)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (90.24742889404297, 34.880393981933594)
        Mix.data_type = "VECTOR"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (262.8182067871094, 262.01055908203125)
        Group_003.inputs["Invert MLight"].default_value = False
        Group_003.inputs["Mix Light and View"].default_value = 0.0
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-291.5524597167969, -49.616004943847656)
        Vector_Math.operation = "DISTANCE"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-104.94308471679688, 2.429431915283203)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-103.17842102050781, -56.677162170410156)
        Math_001.operation = "GREATER_THAN"
        Math_001.inputs["Value"].default_value = 0.0
        Math_001.inputs["Value"].default_value = 0.5
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-130.46658325195312, 366.92657470703125)
        # Create links
        nt.links.new(Mix.outputs["Result"], Group_003.inputs["Normal"])
        nt.links.new(Attribute.outputs["Vector"], Group_003.inputs["Light Dir"])
        nt.links.new(Group_003.outputs["NdotL"], Group_Output.inputs["NdotL"])
        nt.links.new(Vector_Math.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Group_Input.outputs["Normal"], Vector_Math.inputs["Vector"])
        nt.links.new(Geometry.outputs["Normal"], Mix.inputs["A"])
        nt.links.new(Math_001.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Normal"], Mix.inputs["B"])