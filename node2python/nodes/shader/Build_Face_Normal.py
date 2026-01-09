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


class ShaderNodeBuild_Face_Normal(ShaderNode):
    bl_idname = 'ShaderNodeBuild_Face_Normal'
    bl_label = "Build Face Normal"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Face Value"].default_value = 0.5
        self.inputs["Face Map"].default_value = 0.5
        self.inputs["Face To X"].default_value = False
        self.inputs["Face To Y"].default_value = False

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Build Face Normal'

        # Create output sockets
        nt.interface.new_socket('Normal', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Face Value', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Face Map', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.5
        input_socket = nt.interface.new_socket('Face To X', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        input_socket = nt.interface.new_socket('Face To Y', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False

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

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-209.134521484375, -46.846229553222656)
        Math.name = "Math"
        Math.operation = 'GREATER_THAN'

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (-246.9525146484375, -70.42658996582031)
        Reroute_006.name = "Reroute.006"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-246.9525146484375, -48.3992919921875)
        Reroute_003.name = "Reroute.003"

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (704.9998168945312, 4.611240386962891)
        Combine_XYZ.name = "Combine XYZ"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (518.7147827148438, -111.54592895507812)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (520.7042846679688, 67.40652465820312)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (134.796630859375, 173.7809295654297)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (134.796630859375, -8.746414184570312)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'MIX'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-37.6383056640625, -57.37171173095703)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-37.6383056640625, 65.1427001953125)
        Reroute_001.name = "Reroute.001"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-37.6383056640625, -118.19062042236328)
        Reroute_002.name = "Reroute.002"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-213.8873291015625, -91.64509582519531)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-246.8050537109375, -113.26799774169922)
        Reroute_005.name = "Reroute.005"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (-213.8873291015625, -239.9164276123047)
        Reroute_008.name = "Reroute.008"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (-246.8050537109375, -261.5393371582031)
        Reroute_009.name = "Reroute.009"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (423.4469299316406, -239.9164276123047)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (441.6839904785156, -261.5393371582031)
        Reroute_011.name = "Reroute.011"

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (423.4469299316406, -41.1976318359375)
        Reroute_012.name = "Reroute.012"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (441.6839904785156, -221.3079071044922)
        Reroute_013.name = "Reroute.013"

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (-186.6171112060547, 452.4814453125)
        Reroute_014.name = "Reroute.014"

        # Create internal links
        nt.links.new(Reroute_006.outputs[0], Math.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[1], Reroute_006.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Math.inputs[1])
        nt.links.new(GroupInput.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Mix_001.outputs[0], Combine_XYZ.inputs[0])
        nt.links.new(Mix.outputs[0], Combine_XYZ.inputs[1])
        nt.links.new(Mix_002.outputs[0], Mix_001.inputs[2])
        nt.links.new(Mix_003.outputs[0], Mix_001.inputs[3])
        nt.links.new(Mix_002.outputs[0], Mix.inputs[2])
        nt.links.new(Mix_003.outputs[0], Mix.inputs[3])
        nt.links.new(Math.outputs[0], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Mix_002.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Mix_003.inputs[0])
        nt.links.new(GroupInput.outputs[2], Reroute_004.inputs[0])
        nt.links.new(GroupInput.outputs[3], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_010.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_010.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Mix.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Mix_001.inputs[0])

        # Set default values
        Math.inputs[2].default_value = 0.5
        Combine_XYZ.inputs[2].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = -1.0
        Mix_002.inputs[3].default_value = 1.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 1.0
        Mix_003.inputs[3].default_value = -1.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Reroute_014.inputs[0].default_value = 0.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
