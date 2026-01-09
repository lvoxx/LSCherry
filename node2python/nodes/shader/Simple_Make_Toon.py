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


class ShaderNodeSimple_Make_Toon(ShaderNode):
    bl_idname = 'ShaderNodeSimple_Make_Toon'
    bl_label = "Simple Make Toon"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base Color"].default_value = (1.0, 0.0, 0.0, 1.0)
        self.inputs["Shadow Color"].default_value = (0.17788751423358917, 0.0, 0.0, 1.0)
        self.inputs["Rim Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Pattern"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Disable Toon Style"].default_value = False
        self.inputs["Toon Style"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Alpha"].default_value = 1.0
        self.inputs["Rim Size"].default_value = 0.30000001192092896
        self.inputs["Rim Strength"].default_value = 0.10000000149011612
        self.inputs["Enable Dot"].default_value = False
        self.inputs["World Color"].default_value = (1.0, 1.0, 1.0, 1.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Simple Make Toon'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('To AgX', in_out='OUTPUT', socket_type='NodeSocketShader')
        nt.interface.new_socket('Combined', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Alpha', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('Toon Mask', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('Post Toon Mask', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Shadow Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.17788751423358917, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Rim Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Pattern', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Disable Toon Style', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Toon Style', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Rim Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.30000001192092896
        input_socket = nt.interface.new_socket('Rim Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Enable Dot', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('World Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)

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

        Group_011 = nt.nodes.new('ShaderNodeGroup')
        Group_011.location = (-161.967529296875, 325.0082702636719)
        Group_011.name = "Group.011"

        Brightness_Contrast = nt.nodes.new('ShaderNodeBrightContrast')
        Brightness_Contrast.location = (-161.43267822265625, -214.73837280273438)
        Brightness_Contrast.name = "Brightness/Contrast"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (66.22296142578125, 289.8548583984375)
        Reroute_002.name = "Reroute.002"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (189.1661376953125, 209.114013671875)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (-161.967529296875, 178.05282592773438)
        Group_010.name = "Group.010"

        Group_012 = nt.nodes.new('ShaderNodeGroup')
        Group_012.location = (-161.967529296875, 29.134735107421875)
        Group_012.name = "Group.012"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-260.2355041503906, -81.37080383300781)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-260.2355041503906, 244.89666748046875)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-260.2355041503906, -295.9886779785156)
        Reroute_005.name = "Reroute.005"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (118.8331298828125, 144.26217651367188)
        Reroute_007.name = "Reroute.007"

        Group_013 = nt.nodes.new('ShaderNodeGroup')
        Group_013.location = (-442.6522216796875, -227.78414916992188)
        Group_013.name = "Group.013"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-222.15277099609375, -237.87203979492188)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-222.15277099609375, -182.71047973632812)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-222.15277099609375, 53.696380615234375)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-222.15277099609375, 200.4656982421875)
        Reroute_011.name = "Reroute.011"

        Attribute = nt.nodes.new('ShaderNodeAttribute')
        Attribute.location = (-442.30596923828125, -153.39224243164062)
        Attribute.name = "Attribute"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (118.8331298828125, 26.044830322265625)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (118.8331298828125, -27.997406005859375)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (118.8331298828125, 4.653106689453125)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (147.887939453125, 48.583251953125)
        Reroute_015.name = "Reroute.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (147.88787841796875, 377.4309997558594)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (-310.74755859375, 377.4309997558594)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (-310.74755859375, -102.48544311523438)
        Reroute_018.name = "Reroute.018"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (189.1661376953125, -47.2127685546875)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (147.887939453125, -207.46560668945312)
        Reroute_019.name = "Reroute.019"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (66.22296142578125, -228.98312377929688)
        Reroute_020.name = "Reroute.020"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (442.6522216796875, 209.114013671875)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MULTIPLY'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (442.6522216796875, -41.1126708984375)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MULTIPLY'

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (-378.12152099609375, -377.4309997558594)
        Reroute_021.name = "Reroute.021"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (385.47216796875, -377.4309997558594)
        Reroute_022.name = "Reroute.022"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (385.47216796875, -244.53530883789062)
        Reroute_023.name = "Reroute.023"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (385.47216796875, 4.494537353515625)
        Reroute_024.name = "Reroute.024"

        Frame_005 = nt.nodes.new('NodeFrame')
        Frame_005.location = (1560.62744140625, -702.4736328125)
        Frame_005.label = "Rim Core Style"
        Frame_005.name = "Frame.005"

        Group_014 = nt.nodes.new('ShaderNodeGroup')
        Group_014.location = (-271.62548828125, 403.7555847167969)
        Group_014.name = "Group.014"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (-325.4676513671875, 301.59234619140625)
        Reroute_029.name = "Reroute.029"

        Group_005 = nt.nodes.new('ShaderNodeGroup')
        Group_005.location = (-685.4202880859375, 303.63360595703125)
        Group_005.name = "Group.005"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (-500.69091796875, 436.3397216796875)
        Map_Range.name = "Map Range"

        Reroute_030 = nt.nodes.new('NodeReroute')
        Reroute_030.location = (1235.1597900390625, -77.01985168457031)
        Reroute_030.name = "Reroute.030"

        Reroute_031 = nt.nodes.new('NodeReroute')
        Reroute_031.location = (137.4375, 82.68499755859375)
        Reroute_031.name = "Reroute.031"

        Frame_006 = nt.nodes.new('NodeFrame')
        Frame_006.location = (1560.9140625, -237.73440551757812)
        Frame_006.label = "Toon Core Style"
        Frame_006.name = "Frame.006"

        Group_006 = nt.nodes.new('ShaderNodeGroup')
        Group_006.location = (-686.9642333984375, 326.6816711425781)
        Group_006.name = "Group.006"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-507.575439453125, 466.5357360839844)
        Group.name = "Group"

        Reroute_032 = nt.nodes.new('NodeReroute')
        Reroute_032.location = (-592.1317138671875, 411.19091796875)
        Reroute_032.name = "Reroute.032"

        Reroute_033 = nt.nodes.new('NodeReroute')
        Reroute_033.location = (-72.4588623046875, 64.52035522460938)
        Reroute_033.name = "Reroute.033"

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (1667.8426513671875, 128.55874633789062)
        Frame.label = "Add Base + Shadow Color"
        Frame.name = "Frame"

        Mix_004 = nt.nodes.new('ShaderNodeMix')
        Mix_004.location = (97.5694580078125, -76.97722625732422)
        Mix_004.label = "Add Base Color"
        Mix_004.name = "Mix.004"
        Mix_004.blend_type = 'MULTIPLY'

        Invert_Color = nt.nodes.new('ShaderNodeInvert')
        Invert_Color.location = (101.5152587890625, 97.85824584960938)
        Invert_Color.name = "Invert Color"

        Mix_005 = nt.nodes.new('ShaderNodeMix')
        Mix_005.location = (340.3096923828125, 158.81622314453125)
        Mix_005.label = "Add Shadow Color"
        Mix_005.name = "Mix.005"
        Mix_005.blend_type = 'MULTIPLY'

        Reroute_034 = nt.nodes.new('NodeReroute')
        Reroute_034.location = (-72.4588623046875, -211.4200439453125)
        Reroute_034.name = "Reroute.034"

        Mix_006 = nt.nodes.new('ShaderNodeMix')
        Mix_006.location = (537.6343994140625, 129.76974487304688)
        Mix_006.label = "Mix Base And Shadow Base on Shading"
        Mix_006.name = "Mix.006"
        Mix_006.blend_type = 'MULTIPLY'

        Reroute_035 = nt.nodes.new('NodeReroute')
        Reroute_035.location = (-72.4588623046875, 173.44485473632812)
        Reroute_035.name = "Reroute.035"

        Reroute_036 = nt.nodes.new('NodeReroute')
        Reroute_036.location = (503.9747314453125, 173.44485473632812)
        Reroute_036.name = "Reroute.036"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (1590.1153564453125, -417.129150390625)
        Frame_001.label = "Add Rim Color"
        Frame_001.name = "Frame.001"

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (213.46142578125, 89.57038879394531)
        Mix_007.label = "Add Rim Color"
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MULTIPLY'

        Reroute_037 = nt.nodes.new('NodeReroute')
        Reroute_037.location = (137.4375, -70.87164306640625)
        Reroute_037.name = "Reroute.037"

        Reroute_038 = nt.nodes.new('NodeReroute')
        Reroute_038.location = (-37.48681640625, -1028.4466552734375)
        Reroute_038.name = "Reroute.038"

        Mix_012 = nt.nodes.new('ShaderNodeMix')
        Mix_012.location = (-19.26318359375, -733.5491333007812)
        Mix_012.name = "Mix.012"
        Mix_012.blend_type = 'MULTIPLY'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-63.62353515625, -755.1759033203125)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-63.62353515625, -1128.469970703125)
        Reroute_001.name = "Reroute.001"

        Mix_025 = nt.nodes.new('ShaderNodeMix')
        Mix_025.location = (43.81640625, -923.7108764648438)
        Mix_025.name = "Mix.025"
        Mix_025.blend_type = 'MULTIPLY'

        Frame_019 = nt.nodes.new('NodeFrame')
        Frame_019.location = (2839.0869140625, 665.20703125)
        Frame_019.label = "Add World Color"
        Frame_019.name = "Frame.019"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-63.62353515625, -443.20159912109375)
        Reroute_006.name = "Reroute.006"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (-63.62353515625, -743.1082763671875)
        Reroute_025.name = "Reroute.025"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (3083.443115234375, -294.7702331542969)
        Reroute_027.name = "Reroute.027"

        Mix_026 = nt.nodes.new('ShaderNodeMix')
        Mix_026.location = (3198.917724609375, 135.84210205078125)
        Mix_026.name = "Mix.026"
        Mix_026.blend_type = 'ADD'

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (3412.80322265625, 211.02085876464844)
        Group_001.name = "Group.001"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (-378.12152099609375, -35.279937744140625)
        Reroute_028.name = "Reroute.028"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (-92.05169677734375, 753.1353759765625)
        Frame_002.label = "README"
        Frame_002.name = "Frame.002"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (-69.81802368164062, 661.5930786132812)
        Frame_003.label = "This node group is made of old shading tech before v1.0.5"
        Frame_003.name = "Frame.003"

        Frame_004 = nt.nodes.new('NodeFrame')
        Frame_004.location = (-154.81802368164062, 592.7224731445312)
        Frame_004.label = "No Env contaction with this node group"
        Frame_004.name = "Frame.004"

        Frame_007 = nt.nodes.new('NodeFrame')
        Frame_007.location = (-154.81802368164062, 523.851806640625)
        Frame_007.label = "For better shading, use Make Toon"
        Frame_007.name = "Frame.007"

        Group_002 = nt.nodes.new('ShaderNodeGroup')
        Group_002.location = (1287.54833984375, 231.40635681152344)
        Group_002.name = "Group.002"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (-222.15277099609375, -445.148193359375)
        Reroute_026.name = "Reroute.026"

        Reroute_039 = nt.nodes.new('NodeReroute')
        Reroute_039.location = (709.773681640625, -445.148193359375)
        Reroute_039.name = "Reroute.039"

        Reroute_040 = nt.nodes.new('NodeReroute')
        Reroute_040.location = (709.773681640625, -415.07281494140625)
        Reroute_040.name = "Reroute.040"

        Reroute_041 = nt.nodes.new('NodeReroute')
        Reroute_041.location = (709.773681640625, 72.39884185791016)
        Reroute_041.name = "Reroute.041"

        Reroute_042 = nt.nodes.new('NodeReroute')
        Reroute_042.location = (968.7823486328125, 456.9328918457031)
        Reroute_042.name = "Reroute.042"

        Reroute_043 = nt.nodes.new('NodeReroute')
        Reroute_043.location = (3904.29736328125, 456.9328918457031)
        Reroute_043.name = "Reroute.043"

        Reroute_044 = nt.nodes.new('NodeReroute')
        Reroute_044.location = (3904.29736328125, -4.829331398010254)
        Reroute_044.name = "Reroute.044"

        Reroute_045 = nt.nodes.new('NodeReroute')
        Reroute_045.location = (3967.457763671875, 509.5217590332031)
        Reroute_045.name = "Reroute.045"

        Reroute_046 = nt.nodes.new('NodeReroute')
        Reroute_046.location = (3967.457763671875, -28.715904235839844)
        Reroute_046.name = "Reroute.046"

        Reroute_047 = nt.nodes.new('NodeReroute')
        Reroute_047.location = (1595.3837890625, 509.5217590332031)
        Reroute_047.name = "Reroute.047"

        # Create internal links
        nt.links.new(Group_013.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Brightness_Contrast.outputs[0], Mix_001.inputs[7])
        nt.links.new(Reroute_012.outputs[0], Mix.inputs[6])
        nt.links.new(Reroute_020.outputs[0], Mix_001.inputs[6])
        nt.links.new(Reroute_015.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Group_011.inputs[2])
        nt.links.new(Group_012.outputs[1], Reroute_013.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Mix_001.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Mix.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Group_012.inputs[3])
        nt.links.new(Group_011.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Group_011.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Mix.outputs[2], Mix_002.inputs[6])
        nt.links.new(Reroute_024.outputs[0], Mix_002.inputs[7])
        nt.links.new(Reroute_003.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Mix.inputs[7])
        nt.links.new(Group_010.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Reroute_014.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Brightness_Contrast.inputs[1])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Reroute_022.inputs[0])
        nt.links.new(Attribute.outputs[1], Group_012.inputs[1])
        nt.links.new(Mix_001.outputs[2], Mix_003.inputs[6])
        nt.links.new(Reroute_022.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Reroute_024.inputs[0])
        nt.links.new(Group_012.outputs[2], Brightness_Contrast.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Group_010.inputs[2])
        nt.links.new(Reroute_016.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Mix_003.inputs[7])
        nt.links.new(GroupInput.outputs[6], Group_013.inputs[0])
        nt.links.new(GroupInput.outputs[10], Reroute_018.inputs[0])
        nt.links.new(GroupInput.outputs[9], Reroute_003.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Group_014.inputs[1])
        nt.links.new(Map_Range.outputs[0], Group_014.inputs[0])
        nt.links.new(Group_005.outputs[0], Map_Range.inputs[0])
        nt.links.new(GroupInput.outputs[8], Map_Range.inputs[1])
        nt.links.new(Mix_003.outputs[2], Reroute_030.inputs[0])
        nt.links.new(Reroute_030.outputs[0], Reroute_029.inputs[0])
        nt.links.new(Group_014.outputs[0], Reroute_031.inputs[0])
        nt.links.new(GroupInput.outputs[5], Group.inputs[3])
        nt.links.new(Mix_002.outputs[2], Reroute_032.inputs[0])
        nt.links.new(Reroute_032.outputs[0], Group.inputs[1])
        nt.links.new(Group_006.outputs[0], Group.inputs[2])
        nt.links.new(Group_002.outputs[0], Reroute_033.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_004.inputs[7])
        nt.links.new(Reroute_033.outputs[0], Invert_Color.inputs[1])
        nt.links.new(Reroute_033.outputs[0], Reroute_034.inputs[0])
        nt.links.new(Reroute_034.outputs[0], Mix_004.inputs[6])
        nt.links.new(GroupInput.outputs[1], Mix_005.inputs[7])
        nt.links.new(Invert_Color.outputs[0], Mix_005.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_005.inputs[6])
        nt.links.new(Mix_005.outputs[2], Mix_006.inputs[6])
        nt.links.new(Mix_004.outputs[2], Mix_006.inputs[7])
        nt.links.new(Reroute_033.outputs[0], Reroute_035.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_036.inputs[0])
        nt.links.new(Reroute_036.outputs[0], Mix_006.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mix_007.inputs[7])
        nt.links.new(Reroute_031.outputs[0], Reroute_037.inputs[0])
        nt.links.new(Reroute_037.outputs[0], Mix_007.inputs[6])
        nt.links.new(Mix_007.outputs[2], Reroute_038.inputs[0])
        nt.links.new(GroupInput.outputs[11], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Mix_012.inputs[7])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Mix_025.inputs[7])
        nt.links.new(Reroute_038.outputs[0], Mix_025.inputs[6])
        nt.links.new(Mix_006.outputs[2], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Mix_012.inputs[6])
        nt.links.new(Mix_025.outputs[2], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Mix_026.inputs[7])
        nt.links.new(Mix_026.outputs[2], Group_001.inputs[0])
        nt.links.new(Mix_026.outputs[2], GroupOutput.inputs[2])
        nt.links.new(GroupInput.outputs[3], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Group.outputs[0], Group_002.inputs[0])
        nt.links.new(Mix_012.outputs[2], Mix_026.inputs[6])
        nt.links.new(Reroute_008.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Reroute_039.inputs[0])
        nt.links.new(Reroute_039.outputs[0], Reroute_040.inputs[0])
        nt.links.new(Reroute_040.outputs[0], Group_005.inputs[1])
        nt.links.new(Reroute_040.outputs[0], Reroute_041.inputs[0])
        nt.links.new(Reroute_041.outputs[0], Group_006.inputs[1])
        nt.links.new(Reroute_032.outputs[0], Reroute_042.inputs[0])
        nt.links.new(Reroute_042.outputs[0], Reroute_043.inputs[0])
        nt.links.new(Reroute_043.outputs[0], Reroute_044.inputs[0])
        nt.links.new(Reroute_044.outputs[0], GroupOutput.inputs[4])
        nt.links.new(Reroute_045.outputs[0], Reroute_046.inputs[0])
        nt.links.new(Reroute_046.outputs[0], GroupOutput.inputs[5])
        nt.links.new(Reroute_047.outputs[0], Reroute_045.inputs[0])
        nt.links.new(Reroute_035.outputs[0], Reroute_047.inputs[0])
        nt.links.new(GroupInput.outputs[7], Group_001.inputs[1])
        nt.links.new(Group_001.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Group_001.outputs[1], GroupOutput.inputs[1])
        nt.links.new(GroupInput.outputs[7], GroupOutput.inputs[3])
        nt.links.new(GroupInput.outputs[4], Group.inputs[0])

        # Set default values
        Group_011.inputs[1].default_value = 0.10000000149011612
        Brightness_Contrast.inputs[2].default_value = 0.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_010.inputs[0].default_value = 1.0
        Group_010.inputs[1].default_value = 0.10000000149011612
        Group_012.inputs[0].default_value = False
        Group_012.inputs[2].default_value = 0.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[0].default_value = 1.0
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[0].default_value = 1.0
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_005.inputs[0].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 1.0
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)
        Group_006.inputs[0].default_value = 0.0
        Group.inputs[4].default_value = 1.0
        Group.inputs[5].default_value = 0.05000000074505806
        Group.inputs[6].default_value = 0.0
        Group.inputs[7].default_value = 0.0
        Mix_004.inputs[0].default_value = 1.0
        Mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_004.inputs[2].default_value = 0.0
        Mix_004.inputs[3].default_value = 0.0
        Mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_004.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_004.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert_Color.inputs[0].default_value = 1.0
        Mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_005.inputs[2].default_value = 0.0
        Mix_005.inputs[3].default_value = 0.0
        Mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_005.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_005.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_006.inputs[2].default_value = 0.0
        Mix_006.inputs[3].default_value = 0.0
        Mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_006.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_006.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[0].default_value = 1.0
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[3].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_012.inputs[0].default_value = 1.0
        Mix_012.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_012.inputs[2].default_value = 0.0
        Mix_012.inputs[3].default_value = 0.0
        Mix_012.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_012.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_012.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_012.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_025.inputs[0].default_value = 1.0
        Mix_025.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_025.inputs[2].default_value = 0.0
        Mix_025.inputs[3].default_value = 0.0
        Mix_025.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_025.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_025.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_025.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_026.inputs[0].default_value = 1.0
        Mix_026.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_026.inputs[2].default_value = 0.0
        Mix_026.inputs[3].default_value = 0.0
        Mix_026.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_026.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_026.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_026.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Group_002.inputs[1].default_value = 0.10000000149011612

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
