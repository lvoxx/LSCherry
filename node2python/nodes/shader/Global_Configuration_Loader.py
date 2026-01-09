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


class ShaderNodeGlobal_Configuration_Loader(ShaderNode):
    bl_idname = 'ShaderNodeGlobal_Configuration_Loader'
    bl_label = "Global Configuration Loader"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Global Configuration Loader'

        # Create output sockets
        nt.interface.new_socket('Disable Enviroment', in_out='OUTPUT', socket_type='NodeSocketBool')
        nt.interface.new_socket('Value Enhance', in_out='OUTPUT', socket_type='NodeSocketFloat')
        nt.interface.new_socket('World Color', in_out='OUTPUT', socket_type='NodeSocketColor')

        # Create input sockets

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

        Attribute_004 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_004.location = (23.569393157958984, -151.2821044921875)
        Attribute_004.label = "Value Enhance"
        Attribute_004.name = "Attribute.004"

        Attribute_005 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_005.location = (-258.4073791503906, -292.8736572265625)
        Attribute_005.label = "World Color"
        Attribute_005.name = "Attribute.005"

        Group = nt.nodes.new('ShaderNodeGroup')
        Group.location = (-427.8304138183594, -276.7200927734375)
        Group.name = "Group"

        Mix_003 = nt.nodes.new('ShaderNodeMix')
        Mix_003.location = (-253.23985290527344, -253.39212036132812)
        Mix_003.name = "Mix.003"
        Mix_003.blend_type = 'ADD'

        Attribute_006 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_006.location = (-430.35443115234375, -239.7515869140625)
        Attribute_006.label = "World Value Enhance"
        Attribute_006.name = "Attribute.006"

        Mix_007 = nt.nodes.new('ShaderNodeMix')
        Mix_007.location = (24.552425384521484, -244.3995361328125)
        Mix_007.name = "Mix.007"
        Mix_007.blend_type = 'MIX'

        Attribute_008 = nt.nodes.new('ShaderNodeAttribute')
        Attribute_008.location = (-844.7965087890625, -123.70796203613281)
        Attribute_008.label = "Blend Mode"
        Attribute_008.name = "Attribute.008"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-608.106201171875, -168.08091735839844)
        Math.label = "Light Sources"
        Math.name = "Math"
        Math.operation = 'COMPARE'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-608.324462890625, -129.7677459716797)
        Math_001.label = "Background"
        Math_001.name = "Math.001"
        Math_001.operation = 'COMPARE'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-608.106201171875, -92.42906188964844)
        Math_002.label = "None"
        Math_002.name = "Math.002"
        Math_002.operation = 'COMPARE'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-268.3663024902344, -94.06651306152344)
        Math_003.name = "Math.003"
        Math_003.operation = 'SUBTRACT'

        # Create internal links
        nt.links.new(Mix_007.outputs[2], GroupOutput.inputs[2])
        nt.links.new(Attribute_004.outputs[2], GroupOutput.inputs[1])
        nt.links.new(Attribute_006.outputs[2], Mix_003.inputs[0])
        nt.links.new(Attribute_008.outputs[2], Math.inputs[0])
        nt.links.new(Attribute_008.outputs[2], Math_002.inputs[0])
        nt.links.new(Attribute_008.outputs[2], Math_001.inputs[0])
        nt.links.new(Math.outputs[0], Math_003.inputs[1])
        nt.links.new(Math_003.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Math_002.outputs[0], Mix_007.inputs[0])
        nt.links.new(Mix_003.outputs[2], Mix_007.inputs[6])
        nt.links.new(Attribute_005.outputs[0], Mix_007.inputs[7])
        nt.links.new(Group.outputs[1], Mix_003.inputs[6])

        # Set default values
        Mix_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs[2].default_value = 0.0
        Mix_003.inputs[3].default_value = 0.0
        Mix_003.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        Mix_003.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_003.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_007.inputs[2].default_value = 0.0
        Mix_007.inputs[3].default_value = 0.0
        Mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_007.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_007.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[1].default_value = 1.0
        Math.inputs[2].default_value = 0.0
        Math_001.inputs[1].default_value = 2.0
        Math_001.inputs[2].default_value = 0.0
        Math_002.inputs[1].default_value = 3.0
        Math_002.inputs[2].default_value = 0.0
        Math_003.inputs[0].default_value = 1.0
        Math_003.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
