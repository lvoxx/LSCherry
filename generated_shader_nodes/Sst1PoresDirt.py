import bpy
from ..utils import ShaderNode


class ShaderNodeSst1PoresDirt(ShaderNode):
    bl_label = "SST1: Pores Dirt"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (0.0, 0.0, 0.0, 0.0)

        # Input sockets
            Builder_socket = nt.interface.new_socket(
                name="Builder",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Builder_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Pores_(require)_socket = nt.interface.new_socket(
                name="Pores (require)",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Pores_(require)_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Dirt_Color_socket = nt.interface.new_socket(
                name="Dirt Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Dirt_Color_socket.default_value = (0.05000000074505806, 0.01831624284386635, 0.0050119939260184765, 1.0)
            Dirt_Strength_socket = nt.interface.new_socket(
                name="Dirt Strength",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Dirt_Strength_socket.default_value = 0.25
        Dirt_Strength_socket.min_value = 0.0
        Dirt_Strength_socket.max_value = 1.0
        Dirt_Strength_socket.subtype = "NONE"

        # Create nodes
        ColorRamp = nt.nodes.new("ShaderNodeValToRGB")
        ColorRamp.location = (-363.3407287597656, 270.3984680175781)
        ColorRamp.color_ramp.color_mode = "RGB"
        Invert = nt.nodes.new("ShaderNodeInvert")
        Invert.location = (-43.308040618896484, 182.9916229248047)
        Invert.inputs["Fac"].default_value = 1.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (396.7427673339844, 56.03672409057617)
        Mix.data_type = "RGBA"
        Mix.blend_type = "MULTIPLY"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (189.79107666015625, 204.44126892089844)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-607.7374267578125, 91.39417266845703)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (586.7427368164062, 163.21763610839844)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (-23.094100952148438, 401.18756103515625)
        # Create links
        nt.links.new(Group_Input.outputs["Pores (require)"], ColorRamp.inputs["Fac"])
        nt.links.new(Group_Input.outputs["Builder"], Mix.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Group_Output.inputs["Builder"])
        nt.links.new(Group_Input.outputs["Dirt Strength"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(ColorRamp.outputs["Color"], Invert.inputs["Color"])
        nt.links.new(Invert.outputs["Color"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Dirt Color"], Mix.inputs["B"])