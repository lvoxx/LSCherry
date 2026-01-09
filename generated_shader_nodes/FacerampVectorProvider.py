import bpy
from ..utils import ShaderNode


class ShaderNodeFacerampVectorProvider(ShaderNode):
    bl_label = "Faceramp Vector Provider"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Fx_socket = nt.interface.new_socket(
                name="Fx",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Fx_socket.default_value = (0.0, 0.0, 0.0)
        Fx_socket.subtype = "NONE"
            Fy_socket = nt.interface.new_socket(
                name="Fy",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Fy_socket.default_value = (0.0, 0.0, 0.0)
        Fy_socket.subtype = "NONE"
            X(-1,_0,_0)_socket = nt.interface.new_socket(
                name="X(-1, 0, 0)",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        X(-1,_0,_0)_socket.default_value = (0.0, 0.0, 0.0)
        X(-1,_0,_0)_socket.subtype = "NONE"
            X(1,_0,_0)_socket = nt.interface.new_socket(
                name="X(1, 0, 0)",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        X(1,_0,_0)_socket.default_value = (0.0, 0.0, 0.0)
        X(1,_0,_0)_socket.subtype = "NONE"

        # Input sockets

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (644.89990234375, -61.04043197631836)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-361.1856689453125, -61.04043197631836)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (275.03240966796875, 266.2572326660156)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (278.46209716796875, 34.254512786865234)
        Vector_Math_002 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_002.location = (275.03240966796875, 231.08343505859375)
        Vector_Math_002.operation = "NORMALIZE"
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Scale"].default_value = 1.0
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (278.46209716796875, -3.0510311126708984)
        Vector_Math_001.operation = "NORMALIZE"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Attribute_001 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_001.location = (275.03240966796875, 382.68988037109375)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (278.46209716796875, 153.4551544189453)
        Combine_XYZ_002 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_002.location = (275.65203857421875, -242.83462524414062)
        Combine_XYZ_002.inputs["X"].default_value = 1.0
        Combine_XYZ_002.inputs["Y"].default_value = 0.0
        Combine_XYZ_002.inputs["Z"].default_value = 0.0
        Combine_XYZ_003 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_003.location = (275.65203857421875, -108.6993408203125)
        Combine_XYZ_003.inputs["X"].default_value = -1.0
        Combine_XYZ_003.inputs["Y"].default_value = 0.0
        Combine_XYZ_003.inputs["Z"].default_value = 0.0
        # Create links
        nt.links.new(Attribute_001.outputs["Vector"], Group_004.inputs["Oxyz"])
        nt.links.new(Group_003.outputs["Oxy"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Attribute.outputs["Vector"], Group_003.inputs["Oxyz"])
        nt.links.new(Group_004.outputs["Oxy"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Vector_Math_002.outputs["Vector"], Group_Output.inputs["Fx"])
        nt.links.new(Vector_Math_001.outputs["Vector"], Group_Output.inputs["Fy"])
        nt.links.new(Combine_XYZ_002.outputs["Vector"], Group_Output.inputs["X(1, 0, 0)"])
        nt.links.new(Combine_XYZ_003.outputs["Vector"], Group_Output.inputs["X(-1, 0, 0)"])