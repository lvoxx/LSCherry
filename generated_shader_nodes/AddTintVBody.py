import bpy
from ..utils import ShaderNode


class ShaderNodeAddTintVBody(ShaderNode):
    bl_label = "Add Tint V-Body"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Fac_socket = nt.interface.new_socket(
                name="Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fac_socket.default_value = 0.0
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Combine_socket = nt.interface.new_socket(
                name="Combine",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combine_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = 0.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "NONE"
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Pattern_socket.default_value = 1.0
        Pattern_socket.min_value = 0.0
        Pattern_socket.max_value = 1.0
        Pattern_socket.subtype = "NONE"
            Low_Color_socket = nt.interface.new_socket(
                name="Low Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Low_Color_socket.default_value = (1.0, 0.7686304450035095, 0.7463362216949463, 1.0)
            Mid_Color_socket = nt.interface.new_socket(
                name="Mid Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Mid_Color_socket.default_value = (0.6780416965484619, 0.2375265657901764, 0.18046948313713074, 1.0)
            High_Color_socket = nt.interface.new_socket(
                name="High Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        High_Color_socket.default_value = (0.7339583039283752, 0.19292114675045013, 0.14441092312335968, 1.0)
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (464.0, 41.781463623046875)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "MULTIPLY"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1759.9248046875, 845.6693115234375)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (647.0053100585938, -154.46824645996094)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MULTIPLY"
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (850.166259765625, 110.67061614990234)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "SCREEN"
        Mix_001.inputs["Factor"].default_value = 1.0
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1038.4705810546875, 349.002685546875)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "SCREEN"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (604.56298828125, 262.93072509765625)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "MULTIPLY"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Layer_Weight = nt.nodes.new("ShaderNodeLayerWeight")
        Layer_Weight.location = (-384.64544677734375, 272.345703125)
        Layer_Weight.inputs["Blend"].default_value = 0.8999999761581421
        Invert = nt.nodes.new("ShaderNodeInvert")
        Invert.location = (-169.94845581054688, 285.9302978515625)
        Invert.inputs["Fac"].default_value = 1.0
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (18.744552612304688, 394.985595703125)
        ColorRamp.color_ramp.color_mode = "RGB"
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (472.081298828125, -424.84942626953125)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-66.61239624023438, -594.340087890625)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.9000000953674316
        Math.inputs["Value"].default_value = 0.5
        Invert_002 = nt.nodes.new("ShaderNodeInvert")
        Invert_002.location = (-443.4919738769531, -586.1895141601562)
        Invert_002.inputs["Fac"].default_value = 1.0
        ColorRamp_001 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_001.location = (-129.74241638183594, 65.16404724121094)
        ColorRamp_001.color_ramp.color_mode = "RGB"
        Layer_Weight_001 = nt.nodes.new("ShaderNodeLayerWeight")
        Layer_Weight_001.location = (-498.4541015625, -23.90289306640625)
        Layer_Weight_001.inputs["Blend"].default_value = 0.7000000476837158
        Invert_001 = nt.nodes.new("ShaderNodeInvert")
        Invert_001.location = (-321.8406982421875, -33.68381118774414)
        Invert_001.inputs["Fac"].default_value = 1.0
        Layer_Weight_002 = nt.nodes.new("ShaderNodeLayerWeight")
        Layer_Weight_002.location = (-644.3169555664062, -593.8218994140625)
        Layer_Weight_002.inputs["Blend"].default_value = 0.40000009536743164
        ColorRamp_002 = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp_002.location = (-169.03936767578125, -373.980224609375)
        ColorRamp_002.color_ramp.color_mode = "RGB"
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (296.4986267089844, 154.9476318359375)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (240.95913696289062, -511.6242980957031)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (177.59629821777344, -93.43777465820312)
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (369.0453796386719, -294.8052062988281)
        Mix_006 = nt.nodes.new("ShaderNodeMix")
        Mix_006.location = (1552.11083984375, 669.861328125)
        Mix_006.data_type = "RGBA"
        Mix_006.blend_type = "SOFT_LIGHT"
        Mix_006.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs["B"].default_value = 0.0
        Mix_006.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (1027.1785888671875, 501.5791320800781)
        Mix_007 = nt.nodes.new("ShaderNodeMix")
        Mix_007.location = (1295.1007080078125, 684.57763671875)
        Mix_007.data_type = "FLOAT"
        Mix_007.blend_type = "MIX"
        Mix_007.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs["A"].default_value = 0.0
        Mix_007.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_007.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (185.06317138671875, 529.1535034179688)
        Group_Input_005 = nt.nodes.new("NodeGroupInput")
        Group_Input_005.location = (-984.40234375, -318.9919738769531)
        # Create links
        nt.links.new(Layer_Weight_002.outputs["Facing"], Invert_002.inputs["Color"])
        nt.links.new(Layer_Weight_001.outputs["Facing"], Invert_001.inputs["Color"])
        nt.links.new(Layer_Weight.outputs["Facing"], Invert.inputs["Color"])
        nt.links.new(Invert_002.outputs["Color"], ColorRamp_002.inputs["Fac"])
        nt.links.new(Invert.outputs["Color"], ColorRamp.inputs["Fac"])
        nt.links.new(Invert_001.outputs["Color"], ColorRamp_001.inputs["Fac"])
        nt.links.new(Invert_002.outputs["Color"], Math.inputs["Value"])
        nt.links.new(ColorRamp_002.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["B"])
        nt.links.new(Mix_003.outputs["Result"], Mix_001.inputs["A"])
        nt.links.new(Mix_004.outputs["Result"], Mix_002.inputs["A"])
        nt.links.new(Mix_001.outputs["Result"], Mix_002.inputs["B"])
        nt.links.new(Mix_005.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(ColorRamp_001.outputs["Color"], Mix_003.inputs["A"])
        nt.links.new(ColorRamp.outputs["Color"], Mix_004.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_005.inputs["A"])
        nt.links.new(Group_Input.outputs["Low Color"], Mix_004.inputs["B"])
        nt.links.new(Mix_002.outputs["Result"], Mix_006.inputs["A"])
        nt.links.new(Mix_006.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_001.outputs["Combine"], Mix_006.inputs["A"])
        nt.links.new(Mix_002.outputs["Result"], Mix_006.inputs["B"])
        nt.links.new(Group_Input.outputs["Pattern"], Mix_004.inputs["Factor"])
        nt.links.new(Group_Input_002.outputs["Pattern"], Mix.inputs["Factor"])
        nt.links.new(Group_Input_003.outputs["Mid Color"], Mix_003.inputs["B"])
        nt.links.new(Group_Input_003.outputs["Pattern"], Mix_003.inputs["Factor"])
        nt.links.new(Group_Input_004.outputs["High Color"], Mix_005.inputs["B"])
        nt.links.new(Group_Input_004.outputs["Pattern"], Mix_005.inputs["Factor"])
        nt.links.new(Group_Input_001.outputs["Fac"], Mix_007.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Shading"], Mix_007.inputs["Factor"])
        nt.links.new(Mix_007.outputs["Result"], Mix_006.inputs["Factor"])
        nt.links.new(Group_Input_005.outputs["Normal"], Layer_Weight_001.inputs["Normal"])
        nt.links.new(Group_Input_005.outputs["Normal"], Layer_Weight_002.inputs["Normal"])
        nt.links.new(Group_Input_005.outputs["Normal"], Layer_Weight.inputs["Normal"])