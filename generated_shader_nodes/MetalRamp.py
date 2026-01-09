import bpy
from ..utils import ShaderNode


class ShaderNodeMetalRamp(ShaderNode):
    bl_label = "Metal Ramp"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "INPUT"
        nt.description = ""

        # Output sockets
            Custom_Ramp_socket = nt.interface.new_socket(
                name="Custom Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Custom_Ramp_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Mix_1_socket = nt.interface.new_socket(
                name="Mix 1",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_1_socket.default_value = 0.699999988079071
        Mix_1_socket.min_value = 0.0
        Mix_1_socket.max_value = 1.0
        Mix_1_socket.subtype = "NONE"
            Mix_2_socket = nt.interface.new_socket(
                name="Mix 2",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_2_socket.default_value = 0.8500000238418579
        Mix_2_socket.min_value = 0.0
        Mix_2_socket.max_value = 1.0
        Mix_2_socket.subtype = "NONE"
            Mix_3_socket = nt.interface.new_socket(
                name="Mix 3",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mix_3_socket.default_value = 0.949999988079071
        Mix_3_socket.min_value = 0.0
        Mix_3_socket.max_value = 1.0
        Mix_3_socket.subtype = "NONE"
            Lv_1_socket = nt.interface.new_socket(
                name="Lv 1",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lv_1_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Lv_2_socket = nt.interface.new_socket(
                name="Lv 2",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lv_2_socket.default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
            Lv_3_socket = nt.interface.new_socket(
                name="Lv 3",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lv_3_socket.default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
            Lv_4_socket = nt.interface.new_socket(
                name="Lv 4",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lv_4_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1109.6806640625, 308.41461181640625)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-838.0046997070312, -75.87763977050781)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (-39.41969299316406, 157.4116973876953)
        Fresnel_002 = nt.nodes.new("ShaderNodeFresnel")
        Fresnel_002.location = (-461.76947021484375, 245.672607421875)
        Invert_002 = nt.nodes.new("ShaderNodeInvert")
        Invert_002.location = (-193.48995971679688, 245.672607421875)
        Invert_002.inputs["Fac"].default_value = 1.0
        Fresnel = nt.nodes.new("ShaderNodeFresnel")
        Fresnel.location = (-461.76947021484375, 114.10456085205078)
        Fresnel_001 = nt.nodes.new("ShaderNodeFresnel")
        Fresnel_001.location = (-461.76947021484375, -23.183719635009766)
        Invert_001 = nt.nodes.new("ShaderNodeInvert")
        Invert_001.location = (-193.48995971679688, -23.183719635009766)
        Invert_001.inputs["Fac"].default_value = 1.0
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-164.82608032226562, -428.1614990234375)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (-220.14512634277344, -452.1034851074219)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-220.14512634277344, -202.2088623046875)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-164.82608032226562, -178.26687622070312)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (430.79327392578125, -480.0089416503906)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (100.58926391601562, -244.45497131347656)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_007 = nt.nodes.new("NodeReroute")
        Reroute_007.location = (430.79327392578125, -145.89508056640625)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (306.046875, -123.35232543945312)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (306.046875, -278.5502624511719)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-262.6143798828125, -227.64724731445312)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-262.6143798828125, -480.0089416503906)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (-326.5131530761719, -252.51780700683594)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (-326.5131530761719, -510.520751953125)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (837.5003662109375, 294.5899353027344)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (791.1217651367188, -510.520751953125)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (475.93182373046875, 63.14665603637695)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (694.1414794921875, 30.568992614746094)
        Reroute_016 = nt.nodes.new("NodeReroute")
        Reroute_016.location = (753.3070678710938, 211.0162353515625)
        Reroute_017 = nt.nodes.new("NodeReroute")
        Reroute_017.location = (753.3070678710938, 130.48287963867188)
        Reroute_015 = nt.nodes.new("NodeReroute")
        Reroute_015.location = (694.1414794921875, 106.79657745361328)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (791.1217651367188, 86.37303161621094)
        Invert = nt.nodes.new("ShaderNodeInvert")
        Invert.location = (-193.48995971679688, 114.10456085205078)
        Invert.inputs["Fac"].default_value = 1.0
        Reroute_018 = nt.nodes.new("NodeReroute")
        Reroute_018.location = (395.89544677734375, 79.26713562011719)
        Reroute_019 = nt.nodes.new("NodeReroute")
        Reroute_019.location = (395.89544677734375, -99.5643081665039)
        Reroute_020 = nt.nodes.new("NodeReroute")
        Reroute_020.location = (31.915973663330078, -57.867332458496094)
        Reroute_021 = nt.nodes.new("NodeReroute")
        Reroute_021.location = (31.915973663330078, -408.4244384765625)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (301.65924072265625, 376.25958251953125)
        Frame_005 = nt.nodes.new("NodeFrame")
        Frame_005.location = (307.8115234375, 474.3560485839844)
        # Create links
        nt.links.new(Fresnel.outputs["Fac"], Invert.inputs["Color"])
        nt.links.new(Fresnel_001.outputs["Fac"], Invert_001.inputs["Color"])
        nt.links.new(Fresnel_002.outputs["Fac"], Invert_002.inputs["Color"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Mix_001.inputs["A"])
        nt.links.new(Reroute_002.outputs["Output"], Reroute_003.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Mix_001.inputs["B"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_006.outputs["Output"], Reroute_007.inputs["Input"])
        nt.links.new(Reroute_007.outputs["Output"], Mix.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Mix.inputs["A"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_012.outputs["Output"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Mix_002.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Reroute_014.inputs["Input"])
        nt.links.new(Reroute_014.outputs["Output"], Reroute_015.inputs["Input"])
        nt.links.new(Reroute_015.outputs["Output"], Mix_002.inputs["A"])
        nt.links.new(Invert_002.outputs["Color"], Reroute_016.inputs["Input"])
        nt.links.new(Reroute_016.outputs["Output"], Reroute_017.inputs["Input"])
        nt.links.new(Reroute_017.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Invert.outputs["Color"], Reroute_018.inputs["Input"])
        nt.links.new(Reroute_018.outputs["Output"], Reroute_019.inputs["Input"])
        nt.links.new(Reroute_019.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Invert_001.outputs["Color"], Reroute_020.inputs["Input"])
        nt.links.new(Reroute_020.outputs["Output"], Reroute_021.inputs["Input"])
        nt.links.new(Reroute_021.outputs["Output"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Mix 1"], Fresnel_002.inputs["IOR"])
        nt.links.new(Group_Input.outputs["Mix 2"], Fresnel.inputs["IOR"])
        nt.links.new(Group_Input.outputs["Mix 3"], Fresnel_001.inputs["IOR"])
        nt.links.new(Group_Input.outputs["Lv 1"], Reroute.inputs["Input"])
        nt.links.new(Group_Input.outputs["Lv 2"], Reroute_002.inputs["Input"])
        nt.links.new(Group_Input.outputs["Lv 3"], Reroute_004.inputs["Input"])
        nt.links.new(Group_Input.outputs["Lv 4"], Reroute_010.inputs["Input"])
        nt.links.new(Mix_002.outputs["Result"], Group_Output.inputs["Custom Ramp"])
        nt.links.new(Group_Input.outputs["Normal"], Fresnel_002.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Fresnel.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Fresnel_001.inputs["Normal"])