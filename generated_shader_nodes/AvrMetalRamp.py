import bpy
from ..utils import ShaderNode


class ShaderNodeAvrMetalRamp(ShaderNode):
    bl_label = "AVR: Metal Ramp"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "SHADER"
        nt.description = ""

        # Output sockets
            Shader_socket = nt.interface.new_socket(
                name="Shader",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        
            Ramp_socket = nt.interface.new_socket(
                name="Ramp",
                in_out="OUTPUT",
                socket_type="NodeSocketColor"
            )
        
        Ramp_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)

        # Input sockets
            Use_Dot_socket = nt.interface.new_socket(
                name="Use Dot",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Use_Dot_socket.default_value = False
            Roughness_socket = nt.interface.new_socket(
                name="Roughness",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Roughness_socket.default_value = 0.3919999897480011
        Roughness_socket.min_value = 0.0
        Roughness_socket.max_value = 1.0
        Roughness_socket.subtype = "FACTOR"
            Scale_socket = nt.interface.new_socket(
                name="Scale",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Scale_socket.default_value = 4.010000228881836
        Scale_socket.min_value = 0.0
        Scale_socket.max_value = 100.0
        Scale_socket.subtype = "NONE"
            Distortion_socket = nt.interface.new_socket(
                name="Distortion",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Distortion_socket.default_value = 1.0
        Distortion_socket.min_value = 0.0
        Distortion_socket.max_value = 100.0
        Distortion_socket.subtype = "NONE"
            Value_Enhance_socket = nt.interface.new_socket(
                name="Value Enhance",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Value_Enhance_socket.default_value = 0.10000000149011612
        Value_Enhance_socket.min_value = 0.0
        Value_Enhance_socket.max_value = 1.0
        Value_Enhance_socket.subtype = "FACTOR"
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="INPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1540.8656005859375, 215.88504028320312)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-142.33428955078125, -450.5919494628906)
        Texture_Coordinate = nt.nodes.new("ShaderNodeTexCoord")
        Texture_Coordinate.location = (-59.0645751953125, -107.30476379394531)
        Vector_Transform = nt.nodes.new("ShaderNodeVectorTransform")
        Vector_Transform.location = (-58.850982666015625, -139.39349365234375)
        Vector_Transform.vector_type = "NORMAL"
        Vector_Transform.convert_from = "OBJECT"
        Vector_Transform.convert_to = "CAMERA"
        Magic_Texture = nt.nodes.new("ShaderNodeTexMagic")
        Magic_Texture.location = (128.21871948242188, -97.2367935180664)
        Brightness/Contrast = nt.nodes.new("ShaderNodeBrightContrast")
        Brightness/Contrast.location = (315.77288818359375, -107.52403259277344)
        Brightness/Contrast.inputs["Bright"].default_value = 0.0
        Brightness/Contrast.inputs["Contrast"].default_value = 2.0
        RGB = nt.nodes.new("ShaderNodeRGB")
        RGB.location = (311.60113525390625, 87.25995635986328)
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (505.5378723144531, 27.774192810058594)
        Mix.data_type = "RGBA"
        Mix.blend_type = "LINEAR_LIGHT"
        Mix.inputs["Factor"].default_value = 1.0
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = 0.0
        Mix.inputs["B"].default_value = 0.0
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF = nt.nodes.new("ShaderNodeBsdfAnisotropic")
        Glossy_BSDF.location = (785.1636962890625, 134.77391052246094)
        Glossy_BSDF.inputs["Anisotropy"].default_value = 0.0
        Glossy_BSDF.inputs["Rotation"].default_value = 0.0
        Glossy_BSDF.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs["Weight"].default_value = 0.0
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (500.9324035644531, -219.11923217773438)
        Attribute = nt.nodes.new("ShaderNodeAttribute")
        Attribute.location = (313.784423828125, -243.6303253173828)
        Shader_to_RGB = nt.nodes.new("ShaderNodeShaderToRGB")
        Shader_to_RGB.location = (985.3834228515625, 114.62686157226562)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (1180.79248046875, 147.2022247314453)
        Mix_001.data_type = "RGBA"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = 0.0
        Mix_001.inputs["B"].default_value = 0.0
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (785.7068481445312, -96.95433044433594)
        Mix_002.data_type = "RGBA"
        Mix_002.blend_type = "MULTIPLY"
        Mix_002.inputs["Factor"].default_value = 1.0
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = 0.0
        Mix_002.inputs["B"].default_value = 0.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (985.3834228515625, 183.8094482421875)
        Group_Input_002 = nt.nodes.new("NodeGroupInput")
        Group_Input_002.location = (508.8370666503906, 115.42996978759766)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (67.48004150390625, -414.9092102050781)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.0
        Math.inputs["Value"].default_value = 0.5
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (312.6501159667969, -360.6098327636719)
        Mix_003.data_type = "VECTOR"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 0.0
        Mix_003.inputs["B"].default_value = 0.0
        Mix_003.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Normal_Map = nt.nodes.new("ShaderNodeNormalMap")
        Normal_Map.location = (65.7913818359375, -453.1343688964844)
        Normal_Map.inputs["Strength"].default_value = 1.0
        Normal_Map.inputs["Color"].default_value = (0.5, 0.5, 1.0, 1.0)
        Group_Input_003 = nt.nodes.new("NodeGroupInput")
        Group_Input_003.location = (-58.7919921875, -204.24618530273438)
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (1184.102294921875, -86.27543640136719)
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (1361.0, 209.443115234375)
        Math_001.operation = "ADD"
        Math_001.inputs["Value"].default_value = 0.5
        Group_Input_004 = nt.nodes.new("NodeGroupInput")
        Group_Input_004.location = (1179.515869140625, 209.0321807861328)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (644.0200805664062, 294.44549560546875)
        # Create links
        nt.links.new(Vector_Transform.outputs["Vector"], Magic_Texture.inputs["Vector"])
        nt.links.new(Texture_Coordinate.outputs["Normal"], Vector_Transform.inputs["Vector"])
        nt.links.new(RGB.outputs["Color"], Mix.inputs["A"])
        nt.links.new(Brightness/Contrast.outputs["Color"], Mix.inputs["B"])
        nt.links.new(Mix.outputs["Result"], Glossy_BSDF.inputs["Color"])
        nt.links.new(Attribute.outputs["Vector"], Group.inputs["Light Dir"])
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Shader_to_RGB.inputs["Shader"])
        nt.links.new(Shader_to_RGB.outputs["Color"], Mix_001.inputs["A"])
        nt.links.new(Math_001.outputs["Value"], Group_Output.inputs["Ramp"])
        nt.links.new(Mix_002.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Group.outputs["Specular"], Mix_002.inputs["A"])
        nt.links.new(Mix.outputs["Result"], Mix_002.inputs["B"])
        nt.links.new(Group_Input_001.outputs["Use Dot"], Mix_001.inputs["Factor"])
        nt.links.new(Group_Input_002.outputs["Normal"], Glossy_BSDF.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Normal"], Math.inputs["Value"])
        nt.links.new(Math.outputs["Value"], Mix_003.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Normal"], Mix_003.inputs["B"])
        nt.links.new(Normal_Map.outputs["Normal"], Mix_003.inputs["A"])
        nt.links.new(Mix_003.outputs["Result"], Group.inputs["Normal"])
        nt.links.new(Group_Input_003.outputs["Scale"], Magic_Texture.inputs["Scale"])
        nt.links.new(Group_Input_003.outputs["Distortion"], Magic_Texture.inputs["Distortion"])
        nt.links.new(Group_Input_002.outputs["Roughness"], Glossy_BSDF.inputs["Roughness"])
        nt.links.new(Group_Input_001.outputs["Use Dot"], Mix_Shader.inputs["Fac"])
        nt.links.new(Glossy_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_002.outputs["Result"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Magic_Texture.outputs["Fac"], Brightness/Contrast.inputs["Color"])
        nt.links.new(Mix_001.outputs["Result"], Math_001.inputs["Value"])
        nt.links.new(Group_Input_004.outputs["Value Enhance"], Math_001.inputs["Value"])