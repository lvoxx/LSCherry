import bpy
from ..utils import ShaderNode


class ShaderNodeFaceRampBuilder(ShaderNode):
    bl_label = "Face Ramp Builder"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Face_Value_socket = nt.interface.new_socket(
                name="Face Value",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Value_socket.default_value = 0.0
        Face_Value_socket.min_value = -3.4028234663852886e+38
        Face_Value_socket.max_value = 3.4028234663852886e+38
        Face_Value_socket.subtype = "NONE"
            Face_GS-Vector_socket = nt.interface.new_socket(
                name="Face GS-Vector",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Face_GS-Vector_socket.default_value = (0.0, 0.0, 0.0)
        Face_GS-Vector_socket.subtype = "NONE"

        # Input sockets
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"
            Min_Dot_Value_socket = nt.interface.new_socket(
                name="Min Dot Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Min_Dot_Value_socket.default_value = -0.5
        Min_Dot_Value_socket.min_value = -1.0
        Min_Dot_Value_socket.max_value = 1.0
        Min_Dot_Value_socket.subtype = "NONE"
            Max__Dot_Value_socket = nt.interface.new_socket(
                name="Max  Dot Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Max__Dot_Value_socket.default_value = 0.5
        Max__Dot_Value_socket.min_value = -1.0
        Max__Dot_Value_socket.max_value = 1.0
        Max__Dot_Value_socket.subtype = "NONE"
            Default_UV_socket = nt.interface.new_socket(
                name="Default UV",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Default_UV_socket.default_value = -1.0
        Default_UV_socket.min_value = -1.0
        Default_UV_socket.max_value = 1.0
        Default_UV_socket.subtype = "NONE"
            Flip_UV_socket = nt.interface.new_socket(
                name="Flip UV",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Flip_UV_socket.default_value = 1.0
        Flip_UV_socket.min_value = -1.0
        Flip_UV_socket.max_value = 1.0
        Flip_UV_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1063.715576171875, 334.88153076171875)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (484.12030029296875, 202.40728759765625)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-43.1673583984375, 25.653594970703125)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (122.04266357421875, 511.54351806640625)
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (-436.7603759765625, 303.8605041503906)
        Vector_Math.operation = "NORMALIZE"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Vector_Math_004 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_004.location = (-33.008544921875, -7.8170166015625)
        Vector_Math_004.operation = "DOT_PRODUCT"
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs["Scale"].default_value = 1.0
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (415.8372497558594, 366.1020812988281)
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (789.5553588867188, 166.19171142578125)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-184.5743408203125, 268.5618591308594)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (537.69580078125, -36.428680419921875)
        Mix.data_type = "VECTOR"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Group_002 = nt.nodes.new("ShaderNodeGroup")
        Group_002.location = (-614.2136840820312, 303.8605041503906)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-250.7588348388672, -73.22085571289062)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-184.5743408203125, -65.05874633789062)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-213.39797973632812, -51.35321044921875)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-184.5743408203125, 138.08108520507812)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-250.7588348388672, 116.20392608642578)
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (274.46282958984375, -103.37098693847656)
        Combine_XYZ_001.inputs["Y"].default_value = 1.0
        Combine_XYZ_001.inputs["Z"].default_value = 1.0
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (274.46282958984375, -68.40756225585938)
        Combine_XYZ.inputs["Y"].default_value = 1.0
        Combine_XYZ.inputs["Z"].default_value = 1.0
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (42.38671112060547, -110.4229736328125)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Vector_Math_003 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_003.location = (-196.08633422851562, -288.5357360839844)
        Vector_Math_003.operation = "DOT_PRODUCT"
        Vector_Math_003.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs["Scale"].default_value = 1.0
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (150.931396484375, -25.15631103515625)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (-793.5289916992188, 329.8482971191406)
        Group_001.inputs["Invert MLight"].default_value = False
        Group_001.inputs["Mix Light and View"].default_value = 0.0
        Attribute_002 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_002.location = (-1074.020263671875, 238.6177215576172)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-1.090179443359375, 579.9298706054688)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (16.471389770507812, 680.5955810546875)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-200.68682861328125, -186.83587646484375)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (273.7416687011719, -135.9036865234375)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (407.5379333496094, 138.11953735351562)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (450.7052917480469, -71.38351440429688)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (699.2705078125, -22.6007080078125)
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (699.2705078125, 143.70297241210938)
        Reroute_025 = nt.nodes.new("NodeReroute")
        Reroute_025.location = (967.9348754882812, 156.50965881347656)
        Reroute_026 = nt.nodes.new("NodeReroute")
        Reroute_026.location = (967.9348754882812, 278.0309753417969)
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-1073.031005859375, 100.34602355957031)
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (42.878692626953125, -363.50543212890625)
        Math_003.operation = "GREATER_THAN"
        Math_003.inputs["Value"].default_value = 0.0
        Math_003.inputs["Value"].default_value = 0.5
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-576.6366577148438, -16.496978759765625)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (-213.39797973632812, -89.3150634765625)
        # Create links
        nt.links.new(Reroute_004.outputs["Output"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Vector_Math.outputs["Vector"], Reroute.inputs["Input"])
        nt.links.new(Group_002.outputs["Oxy"], Vector_Math.inputs["Vector"])
        nt.links.new(Group_001.outputs["Main Light Vector"], Group_002.inputs["Oxyz"])
        nt.links.new(Reroute_006.outputs["Output"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mix.inputs["A"])
        nt.links.new(Map_Range.outputs["Result"], Reroute_010.inputs["Input"])
        nt.links.new(Group.outputs["Fy"], Reroute_002.inputs["Input"])
        nt.links.new(Attribute_002.outputs["Vector"], Group_001.inputs["Light Dir"])
        nt.links.new(Group_Input_001.outputs["Min Dot Value"], Map_Range.inputs["From Min"])
        nt.links.new(Group_Input_001.outputs["Max  Dot Value"], Map_Range.inputs["From Max"])
        nt.links.new(Group_Input_002.outputs["Flip UV"], Combine_XYZ_001.inputs["X"])
        nt.links.new(Group_Input_002.outputs["Default UV"], Combine_XYZ.inputs["X"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Mix.outputs["Result"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Mapping.inputs["Scale"])
        nt.links.new(Reroute_025.outputs["Output"], Reroute_026.inputs["Input"])
        nt.links.new(Reroute_026.outputs["Output"], Group_Output.inputs["Face GS-Vector"])
        nt.links.new(Geometry.outputs["Normal"], Group_001.inputs["Normal"])
        nt.links.new(Reroute_010.outputs["Output"], Group_Output.inputs["Face Value"])
        nt.links.new(Mapping.outputs["Vector"], Reroute_025.inputs["Input"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Mix.inputs["B"])
        nt.links.new(Math_003.outputs["Value"], Reroute_007.inputs["Input"])
        nt.links.new(Vector_Math_004.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Group.outputs["Fx"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Vector_Math_003.outputs["Value"], Map_Range.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Math_003.inputs["Value"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])