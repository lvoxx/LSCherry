import bpy
from ..utils import ShaderNode


class ShaderNodeGiBuildRampFromMap(ShaderNode):
    bl_label = "GI: Build Ramp From Map"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            Hot-UV1_socket = nt.interface.new_socket(
                name="Hot-UV1",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Hot-UV1_socket.default_value = (0.0, 0.0, 0.0)
        Hot-UV1_socket.subtype = "NONE"
            Hot-UV2_socket = nt.interface.new_socket(
                name="Hot-UV2",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Hot-UV2_socket.default_value = (0.0, 0.0, 0.0)
        Hot-UV2_socket.subtype = "NONE"
            Hot-UV3_socket = nt.interface.new_socket(
                name="Hot-UV3",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Hot-UV3_socket.default_value = (0.0, 0.0, 0.0)
        Hot-UV3_socket.subtype = "NONE"
            Hot-UV4_socket = nt.interface.new_socket(
                name="Hot-UV4",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Hot-UV4_socket.default_value = (0.0, 0.0, 0.0)
        Hot-UV4_socket.subtype = "NONE"
            Hot-UV5_socket = nt.interface.new_socket(
                name="Hot-UV5",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Hot-UV5_socket.default_value = (0.0, 0.0, 0.0)
        Hot-UV5_socket.subtype = "NONE"
            Cold-UV1_socket = nt.interface.new_socket(
                name="Cold-UV1",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Cold-UV1_socket.default_value = (0.0, 0.0, 0.0)
        Cold-UV1_socket.subtype = "NONE"
            Cold-UV2_socket = nt.interface.new_socket(
                name="Cold-UV2",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Cold-UV2_socket.default_value = (0.0, 0.0, 0.0)
        Cold-UV2_socket.subtype = "NONE"
            Cold-UV3_socket = nt.interface.new_socket(
                name="Cold-UV3",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Cold-UV3_socket.default_value = (0.0, 0.0, 0.0)
        Cold-UV3_socket.subtype = "NONE"
            Cold-UV4_socket = nt.interface.new_socket(
                name="Cold-UV4",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Cold-UV4_socket.default_value = (0.0, 0.0, 0.0)
        Cold-UV4_socket.subtype = "NONE"
            Cold-UV5_socket = nt.interface.new_socket(
                name="Cold-UV5",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Cold-UV5_socket.default_value = (0.0, 0.0, 0.0)
        Cold-UV5_socket.subtype = "NONE"

        # Input sockets
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Toon_socket.default_value = 0.0
        Toon_socket.min_value = 0.0
        Toon_socket.max_value = 1.0
        Toon_socket.subtype = "NONE"
            Shadow_Factor_socket = nt.interface.new_socket(
                name="Shadow Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Factor_socket.default_value = 1.0
        Shadow_Factor_socket.min_value = 0.0
        Shadow_Factor_socket.max_value = 1.0
        Shadow_Factor_socket.subtype = "FACTOR"
            Shadow_Mask_socket = nt.interface.new_socket(
                name="Shadow Mask",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shadow_Mask_socket.default_value = 0.0
        Shadow_Mask_socket.min_value = 0.0
        Shadow_Mask_socket.max_value = 1.0
        Shadow_Mask_socket.subtype = "NONE"

        # Create nodes
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-112.73562622070312, -19.041732788085938)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (924.283935546875, 159.4969940185547)
        Group_009 = nt.nodes.new("ShaderNodeGroup")
        Group_009.location = (110.99164581298828, 14.680463790893555)
        Group_009.inputs["Ramp Size"].default_value = 0.10000000149011612
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-590.9628295898438, -61.165870666503906)
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (9.757568359375, -58.710289001464844)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Value = nt.nodes.new("ShaderNodeValue")
        Value.location = (113.41205596923828, -121.33500671386719)
        Mapping_001 = nt.nodes.new("ShaderNodeMapping")
        Mapping_001.location = (9.757568359375, -92.29483032226562)
        Mapping_001.vector_type = "POINT"
        Mapping_001.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_001.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Mapping_002 = nt.nodes.new("ShaderNodeMapping")
        Mapping_002.location = (9.757568359375, -131.1036376953125)
        Mapping_002.vector_type = "POINT"
        Mapping_002.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_002.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Mapping_003 = nt.nodes.new("ShaderNodeMapping")
        Mapping_003.location = (9.757568359375, -167.6734619140625)
        Mapping_003.vector_type = "POINT"
        Mapping_003.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_003.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Mapping_004 = nt.nodes.new("ShaderNodeMapping")
        Mapping_004.location = (9.757568359375, -205.7359619140625)
        Mapping_004.vector_type = "POINT"
        Mapping_004.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_004.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Value_001 = nt.nodes.new("ShaderNodeValue")
        Value_001.location = (113.41205596923828, -156.1265411376953)
        Value_002 = nt.nodes.new("ShaderNodeValue")
        Value_002.location = (113.41205596923828, -190.33822631835938)
        Value_003 = nt.nodes.new("ShaderNodeValue")
        Value_003.location = (108.45938110351562, -227.64901733398438)
        Value_004 = nt.nodes.new("ShaderNodeValue")
        Value_004.location = (108.45939636230469, -258.38153076171875)
        Mapping_005 = nt.nodes.new("ShaderNodeMapping")
        Mapping_005.location = (6.929473876953125, -58.506622314453125)
        Mapping_005.vector_type = "POINT"
        Mapping_005.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_005.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Value_005 = nt.nodes.new("ShaderNodeValue")
        Value_005.location = (113.41205596923828, 184.49720764160156)
        Mapping_006 = nt.nodes.new("ShaderNodeMapping")
        Mapping_006.location = (6.929473876953125, -92.0911865234375)
        Mapping_006.vector_type = "POINT"
        Mapping_006.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_006.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Mapping_007 = nt.nodes.new("ShaderNodeMapping")
        Mapping_007.location = (6.929473876953125, -130.89999389648438)
        Mapping_007.vector_type = "POINT"
        Mapping_007.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Mapping_007.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_007.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Mapping_008 = nt.nodes.new("ShaderNodeMapping")
        Mapping_008.location = (6.929473876953125, -167.46981811523438)
        Mapping_008.vector_type = "POINT"
        Mapping_008.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_008.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Mapping_009 = nt.nodes.new("ShaderNodeMapping")
        Mapping_009.location = (6.929473876953125, -205.5323028564453)
        Mapping_009.vector_type = "POINT"
        Mapping_009.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping_009.inputs["Scale"].default_value = (1.0, 0.10000000149011612, 1.0)
        Value_006 = nt.nodes.new("ShaderNodeValue")
        Value_006.location = (113.41205596923828, 149.70567321777344)
        Value_007 = nt.nodes.new("ShaderNodeValue")
        Value_007.location = (113.41205596923828, 115.49398803710938)
        Value_008 = nt.nodes.new("ShaderNodeValue")
        Value_008.location = (113.41205596923828, 83.31179809570312)
        Value_009 = nt.nodes.new("ShaderNodeValue")
        Value_009.location = (113.41205596923828, 52.57928466796875)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (698.57861328125, -24.5408935546875)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (701.57861328125, 292.301513671875)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (384.42578125, -626.47314453125)
        Combine_XYZ.inputs["X"].default_value = 0.0
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Combine_XYZ_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_001.location = (385.53460693359375, -503.95599365234375)
        Combine_XYZ_001.inputs["X"].default_value = 0.0
        Combine_XYZ_001.inputs["Z"].default_value = 0.0
        Combine_XYZ_002 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_002.location = (383.31707763671875, -368.67242431640625)
        Combine_XYZ_002.inputs["X"].default_value = 0.0
        Combine_XYZ_002.inputs["Z"].default_value = 0.0
        Combine_XYZ_003 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_003.location = (383.31707763671875, -234.4977569580078)
        Combine_XYZ_003.inputs["X"].default_value = 0.0
        Combine_XYZ_003.inputs["Z"].default_value = 0.0
        Combine_XYZ_004 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_004.location = (383.31707763671875, -103.49919891357422)
        Combine_XYZ_004.inputs["X"].default_value = 0.0
        Combine_XYZ_004.inputs["Z"].default_value = 0.0
        Combine_XYZ_005 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_005.location = (384.42578125, 159.09683227539062)
        Combine_XYZ_005.inputs["X"].default_value = 0.0
        Combine_XYZ_005.inputs["Z"].default_value = 0.0
        Combine_XYZ_006 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_006.location = (385.53460693359375, 281.6139831542969)
        Combine_XYZ_006.inputs["X"].default_value = 0.0
        Combine_XYZ_006.inputs["Z"].default_value = 0.0
        Combine_XYZ_007 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_007.location = (383.31707763671875, 416.8975524902344)
        Combine_XYZ_007.inputs["X"].default_value = 0.0
        Combine_XYZ_007.inputs["Z"].default_value = 0.0
        Combine_XYZ_008 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_008.location = (383.31707763671875, 551.072265625)
        Combine_XYZ_008.inputs["X"].default_value = 0.0
        Combine_XYZ_008.inputs["Z"].default_value = 0.0
        Combine_XYZ_009 = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ_009.location = (383.31707763671875, 682.07080078125)
        Combine_XYZ_009.inputs["X"].default_value = 0.0
        Combine_XYZ_009.inputs["Z"].default_value = 0.0
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-406.3336181640625, 117.65444946289062)
        # Create links
        nt.links.new(Mix.outputs["Result"], Group_009.inputs["Toon"])
        nt.links.new(Mapping.outputs["Vector"], Group_Output.inputs["Cold-UV1"])
        nt.links.new(Group_Input.outputs["Shadow Mask"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Shadow Factor"], Mix.inputs["Factor"])
        nt.links.new(Group_009.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Combine_XYZ_004.outputs["Vector"], Mapping.inputs["Location"])
        nt.links.new(Group_009.outputs["UV"], Mapping_001.inputs["Vector"])
        nt.links.new(Combine_XYZ_003.outputs["Vector"], Mapping_001.inputs["Location"])
        nt.links.new(Combine_XYZ_002.outputs["Vector"], Mapping_002.inputs["Location"])
        nt.links.new(Group_009.outputs["UV"], Mapping_002.inputs["Vector"])
        nt.links.new(Group_009.outputs["UV"], Mapping_003.inputs["Vector"])
        nt.links.new(Combine_XYZ_001.outputs["Vector"], Mapping_003.inputs["Location"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Mapping_004.inputs["Location"])
        nt.links.new(Group_009.outputs["UV"], Mapping_004.inputs["Vector"])
        nt.links.new(Mapping_001.outputs["Vector"], Group_Output.inputs["Cold-UV2"])
        nt.links.new(Mapping_002.outputs["Vector"], Group_Output.inputs["Cold-UV3"])
        nt.links.new(Mapping_003.outputs["Vector"], Group_Output.inputs["Cold-UV4"])
        nt.links.new(Mapping_004.outputs["Vector"], Group_Output.inputs["Cold-UV5"])
        nt.links.new(Group_009.outputs["UV"], Mapping_005.inputs["Vector"])
        nt.links.new(Group_009.outputs["UV"], Mapping_006.inputs["Vector"])
        nt.links.new(Group_009.outputs["UV"], Mapping_008.inputs["Vector"])
        nt.links.new(Group_009.outputs["UV"], Mapping_009.inputs["Vector"])
        nt.links.new(Mapping_006.outputs["Vector"], Group_Output.inputs["Hot-UV2"])
        nt.links.new(Mapping_007.outputs["Vector"], Group_Output.inputs["Hot-UV3"])
        nt.links.new(Mapping_008.outputs["Vector"], Group_Output.inputs["Hot-UV4"])
        nt.links.new(Mapping_009.outputs["Vector"], Group_Output.inputs["Hot-UV5"])
        nt.links.new(Group_Input.outputs["Toon"], Mix.inputs["A"])
        nt.links.new(Mapping_005.outputs["Vector"], Group_Output.inputs["Hot-UV1"])
        nt.links.new(Value_004.outputs["Value"], Combine_XYZ.inputs["Y"])
        nt.links.new(Value_003.outputs["Value"], Combine_XYZ_001.inputs["Y"])
        nt.links.new(Value_002.outputs["Value"], Combine_XYZ_002.inputs["Y"])
        nt.links.new(Value_001.outputs["Value"], Combine_XYZ_003.inputs["Y"])
        nt.links.new(Value.outputs["Value"], Combine_XYZ_004.inputs["Y"])
        nt.links.new(Value_009.outputs["Value"], Combine_XYZ_005.inputs["Y"])
        nt.links.new(Combine_XYZ_005.outputs["Vector"], Mapping_009.inputs["Location"])
        nt.links.new(Value_008.outputs["Value"], Combine_XYZ_006.inputs["Y"])
        nt.links.new(Combine_XYZ_006.outputs["Vector"], Mapping_008.inputs["Location"])
        nt.links.new(Value_007.outputs["Value"], Combine_XYZ_007.inputs["Y"])
        nt.links.new(Combine_XYZ_007.outputs["Vector"], Mapping_007.inputs["Location"])
        nt.links.new(Value_006.outputs["Value"], Combine_XYZ_008.inputs["Y"])
        nt.links.new(Combine_XYZ_008.outputs["Vector"], Mapping_006.inputs["Location"])
        nt.links.new(Value_005.outputs["Value"], Combine_XYZ_009.inputs["Y"])
        nt.links.new(Combine_XYZ_009.outputs["Vector"], Mapping_005.inputs["Location"])