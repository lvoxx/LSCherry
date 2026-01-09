import bpy
from ..utils import ShaderNode


class ShaderNodeSimplePantyhoseType1(ShaderNode):
    bl_label = "Simple Pantyhose Type 1"
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
            Pattern_socket = nt.interface.new_socket(
                name="Pattern",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Pattern_socket.default_value = 0.0
        Pattern_socket.min_value = -3.4028234663852886e+38
        Pattern_socket.max_value = 3.4028234663852886e+38
        Pattern_socket.subtype = "NONE"

        # Input sockets
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (1.0, 1.0, 1.0, 1.0)
            Color_socket = nt.interface.new_socket(
                name="Color",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Color_socket.default_value = (0.5, 0.5, 0.5, 1.0)
            Factor_socket = nt.interface.new_socket(
                name="Factor",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Factor_socket.default_value = 1.0
        Factor_socket.min_value = 0.0
        Factor_socket.max_value = 1.0
        Factor_socket.subtype = "FACTOR"
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 50.0
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 1000.0
        Scale_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1597.955322265625, 370.5539245605469)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-571.8013305664062, 2.3831138610839844)
        Brick_Texture = nt.nodes.new("ShaderNodeTexBrick")
        Brick_Texture.location = (0.9044647216796875, 217.58111572265625)
        Brick_Texture.inputs["Color1"].default_value = (1.0, 1.0, 1.0, 1.0)
        Brick_Texture.inputs["Color2"].default_value = (1.0, 1.0, 1.0, 1.0)
        Brick_Texture.inputs["Mortar"].default_value = (0.0, 0.0, 0.0, 1.0)
        Brick_Texture.inputs["Mortar Size"].default_value = 0.10000000149011612
        Brick_Texture.inputs["Mortar Smooth"].default_value = 1.0
        Brick_Texture.inputs["Bias"].default_value = 0.0
        Brick_Texture.inputs["Brick Width"].default_value = 0.30000001192092896
        Brick_Texture.inputs["Row Height"].default_value = 0.10000000149011612
        Invert_Color = nt.nodes.new("ShaderNodeInvert")
        Invert_Color.location = (230.46725463867188, 70.99293518066406)
        Invert_Color.inputs["Fac"].default_value = 1.0
        Invert_Color_001 = nt.nodes.new("ShaderNodeInvert")
        Invert_Color_001.location = (230.46725463867188, -119.0087890625)
        Invert_Color_001.inputs["Fac"].default_value = 0.0
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (-215.34666442871094, 145.64297485351562)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
        Geometry = nt.nodes.new("ShaderNodeNewGeometry")
        Geometry.location = (-234.94956970214844, -182.9010467529297)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-239.86407470703125, -262.2213134765625)
        Math.operation = "MULTIPLY"
        Math.inputs["Value"].default_value = 3.0
        Math.inputs["Value"].default_value = 0.5
        Voronoi_Texture = nt.nodes.new("ShaderNodeTexVoronoi")
        Voronoi_Texture.location = (0.8156051635742188, -169.9659881591797)
        Voronoi_Texture.inputs["W"].default_value = 0.0
        Voronoi_Texture.inputs["Detail"].default_value = 0.0
        Voronoi_Texture.inputs["Roughness"].default_value = 0.5
        Voronoi_Texture.inputs["Lacunarity"].default_value = 2.0
        Voronoi_Texture.inputs["Smoothness"].default_value = 1.0
        Voronoi_Texture.inputs["Exponent"].default_value = 0.5
        Voronoi_Texture.inputs["Randomness"].default_value = 0.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (450.9528503417969, 96.89138793945312)
        Mix.data_type = "RGBA"
        Mix.blend_type = "SUBTRACT"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (1267.336669921875, 581.9349975585938)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MULTIPLY"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (1081.6785888671875, 391.4034729003906)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Color_Ramp = nt.nodes.new("ShaderNodeValToRGB")
        Color_Ramp.location = (656.121826171875, 154.5895538330078)
        Color_Ramp.color_ramp.color_mode = "RGB"
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (668.19775390625, 564.76708984375)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (480.57763671875, 708.815673828125)
        # Create links
        nt.links.new(Brick_Texture.outputs["Fac"], Invert_Color.inputs["Color"])
        nt.links.new(Invert_Color_001.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Invert_Color.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Geometry.outputs["Incoming"], Voronoi_Texture.inputs["Vector"])
        nt.links.new(Voronoi_Texture.outputs["Distance"], Invert_Color_001.inputs["Color"])
        nt.links.new(Mapping.outputs["Vector"], Brick_Texture.inputs["Vector"])
        nt.links.new(Mix_002.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Math.outputs["Value"], Voronoi_Texture.inputs["Scale"])
        nt.links.new(Mix.outputs["Result"], Color_Ramp.inputs["Fac"])
        nt.links.new(Color_Ramp.outputs["Color"], Mix_002.inputs["A"])
        nt.links.new(Group_Input.outputs["UV"], Mapping.inputs["Vector"])
        nt.links.new(Group_Input.outputs["Scale"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Scale"], Brick_Texture.inputs["Scale"])
        nt.links.new(Color_Ramp.outputs["Color"], Group_Output.inputs["Pattern"])
        nt.links.new(Mix_001.outputs["Result"], Group_Output.inputs["Combined"])
        nt.links.new(Group_Input_001.outputs["Color"], Mix_002.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Combined"], Mix_001.inputs["A"])
        nt.links.new(Group_Input_001.outputs["Factor"], Mix_001.inputs["Factor"])