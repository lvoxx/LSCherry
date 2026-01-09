import bpy
from ..utils import ShaderNode


class ShaderNodeToonDot(ShaderNode):
    bl_label = "Toon Dot"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            NdotV_socket = nt.interface.new_socket(
                name="NdotV",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        NdotV_socket.default_value = 0.0
        NdotV_socket.min_value = -3.4028234663852886e+38
        NdotV_socket.max_value = 3.4028234663852886e+38
        NdotV_socket.subtype = "NONE"
            NdotL_socket = nt.interface.new_socket(
                name="NdotL",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        NdotL_socket.default_value = 0.0
        NdotL_socket.min_value = -3.4028234663852886e+38
        NdotL_socket.max_value = 3.4028234663852886e+38
        NdotL_socket.subtype = "NONE"
            VcrsNcrsL_socket = nt.interface.new_socket(
                name="VcrsNcrsL",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        VcrsNcrsL_socket.default_value = 0.0
        VcrsNcrsL_socket.min_value = -3.4028234663852886e+38
        VcrsNcrsL_socket.max_value = 3.4028234663852886e+38
        VcrsNcrsL_socket.subtype = "NONE"
            Mix_L_and_V_socket = nt.interface.new_socket(
                name="Mix L and V",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_L_and_V_socket.default_value = 0.0
        Mix_L_and_V_socket.min_value = -3.4028234663852886e+38
        Mix_L_and_V_socket.max_value = 3.4028234663852886e+38
        Mix_L_and_V_socket.subtype = "NONE"
            Main_Light_Vector_socket = nt.interface.new_socket(
                name="Main Light Vector",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Main_Light_Vector_socket.default_value = (0.0, 0.0, 0.0)
        Main_Light_Vector_socket.subtype = "NONE"
            Face_To_X_socket = nt.interface.new_socket(
                name="Face To X",
                in_out="OUTPUT",
                socket_type="NodeSocketBool"
            )
        
        Face_To_X_socket.default_value = False
            Face_To_Y_socket = nt.interface.new_socket(
                name="Face To Y",
                in_out="OUTPUT",
                socket_type="NodeSocketBool"
            )
        
        Face_To_Y_socket.default_value = False

        # Input sockets
            Invert_MLight_socket = nt.interface.new_socket(
                name="Invert MLight",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Invert_MLight_socket.default_value = False
            Light_Dir_socket = nt.interface.new_socket(
                name="Light Dir",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Light_Dir_socket.default_value = (0.0, 0.0, 0.0)
        Light_Dir_socket.subtype = "XYZ"
            Mix_Light_and_View_socket = nt.interface.new_socket(
                name="Mix Light and View",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_Light_and_View_socket.default_value = 0.0
        Mix_Light_and_View_socket.min_value = 0.0
        Mix_Light_and_View_socket.max_value = 1.0
        Mix_Light_and_View_socket.subtype = "FACTOR"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (-31.3594970703125, 1157.6689453125)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-31.3594970703125, 265.5730895996094)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (264.9783935546875, 898.517578125)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (1213.926025390625, 89.26538848876953)
        Vector_Math_004 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_004.location = (126.94804382324219, -402.45391845703125)
        Vector_Math_004.operation = "NORMALIZE"
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_004.inputs["Scale"].default_value = 1.0
        Vector_Rotate = nt.nodes.new("ShaderNodeVectorRotate")
        Vector_Rotate.location = (-95.94075012207031, -324.20428466796875)
        Vector_Rotate.inputs["Center"].default_value = (0.0, 0.0, 0.0)
        Vector_Rotate.inputs["Axis"].default_value = (0.0, 0.0, 1.0)
        Vector_Rotate.inputs["Angle"].default_value = 0.0
        Vector_Math_001 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_001.location = (126.94804382324219, -128.33355712890625)
        Vector_Math_001.operation = "NORMALIZE"
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs["Scale"].default_value = 1.0
        Vector_Math = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math.location = (126.94804382324219, -265.80462646484375)
        Vector_Math.operation = "NORMALIZE"
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs["Scale"].default_value = 1.0
        Vector_Math_003 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_003.location = (430.491455078125, -430.894775390625)
        Vector_Math_003.operation = "DOT_PRODUCT"
        Vector_Math_003.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_003.inputs["Scale"].default_value = 1.0
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (297.0549621582031, -163.7908935546875)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (355.698486328125, -438.22857666015625)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (297.0549621582031, -533.698974609375)
        Vector_Math_002 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_002.location = (397.5554504394531, -160.74398803710938)
        Vector_Math_002.operation = "DOT_PRODUCT"
        Vector_Math_002.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs["Scale"].default_value = 1.0
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (1213.926025390625, 691.8231201171875)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (478.1412353515625, -442.7287902832031)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (656.6358032226562, 691.8231201171875)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (391.65740966796875, -575.040771484375)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (1155.611083984375, 26.827266693115234)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (1155.611083984375, 420.6535339355469)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (699.0987548828125, 67.21537780761719)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (434.120361328125, -597.2357788085938)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-410.48394775390625, -353.64141845703125)
        Combine_XYZ.inputs["X"].default_value = 0.0
        Combine_XYZ.inputs["Y"].default_value = 0.0
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-54.156494140625, -452.8433837890625)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (297.0549621582031, -244.2223663330078)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (223.2584228515625, -516.0947875976562)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (321.83795166015625, -299.7584228515625)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (1210.61328125, -34.185333251953125)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1361.9256591796875, 124.57601928710938)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (-347.0815124511719, -489.9013671875)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (-980.5386962890625, -257.9797058105469)
        Vector_Math_005 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_005.location = (361.0902404785156, -419.984375)
        Vector_Math_005.operation = "CROSS_PRODUCT"
        Vector_Math_005.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_005.inputs["Scale"].default_value = 1.0
        Vector_Math_006 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_006.location = (562.9507446289062, -319.67523193359375)
        Vector_Math_006.operation = "CROSS_PRODUCT"
        Vector_Math_006.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_006.inputs["Scale"].default_value = 1.0
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (355.698486328125, -400.71527099609375)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (321.83795166015625, -527.7340087890625)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (297.0549621582031, -506.0687255859375)
        Vector_Math_007 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_007.location = (751.1427001953125, -325.10028076171875)
        Vector_Math_007.operation = "LENGTH"
        Vector_Math_007.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_007.inputs["Scale"].default_value = 1.0
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (948.2926025390625, -327.5105285644531)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (375.4696350097656, 943.408203125)
        Vector_Math_008 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_008.location = (384.3673095703125, -361.69512939453125)
        Vector_Math_008.operation = "DOT_PRODUCT"
        Vector_Math_008.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_008.inputs["Scale"].default_value = 1.0
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (147.62876892089844, -429.7706298828125)
        Combine_XYZ_001.inputs["X"].default_value = 1.0
        Combine_XYZ_001.inputs["Y"].default_value = 0.0
        Combine_XYZ_001.inputs["Z"].default_value = 0.0
        Vector_Math_009 = nt.nodes.new("ShaderNodeVectorMath")
        Vector_Math_009.location = (384.3673095703125, -488.478759765625)
        Vector_Math_009.operation = "DOT_PRODUCT"
        Vector_Math_009.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Vector_Math_009.inputs["Scale"].default_value = 1.0
        Combine_XYZ_002 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_002.location = (147.62876892089844, -564.70458984375)
        Combine_XYZ_002.inputs["X"].default_value = 0.0
        Combine_XYZ_002.inputs["Y"].default_value = 1.0
        Combine_XYZ_002.inputs["Z"].default_value = 0.0
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (665.54052734375, -371.33685302734375)
        Math.operation = "LESS_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (665.54052734375, -528.9599609375)
        Math_001.operation = "LESS_THAN"
        Math_001.inputs["Value"].default_value = 0.0
        Math_001.inputs["Value"].default_value = 0.5
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (290.47845458984375, -374.2950744628906)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (1153.4193115234375, -407.2030029296875)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (1179.7286376953125, -566.2504272460938)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (-691.4459228515625, -330.23748779296875)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 1.0
        Mix_001.inputs["B"].default_value = -1.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        # Create links
        nt.links.new(Vector_Rotate.outputs["Vector"], Vector_Math.inputs["Vector"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Vector_Rotate.inputs["Vector"])
        nt.links.new(Geometry.outputs["Incoming"], Vector_Math_004.inputs["Vector"])
        nt.links.new(Vector_Math_001.outputs["Vector"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Reroute_002.outputs["Output"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Vector_Math_004.outputs["Vector"], Reroute_004.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Vector_Math_003.inputs["Vector"])
        nt.links.new(Vector_Math.outputs["Vector"], Reroute_007.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Group_Output.inputs["NdotV"])
        nt.links.new(Reroute_012.outputs["Output"], Group_Output.inputs["Mix L and V"])
        nt.links.new(Vector_Math_002.outputs["Value"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Group_Output.inputs["NdotL"])
        nt.links.new(Group_Input.outputs["Mix Light and View"], Mix.inputs["Factor"])
        nt.links.new(Reroute.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Vector_Math_003.outputs["Value"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Reroute_014.inputs["Input"])
        nt.links.new(Reroute_014.outputs["Output"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Mix.inputs["B"])
        nt.links.new(Group_Input_002.outputs["Light Dir"], Vector_Rotate.inputs["Rotation"])
        nt.links.new(Reroute_007.outputs["Output"], Vector_Math_002.inputs["Vector"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Group_Output.inputs["Main Light Vector"])
        nt.links.new(Group_Input_001.outputs["Normal"], Vector_Math_001.inputs["Vector"])
        nt.links.new(Vector_Math_005.outputs["Vector"], Vector_Math_006.inputs["Vector"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Vector_Math_005.inputs["Vector"])
        nt.links.new(Reroute_001.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Vector_Math_005.inputs["Vector"])
        nt.links.new(Reroute_005.outputs["Output"], Vector_Math_006.inputs["Vector"])
        nt.links.new(Vector_Math_006.outputs["Vector"], Vector_Math_007.inputs["Vector"])
        nt.links.new(Invert_Color.outputs["Color"], Group_Output.inputs["VcrsNcrsL"])
        nt.links.new(Vector_Math_007.outputs["Value"], Invert_Color.inputs["Color"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Vector_Math_008.inputs["Vector"])
        nt.links.new(Combine_XYZ_002.outputs["Vector"], Vector_Math_009.inputs["Vector"])
        nt.links.new(Vector_Math_008.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Vector_Math_009.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Vector_Math_008.inputs["Vector"])
        nt.links.new(Reroute_018.outputs["Output"], Vector_Math_009.inputs["Vector"])
        nt.links.new(Math.outputs["Value"], Reroute_019.inputs["Input"])
        nt.links.new(Math_001.outputs["Value"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Group_Output.inputs["Face To X"])
        nt.links.new(Reroute_020.outputs["Output"], Group_Output.inputs["Face To Y"])
        nt.links.new(Mix_001.outputs["Result"], Combine_XYZ.inputs["Z"])
        nt.links.new(Group_Input_001.outputs["Invert MLight"], Mix_001.inputs["Factor"])