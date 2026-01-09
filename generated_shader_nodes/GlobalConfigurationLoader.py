import bpy
from ..utils import ShaderNode


class ShaderNodeGlobalConfigurationLoader(ShaderNode):
    bl_label = "Global Configuration Loader"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Disable_Enviroment_socket = nt.interface.new_socket(
                name="Disable Enviroment",
                in_out="OUTPUT",
                socket_type="NodeSocketBool"
            )
        
        Disable_Enviroment_socket.default_value = False
            Value_Enhance_socket = nt.interface.new_socket(
                name="Value Enhance",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Value_Enhance_socket.default_value = 0.10000000149011612
        Value_Enhance_socket.min_value = 0.0
        Value_Enhance_socket.max_value = 1.0
        Value_Enhance_socket.subtype = "NONE"
            World_Color_socket = nt.interface.new_socket(
                name="World Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        World_Color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (320.8227233886719, -111.73416137695312)
        Attribute_004 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_004.location = (23.569393157958984, -151.2821044921875)
        Attribute_005 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_005.location = (-258.4073791503906, -292.8736572265625)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-59.643341064453125, 311.547119140625)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (-427.8304138183594, -276.7200927734375)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (-253.23985290527344, -253.39212036132812)
        Mix_003.data_type = "RGBA"
        Mix_003.blend_type = "ADD"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (1.0, 1.0, 1.0, 1.0)
        Attribute_006 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_006.location = (-430.35443115234375, -239.7515869140625)
        Mix_007 = nt.nodes.new("ShaderNodeMix")
        Mix_007.location = (24.552425384521484, -244.3995361328125)
        Mix_007.data_type = "RGBA"
        Mix_007.blend_type = "MIX"
        Mix_007.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs["A"].default_value = 0.0
        Mix_007.inputs["B"].default_value = 0.0
        Mix_007.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Attribute_008 = nt.nodes.new("ShaderNodeAttribute")
        Attribute_008.location = (-844.7965087890625, -123.70796203613281)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-608.106201171875, -168.08091735839844)
        Math.operation = "COMPARE"
        Math.inputs["Value"].default_value = 1.0
        Math.inputs["Value"].default_value = 0.0
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-608.324462890625, -129.7677459716797)
        Math_001.operation = "COMPARE"
        Math_001.inputs["Value"].default_value = 2.0
        Math_001.inputs["Value"].default_value = 0.0
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (-608.106201171875, -92.42906188964844)
        Math_002.operation = "COMPARE"
        Math_002.inputs["Value"].default_value = 3.0
        Math_002.inputs["Value"].default_value = 0.0
        Math_003 = nt.nodes.new("ShaderNodeMath")
        Math_003.location = (-268.3663024902344, -94.06651306152344)
        Math_003.operation = "SUBTRACT"
        Math_003.inputs["Value"].default_value = 1.0
        Math_003.inputs["Value"].default_value = 0.5
        # Create links
        nt.links.new(Mix_007.outputs["Result"], Group_Output.inputs["World Color"])
        nt.links.new(Attribute_004.outputs["Fac"], Group_Output.inputs["Value Enhance"])
        nt.links.new(Attribute_006.outputs["Fac"], Mix_003.inputs["Factor"])
        nt.links.new(Attribute_008.outputs["Fac"], Math.inputs["Value"])
        nt.links.new(Attribute_008.outputs["Fac"], Math_002.inputs["Value"])
        nt.links.new(Attribute_008.outputs["Fac"], Math_001.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Math_003.inputs["Value"])
        nt.links.new(Math_003.outputs["Value"], Group_Output.inputs["Disable Enviroment"])
        nt.links.new(Math_002.outputs["Value"], Mix_007.inputs["Factor"])
        nt.links.new(Mix_003.outputs["Result"], Mix_007.inputs["A"])
        nt.links.new(Attribute_005.outputs["Color"], Mix_007.inputs["B"])
        nt.links.new(Group.outputs["Stylized"], Mix_003.inputs["A"])