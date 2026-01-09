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


class ShaderNodeStylized_Fresnel(ShaderNode):
    bl_idname = 'ShaderNodeStylized_Fresnel'
    bl_label = "Stylized Fresnel"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Roughness"].default_value = 0.0
        self.inputs["Normal"].default_value = (0.0, 0.0, 0.0)

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'ShaderNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'Stylized Fresnel'

        # Create output sockets
        nt.interface.new_socket('Fresnel', in_out='OUTPUT', socket_type='NodeSocketFloat')

        # Create input sockets
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
        Frame.location = (36.82098388671875, -101.02154541015625)
        Frame.label = "Use Flatten Normal to make \"Dead-On\""
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (4.189537048339844, 344.4308776855469)
        Frame_001.label = "Fresnel for backfacing"
        Frame_001.name = "Frame.001"

        Fresnel = nt.nodes.new('ShaderNodeFresnel')
        Fresnel.location = (516.5775146484375, 0.0)
        Fresnel.name = "Fresnel"

        Geometry_001 = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry_001.location = (-94.75682830810547, -270.8712158203125)
        Geometry_001.label = "Flatten Normal"
        Geometry_001.name = "Geometry.001"

        Bump = nt.nodes.new('ShaderNodeBump')
        Bump.location = (-92.44503021240234, -89.64186096191406)
        Bump.name = "Bump"

        Mix_001 = nt.nodes.new('ShaderNodeMix')
        Mix_001.location = (177.30618286132812, -47.9111328125)
        Mix_001.name = "Mix.001"
        Mix_001.blend_type = 'MIX'

        Geometry = nt.nodes.new('ShaderNodeNewGeometry')
        Geometry.location = (-57.642555236816406, -39.89361572265625)
        Geometry.name = "Geometry"

        Mix = nt.nodes.new('ShaderNodeMix')
        Mix.location = (179.46578979492188, -55.05224609375)
        Mix.name = "Mix"
        Mix.blend_type = 'MIX'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-17.78949546813965, -254.08999633789062)
        Math.label = "BackFace Fresnel"
        Math.name = "Math"
        Math.operation = 'DIVIDE'

        Value = nt.nodes.new('ShaderNodeValue')
        Value.location = (-512.1998901367188, 244.6036834716797)
        Value.name = "Value"

        # Create internal links
        nt.links.new(Fresnel.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Geometry.outputs[6], Mix.inputs[0])
        nt.links.new(Mix.outputs[2], Fresnel.inputs[0])
        nt.links.new(Bump.outputs[0], Mix_001.inputs[6])
        nt.links.new(Geometry_001.outputs[4], Mix_001.inputs[7])
        nt.links.new(GroupInput.outputs[0], Mix_001.inputs[0])
        nt.links.new(Mix_001.outputs[2], Fresnel.inputs[1])
        nt.links.new(Math.outputs[0], Mix.inputs[7])
        nt.links.new(Value.outputs[0], Mix.inputs[6])
        nt.links.new(Value.outputs[0], Math.inputs[1])
        nt.links.new(GroupInput.outputs[1], Bump.inputs[3])

        # Set default values
        Bump.inputs[0].default_value = 0.0
        Bump.inputs[1].default_value = 0.10000000149011612
        Bump.inputs[2].default_value = 1.0
        Mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs[2].default_value = 0.0
        Mix_001.inputs[3].default_value = 0.0
        Mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix_001.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        Mix.inputs[2].default_value = 0.0
        Mix.inputs[3].default_value = 0.0
        Mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        Mix.inputs[8].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Mix.inputs[9].default_value = Euler((0.0, 0.0, 0.0), 'XYZ')
        Math.inputs[0].default_value = 1.0
        Math.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
