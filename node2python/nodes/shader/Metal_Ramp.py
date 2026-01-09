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


class ShaderNodeMetal_Ramp(ShaderNode):
    bl_idname = 'ShaderNodeMetal_Ramp'
    bl_label = "Metal Ramp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Mix 1"].default_value = 0.699999988079071
        self.inputs["Mix 2"].default_value = 0.8500000238418579
        self.inputs["Mix 3"].default_value = 0.949999988079071
        self.inputs["Lv 1"].default_value = (0.0, 0.0, 0.0, 1.0)
        self.inputs["Lv 2"].default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        self.inputs["Lv 3"].default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        self.inputs["Lv 4"].default_value = (1.0, 1.0, 1.0, 1.0)
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Metal Ramp'

        # Create output sockets
        nt.interface.new_socket('Custom Ramp', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets
        input_socket = nt.interface.new_socket('Mix 1', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.699999988079071
        input_socket = nt.interface.new_socket('Mix 2', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.8500000238418579
        input_socket = nt.interface.new_socket('Mix 3', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.949999988079071
        input_socket = nt.interface.new_socket('Lv 1', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        input_socket = nt.interface.new_socket('Lv 2', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.024790925905108452, 0.024790925905108452, 0.024790925905108452, 1.0)
        input_socket = nt.interface.new_socket('Lv 3', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (0.12354078888893127, 0.12354078888893127, 0.12354078888893127, 1.0)
        input_socket = nt.interface.new_socket('Lv 4', in_out='INPUT', socket_type='NodeSocketColor')
        input_socket.default_value = (1.0, 1.0, 1.0, 1.0)
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

        Fresnel_002 = nt.nodes.new('ShaderNodeFresnel')
        Fresnel_002.location = (-461.76947021484375, 245.672607421875)
        Fresnel_002.name = "Fresnel.002"

        Invert_002 = nt.nodes.new('ShaderNodeInvert')
        Invert_002.location = (-193.48995971679688, 245.672607421875)
        Invert_002.name = "Invert.002"

        Fresnel = nt.nodes.new('ShaderNodeFresnel')
        Fresnel.location = (-461.76947021484375, 114.10456085205078)
        Fresnel.name = "Fresnel"

        Fresnel_001 = nt.nodes.new('ShaderNodeFresnel')
        Fresnel_001.location = (-461.76947021484375, -23.183719635009766)
        Fresnel_001.name = "Fresnel.001"

        Invert_001 = nt.nodes.new('ShaderNodeInvert')
        Invert_001.location = (-193.48995971679688, -23.183719635009766)
        Invert_001.name = "Invert.001"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-164.82608032226562, -428.1614990234375)
        Reroute_001.name = "Reroute.001"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (-220.14512634277344, -452.1034851074219)
        Reroute_003.name = "Reroute.003"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (-220.14512634277344, -202.2088623046875)
        Reroute_002.name = "Reroute.002"

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-164.82608032226562, -178.26687622070312)
        Reroute.name = "Reroute"

        Reroute_006 = nt.nodes.new('NodeReroute')
        Reroute_006.location = (430.79327392578125, -480.0089416503906)
        Reroute_006.name = "Reroute.006"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (100.58926391601562, -244.45497131347656)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Reroute_007 = nt.nodes.new('NodeReroute')
        Reroute_007.location = (430.79327392578125, -145.89508056640625)
        Reroute_007.name = "Reroute.007"

        Reroute_009 = nt.nodes.new('NodeReroute')
        Reroute_009.location = (306.046875, -123.35232543945312)
        Reroute_009.name = "Reroute.009"

        Reroute_008 = nt.nodes.new('NodeReroute')
        Reroute_008.location = (306.046875, -278.5502624511719)
        Reroute_008.name = "Reroute.008"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-262.6143798828125, -227.64724731445312)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-262.6143798828125, -480.0089416503906)
        Reroute_005.name = "Reroute.005"

        Reroute_010 = nt.nodes.new('NodeReroute')
        Reroute_010.location = (-326.5131530761719, -252.51780700683594)
        Reroute_010.name = "Reroute.010"

        Reroute_011 = nt.nodes.new('NodeReroute')
        Reroute_011.location = (-326.5131530761719, -510.520751953125)
        Reroute_011.name = "Reroute.011"

        Mix_002 = nt.nodes.new('ShaderNodeMix')
        Mix_002.location = (837.5003662109375, 294.5899353027344)
        Mix_002.name = "Mix.002"
        Mix_002.blend_type = 'MIX'

        Reroute_012 = nt.nodes.new('NodeReroute')
        Reroute_012.location = (791.1217651367188, -510.520751953125)
        Reroute_012.name = "Reroute.012"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (475.93182373046875, 63.14665603637695)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Reroute_014 = nt.nodes.new('NodeReroute')
        Reroute_014.location = (694.1414794921875, 30.568992614746094)
        Reroute_014.name = "Reroute.014"

        Reroute_016 = nt.nodes.new('NodeReroute')
        Reroute_016.location = (753.3070678710938, 211.0162353515625)
        Reroute_016.name = "Reroute.016"

        Reroute_017 = nt.nodes.new('NodeReroute')
        Reroute_017.location = (753.3070678710938, 130.48287963867188)
        Reroute_017.name = "Reroute.017"

        Reroute_015 = nt.nodes.new('NodeReroute')
        Reroute_015.location = (694.1414794921875, 106.79657745361328)
        Reroute_015.name = "Reroute.015"

        Reroute_013 = nt.nodes.new('NodeReroute')
        Reroute_013.location = (791.1217651367188, 86.37303161621094)
        Reroute_013.name = "Reroute.013"

        Invert = nt.nodes.new('ShaderNodeInvert')
        Invert.location = (-193.48995971679688, 114.10456085205078)
        Invert.name = "Invert"

        Reroute_018 = nt.nodes.new('NodeReroute')
        Reroute_018.location = (395.89544677734375, 79.26713562011719)
        Reroute_018.name = "Reroute.018"

        Reroute_019 = nt.nodes.new('NodeReroute')
        Reroute_019.location = (395.89544677734375, -99.5643081665039)
        Reroute_019.name = "Reroute.019"

        Reroute_020 = nt.nodes.new('NodeReroute')
        Reroute_020.location = (31.915973663330078, -57.867332458496094)
        Reroute_020.name = "Reroute.020"

        Reroute_021 = nt.nodes.new('NodeReroute')
        Reroute_021.location = (31.915973663330078, -408.4244384765625)
        Reroute_021.name = "Reroute.021"

        Frame_003 = nt.nodes.new('NodeFrame')
        Frame_003.location = (301.65924072265625, 376.25958251953125)
        Frame_003.label = "Changed to \"Metal Ramp\""
        Frame_003.name = "Frame.003"

        # Create internal links
        nt.links.new(Fresnel.outputs[0], Invert.inputs[1])
        nt.links.new(Fresnel_001.outputs[0], Invert_001.inputs[1])
        nt.links.new(Fresnel_002.outputs[0], Invert_002.inputs[1])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Mix_001.inputs[6])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Mix_001.inputs[7])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Reroute_006.inputs[0])
        nt.links.new(Reroute_006.outputs[0], Reroute_007.inputs[0])
        nt.links.new(Reroute_007.outputs[0], Mix.inputs[7])
        nt.links.new(Mix_001.outputs[2], Reroute_008.inputs[0])
        nt.links.new(Reroute_008.outputs[0], Reroute_009.inputs[0])
        nt.links.new(Reroute_009.outputs[0], Mix.inputs[6])
        nt.links.new(Reroute_010.outputs[0], Reroute_011.inputs[0])
        nt.links.new(Reroute_011.outputs[0], Reroute_012.inputs[0])
        nt.links.new(Reroute_012.outputs[0], Reroute_013.inputs[0])
        nt.links.new(Reroute_013.outputs[0], Mix_002.inputs[7])
        nt.links.new(Mix.outputs[2], Reroute_014.inputs[0])
        nt.links.new(Reroute_014.outputs[0], Reroute_015.inputs[0])
        nt.links.new(Reroute_015.outputs[0], Mix_002.inputs[6])
        nt.links.new(Invert_002.outputs[0], Reroute_016.inputs[0])
        nt.links.new(Reroute_016.outputs[0], Reroute_017.inputs[0])
        nt.links.new(Reroute_017.outputs[0], Mix_002.inputs[0])
        nt.links.new(Invert.outputs[0], Reroute_018.inputs[0])
        nt.links.new(Reroute_018.outputs[0], Reroute_019.inputs[0])
        nt.links.new(Reroute_019.outputs[0], Mix.inputs[0])
        nt.links.new(Invert_001.outputs[0], Reroute_020.inputs[0])
        nt.links.new(Reroute_020.outputs[0], Reroute_021.inputs[0])
        nt.links.new(Reroute_021.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Fresnel_002.inputs[0])
        nt.links.new(GroupInput.outputs[1], Fresnel.inputs[0])
        nt.links.new(GroupInput.outputs[2], Fresnel_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Reroute.inputs[0])
        nt.links.new(GroupInput.outputs[4], Reroute_002.inputs[0])
        nt.links.new(GroupInput.outputs[5], Reroute_004.inputs[0])
        nt.links.new(GroupInput.outputs[6], Reroute_010.inputs[0])
        nt.links.new(Mix_002.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[7], Fresnel_002.inputs[1])
        nt.links.new(GroupInput.outputs[7], Fresnel.inputs[1])
        nt.links.new(GroupInput.outputs[7], Fresnel_001.inputs[1])

        # Set default values
        Invert_002.inputs[0].default_value = 1.0
        Invert_001.inputs[0].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs[2].default_value = 0.0
        Mix_002.inputs[3].default_value = 0.0
        Mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_002.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Invert.inputs[0].default_value = 1.0

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
