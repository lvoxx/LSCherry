import bpy
from ..utils import ShaderNode


class ShaderNodeAddHightlightFromSpheremap(ShaderNode):
    bl_label = "Add HightLight From SphereMap"
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
            Result_socket = nt.interface.new_socket(
                name="Result",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Result_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

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
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            SphereMap_socket = nt.interface.new_socket(
                name="SphereMap",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        SphereMap_socket.default_value = 0.0
        SphereMap_socket.min_value = -3.4028234663852886e+38
        SphereMap_socket.max_value = 3.4028234663852886e+38
        SphereMap_socket.subtype = "NONE"
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (502.9930114746094, 148.2067108154297)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (0.0, 0.0)
        Mix.data_type = "RGBA"
        Mix.blend_type = "ADD"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-527.9237670898438, -131.54598999023438)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (200.5462646484375, 201.74594116210938)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-306.9708251953125, 136.01170349121094)
        # Create links
        nt.links.new(Group_Input.outputs["SphereMap"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Combined"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Group_Input.outputs["Fac"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Combined"], Mix_001.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Result"])