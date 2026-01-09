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


class ShaderNodeSST1__Pores(ShaderNode):
    bl_idname = 'ShaderNodeSST1__Pores'
    bl_label = "SST1: Pores"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Factor"].default_value = 0.0
        self.inputs["Scale"].default_value = 1.5
        self.inputs["UV"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'SST1: Pores'

        # Create output sockets
        nt.interface.new_socket('Pores', in_out='OUTPUT', socket_type='NodeSocketColor')
        nt.interface.new_socket('UV', in_out='OUTPUT', socket_type='NodeSocketVector')

        # Create input sockets
        input_socket = nt.interface.new_socket('Factor', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Scale', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.5
        input_socket = nt.interface.new_socket('UV', in_out='INPUT', socket_type='NodeSocketVector')
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

        Voronoi_Texture_001 = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture_001.location = (-68.9775390625, 171.57217407226562)
        Voronoi_Texture_001.name = "Voronoi Texture.001"

        ColorRamp_001 = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp_001.location = (150.834228515625, 209.84768676757812)
        ColorRamp_001.name = "ColorRamp.001"

        Mapping = nt.nodes.new('ShaderNodeMapping')
        Mapping.location = (-290.802490234375, -209.84765625)
        Mapping.name = "Mapping"

        Mapping_002 = nt.nodes.new('ShaderNodeMapping')
        Mapping_002.location = (-295.344482421875, 169.09503173828125)
        Mapping_002.name = "Mapping.002"

        ColorRamp = nt.nodes.new('ShaderNodeValToRGB')
        ColorRamp.location = (155.376220703125, -169.0950927734375)
        ColorRamp.name = "ColorRamp"

        Voronoi_Texture = nt.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_Texture.location = (-64.435546875, -207.37060546875)
        Voronoi_Texture.name = "Voronoi Texture"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (475.344482421875, 15.2484130859375)
        Mix.name = "Mix"
        Mix.blend_type = 'MULTIPLY'

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (849.596923828125, 142.86874389648438)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Combine_XYZ = nt.nodes.new('ShaderNodeCombineXYZ')
        Combine_XYZ.location = (-643.5103759765625, -309.8591613769531)
        Combine_XYZ.name = "Combine XYZ"

        # Create internal links
        nt.links.new(Mapping.outputs[0], Voronoi_Texture.inputs[0])
        nt.links.new(Voronoi_Texture.outputs[0], ColorRamp.inputs[0])
        nt.links.new(Mapping_002.outputs[0], Voronoi_Texture_001.inputs[0])
        nt.links.new(Voronoi_Texture_001.outputs[0], ColorRamp_001.inputs[0])
        nt.links.new(ColorRamp.outputs[0], Mix.inputs[6])
        nt.links.new(ColorRamp_001.outputs[0], Mix.inputs[7])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[2])
        nt.links.new(Mix.outputs[2], Mix_001.inputs[7])
        nt.links.new(Mix_001.outputs[2], GroupOutput.inputs[0])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])
        nt.links.new(GroupInput.outputs[1], Combine_XYZ.inputs[0])
        nt.links.new(Combine_XYZ.outputs[0], Mapping.inputs[3])
        nt.links.new(Combine_XYZ.outputs[0], Mapping_002.inputs[3])
        nt.links.new(GroupInput.outputs[1], Combine_XYZ.inputs[1])
        nt.links.new(GroupInput.outputs[1], Combine_XYZ.inputs[2])
        nt.links.new(GroupInput.outputs[2], Mapping_002.inputs[0])
        nt.links.new(GroupInput.outputs[2], Mapping.inputs[0])
        nt.links.new(GroupInput.outputs[2], GroupOutput.inputs[1])

        # Set default values
        Voronoi_Texture_001.inputs[1].default_value = 0.0
        Voronoi_Texture_001.inputs[2].default_value = 800.0
        Voronoi_Texture_001.inputs[3].default_value = 0.0
        Voronoi_Texture_001.inputs[4].default_value = 0.5
        Voronoi_Texture_001.inputs[5].default_value = 2.0
        Voronoi_Texture_001.inputs[6].default_value = 1.0
        Voronoi_Texture_001.inputs[7].default_value = 0.5
        Voronoi_Texture_001.inputs[8].default_value = 0.6000000238418579
        Mapping.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping.inputs[2].default_value = Euler((0.0, 0.0, 1.5707963705062866), 'XYZ')
        Mapping_002.inputs[1].default_value = Vector((0.0, 0.0, 0.0))
        Mapping_002.inputs[2].default_value = Euler((0.0, 0.0, 0.7853981852531433), 'XYZ')
        Voronoi_Texture.inputs[1].default_value = 0.0
        Voronoi_Texture.inputs[2].default_value = 1000.0
        Voronoi_Texture.inputs[3].default_value = 0.0
        Voronoi_Texture.inputs[4].default_value = 0.5
        Voronoi_Texture.inputs[5].default_value = 2.0
        Voronoi_Texture.inputs[6].default_value = 1.0
        Voronoi_Texture.inputs[7].default_value = 0.5
        Voronoi_Texture.inputs[8].default_value = 0.6000000238418579
        Mix.inputs[0].default_value = 1.0
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
