import bpy
from ..utils import ShaderNode


class ShaderNodeUseDefaultNormal(ShaderNode):
    bl_label = "Use Default Normal"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

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
        Group_Output.location = (406.86029052734375, 95.66910552978516)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-402.7498779296875, 108.71489715576172)
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-144.440185546875, 16.198043823242188)
        Vector_Math.operation = "DISTANCE"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (36.21836853027344, -17.059417724609375)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.5
        Math.inputs["Value"].default_value = 0.5
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (35.09747314453125, -55.27488708496094)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (200.5790557861328, 32.153717041015625)
        Mix.data_type = "VECTOR"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (8.742263793945312, 234.86492919921875)
        # Create links
        nt.links.new(Vector_Math.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Geometry.outputs["Normal"], Mix.inputs["A"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Normal"], Vector_Math.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Normal"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Normal"])