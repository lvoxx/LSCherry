import bpy
from ..utils import ShaderNode


class ShaderNodeSimpleToonDot(ShaderNode):
    bl_label = "Simple Toon Dot"
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
        Group_Output.location = (475.9968566894531, 168.12722778320312)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-609.9403076171875, 0.0)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (-71.05621337890625, 117.50799560546875)
        Group_002 = nt.nodes.new("ShaderNodeGroup")
        Group_002.location = (233.4727783203125, 186.78564453125)
        Group_002.inputs["Invert MLight"].default_value = False
        Group_002.inputs["Mix Light and View"].default_value = 0.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (51.721923828125, -13.873443603515625)
        Mix.data_type = "VECTOR"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-367.0025329589844, -156.52699279785156)
        Vector_Math.operation = "DISTANCE"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-180.3931884765625, -104.48155212402344)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-178.62852478027344, -163.588134765625)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-220.32826232910156, 307.5902404785156)
        # Create links
        nt.links.new(Attribute.outputs["Vector"], Group_002.inputs["Light Dir"])
        nt.links.new(Mix.outputs["Result"], Group_002.inputs["Normal"])
        nt.links.new(Group_002.outputs["NdotL"], Group_Output.inputs["NdotL"])
        nt.links.new(Group_Input.outputs["Normal"], Vector_Math.inputs["Vector"])
        nt.links.new(Geometry.outputs["Normal"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Normal"], Mix.inputs["B"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Vector_Math.outputs["Value"], Math.inputs["Value"])