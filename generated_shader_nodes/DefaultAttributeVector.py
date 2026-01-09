import bpy
from ..utils import ShaderNode


class ShaderNodeDefaultAttributeVector(ShaderNode):
    bl_label = "Default Attribute: Vector"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            Result_socket = nt.interface.new_socket(
                name="Result",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Result_socket.default_value = (0.0, 0.0, 0.0)
        Result_socket.subtype = "NONE"
            Compare_socket = nt.interface.new_socket(
                name="Compare",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Compare_socket.default_value = 0.0
        Compare_socket.min_value = -3.4028234663852886e+38
        Compare_socket.max_value = 3.4028234663852886e+38
        Compare_socket.subtype = "NONE"

        # Input sockets
            Vector_socket = nt.interface.new_socket(
                name="Vector",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Vector_socket.default_value = (0.0, 0.0, 0.0)
        Vector_socket.subtype = "NONE"
            Default_socket = nt.interface.new_socket(
                name="Default",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Default_socket.default_value = (0.0, 0.0, 0.0)
        Default_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (304.9979248046875, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-651.058349609375, -95.36563873291016)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-118.84967803955078, -131.5231475830078)
        Mix.data_type = "VECTOR"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (105.66834259033203, -142.41546630859375)
        Math.operation = "COMPARE"
        Math.inputs["Value"].default_value = 0.0
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-391.99237060546875, -56.42120361328125)
        Vector_Math.operation = "LENGTH"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-389.460693359375, -90.3770523071289)
        Group.inputs["B"].default_value = 0.0
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (-118.77096557617188, -217.74578857421875)
        Vector_Math_001.operation = "LENGTH"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Vector_Math_002 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_002.location = (-118.77096557617188, -253.0888671875)
        Vector_Math_002.operation = "LENGTH"
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Scale"].default_value = 1.0
        # Create links
        nt.links.new(Group_Input.outputs["Default"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Vector"], Mix.inputs["B"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Compare"])
        nt.links.new(Group_Input.outputs["Vector"], Vector_Math.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Vector"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Default"], Mix.inputs["A"])
        nt.links.new(Vector_Math.outputs["Value"], Group.inputs["A"])
        nt.links.new(Group.outputs["Boolean"], Mix.inputs["Factor"])
        nt.links.new(Vector_Math_001.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Vector"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Default"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Vector_Math_002.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Result"])