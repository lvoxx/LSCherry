import bpy
from ..utils import ShaderNode


class ShaderNodeAddDotSpecular(ShaderNode):
    bl_label = "Add Dot Specular"
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
        Group_Input.location = (-201.00294494628906, 25.18505859375)
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
        Group.location = (15.255111694335938, -33.571533203125)
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (207.5911102294922, 95.90776062011719)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (15.255111694335938, 89.44328308105469)
        Map_Range_001 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_001.location = (394.48388671875, 119.24790954589844)
        Map_Range_001.data_type = "FLOAT"
        Map_Range_001.interpolation_type = "LINEAR"
        Map_Range_001.inputs["From Max"].default_value = 1.0
        Map_Range_001.inputs["To Min"].default_value = 0.0
        Map_Range_001.inputs["To Max"].default_value = 1.0
        Map_Range_001.inputs["Steps"].default_value = 4.0
        Map_Range_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (207.233642578125, -30.12530517578125)
        Math.operation = "SUBTRACT"
        Math.inputs["Value"].default_value = 1.0
        Math.inputs["Value"].default_value = 0.5
        # Create links
        nt.links.new(Group_Input_002.outputs["Combined"], Mix_004.inputs["A"])
        nt.links.new(Group_Input_002.outputs["Color"], Mix_004.inputs["B"])
        nt.links.new(Mix_005.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_002.outputs["Combined"], Mix_005.inputs["A"])
        nt.links.new(Mix_004.outputs["Result"], Mix_005.inputs["B"])
        nt.links.new(Group_Input_002.outputs["Factor"], Mix_005.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Normal"], Group.inputs["Normal"])
        nt.links.new(Attribute.outputs["Vector"], Group_004.inputs["Light Dir"])
        nt.links.new(Math.outputs["Value"], Map_Range_001.inputs["From Min"])
        nt.links.new(Group_004.outputs["Specular"], Map_Range_001.inputs["Value"])
        nt.links.new(Group.outputs["Normal"], Group_004.inputs["Normal"])
        nt.links.new(Map_Range_001.outputs["Result"], Mix_004.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Roughness"], Math.inputs["Value"])