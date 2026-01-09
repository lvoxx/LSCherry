import bpy
from ..utils import ShaderNode


class ShaderNodeXtrParallaxUv(ShaderNode):
    bl_label = "XTR: Parallax UV"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            Parallax_UV_socket = nt.interface.new_socket(
                name="Parallax UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Parallax_UV_socket.default_value = (0.0, 0.0, 0.0)
        Parallax_UV_socket.subtype = "NONE"

        # Input sockets
            UV_Map_socket = nt.interface.new_socket(
                name="UV Map",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_Map_socket.default_value = (0.0, 0.0, 0.0)
        UV_Map_socket.subtype = "NONE"
            Tangent_UV_socket = nt.interface.new_socket(
                name="Tangent UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Tangent_UV_socket.default_value = (0.0, 0.0, 0.0)
        Tangent_UV_socket.subtype = "NONE"
            Distance_socket = nt.interface.new_socket(
                name="Distance",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Distance_socket.default_value = 0.0
        Distance_socket.min_value = 0.0
        Distance_socket.max_value = 100.0
        Distance_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (832.8324584960938, 56.038211822509766)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-860.593017578125, -137.4239044189453)
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-649.3381958007812, 73.59461975097656)
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-369.15557861328125, -109.80319213867188)
        Vector_Math.operation = "CROSS_PRODUCT"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (-128.464111328125, -38.04986572265625)
        Vector_Math_001.operation = "DOT_PRODUCT"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Vector_Math_002 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_002.location = (-128.464111328125, -75.01606750488281)
        Vector_Math_002.operation = "DOT_PRODUCT"
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Scale"].default_value = 1.0
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (62.574005126953125, -29.362245559692383)
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Vector_Math_003 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_003.location = (238.40826416015625, 1.087677001953125)
        Vector_Math_003.operation = "TANGENT"
        Vector_Math_003.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs["Scale"].default_value = 1.0
        Vector_Math_004 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_004.location = (429.43560791015625, -19.763751983642578)
        Vector_Math_004.operation = "SCALE"
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_005.location = (635.0256958007812, 58.97786331176758)
        Vector_Math_005.operation = "SUBTRACT"
        Vector_Math_005.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs["Scale"].default_value = 1.159999966621399
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (237.5664520263672, -112.66283416748047)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (302.40301513671875, 68.76893615722656)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-681.0000610351562, -198.0869903564453)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-444.33599853515625, 228.45675659179688)
        # Create links
        nt.links.new(Geometry.outputs["Incoming"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Vector_Math_002.outputs["Value"], Combine_XYZ.inputs["Y"])
        nt.links.new(Vector_Math_001.outputs["Value"], Combine_XYZ.inputs["X"])
        nt.links.new(Geometry.outputs["Normal"], Vector_Math.inputs["Vector"])
        nt.links.new(Vector_Math.outputs["Vector"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Vector_Math_004.outputs["Vector"], Vector_Math_005.inputs["Vector"])
        nt.links.new(Vector_Math_003.outputs["Vector"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Geometry.outputs["Incoming"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Reroute_001.outputs["Output"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Reroute.outputs["Output"], Vector_Math_005.inputs["Vector"])
        nt.links.new(Group_Input_001.outputs["Distance"], Vector_Math_004.inputs["Scale"])
        nt.links.new(Vector_Math_005.outputs["Vector"], Group_Output.inputs["Parallax UV"])
        nt.links.new(Group_Input.outputs["UV Map"], Reroute.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Vector_Math.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Tangent UV"], Reroute_001.inputs["Input"])