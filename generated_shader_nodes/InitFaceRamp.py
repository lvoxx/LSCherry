import bpy
from ..utils import ShaderNode


class ShaderNodeInitFaceRamp(ShaderNode):
    bl_label = "Init Face Ramp"
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
            Face_Vector_socket = nt.interface.new_socket(
                name="Face Vector",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Face_Vector_socket.default_value = (0.0, 0.0, 0.0)
        Face_Vector_socket.subtype = "NONE"
            Is_X_Side_socket = nt.interface.new_socket(
                name="Is X Side",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Is_X_Side_socket.default_value = 0.0
        Is_X_Side_socket.min_value = -3.4028234663852886e+38
        Is_X_Side_socket.max_value = 3.4028234663852886e+38
        Is_X_Side_socket.subtype = "NONE"

        # Input sockets
            Deprecated_socket = nt.interface.new_socket(
                name="Deprecated",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
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
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (97.22677612304688, -255.40377807617188)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (261.4367980957031, 511.54351806640625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-618.3001098632812, 88.67147827148438)
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
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (423.24176025390625, -185.3865966796875)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (844.465087890625, 347.05712890625)
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (977.9639282226562, 54.206703186035156)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-169.753173828125, 268.5618591308594)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (485.61187744140625, -44.27337646484375)
        Mix.data_type = "VECTOR"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (813.0778198242188, -336.0631408691406)
        Group_002 = nt.nodes.new("ShaderNodeGroup")
        Group_002.location = (-614.2136840820312, 303.8605041503906)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-129.55636596679688, -28.63583755493164)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-169.753173828125, -352.84197998046875)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-251.4383544921875, -375.2464904785156)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-169.753173828125, 132.0079345703125)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-129.55636596679688, 106.93687438964844)
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (288.5528259277344, -325.3872985839844)
        Combine_XYZ_001.inputs["Y"].default_value = 1.0
        Combine_XYZ_001.inputs["Z"].default_value = 1.0
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (288.5528259277344, -194.30615234375)
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
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-196.0395050048828, -421.54840087890625)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (423.2417297363281, -32.905548095703125)
        Vector_Math_003 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_003.location = (-196.08633422851562, -288.5357360839844)
        Vector_Math_003.operation = "DOT_PRODUCT"
        Vector_Math_003.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs["Scale"].default_value = 1.0
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (-251.4383544921875, -197.71432495117188)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (-14.38739013671875, -251.07644653320312)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (-14.38739013671875, -80.17926025390625)
        Vector_Math_002 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_002.location = (162.78460693359375, -251.07644653320312)
        Vector_Math_002.operation = "NORMALIZE"
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Scale"].default_value = 1.0
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (162.78460693359375, -80.17926025390625)
        Vector_Math_001.operation = "NORMALIZE"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (9.15557861328125, -211.96096801757812)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (166.67138671875, 2.3528900146484375)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (621.8849487304688, -10.73919677734375)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1243.07861328125, 343.13787841796875)
        Group_001 = nt.nodes.new("ShaderNodeGroup")
        Group_001.location = (-793.5289916992188, 329.8482971191406)
        Group_001.inputs["Invert MLight"].default_value = False
        Group_001.inputs["Mix Light and View"].default_value = 0.0
        Attribute_001 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_001.location = (-1074.020263671875, -181.37783813476562)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (-1074.020263671875, -59.146995544433594)
        Normal_Map = nt.nodes.new("ShaderNodeNormalMap")
        Normal_Map.location = (-1072.22021484375, 109.19798278808594)
        Normal_Map.inputs["Strength"].default_value = 1.0
        Normal_Map.inputs["Color"].default_value = (0.5, 0.5, 1.0, 1.0)
        Attribute_002 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_002.location = (-1074.020263671875, 238.6177215576172)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-1.090179443359375, 579.9298706054688)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (520.468505859375, 259.1134338378906)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (794.4168701171875, 300.3866271972656)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (16.471389770507812, 680.5955810546875)
        # Create links
        nt.links.new(Group_004.outputs["Oxy"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Reroute_003.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Group_003.outputs["Oxy"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Vector_Math.outputs["Vector"], Reroute.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Math.outputs["Value"], Reroute_007.inputs["Input"])
        nt.links.new(Group_002.outputs["Oxy"], Vector_Math.inputs["Vector"])
        nt.links.new(Vector_Math_003.outputs["Value"], Map_Range.inputs["Value"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Vector_Math_004.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Group_001.outputs["Main Light Vector"], Group_002.inputs["Oxyz"])
        nt.links.new(Reroute_006.outputs["Output"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Group_Output.inputs["Face Value"])
        nt.links.new(Group_Input_001.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Mapping.outputs["Vector"], Group_Output.inputs["Face Vector"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Reroute_005.outputs["Output"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Reroute_011.outputs["Output"], Mapping.inputs["Scale"])
        nt.links.new(Mix.outputs["Result"], Reroute_011.inputs["Input"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mix.inputs["A"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Mix.inputs["B"])
        nt.links.new(Group_Input_003.outputs["Default UV"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input_003.outputs["Flip UV"], Combine_XYZ_001.inputs["X"])
        nt.links.new(Group_Input.outputs["Min Dot Value"], Map_Range.inputs["From Min"])
        nt.links.new(Group_Input.outputs["Max  Dot Value"], Map_Range.inputs["From Max"])
        nt.links.new(Map_Range.outputs["Result"], Reroute_010.inputs["Input"])
        nt.links.new(Vector_Math_002.outputs["Vector"], Reroute_003.inputs["Input"])
        nt.links.new(Vector_Math_001.outputs["Vector"], Reroute_002.inputs["Input"])
        nt.links.new(Normal_Map.outputs["Normal"], Group_001.inputs["Normal"])
        nt.links.new(Attribute.outputs["Vector"], Group_003.inputs["Oxyz"])
        nt.links.new(Attribute_001.outputs["Vector"], Group_004.inputs["Oxyz"])
        nt.links.new(Attribute_002.outputs["Vector"], Group_001.inputs["Light Dir"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Invert_Color.outputs["Color"], Group_Output.inputs["Is X Side"])
        nt.links.new(Reroute_009.outputs["Output"], Invert_Color.inputs["Color"])