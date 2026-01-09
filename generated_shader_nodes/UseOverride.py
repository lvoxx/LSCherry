import bpy
from ..utils import ShaderNode


class ShaderNodeUseOverride(ShaderNode):
    bl_label = "? Use Override"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Condition__socket = nt.interface.new_socket(
                name="Condition ",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Condition__socket.default_value = 0.0
        Condition__socket.min_value = 0.0
        Condition__socket.max_value = 1.0
        Condition__socket.subtype = "NONE"
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            Override_Color_socket = nt.interface.new_socket(
                name="Override Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Override_Color_socket.default_value = (0.0, 0.0, 0.0, 1.0)

        # Create nodes
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (292.4040222167969, 121.61607360839844)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (536.1361694335938, 124.32176208496094)
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (-167.44644165039062, 138.94482421875)
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (59.84764099121094, 165.4730224609375)
        Math_002.operation = "GREATER_THAN"
        Math_002.inputs["Value"].default_value = 0.0
        Math_002.inputs["Value"].default_value = 0.5
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-388.5632629394531, 33.71437454223633)
        Frame_008 = nt.nodes.new("NodeFrame")
        Frame_008.location = (32.24650573730469, 276.79217529296875)
        # Create links
        nt.links.new(Math_002.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Group_Input.outputs["Override Color"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Color"])
        nt.links.new(Group_Input.outputs["Condition "], Separate_Color.inputs["Color"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_002.inputs["Value"])