import bpy
from ..utils import ShaderNode


class ShaderNodeSpecularDot001(ShaderNode):
    bl_label = "Specular Dot.001"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "NONE"
        nt.description = ""

        # Output sockets
            Specular_socket = nt.interface.new_socket(
                name="Specular",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Specular_socket.default_value = 0.0
        Specular_socket.min_value = -3.4028234663852886e+38
        Specular_socket.max_value = 3.4028234663852886e+38
        Specular_socket.subtype = "NONE"

        # Input sockets
            Light_Dir_socket = nt.interface.new_socket(
                name="Light Dir",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Light_Dir_socket.default_value = (0.0, 0.0, 0.0)
        Light_Dir_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (586.1936645507812, 51.95869445800781)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1177.8431396484375, -14.91910457611084)
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-774.6715698242188, -102.4208984375)
        Vector_Math_004 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_004.location = (-594.3843994140625, -64.6788330078125)
        Vector_Math_004.operation = "NORMALIZE"
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs["Scale"].default_value = 1.0
        Vector_Math_005 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_005.location = (-362.0174560546875, 51.208518981933594)
        Vector_Math_005.operation = "DOT_PRODUCT"
        Vector_Math_005.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs["Scale"].default_value = 1.0
        Vector_Rotate = nt.nodes.new("ShaderNodeVectorRotate")
        Vector_Rotate.location = (-955.6923828125, 116.63909149169922)
        Vector_Rotate.inputs["Center"].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate.inputs["Axis"].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate.inputs["Angle"].default_value = 0.0
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-1316.3924560546875, 135.5072784423828)
        Combine_XYZ.inputs["X"].default_value = 0.0
        Combine_XYZ.inputs["Y"].default_value = 0.0
        Combine_XYZ.inputs["Z"].default_value = -1.0
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (401.16302490234375, 34.977012634277344)
        Math.operation = "POWER"
        Math.inputs["Value"].default_value = 0.5
        Math.inputs["Value"].default_value = 0.5
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (166.819580078125, -90.20521545410156)
        Vector_Math_006 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_006.location = (-568.5167236328125, 57.11375427246094)
        Vector_Math_006.operation = "NORMALIZE"
        Vector_Math_006.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs["Scale"].default_value = 1.0
        Vector_Math_010 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_010.location = (-761.449462890625, 77.2073974609375)
        Vector_Math_010.operation = "REFLECT"
        Vector_Math_010.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_010.inputs["Scale"].default_value = 1.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-1.6712188720703125, 237.70672607421875)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Vector_Math_012 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_012.location = (-465.1744384765625, 312.0865783691406)
        Vector_Math_012.operation = "DOT_PRODUCT"
        Vector_Math_012.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_012.inputs["Scale"].default_value = 1.0
        Vector_Math_007 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_007.location = (-285.43194580078125, 276.3628234863281)
        Vector_Math_007.operation = "NORMALIZE"
        Vector_Math_007.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs["Scale"].default_value = 1.0
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-1065.779052734375, 334.2599792480469)
        Vector_Rotate_001 = nt.nodes.new("ShaderNodeVectorRotate")
        Vector_Rotate_001.location = (-843.6282958984375, 465.81817626953125)
        Vector_Rotate_001.inputs["Center"].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate_001.inputs["Axis"].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate_001.inputs["Angle"].default_value = 0.0
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (-1204.328369140625, 484.68634033203125)
        Combine_XYZ_001.inputs["X"].default_value = 0.0
        Combine_XYZ_001.inputs["Y"].default_value = 0.0
        Combine_XYZ_001.inputs["Z"].default_value = 1.0
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-352.8446044921875, 474.5015563964844)
        # Create links
        nt.links.new(Geometry.outputs["Incoming"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Vector_Math_006.outputs["Vector"], Vector_Math_005.inputs["Vector"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Vector_Rotate.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Light Dir"], Vector_Rotate.inputs["Rotation"])
        nt.links.new(Math.outputs["Value"], Group_Output.inputs["Specular"])
        nt.links.new(Group_Input.outputs["Normal"], Vector_Math_010.inputs["Vector"])
        nt.links.new(Vector_Math_007.outputs["Vector"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Normal"], Mix.inputs["A"])
        nt.links.new(Vector_Math_004.outputs["Vector"], Mix.inputs["B"])
        nt.links.new(Vector_Math_012.outputs["Value"], Vector_Math_007.inputs["Vector"])
        nt.links.new(Vector_Math_004.outputs["Vector"], Vector_Math_005.inputs["Vector"])
        nt.links.new(Vector_Math_012.outputs["Value"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Math.inputs["Value"])
        nt.links.new(Vector_Math_005.outputs["Value"], Mix.inputs["B"])
        nt.links.new(Vector_Rotate.outputs["Vector"], Vector_Math_010.inputs["Vector"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Vector_Rotate_001.inputs["Vector"])
        nt.links.new(Group_Input_002.outputs["Light Dir"], Vector_Rotate_001.inputs["Rotation"])
        nt.links.new(Vector_Rotate_001.outputs["Vector"], Vector_Math_012.inputs["Vector"])
        nt.links.new(Group_Input_002.outputs["Normal"], Vector_Math_012.inputs["Vector"])
        nt.links.new(Vector_Math_010.outputs["Vector"], Vector_Math_006.inputs["Vector"])