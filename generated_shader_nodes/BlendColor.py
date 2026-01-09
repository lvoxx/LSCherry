import bpy
from ..utils import ShaderNode


class ShaderNodeBlendColor(ShaderNode):
    bl_label = "Blend Color"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Blend_Color_socket = nt.interface.new_socket(
                name="Blend Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Blend_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Input sockets
            Mix_socket = nt.interface.new_socket(
                name="Mix",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_socket.default_value = 1.0
        Mix_socket.min_value = 0.0
        Mix_socket.max_value = 1.0
        Mix_socket.subtype = "FACTOR"
            Base_Color_socket = nt.interface.new_socket(
                name="Base Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Base_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Outer_Color_socket = nt.interface.new_socket(
                name="Outer Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Outer_Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (770.763916015625, 317.99420166015625)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-550.531982421875, 257.1604919433594)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-307.2112121582031, 71.15016174316406)
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (314.899658203125, 57.46061706542969)
        Separate_Color_001 = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color_001.location = (-307.2112121582031, -98.38943481445312)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-104.336181640625, 158.2195587158203)
        Math.operation = "ADD"
        Math.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-104.336181640625, 2.8958587646484375)
        Math_001.operation = "ADD"
        Math_001.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-104.336181640625, -158.21954345703125)
        Math_002.operation = "ADD"
        Math_002.inputs["Value"].default_value = 0.5
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (96.61370849609375, 158.2195587158203)
        Math_003.operation = "DIVIDE"
        Math_003.inputs["Value"].default_value = 2.0
        Math_003.inputs["Value"].default_value = 0.5
        Math_004 = nt.nodes.new("ShaderNodeMath")
        Math_004.location = (96.61370849609375, 2.369232177734375)
        Math_004.operation = "DIVIDE"
        Math_004.inputs["Value"].default_value = 2.0
        Math_004.inputs["Value"].default_value = 0.5
        Math_005 = nt.nodes.new("ShaderNodeMath")
        Math_005.location = (96.61370849609375, -152.4280548095703)
        Math_005.operation = "DIVIDE"
        Math_005.inputs["Value"].default_value = 2.0
        Math_005.inputs["Value"].default_value = 0.5
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (521.6471557617188, 332.6307067871094)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (295.20477294921875, 299.82183837890625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (195.90890502929688, 472.49908447265625)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-13.995742797851562, 409.4175109863281)
        # Create links
        nt.links.new(Math_002.outputs["Value"], Math_005.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Math_004.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Math_003.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_002.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color_001.outputs["Green"], Math_001.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Green"], Math_001.inputs["Value"])
        nt.links.new(Group_Input.outputs["Base Color"], Separate_Color.inputs["Color"])
        nt.links.new(Group_Input.outputs["Outer Color"], Separate_Color_001.inputs["Color"])
        nt.links.new(Group_Input_001.outputs["Mix"], Mix.inputs["Factor"])
        nt.links.new(Combine_Color.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Blend Color"])
        nt.links.new(Separate_Color_001.outputs["Blue"], Math_002.inputs["Value"])
        nt.links.new(Group_Input.outputs["Base Color"], Mix.inputs["A"])
        nt.links.new(Math_003.outputs["Value"], Combine_Color.inputs["Red"])
        nt.links.new(Math_004.outputs["Value"], Combine_Color.inputs["Green"])
        nt.links.new(Math_005.outputs["Value"], Combine_Color.inputs["Blue"])