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


class ShaderNodeToon_Core(ShaderNode):
    bl_idname = 'ShaderNodeToon_Core'
    bl_label = "Toon Core"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["AO Fac"].default_value = 1.0
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Toon Core'

        # Create output sockets
        nt.interface.new_socket('Toon', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('AO Fac', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0
        input_socket = nt.interface.new_socket('Roughness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Normal', in_out='INPUT', socket_type='NodeSocketVector')
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

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (138.1495361328125, 102.3504638671875)
        Frame.label = "Diffuse"
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (60.67625427246094, -398.3809814453125)
        Frame_001.label = "AO"
        Frame_001.name = "Frame.001"

        Diffuse_BSDF = nt.nodes.new('ShaderNodeBsdfDiffuse')
        Diffuse_BSDF.location = (-199.08876037597656, -44.15856170654297)
        Diffuse_BSDF.name = "Diffuse BSDF"

        Shader_to_RGB = nt.nodes.new('ShaderNodeShaderToRGB')
        Shader_to_RGB.location = (-5.5664825439453125, -50.39952850341797)
        Shader_to_RGB.name = "Shader to RGB"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-321.73590087890625, -480.62371826171875)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (277.157958984375, -480.62371826171875)
        Reroute_002.name = "Reroute.002"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-321.7359313964844, 2.2898635864257812)
        Reroute.name = "Reroute"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-366.1334228515625, -354.88592529296875)
        Reroute_005.name = "Reroute.005"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (507.2261657714844, 100.90921020507812)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'DARKEN'

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-366.1334228515625, -42.12685012817383)
        Reroute_004.name = "Reroute.004"

        Ambient_Occlusion = nt.nodes.new('ShaderNodeAmbientOcclusion')
        Ambient_Occlusion.location = (-225.97164916992188, 248.52731323242188)
        Ambient_Occlusion.name = "Ambient Occlusion"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (-45.820945739746094, 242.20018005371094)
        ColorRamp.name = "ColorRamp"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (251.40228271484375, 225.54747009277344)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (216.48170471191406, 61.402801513671875)
        Reroute_003.name = "Reroute.003"

        # Create internal links
        nt.links.new(Diffuse_BSDF.outputs[0], Shader_to_RGB.inputs[0])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(Ambient_Occlusion.outputs[0], ColorRamp.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix.inputs[7])
        nt.links.new(Shader_to_RGB.outputs[0], Mix_001.inputs[6])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[1], Diffuse_BSDF.inputs[1])
        nt.links.new(GroupInput.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Diffuse_BSDF.inputs[2])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Ambient_Occlusion.inputs[2])
        nt.links.new(GroupInput.outputs[2], Reroute_004.inputs[0])

        # Set default values
        Diffuse_BSDF.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Diffuse_BSDF.inputs[3].default_value = 0.0
        Mix_001.inputs[0].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Ambient_Occlusion.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        Ambient_Occlusion.inputs[1].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
