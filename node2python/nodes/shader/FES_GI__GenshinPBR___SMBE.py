import bpy
import sys
from pathlib import Path

# Import utils (handle both relative and absolute imports)
try:
    from ..utils import ShaderNode
except ImportError:
    # Fallback for direct execution
    import importlib.util
    utils_path = Path(__file__).parent.parent / 'utils.py'
    spec = importlib.util.spec_from_file_location('utils', utils_path)
    utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utils)
    ShaderNode = utils.ShaderNode


class ShaderNodeFES_GI__GenshinPBR___SMBE(ShaderNode):
    bl_idname = 'ShaderNodeFES_GI__GenshinPBR___SMBE'
    bl_label = "FES_GI: GenshinPBR - SMBE"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Base Alpha"].default_value = 1.0
        self.inputs["SMBE"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["SMBE Alpha"].default_value = 0.0
        self.inputs["Emission Strength"].default_value = 1.0
        self.inputs["Mix Diffuse with Emission"].default_value = 0.0
        self.inputs["Emission Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["0 = OpenGL, 1 = DirectX"].default_value = 1.0
        self.inputs["Normal Strength"].default_value = 1.0
        self.inputs["Height"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Height Strength"].default_value = 1.0
        self.inputs["Height Distance"].default_value = 0.25
        self.inputs["----------------"].default_value = 0.0
        self.inputs["Principled BSDF = 0, Specular BSDF = 1"].default_value = 0.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'FES_GI: GenshinPBR - SMBE'

        # Create output sockets
        nt.interface.new_socket('BSDF', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Base', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Base Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('SMBE', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('SMBE Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Mix Diffuse with Emission', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Emission Tint', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('0 = OpenGL, 1 = DirectX', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Normal Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Height', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Height Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Height Distance', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.25
        input_socket = nt.interface.new_socket('----------------', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Principled BSDF = 0, Specular BSDF = 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0

        # Build node tree
        self.rebuildNodetree(None)

    def rebuildNodetree(self, context):
        if context is not None:
            if self.node_tree.users > 1:
                self.duplicate()

        nt = self.node_tree

        # Clear existing nodes
        for node in list(nt.nodes):
            nt.nodes.remove(node)

        # Create group input/output
        GroupInput = nt.nodes.new('NodeGroupInput')
        GroupInput.location = (-400, 0)
        GroupOutput = nt.nodes.new('NodeGroupOutput')
        GroupOutput.location = (400, 0)

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-644.9751586914062, 70.93974304199219)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-648.4550170898438, -191.36419677734375)
        Reroute_006.name = "Reroute.006"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-643.0197143554688, 324.29852294921875)
        Reroute_004.name = "Reroute.004"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (646.2061767578125, 70.25714111328125)
        Mix_Shader.name = "Mix Shader"

        Principled_BSDF = nt.nodes.new('ShaderNodeBsdfPrincipled')
        Principled_BSDF.location = (166.5567626953125, 664.8359375)
        Principled_BSDF.name = "Principled BSDF"

        Specular_BSDF = nt.nodes.new('ShaderNodeEeveeSpecular')
        Specular_BSDF.location = (265.9041748046875, -21.532257080078125)
        Specular_BSDF.name = "Specular BSDF"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (91.8416748046875, 552.5823974609375)
        Reroute.name = "Reroute"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-212.31427001953125, 133.84725952148438)
        Reroute_010.name = "Reroute.010"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (-190.29537963867188, 106.12901306152344)
        Reroute_012.name = "Reroute.012"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-192.7764892578125, -138.50494384765625)
        Reroute_011.name = "Reroute.011"

        Invert = nt.nodes.new('ShaderNodeInvert')
        Invert.location = (-313.77777099609375, 500.6892395019531)
        Invert.name = "Invert"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-689.4768676757812, 367.7322082519531)
        Reroute_003.name = "Reroute.003"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (-395.6708984375, 420.4356994628906)
        Reroute_022.name = "Reroute.022"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-397.839599609375, 531.662353515625)
        Reroute_014.name = "Reroute.014"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-688.9718017578125, 551.521484375)
        Reroute_002.name = "Reroute.002"

        Separate_RGB = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_RGB.location = (-1885.0413818359375, 507.4046325683594)
        Separate_RGB.name = "Separate RGB"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (-1653.15380859375, 390.3589782714844)
        Reroute_021.name = "Reroute.021"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-1655.025146484375, 426.0024108886719)
        Reroute_013.name = "Reroute.013"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (-1690.544677734375, 529.8931884765625)
        Reroute_020.name = "Reroute.020"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (-1689.365234375, 472.1393737792969)
        Reroute_019.name = "Reroute.019"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (-1619.9151611328125, 471.4594421386719)
        Reroute_024.name = "Reroute.024"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (-1639.67529296875, 450.108642578125)
        Reroute_026.name = "Reroute.026"

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-1078.6842041015625, 300.11431884765625)
        Math_003.name = "Math.003"
        Math_003.operation = 'LESS_THAN'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (-822.3997192382812, 303.8578796386719)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-1606.45458984375, 114.23965454101562)
        Math.name = "Math"
        Math.operation = 'ADD'

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (-1624.02734375, 3.630218505859375)
        Reroute_025.name = "Reroute.025"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (-1644.78662109375, -19.865478515625)
        Reroute_023.name = "Reroute.023"

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-1436.106689453125, 113.92031860351562)
        Math_001.name = "Math.001"
        Math_001.operation = 'DIVIDE'

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (-898.8671875, 82.71218872070312)
        Reroute_027.name = "Reroute.027"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (-898.0379638671875, 172.47549438476562)
        Reroute_028.name = "Reroute.028"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-1271.536376953125, 113.92031860351562)
        Math_002.name = "Math.002"
        Math_002.operation = 'MULTIPLY'

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (-1642.39306640625, 183.52137756347656)
        Reroute_017.name = "Reroute.017"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (-412.0425720214844, 463.7023010253906)
        Reroute_030.name = "Reroute.030"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (-413.8198547363281, 294.154052734375)
        Reroute_018.name = "Reroute.018"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (-80.07540893554688, 394.37054443359375)
        Reroute_031.name = "Reroute.031"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (-571.1637573242188, 498.6971130371094)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (60.9649658203125, 463.6167297363281)
        Reroute_032.name = "Reroute.032"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (60.20050048828125, 353.7098388671875)
        Reroute_015.name = "Reroute.015"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (-82.55352783203125, 301.8550720214844)
        Reroute_029.name = "Reroute.029"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (39.741943359375, -148.5732421875)
        Reroute_033.name = "Reroute.033"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (39.699432373046875, -59.17791748046875)
        Reroute_034.name = "Reroute.034"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (-87.72216796875, 12.127609252929688)
        Reroute_035.name = "Reroute.035"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (128.23593139648438, 10.941986083984375)
        Reroute_036.name = "Reroute.036"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (126.53964233398438, -102.49162292480469)
        Reroute_037.name = "Reroute.037"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (89.44168090820312, -82.0297622680664)
        Reroute_001.name = "Reroute.001"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (55.111236572265625, -126.69664764404297)
        Reroute_016.name = "Reroute.016"

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (-266.682861328125, 128.5651092529297)
        Reroute_039.name = "Reroute.039"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (-269.8321533203125, -307.91131591796875)
        Reroute_040.name = "Reroute.040"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (-266.67144775390625, 89.37290954589844)
        Reroute_038.name = "Reroute.038"

        Reroute_041 = nt.nodes.new('NodeReroute')
        Reroute_041.location = (208.4625244140625, -267.1594543457031)
        Reroute_041.name = "Reroute.041"

        Reroute_042 = nt.nodes.new('NodeReroute')
        Reroute_042.location = (210.52410888671875, -171.14093017578125)
        Reroute_042.name = "Reroute.042"

        Invert_001 = nt.nodes.new('ShaderNodeInvert')
        Invert_001.location = (26.2003173828125, -230.82920837402344)
        Invert_001.name = "Invert.001"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (-121.96560668945312, -24.280853271484375)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'MULTIPLY'

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-214.43165588378906, -116.34626770019531)
        Reroute_009.name = "Reroute.009"

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (-953.6607055664062, -82.64456176757812)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'MULTIPLY'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (-1251.4854736328125, -176.5738525390625)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (-1544.9970703125, 374.8545227050781)
        Bump.name = "Bump"

        Separate_RGB_001 = nt.nodes.new('ShaderNodeSeparateColor')
        Separate_RGB_001.location = (-1883.408203125, 188.9181365966797)
        Separate_RGB_001.name = "Separate RGB.001"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (-1553.09375, -178.70071411132812)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Normal_Map = nt.nodes.new('ShaderNodeNormalMap')
        Normal_Map.location = (-1889.6505126953125, 360.1208190917969)
        Normal_Map.name = "Normal Map"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-2583.58544921875, -146.96011352539062)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-2568.2626953125, -121.54046630859375)
        Reroute_008.name = "Reroute.008"

        Separate_XYZ = nt.nodes.new('ShaderNodeSeparateXYZ')
        Separate_XYZ.location = (-2468.705322265625, 36.60798645019531)
        Separate_XYZ.name = "Separate XYZ"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-2126.672607421875, 40.971038818359375)
        Combine_XYZ.name = "Combine XYZ"

        Invert_002 = nt.nodes.new('ShaderNodeInvert')
        Invert_002.location = (-2300.2724609375, 19.94091796875)
        Invert_002.name = "Invert.002"

        # Create internal links
        nt.links.new(GroupInput.outputs[14], Mix_Shader.inputs[0])
        nt.links.new(Principled_BSDF.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Mix_Shader.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Specular_BSDF.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Reroute.outputs[0], Principled_BSDF.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Specular_BSDF.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute.inputs[0])
        nt.links.new(GroupInput.outputs[2], Separate_RGB.inputs[0])
        nt.links.new(GroupInput.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix.inputs[6])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(GroupInput.outputs[9], Normal_Map.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Principled_BSDF.inputs[5])
        nt.links.new(Normal_Map.outputs[0], Bump.inputs[3])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Specular_BSDF.inputs[5])
        nt.links.new(Reroute_005.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Vector_Math.inputs[1])
        nt.links.new(GroupInput.outputs[4], Reroute_007.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Specular_BSDF.inputs[3])
        nt.links.new(GroupInput.outputs[3], Reroute_008.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Principled_BSDF.inputs[27])
        nt.links.new(Reroute_009.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Principled_BSDF.inputs[28])
        nt.links.new(Reroute_011.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Mix.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Invert.inputs[1])
        nt.links.new(Reroute_015.outputs[0], Principled_BSDF.inputs[2])
        nt.links.new(Reroute_032.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Specular_BSDF.inputs[2])
        nt.links.new(Reroute_015.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Separate_RGB.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Separate_RGB.outputs[2], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Math.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Math.inputs[1])
        nt.links.new(Reroute_017.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Math.outputs[0], Math_001.inputs[0])
        nt.links.new(Math_001.outputs[0], Math_002.inputs[0])
        nt.links.new(Separate_RGB.outputs[1], Reroute_026.inputs[0])
        nt.links.new(Math_003.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Mix_001.inputs[6])
        nt.links.new(Math_002.outputs[0], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Math_003.inputs[0])
        nt.links.new(Mix_001.outputs[2], Mix.inputs[7])
        nt.links.new(Reroute_031.outputs[0], Principled_BSDF.inputs[13])
        nt.links.new(Reroute_030.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_029.inputs[0])
        nt.links.new(Mix.outputs[2], Reroute_030.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Reroute_031.inputs[0])
        nt.links.new(Invert.outputs[0], Reroute_032.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Specular_BSDF.inputs[1])
        nt.links.new(Reroute_034.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_038.outputs[0], Principled_BSDF.inputs[4])
        nt.links.new(Reroute_039.outputs[0], Reroute_038.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_039.inputs[0])
        nt.links.new(Reroute_040.outputs[0], Invert_001.inputs[1])
        nt.links.new(Reroute_038.outputs[0], Reroute_040.inputs[0])
        nt.links.new(Reroute_042.outputs[0], Specular_BSDF.inputs[4])
        nt.links.new(Invert_001.outputs[0], Reroute_041.inputs[0])
        nt.links.new(Reroute_041.outputs[0], Reroute_042.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], Reroute_009.inputs[0])
        nt.links.new(GroupInput.outputs[6], Mix_002.inputs[7])
        nt.links.new(Mix_002.outputs[2], Vector_Math_001.inputs[1])
        nt.links.new(Bump.outputs[0], Reroute_004.inputs[0])
        nt.links.new(GroupInput.outputs[12], Bump.inputs[1])
        nt.links.new(GroupInput.outputs[11], Bump.inputs[0])
        nt.links.new(Separate_RGB_001.outputs[0], Bump.inputs[2])
        nt.links.new(GroupInput.outputs[10], Separate_RGB_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_003.inputs[7])
        nt.links.new(GroupInput.outputs[5], Mix_003.inputs[0])
        nt.links.new(Mix_003.outputs[2], Mix_002.inputs[6])
        nt.links.new(GroupInput.outputs[7], Separate_XYZ.inputs[0])
        nt.links.new(Separate_XYZ.outputs[1], Invert_002.inputs[1])
        nt.links.new(Separate_XYZ.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(Invert_002.outputs[0], Combine_XYZ.inputs[1])
        nt.links.new(Separate_XYZ.outputs[2], Combine_XYZ.inputs[2])
        nt.links.new(Combine_XYZ.outputs[0], Normal_Map.inputs[1])
        nt.links.new(GroupInput.outputs[8], Invert_002.inputs[0])

        # Set default values
        Principled_BSDF.inputs[1].default_value = 0.0
        Principled_BSDF.inputs[3].default_value = 1.4500000476837158
        Principled_BSDF.inputs[6].default_value = 0.0
        Principled_BSDF.inputs[7].default_value = 0.0
        Principled_BSDF.inputs[8].default_value = 0.0
        Principled_BSDF.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
        Principled_BSDF.inputs[10].default_value = 0.05000000074505806
        Principled_BSDF.inputs[11].default_value = 1.399999976158142
        Principled_BSDF.inputs[12].default_value = 0.0
        Principled_BSDF.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs[15].default_value = 0.0
        Principled_BSDF.inputs[16].default_value = 0.0
        Principled_BSDF.inputs[17].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs[18].default_value = 0.0
        Principled_BSDF.inputs[19].default_value = 0.0
        Principled_BSDF.inputs[20].default_value = 0.029999999329447746
        Principled_BSDF.inputs[21].default_value = 1.5
        Principled_BSDF.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs[23].default_value = (0.0, 0.0, 0.0)
        Principled_BSDF.inputs[24].default_value = 0.0
        Principled_BSDF.inputs[25].default_value = 0.5
        Principled_BSDF.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
        Principled_BSDF.inputs[29].default_value = 0.0
        Principled_BSDF.inputs[30].default_value = 1.3300000429153442
        Specular_BSDF.inputs[6].default_value = 0.0
        Specular_BSDF.inputs[7].default_value = 0.0
        Specular_BSDF.inputs[8].default_value = (0.0, 0.0, 0.0)
        Specular_BSDF.inputs[9].default_value = 0.0
        Invert.inputs[0].default_value = 1.0
        Math_003.inputs[1].default_value = 0.5
        Math_003.inputs[2].default_value = 0.5
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[2].default_value = 0.5
        Math_001.inputs[1].default_value = 2.0
        Math_001.inputs[2].default_value = 0.5
        Math_002.inputs[1].default_value = 2.0
        Math_002.inputs[2].default_value = 0.5
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_001.inputs[0].default_value = 1.0
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[3].default_value = 1.0
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Mix_002.inputs[0].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[6].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
