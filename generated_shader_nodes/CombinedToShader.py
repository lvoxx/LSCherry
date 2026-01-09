import bpy
from ..utils import ShaderNode


class ShaderNodeCombinedToShader(ShaderNode):
    bl_label = "Combined To Shader"
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
        
            To_AgX_socket = nt.interface.new_socket(
                name="To AgX",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Combined_socket = nt.interface.new_socket(
                name="Combined",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Combined_socket.default_value = (0.0, 0.0, 0.0, 1.0)
            Alpha_socket = nt.interface.new_socket(
                name="Alpha",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Alpha_socket.default_value = 1.0
        Alpha_socket.min_value = 0.0
        Alpha_socket.max_value = 1.0
        Alpha_socket.subtype = "FACTOR"

        # Create nodes
        Light_Path = nt.nodes.new("ShaderNodeLightPath")
        Light_Path.location = (-80.0, -16.71942138671875)
        Diffuse_BSDF = nt.nodes.new("ShaderNodeBsdfDiffuse")
        Diffuse_BSDF.location = (-82.93646240234375, -78.18234252929688)
        Diffuse_BSDF.inputs["Roughness"].default_value = 0.0
        Diffuse_BSDF.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        Diffuse_BSDF.inputs["Weight"].default_value = 0.0
        Emission = nt.nodes.new("ShaderNodeEmission")
        Emission.location = (1006.1566772460938, -240.0)
        Emission.inputs["Strength"].default_value = 1.0
        Emission.inputs["Weight"].default_value = 0.0
        Mix_Shader = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader.location = (1206.15673828125, -107.67730712890625)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-291.4339599609375, -272.70123291015625)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (1674.5543212890625, -175.69888305664062)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-529.3432006835938, -247.52410888671875)
        Brightness/Contrast = nt.nodes.new("ShaderNodeBrightContrast")
        Brightness/Contrast.location = (-47.81293487548828, -411.03436279296875)
        Brightness/Contrast.inputs["Bright"].default_value = 0.0
        Brightness/Contrast.inputs["Contrast"].default_value = -0.15000000596046448
        Separate_Color = nt.nodes.new("ShaderNodeSeparateColor")
        Separate_Color.location = (128.25906372070312, -419.6368713378906)
        Combine_Color = nt.nodes.new("ShaderNodeCombineColor")
        Combine_Color.location = (638.796875, -406.7232666015625)
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (401.1755065917969, -339.4941711425781)
        Math.operation = "POWER"
        Math.inputs["Value"].default_value = 0.5
        Math_001 = nt.nodes.new("ShaderNodeMath")
        Math_001.location = (401.1755065917969, -396.31781005859375)
        Math_001.operation = "POWER"
        Math_001.inputs["Value"].default_value = 0.5
        Math_002 = nt.nodes.new("ShaderNodeMath")
        Math_002.location = (401.1755065917969, -455.41436767578125)
        Math_002.operation = "POWER"
        Math_002.inputs["Value"].default_value = 0.5
        Value = nt.nodes.new("ShaderNodeValue")
        Value.location = (-52.81246566772461, -539.0415649414062)
        Gamma_001 = nt.nodes.new("ShaderNodeGamma")
        Gamma_001.location = (-227.9216766357422, -359.40374755859375)
        Gamma_001.inputs["Gamma"].default_value = 1.149999976158142
        Emission_001 = nt.nodes.new("ShaderNodeEmission")
        Emission_001.location = (1006.1566772460938, -376.60821533203125)
        Emission_001.inputs["Strength"].default_value = 1.0
        Emission_001.inputs["Weight"].default_value = 0.0
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (646.897705078125, 130.6472930908203)
        Transparent_BSDF = nt.nodes.new("ShaderNodeBsdfTransparent")
        Transparent_BSDF.location = (1206.8447265625, -3.847503662109375)
        Transparent_BSDF.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs["Weight"].default_value = 0.0
        Mix_Shader_001 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_001.location = (1419.8065185546875, -107.67730712890625)
        Mix_Shader_002 = nt.nodes.new("ShaderNodeMixShader")
        Mix_Shader_002.location = (1419.8065185546875, -259.1390380859375)
        Group_Input_001 = nt.nodes.new("NodeGroupInput")
        Group_Input_001.location = (1204.007568359375, -240.00601196289062)
        # Create links
        nt.links.new(Light_Path.outputs["Is Camera Ray"], Mix_Shader.inputs["Fac"])
        nt.links.new(Diffuse_BSDF.outputs["BSDF"], Mix_Shader.inputs["Shader"])
        nt.links.new(Emission.outputs["Emission"], Mix_Shader.inputs["Shader"])
        nt.links.new(Mix_Shader_001.outputs["Shader"], Group_Output.inputs["Shader"])
        nt.links.new(Reroute.outputs["Output"], Diffuse_BSDF.inputs["Color"])
        nt.links.new(Gamma_001.outputs["Color"], Brightness/Contrast.inputs["Color"])
        nt.links.new(Brightness/Contrast.outputs["Color"], Separate_Color.inputs["Color"])
        nt.links.new(Math.outputs["Value"], Combine_Color.inputs["Red"])
        nt.links.new(Math_001.outputs["Value"], Combine_Color.inputs["Green"])
        nt.links.new(Math_002.outputs["Value"], Combine_Color.inputs["Blue"])
        nt.links.new(Separate_Color.outputs["Red"], Math.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Green"], Math_001.inputs["Value"])
        nt.links.new(Value.outputs["Value"], Math.inputs["Value"])
        nt.links.new(Value.outputs["Value"], Math_002.inputs["Value"])
        nt.links.new(Value.outputs["Value"], Math_001.inputs["Value"])
        nt.links.new(Separate_Color.outputs["Blue"], Math_002.inputs["Value"])
        nt.links.new(Reroute.outputs["Output"], Gamma_001.inputs["Color"])
        nt.links.new(Reroute.outputs["Output"], Emission.inputs["Color"])
        nt.links.new(Group_Input.outputs["Combined"], Reroute.inputs["Input"])
        nt.links.new(Combine_Color.outputs["Color"], Emission_001.inputs["Color"])
        nt.links.new(Mix_Shader_002.outputs["Shader"], Group_Output.inputs["To AgX"])
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Mix_Shader.outputs["Shader"], Mix_Shader_001.inputs["Shader"])
        nt.links.new(Transparent_BSDF.outputs["BSDF"], Mix_Shader_002.inputs["Shader"])
        nt.links.new(Emission_001.outputs["Emission"], Mix_Shader_002.inputs["Shader"])
        nt.links.new(Group_Input_001.outputs["Alpha"], Mix_Shader_001.inputs["Fac"])
        nt.links.new(Group_Input_001.outputs["Alpha"], Mix_Shader_002.inputs["Fac"])