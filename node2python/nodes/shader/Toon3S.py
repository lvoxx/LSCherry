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


class ShaderNodeToon3S(ShaderNode):
    bl_idname = 'ShaderNodeToon3S'
    bl_label = "Toon3S"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        self.inputs["Spec Color"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Shallow Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Shallow Scale"].default_value = 0.05000000074505806
        self.inputs["Mid Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Mid Scale"].default_value = 0.05000000074505806
        self.inputs["Mid Weight"].default_value = 0.6000000238418579
        self.inputs["Deep Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Deep Scale"].default_value = 0.05000000074505806
        self.inputs["Deep Weight"].default_value = 0.4000000059604645
        self.inputs["Spec Tint"].default_value = 0.10000000149011612
        self.inputs["Spec Roughness"].default_value = 0.5
        self.inputs["Oil Spec"].default_value = 0.5
        self.inputs["Oil Roughness"].default_value = 0.5

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Toon3S'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        input_socket = nt.interface.new_socket('Spec Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Shallow Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shallow Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Mid Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Mid Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Mid Weight', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.6000000238418579
        input_socket = nt.interface.new_socket('Deep Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Deep Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.05000000074505806
        input_socket = nt.interface.new_socket('Deep Weight', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.4000000059604645
        input_socket = nt.interface.new_socket('Spec Tint', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Spec Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Oil Spec', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Oil Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5

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

        Subsurface_Scattering = nt.nodes.new('ShaderNodeSubsurfaceScattering')
        Subsurface_Scattering.location = (-282.62103271484375, 387.3582763671875)
        Subsurface_Scattering.name = "Subsurface Scattering"

        Mix_Shader_001 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_001.location = (209.8820037841797, 189.564453125)
        Mix_Shader_001.name = "Mix Shader.001"

        Mix_Shader_003 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_003.location = (603.1105346679688, -55.93438720703125)
        Mix_Shader_003.name = "Mix Shader.003"

        Subsurface_Scattering_002 = nt.nodes.new('ShaderNodeSubsurfaceScattering')
        Subsurface_Scattering_002.location = (-285.1087646484375, 34.13592529296875)
        Subsurface_Scattering_002.name = "Subsurface Scattering.002"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (-2.0064125061035156, 296.5262451171875)
        Mix_Shader.name = "Mix Shader"

        Mix_Shader_002 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_002.location = (407.631103515625, 61.1195068359375)
        Mix_Shader_002.name = "Mix Shader.002"

        Subsurface_Scattering_001 = nt.nodes.new('ShaderNodeSubsurfaceScattering')
        Subsurface_Scattering_001.location = (-283.8648681640625, 210.7469482421875)
        Subsurface_Scattering_001.name = "Subsurface Scattering.001"

        Glossy_BSDF = nt.nodes.new('ShaderNodeBsdfAnisotropic')
        Glossy_BSDF.location = (-285.16619873046875, -151.75439453125)
        Glossy_BSDF.name = "Glossy BSDF"

        Glossy_BSDF_001 = nt.nodes.new('ShaderNodeBsdfAnisotropic')
        Glossy_BSDF_001.location = (-289.7405090332031, -380.2276611328125)
        Glossy_BSDF_001.name = "Glossy BSDF.001"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-390.04559326171875, 111.63278198242188)
        Reroute.name = "Reroute"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (404.612548828125, -413.80865478515625)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (404.612548828125, -161.0088348388672)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (154.65293884277344, -187.4000244140625)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (154.65293884277344, -41.55397033691406)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-48.092063903808594, -1.272679328918457)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-48.092063903808594, 90.40198516845703)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-575.1041259765625, 88.8038330078125)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-575.1041259765625, 255.6617889404297)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-556.4973754882812, 67.95903015136719)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-556.4973754882812, 279.9482116699219)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (-459.9254150390625, 153.9003448486328)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-459.9254150390625, 300.55841064453125)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-459.9254150390625, 127.84435272216797)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (-459.9254150390625, -51.56983184814453)
        Reroute_015.name = "Reroute.015"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-390.04559326171875, 61.75859451293945)
        Reroute_001.name = "Reroute.001"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (-390.04559326171875, -325.6309814453125)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (-390.04559326171875, -552.4190063476562)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (-605.3943481445312, 43.35251998901367)
        Reroute_018.name = "Reroute.018"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (-605.3943481445312, 80.5710220336914)
        Reroute_019.name = "Reroute.019"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (-504.17327880859375, 21.018779754638672)
        Reroute_020.name = "Reroute.020"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (-504.17327880859375, 103.43978881835938)
        Reroute_021.name = "Reroute.021"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (-390.04559326171875, 237.6549530029297)
        Reroute_022.name = "Reroute.022"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-668.2432250976562, -191.4008331298828)
        Map_Range.name = "Map Range"

        Map_Range_001 = nt.nodes.new('ShaderNodeMapRange')
        Map_Range_001.location = (-668.2432250976562, -439.79241943359375)
        Map_Range_001.name = "Map Range.001"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (-706.2932739257812, -88.47581481933594)
        Reroute_023.name = "Reroute.023"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (-706.2932739257812, -328.0354309082031)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (-727.1329956054688, -131.7624969482422)
        Reroute_025.name = "Reroute.025"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (-727.1329956054688, -575.9407348632812)
        Reroute_026.name = "Reroute.026"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (-368.16827392578125, -154.76992797851562)
        Reroute_027.name = "Reroute.027"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (-368.16827392578125, -484.0857849121094)
        Reroute_028.name = "Reroute.028"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (-339.00250244140625, -109.99342346191406)
        Reroute_029.name = "Reroute.029"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (-339.00250244140625, -257.5858459472656)
        Reroute_030.name = "Reroute.030"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (-499.0847473144531, -226.28814697265625)
        Reroute_031.name = "Reroute.031"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (-445.43499755859375, -474.9310302734375)
        Reroute_032.name = "Reroute.032"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (-499.0847473144531, -660.1091918945312)
        Reroute_033.name = "Reroute.033"

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (-445.43499755859375, -636.6358642578125)
        Reroute_034.name = "Reroute.034"

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (277.1611328125, -660.1091918945312)
        Reroute_035.name = "Reroute.035"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (173.1964569091797, -636.6358642578125)
        Reroute_036.name = "Reroute.036"

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (277.1611328125, -117.40963745117188)
        Reroute_037.name = "Reroute.037"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (173.1964569091797, 2.25335693359375)
        Reroute_038.name = "Reroute.038"

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (-673.8922119140625, -21.885255813598633)
        Reroute_039.name = "Reroute.039"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (-673.8922119140625, -95.65498352050781)
        Reroute_040.name = "Reroute.040"

        Reroute_041 = nt.nodes.new('NodeReroute')
        Reroute_041.location = (-340.4649353027344, -40.342864990234375)
        Reroute_041.name = "Reroute.041"

        Reroute_042 = nt.nodes.new('NodeReroute')
        Reroute_042.location = (-721.3831787109375, -0.2634773254394531)
        Reroute_042.name = "Reroute.042"

        Reroute_043 = nt.nodes.new('NodeReroute')
        Reroute_043.location = (-721.3831787109375, 457.9627990722656)
        Reroute_043.name = "Reroute.043"

        Reroute_044 = nt.nodes.new('NodeReroute')
        Reroute_044.location = (-64.14337158203125, 457.9627990722656)
        Reroute_044.name = "Reroute.044"

        Reroute_045 = nt.nodes.new('NodeReroute')
        Reroute_045.location = (-64.14337158203125, 238.48960876464844)
        Reroute_045.name = "Reroute.045"

        Reroute_046 = nt.nodes.new('NodeReroute')
        Reroute_046.location = (-656.3702392578125, -65.56478881835938)
        Reroute_046.name = "Reroute.046"

        Reroute_047 = nt.nodes.new('NodeReroute')
        Reroute_047.location = (-656.3702392578125, 422.4000244140625)
        Reroute_047.name = "Reroute.047"

        Reroute_048 = nt.nodes.new('NodeReroute')
        Reroute_048.location = (168.4810791015625, 422.4000244140625)
        Reroute_048.name = "Reroute.048"

        Reroute_049 = nt.nodes.new('NodeReroute')
        Reroute_049.location = (168.4810791015625, 130.16751098632812)
        Reroute_049.name = "Reroute.049"

        Reroute_050 = nt.nodes.new('NodeReroute')
        Reroute_050.location = (-390.04559326171875, -115.28192901611328)
        Reroute_050.name = "Reroute.050"

        Reroute_051 = nt.nodes.new('NodeReroute')
        Reroute_051.location = (-423.5605773925781, 133.0816192626953)
        Reroute_051.name = "Reroute.051"

        Reroute_052 = nt.nodes.new('NodeReroute')
        Reroute_052.location = (-423.5605773925781, -236.44715881347656)
        Reroute_052.name = "Reroute.052"

        Reroute_053 = nt.nodes.new('NodeReroute')
        Reroute_053.location = (-423.5605773925781, -466.0821533203125)
        Reroute_053.name = "Reroute.053"

        # Create internal links
        nt.links.new(Mix_Shader_003.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Subsurface_Scattering.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Subsurface_Scattering_001.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(Mix_Shader.outputs[0], Mix_Shader_001.inputs[1])
        nt.links.new(Mix_Shader_002.outputs[0], Mix_Shader_003.inputs[1])
        nt.links.new(Mix_Shader_001.outputs[0], Mix_Shader_002.inputs[1])
        nt.links.new(Reroute_041.outputs[0], Subsurface_Scattering_002.inputs[1])
        nt.links.new(GroupInput.outputs[2], Reroute.inputs[0])
        nt.links.new(Glossy_BSDF_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix_Shader_003.inputs[2])
        nt.links.new(Glossy_BSDF.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Mix_Shader_002.inputs[2])
        nt.links.new(Subsurface_Scattering_002.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Mix_Shader_001.inputs[2])
        nt.links.new(GroupInput.outputs[3], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Subsurface_Scattering.inputs[2])
        nt.links.new(GroupInput.outputs[4], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Subsurface_Scattering.inputs[1])
        nt.links.new(GroupInput.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Subsurface_Scattering.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Subsurface_Scattering_001.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Subsurface_Scattering_002.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Subsurface_Scattering_001.inputs[6])
        nt.links.new(Reroute_050.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Glossy_BSDF.inputs[4])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Glossy_BSDF_001.inputs[4])
        nt.links.new(GroupInput.outputs[5], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Subsurface_Scattering_001.inputs[2])
        nt.links.new(GroupInput.outputs[6], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Subsurface_Scattering_001.inputs[1])
        nt.links.new(Reroute_022.outputs[0], Subsurface_Scattering.inputs[6])
        nt.links.new(GroupInput.outputs[11], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Map_Range.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Map_Range_001.inputs[0])
        nt.links.new(GroupInput.outputs[13], Reroute_025.inputs[0])
        nt.links.new(GroupInput.outputs[14], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Glossy_BSDF_001.inputs[1])
        nt.links.new(GroupInput.outputs[12], Reroute_029.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Reroute_030.inputs[0])
        nt.links.new(Reroute_030.outputs[0], Glossy_BSDF.inputs[1])
        nt.links.new(Map_Range.outputs[0], Reroute_031.inputs[0])
        nt.links.new(Map_Range_001.outputs[0], Reroute_032.inputs[0])
        nt.links.new(Reroute_031.outputs[0], Reroute_033.inputs[0])
        nt.links.new(Reroute_032.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_033.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Reroute_038.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_038.outputs[0], Mix_Shader_002.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Mix_Shader_003.inputs[0])
        nt.links.new(GroupInput.outputs[8], Reroute_039.inputs[0])
        nt.links.new(Reroute_039.outputs[0], Reroute_040.inputs[0])
        nt.links.new(Reroute_040.outputs[0], Subsurface_Scattering_002.inputs[2])
        nt.links.new(GroupInput.outputs[9], Reroute_041.inputs[0])
        nt.links.new(GroupInput.outputs[7], Reroute_042.inputs[0])
        nt.links.new(Reroute_042.outputs[0], Reroute_043.inputs[0])
        nt.links.new(Reroute_043.outputs[0], Reroute_044.inputs[0])
        nt.links.new(Reroute_044.outputs[0], Reroute_045.inputs[0])
        nt.links.new(Reroute_045.outputs[0], Mix_Shader.inputs[0])
        nt.links.new(GroupInput.outputs[10], Reroute_046.inputs[0])
        nt.links.new(Reroute_046.outputs[0], Reroute_047.inputs[0])
        nt.links.new(Reroute_047.outputs[0], Reroute_048.inputs[0])
        nt.links.new(Reroute_048.outputs[0], Reroute_049.inputs[0])
        nt.links.new(Reroute_049.outputs[0], Mix_Shader_001.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_050.inputs[0])
        nt.links.new(Reroute_050.outputs[0], Subsurface_Scattering_002.inputs[6])
        nt.links.new(GroupInput.outputs[1], Reroute_051.inputs[0])
        nt.links.new(Reroute_051.outputs[0], Reroute_052.inputs[0])
        nt.links.new(Reroute_052.outputs[0], Glossy_BSDF.inputs[0])
        nt.links.new(Reroute_052.outputs[0], Reroute_053.inputs[0])
        nt.links.new(Reroute_053.outputs[0], Glossy_BSDF_001.inputs[0])

        # Set default values
        Subsurface_Scattering.inputs[3].default_value = 1.399999976158142
        Subsurface_Scattering.inputs[4].default_value = 1.0
        Subsurface_Scattering.inputs[5].default_value = 0.0
        Subsurface_Scattering.inputs[7].default_value = 0.0
        Subsurface_Scattering_002.inputs[3].default_value = 1.399999976158142
        Subsurface_Scattering_002.inputs[4].default_value = 1.0
        Subsurface_Scattering_002.inputs[5].default_value = 0.0
        Subsurface_Scattering_002.inputs[7].default_value = 0.0
        Subsurface_Scattering_001.inputs[3].default_value = 1.399999976158142
        Subsurface_Scattering_001.inputs[4].default_value = 1.0
        Subsurface_Scattering_001.inputs[5].default_value = 0.0
        Subsurface_Scattering_001.inputs[7].default_value = 0.0
        Glossy_BSDF.inputs[2].default_value = 0.0
        Glossy_BSDF.inputs[3].default_value = 0.0
        Glossy_BSDF.inputs[5].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF.inputs[6].default_value = 0.0
        Glossy_BSDF_001.inputs[2].default_value = 0.0
        Glossy_BSDF_001.inputs[3].default_value = 0.0
        Glossy_BSDF_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Glossy_BSDF_001.inputs[6].default_value = 0.0
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 0.8999999761581421
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Map_Range_001.inputs[1].default_value = 0.0
        Map_Range_001.inputs[2].default_value = 1.0
        Map_Range_001.inputs[3].default_value = 0.0
        Map_Range_001.inputs[4].default_value = 0.8999999761581421
        Map_Range_001.inputs[5].default_value = 4.0
        Map_Range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range_001.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
