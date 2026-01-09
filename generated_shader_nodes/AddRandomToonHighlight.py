import bpy
from ..utils import ShaderNode


class ShaderNodeAddRandomToonHighlight(ShaderNode):
    bl_label = "Add Random Toon Highlight"
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
        
        Fac_socket.default_value = 1.0
        Fac_socket.min_value = 0.0
        Fac_socket.max_value = 1.0
        Fac_socket.subtype = "FACTOR"
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Shading_socket = nt.interface.new_socket(
                name="Shading",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Shading_socket.default_value = 1.0
        Shading_socket.min_value = 0.0
        Shading_socket.max_value = 1.0
        Shading_socket.subtype = "FACTOR"
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Pattern_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Size_socket = nt.interface.new_socket(
                name="Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Size_socket.default_value = 0.7000000476837158
        Size_socket.min_value = 0.0
        Size_socket.max_value = 1.0
        Size_socket.subtype = "NONE"
            Seed_socket = nt.interface.new_socket(
                name="Seed",
                in_out="INPUT",
                socket_type="NodeSocketInt"
            )
        
        Seed_socket.default_value = 0
        Seed_socket.min_value = 0
        Seed_socket.max_value = 100
        Seed_socket.subtype = "NONE"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (733.1934814453125, 45.67413330078125)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-1289.4866943359375, 20.331787109375)
        Layer_Weight = nt.nodes.new("ShaderNodeLayerWeight")
        Layer_Weight.location = (-971.7139892578125, 290.26519775390625)
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (-750.8175048828125, 282.51739501953125)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Color_Ramp = nt.nodes.new("ShaderNodeValToRGB")
        Color_Ramp.location = (-514.8946533203125, 351.01373291015625)
        Color_Ramp.color_ramp.color_mode = "RGB"
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-192.53042602539062, 247.9304962158203)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 0.5
        Group_004 = nt.nodes.new("ShaderNodeGroup")
        Group_004.location = (-165.87347412109375, -273.5133972167969)
        Hue/Saturation/Value = nt.nodes.new("ShaderNodeHueSaturation")
        Hue/Saturation/Value.location = (68.14691162109375, -99.08222961425781)
        Hue/Saturation/Value.inputs["Saturation"].default_value = 1.0
        Hue/Saturation/Value.inputs["Value"].default_value = 1.0
        Hue/Saturation/Value.inputs["Fac"].default_value = 1.0
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (-753.8392333984375, -253.73004150390625)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = 0.0
        Map_Range.inputs["From Max"].default_value = 49.0
        Map_Range.inputs["To Min"].default_value = 0.5
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 0.5
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (-745.32568359375, -91.35757446289062)
        Math_001.operation = "GREATER_THAN"
        Math_001.inputs["Value"].default_value = 50.0
        Math_001.inputs["Value"].default_value = 0.5
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (-429.0243225097656, -115.80615234375)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Map_Range_001 = nt.nodes.new("ShaderNodeMapRange")
        Map_Range_001.location = (-753.8392333984375, -530.9930419921875)
        Map_Range_001.data_type = "FLOAT"
        Map_Range_001.interpolation_type = "LINEAR"
        Map_Range_001.inputs["From Min"].default_value = 50.0
        Map_Range_001.inputs["From Max"].default_value = 100.0
        Map_Range_001.inputs["To Min"].default_value = 0.0
        Map_Range_001.inputs["To Max"].default_value = 0.5
        Map_Range_001.inputs["Steps"].default_value = 1.0
        Map_Range_001.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (547.5572509765625, 319.479248046875)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (207.85205078125, 324.0546569824219)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (319.4386291503906, 105.1480712890625)
        Group.inputs["Fac"].default_value = 1.0
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (-287.7982177734375, 528.4593505859375)
        # Create links
        nt.links.new(Layer_Weight.outputs["Facing"], Invert_Color.inputs["Color"])
        nt.links.new(Invert_Color.outputs["Color"], Color_Ramp.inputs["Fac"])
        nt.links.new(Color_Ramp.outputs["Color"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Shading"], Math.inputs["Value"])
        nt.links.new(Group_004.outputs["Color"], Hue/Saturation/Value.inputs["Color"])
        nt.links.new(Group_Input.outputs["Seed"], Map_Range.inputs["Value"])
        nt.links.new(Group_Input.outputs["Seed"], Math_001.inputs["Value"])
        nt.links.new(Math_001.outputs["Value"], Mix.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Seed"], Map_Range_001.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Mix.inputs["A"])
        nt.links.new(Map_Range_001.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Hue/Saturation/Value.inputs["Hue"])
        nt.links.new(Group_Input.outputs["Size"], Layer_Weight.inputs["Blend"])
        nt.links.new(Group_Input.outputs["Combined"], Mix_001.inputs["A"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_001.outputs["Fac"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Combined"], Group.inputs["Combined"])
        nt.links.new(Math.outputs["Value"], Group.inputs["Shading"])
        nt.links.new(Group_Input.outputs["Pattern"], Group.inputs["Color"])
        nt.links.new(Hue/Saturation/Value.outputs["Color"], Group.inputs["Pattern"])
        nt.links.new(Group.outputs["Combined"], Mix_001.inputs["B"])
        nt.links.new(Group_Input.outputs["Normal"], Layer_Weight.inputs["Normal"])