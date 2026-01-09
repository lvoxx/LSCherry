import bpy
from ..utils import ShaderNode


class ShaderNodeBlendIt(ShaderNode):
    bl_label = "Blend It"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "COLOR"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Fac_socket = nt.interface.new_socket(
                name="Fac",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Fac_socket.default_value = 1.0
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Color_A_socket = nt.interface.new_socket(
                name="Color A",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_A_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Color_B_socket = nt.interface.new_socket(
                name="Color B",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_B_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (889.7679443359375, -262.6689758300781)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-199.58285522460938, -450.3699645996094)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (174.92910766601562, -510.36932373046875)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "COLOR"
        Mix_004.inputs["Factor"].default_value = 1.0
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (173.12796020507812, -548.8197021484375)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MULTIPLY"
        Mix_005.inputs["Factor"].default_value = 1.0
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_006 = nt.nodes.new("ShaderNodeMix")
        Mix_006.location = (356.3647766113281, -530.2689208984375)
        Mix_006.data_type = "RGBA"
        Mix_006.blend_type = "MIX"
        Mix_006.inputs["Factor"].default_value = 0.30000001192092896
        Mix_006.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs["A"].default_value = 0.0
        Mix_006.inputs["B"].default_value = 0.0
        Mix_006.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_007 = nt.nodes.new("ShaderNodeMix")
        Mix_007.location = (530.0919799804688, -571.5687255859375)
        Mix_007.data_type = "RGBA"
        Mix_007.blend_type = "MIX"
        Mix_007.inputs["Factor"].default_value = 0.699999988079071
        Mix_007.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs["A"].default_value = 0.0
        Mix_007.inputs["B"].default_value = 0.0
        Mix_007.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_008 = nt.nodes.new("ShaderNodeMix")
        Mix_008.location = (173.12796020507812, -594.1279296875)
        Mix_008.data_type = "RGBA"
        Mix_008.blend_type = "SOFT_LIGHT"
        Mix_008.inputs["Factor"].default_value = 1.0
        Mix_008.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_008.inputs["A"].default_value = 0.0
        Mix_008.inputs["B"].default_value = 0.0
        Mix_008.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_008.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (486.948486328125, -149.55459594726562)
        Mix_009 = nt.nodes.new("ShaderNodeMix")
        Mix_009.location = (-219.792724609375, 5.88232421875)
        Mix_009.data_type = "RGBA"
        Mix_009.blend_type = "SOFT_LIGHT"
        Mix_009.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_009.inputs["A"].default_value = 0.0
        Mix_009.inputs["B"].default_value = 0.0
        Mix_009.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_009.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_010 = nt.nodes.new("ShaderNodeMix")
        Mix_010.location = (710.0000610351562, -475.3290100097656)
        Mix_010.data_type = "RGBA"
        Mix_010.blend_type = "MIX"
        Mix_010.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_010.inputs["A"].default_value = 0.0
        Mix_010.inputs["B"].default_value = 0.0
        Mix_010.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_010.inputs["B"].default_value = (0.0, 0.0, 0.0)
        # Create links
        nt.links.new(Group_Input.outputs["Color A"], Mix_004.inputs["A"])
        nt.links.new(Group_Input.outputs["Color B"], Mix_004.inputs["B"])
        nt.links.new(Group_Input.outputs["Color A"], Mix_005.inputs["A"])
        nt.links.new(Group_Input.outputs["Color B"], Mix_005.inputs["B"])
        nt.links.new(Mix_004.outputs["Result"], Mix_006.inputs["A"])
        nt.links.new(Mix_005.outputs["Result"], Mix_006.inputs["B"])
        nt.links.new(Mix_006.outputs["Result"], Mix_007.inputs["A"])
        nt.links.new(Group_Input.outputs["Color A"], Mix_008.inputs["A"])
        nt.links.new(Group_Input.outputs["Color B"], Mix_008.inputs["B"])
        nt.links.new(Mix_008.outputs["Result"], Mix_007.inputs["B"])
        nt.links.new(Group_Input.outputs["Color B"], Mix_009.inputs["B"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_009.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Color A"], Mix_009.inputs["A"])
        nt.links.new(Mix_010.outputs["Result"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_010.inputs["Factor"])
        nt.links.new(Mix_007.outputs["Result"], Mix_010.inputs["B"])
        nt.links.new(Group_Input.outputs["Color A"], Mix_010.inputs["A"])