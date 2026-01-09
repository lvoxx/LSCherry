import bpy
from ..utils import ShaderNode


class ShaderNodeAddCoreSpecular(ShaderNode):
    bl_label = "Add Core Specular"
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
        
        Combined_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 1.0
        Factor_socket.min_value = 0.0
        Factor_socket.max_value = 1.0
        Factor_socket.subtype = "FACTOR"
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.10000000149011612
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1069.84814453125, 387.96429443359375)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (90.36099243164062, 51.715213775634766)
        Group_003 = nt.nodes.new("ShaderNodeGroup")
        Group_003.location = (493.1129455566406, 75.56783294677734)
        Mix_004 = nt.nodes.new("ShaderNodeMix")
        Mix_004.location = (695.7699584960938, 207.0552978515625)
        Mix_004.data_type = "RGBA"
        Mix_004.blend_type = "ADD"
        Mix_004.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs["A"].default_value = 0.0
        Mix_004.inputs["B"].default_value = 0.0
        Mix_004.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (57.238372802734375, 278.1915588378906)
        Mix_005 = nt.nodes.new("ShaderNodeMix")
        Mix_005.location = (870.9095458984375, 404.9409484863281)
        Mix_005.data_type = "RGBA"
        Mix_005.blend_type = "MIX"
        Mix_005.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs["A"].default_value = 0.0
        Mix_005.inputs["B"].default_value = 0.0
        Mix_005.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-662.2670288085938, 152.6162567138672)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (289.0065002441406, -16.468399047851562)
        # Create links
        nt.links.new(Group_Input.outputs["Roughness"], Group_003.inputs["Roughness"])
        nt.links.new(Group_Input_002.outputs["Combined"], Mix_004.inputs["A"])
        nt.links.new(Group_Input_002.outputs["Color"], Mix_004.inputs["B"])
        nt.links.new(Mix_005.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_002.outputs["Combined"], Mix_005.inputs["A"])
        nt.links.new(Mix_004.outputs["Result"], Mix_005.inputs["B"])
        nt.links.new(Group_Input_002.outputs["Factor"], Mix_005.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Normal"], Group.inputs["Normal"])
        nt.links.new(Group.outputs["Normal"], Group_003.inputs["Normal"])
        nt.links.new(Group_003.outputs["Specular"], Mix_004.inputs["Factor"])