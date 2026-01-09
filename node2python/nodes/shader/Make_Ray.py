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


class ShaderNodeMake_Ray(ShaderNode):
    bl_idname = 'ShaderNodeMake_Ray'
    bl_label = "Make Ray"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Base Color"].default_value = (1.0, 0.0, 0.0, 1.0)
        self.inputs["Specular Color"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Edge Tint"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Size"].default_value = 0.8999999761581421
        self.inputs["Smooth"].default_value = 0.10000000149011612
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Metal"].default_value = 0.0
        self.inputs["Alpha"].default_value = 1.0
        self.inputs["Emission Color"].default_value = (0.049706313759088516, 0.006048834882676601, 0.0, 1.0)
        self.inputs["Emission Strength"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)
        self.inputs["Tangent"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Make Ray'

        # Create output sockets
        nt.interface.new_socket('Shader', in_out='OUTPUT', socket_type='NodeSocketShader')

        # Create input sockets
        nt.interface.new_socket('―【CORE】―', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Base Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Specular Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        input_socket = nt.interface.new_socket('Edge Tint', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        nt.interface.new_socket('―【GENERAL】―', in_out='INPUT', socket_type='NodeSocketShader')
        input_socket = nt.interface.new_socket('Size', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8999999761581421
        input_socket = nt.interface.new_socket('Smooth', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.10000000149011612
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Metal', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Alpha', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Emission Color', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.049706313759088516, 0.006048834882676601, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Emission Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket = nt.interface.new_socket('Tangent', in_out='INPUT', socket_type='NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)

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

        Group_008 = nt.nodes.new('ShaderNodeGroup')
        Group_008.location = (-313.228759765625, 153.92971801757812)
        Group_008.name = "Group.008"

        Group_009 = nt.nodes.new('ShaderNodeGroup')
        Group_009.location = (-313.228759765625, -47.740570068359375)
        Group_009.name = "Group.009"

        Mix_Shader = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader.location = (-52.30828094482422, 105.36119079589844)
        Mix_Shader.name = "Mix Shader"

        Group_010 = nt.nodes.new('ShaderNodeGroup')
        Group_010.location = (-313.228759765625, 279.9310607910156)
        Group_010.name = "Group.010"

        Emission = nt.nodes.new('ShaderNodeEmission')
        Emission.location = (418.5204162597656, -13.192481994628906)
        Emission.name = "Emission"

        Add_Shader = nt.nodes.new('ShaderNodeAddShader')
        Add_Shader.location = (644.9150390625, 83.19893646240234)
        Add_Shader.name = "Add Shader"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-461.08612060546875, -266.0368957519531)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-440.595703125, -287.8684997558594)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-416.90802001953125, -309.8193359375)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-387.371337890625, -332.50982666015625)
        Reroute_003.name = "Reroute.003"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-461.08612060546875, -151.65081787109375)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-461.08612060546875, 50.359310150146484)
        Reroute_005.name = "Reroute.005"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-440.595703125, -171.08148193359375)
        Reroute_006.name = "Reroute.006"

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (-440.595703125, 30.761253356933594)
        Reroute_007.name = "Reroute.007"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-416.90802001953125, -194.12335205078125)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-416.90802001953125, 7.00199031829834)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-387.371337890625, -216.81240844726562)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-461.08612060546875, -427.91943359375)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (-440.595703125, -449.4589538574219)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (-416.90802001953125, -472.3288879394531)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-387.371337890625, -494.3876647949219)
        Reroute_014.name = "Reroute.014"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (-387.371337890625, -14.748672485351562)
        Reroute_015.name = "Reroute.015"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (-516.3226318359375, -198.2943572998047)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (-516.3226318359375, 74.75299072265625)
        Reroute_017.name = "Reroute.017"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (-516.3226318359375, -383.21392822265625)
        Reroute_018.name = "Reroute.018"

        Mix_Shader_001 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_001.location = (418.5204162597656, 110.16600799560547)
        Mix_Shader_001.name = "Mix Shader.001"

        Transparent_BSDF = nt.nodes.new('ShaderNodeBsdfTransparent')
        Transparent_BSDF.location = (640.0816650390625, 184.20404052734375)
        Transparent_BSDF.name = "Transparent BSDF"

        Mix_Shader_002 = nt.nodes.new('ShaderNodeMixShader')
        Mix_Shader_002.location = (855.1224975585938, 186.701416015625)
        Mix_Shader_002.name = "Mix Shader.002"

        Group_001 = nt.nodes.new('ShaderNodeGroup')
        Group_001.location = (-313.228759765625, -304.36077880859375)
        Group_001.name = "Group.001"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (-366.1617126464844, -353.7314147949219)
        Reroute_019.name = "Reroute.019"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (-366.1617126464844, -239.83929443359375)
        Reroute_020.name = "Reroute.020"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (-366.1617126464844, -516.983642578125)
        Reroute_021.name = "Reroute.021"

        Map_Range = nt.nodes.new('ShaderNodeMapRange')
        Map_Range.location = (164.727783203125, 346.49560546875)
        Map_Range.name = "Map Range"

        Reroute_022 = nt.nodes.new('NodeReroute')
        Reroute_022.location = (-497.20660400390625, -220.6082000732422)
        Reroute_022.name = "Reroute.022"

        Reroute_023 = nt.nodes.new('NodeReroute')
        Reroute_023.location = (-497.20660400390625, -129.75897216796875)
        Reroute_023.name = "Reroute.023"

        Reroute_024 = nt.nodes.new('NodeReroute')
        Reroute_024.location = (-482.86956787109375, -242.9220428466797)
        Reroute_024.name = "Reroute.024"

        Reroute_025 = nt.nodes.new('NodeReroute')
        Reroute_025.location = (-482.86956787109375, -406.291259765625)
        Reroute_025.name = "Reroute.025"

        Reroute_026 = nt.nodes.new('NodeReroute')
        Reroute_026.location = (247.0649871826172, -339.34967041015625)
        Reroute_026.name = "Reroute.026"

        Reroute_027 = nt.nodes.new('NodeReroute')
        Reroute_027.location = (247.0649871826172, 4.1244049072265625)
        Reroute_027.name = "Reroute.027"

        Reroute_028 = nt.nodes.new('NodeReroute')
        Reroute_028.location = (247.0649871826172, 68.67523193359375)
        Reroute_028.name = "Reroute.028"

        Reroute_029 = nt.nodes.new('NodeReroute')
        Reroute_029.location = (247.0649871826172, 29.625961303710938)
        Reroute_029.name = "Reroute.029"

        # Create internal links
        nt.links.new(Emission.outputs[0], Add_Shader.inputs[1])
        nt.links.new(Group_008.outputs[0], Mix_Shader.inputs[1])
        nt.links.new(Group_009.outputs[0], Mix_Shader.inputs[2])
        nt.links.new(GroupInput.outputs[12], Group_010.inputs[1])
        nt.links.new(GroupInput.outputs[7], Group_010.inputs[0])
        nt.links.new(GroupInput.outputs[10], Emission.inputs[0])
        nt.links.new(GroupInput.outputs[11], Emission.inputs[1])
        nt.links.new(GroupInput.outputs[5], Reroute.inputs[0])
        nt.links.new(GroupInput.outputs[6], Reroute_001.inputs[0])
        nt.links.new(GroupInput.outputs[12], Reroute_003.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Group_008.inputs[1])
        nt.links.new(Reroute_001.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Group_009.inputs[2])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Group_008.inputs[2])
        nt.links.new(Reroute_002.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Group_009.inputs[3])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Group_008.inputs[3])
        nt.links.new(Reroute_003.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Group_009.inputs[4])
        nt.links.new(Reroute.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Reroute_014.inputs[0])
        nt.links.new(GroupInput.outputs[7], Reroute_002.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Group_008.inputs[4])
        nt.links.new(GroupInput.outputs[1], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Group_008.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Map_Range.outputs[0], Mix_Shader_001.inputs[0])
        nt.links.new(Mix_Shader_001.outputs[0], Add_Shader.inputs[0])
        nt.links.new(Transparent_BSDF.outputs[0], Mix_Shader_002.inputs[1])
        nt.links.new(Add_Shader.outputs[0], Mix_Shader_002.inputs[2])
        nt.links.new(GroupInput.outputs[9], Mix_Shader_002.inputs[0])
        nt.links.new(Mix_Shader_002.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Group_009.inputs[1])
        nt.links.new(Group_010.outputs[0], Mix_Shader.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Group_001.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Group_001.inputs[2])
        nt.links.new(Reroute_012.outputs[0], Group_001.inputs[3])
        nt.links.new(Reroute_013.outputs[0], Group_001.inputs[4])
        nt.links.new(Reroute_014.outputs[0], Group_001.inputs[5])
        nt.links.new(GroupInput.outputs[13], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Group_009.inputs[5])
        nt.links.new(Reroute_021.outputs[0], Group_001.inputs[6])
        nt.links.new(Reroute_019.outputs[0], Reroute_021.inputs[0])
        nt.links.new(GroupInput.outputs[8], Map_Range.inputs[0])
        nt.links.new(GroupInput.outputs[2], Reroute_022.inputs[0])
        nt.links.new(Reroute_022.outputs[0], Reroute_023.inputs[0])
        nt.links.new(Reroute_023.outputs[0], Group_009.inputs[0])
        nt.links.new(GroupInput.outputs[3], Reroute_024.inputs[0])
        nt.links.new(Reroute_024.outputs[0], Reroute_025.inputs[0])
        nt.links.new(Reroute_025.outputs[0], Group_001.inputs[1])
        nt.links.new(Group_001.outputs[0], Reroute_026.inputs[0])
        nt.links.new(Reroute_026.outputs[0], Reroute_027.inputs[0])
        nt.links.new(Reroute_027.outputs[0], Mix_Shader_001.inputs[2])
        nt.links.new(Mix_Shader.outputs[0], Reroute_028.inputs[0])
        nt.links.new(Reroute_028.outputs[0], Reroute_029.inputs[0])
        nt.links.new(Reroute_029.outputs[0], Mix_Shader_001.inputs[1])

        # Set default values
        Emission.inputs[2].default_value = 0.0
        Transparent_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Transparent_BSDF.inputs[1].default_value = 0.0
        Map_Range.inputs[1].default_value = 0.0
        Map_Range.inputs[2].default_value = 1.0
        Map_Range.inputs[3].default_value = 0.0
        Map_Range.inputs[4].default_value = 0.800000011920929
        Map_Range.inputs[5].default_value = 4.0
        Map_Range.inputs[6].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[7].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[8].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[9].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs[10].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs[11].default_value = (4.0, 4.0, 4.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
