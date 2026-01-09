import bpy
import sys
from pathlib import Path

# Import utils (handle both relative and absolute imports)
try:
    from ..utils import GeometryNode
except ImportError:
    # Fallback for direct execution
    import importlib.util
    utils_path = Path(__file__).parent.parent / 'utils.py'
    spec = importlib.util.spec_from_file_location('utils', utils_path)
    utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utils)
    GeometryNode = utils.GeometryNode


class GeometryNodeLS_Outline_And_ShrinkWarp(GeometryNode):
    bl_idname = 'GeometryNodeLS_Outline_And_ShrinkWarp'
    bl_label = "LS Outline And ShrinkWarp"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Ratio"].default_value = 1.2000000476837158
        self.inputs["Affected Vertex"].default_value = False
        self.inputs["Strength"].default_value = 1.0

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'GeometryNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'LS Outline And ShrinkWarp'

        # Create output sockets
        nt.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')

        # Create input sockets
        nt.interface.new_socket('Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
        nt.interface.new_socket('Outlined Material', in_out='INPUT', socket_type='NodeSocketMaterial')
        input_socket = nt.interface.new_socket('Ratio', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.2000000476837158
        input_socket = nt.interface.new_socket('Affected Vertex', in_out='INPUT', socket_type='NodeSocketBool')
        input_socket.default_value = False
        nt.interface.new_socket('Shrink To', in_out='INPUT', socket_type='NodeSocketObject')
        input_socket = nt.interface.new_socket('Strength', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.0

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

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-860.4244995117188, -282.4170227050781)
        Frame_001.label = "Make Object Extend alone with normal"
        Frame_001.name = "Frame.001"

        Set_Material = nt.nodes.new('GeometryNodeSetMaterial')
        Set_Material.location = (-238.66311645507812, -106.72352600097656)
        Set_Material.name = "Set Material"

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-837.0912475585938, -128.90017700195312)
        Math_002.label = "Invert"
        Math_002.name = "Math.002"
        Math_002.operation = 'SUBTRACT'

        Set_Position = nt.nodes.new('GeometryNodeSetPosition')
        Set_Position.location = (-448.4311218261719, -68.22897338867188)
        Set_Position.name = "Set Position"

        Flip_Faces = nt.nodes.new('GeometryNodeFlipFaces')
        Flip_Faces.location = (-14.683799743652344, -80.92935180664062)
        Flip_Faces.name = "Flip Faces"

        Join_Geometry = nt.nodes.new('GeometryNodeJoinGeometry')
        Join_Geometry.location = (169.6592254638672, 20.218700408935547)
        Join_Geometry.name = "Join Geometry"

        Normal = nt.nodes.new('GeometryNodeInputNormal')
        Normal.location = (-111.53131103515625, -84.91717529296875)
        Normal.name = "Normal"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (91.91107177734375, 28.883590698242188)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'SCALE'

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (-109.2884521484375, 74.62899780273438)
        Math.name = "Math"
        Math.operation = 'DIVIDE'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-608.0664672851562, -19.050201416015625)
        Reroute.name = "Reroute"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (11.403121948242188, -19.050201416015625)
        Reroute_001.name = "Reroute.001"

        Object_Info = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info.location = (-172.16259765625, 30.95238494873047)
        Object_Info.name = "Object Info"

        Frame_002 = nt.nodes.new('NodeFrame')
        Frame_002.location = (-1728.82421875, -119.26325988769531)
        Frame_002.label = "Shrinkwarp"
        Frame_002.name = "Frame.002"

        Geometry_Proximity = nt.nodes.new('GeometryNodeProximity')
        Geometry_Proximity.location = (2.26220703125, 33.50927734375)
        Geometry_Proximity.name = "Geometry Proximity"

        Set_Position_001 = nt.nodes.new('GeometryNodeSetPosition')
        Set_Position_001.location = (337.6585693359375, 145.0020751953125)
        Set_Position_001.name = "Set Position.001"

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (184.0706787109375, -20.819442749023438)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'MULTIPLY'

        Vector_Math_002 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_002.location = (-4.01123046875, -80.59571838378906)
        Vector_Math_002.name = "Vector Math.002"
        Vector_Math_002.operation = 'SCALE'

        Normal_001 = nt.nodes.new('GeometryNodeInputNormal')
        Normal_001.location = (-172.16259765625, -90.36174011230469)
        Normal_001.name = "Normal.001"

        # Create internal links
        nt.links.new(Join_Geometry.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Set_Position.outputs[0], Set_Material.inputs[0])
        nt.links.new(Set_Material.outputs[0], Flip_Faces.inputs[0])
        nt.links.new(Flip_Faces.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(Normal.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Set_Position.inputs[3])
        nt.links.new(Math_002.outputs[0], Set_Position.inputs[1])
        nt.links.new(GroupInput.outputs[1], Set_Material.inputs[2])
        nt.links.new(GroupInput.outputs[2], Math.inputs[0])
        nt.links.new(Math.outputs[0], Vector_Math.inputs[3])
        nt.links.new(Reroute.outputs[0], Set_Position.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(GroupInput.outputs[3], Math_002.inputs[1])
        nt.links.new(Object_Info.outputs[4], Geometry_Proximity.inputs[0])
        nt.links.new(Geometry_Proximity.outputs[0], Set_Position_001.inputs[2])
        nt.links.new(GroupInput.outputs[0], Set_Position_001.inputs[0])
        nt.links.new(Set_Position_001.outputs[0], Reroute.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], Set_Position_001.inputs[3])
        nt.links.new(Vector_Math_002.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Normal_001.outputs[0], Vector_Math_002.inputs[0])
        nt.links.new(GroupInput.outputs[4], Object_Info.inputs[0])
        nt.links.new(GroupInput.outputs[5], Vector_Math_002.inputs[3])
        nt.links.new(Math_002.outputs[0], Set_Material.inputs[1])
        nt.links.new(Math_002.outputs[0], Flip_Faces.inputs[1])

        # Set default values
        Math_002.inputs[0].default_value = 1.0
        Math_002.inputs[2].default_value = 0.5
        Set_Position.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Math.inputs[1].default_value = 1000.0
        Math.inputs[2].default_value = 0.5
        Object_Info.inputs[1].default_value = False
        Geometry_Proximity.inputs[1].default_value = 0
        Geometry_Proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
        Geometry_Proximity.inputs[3].default_value = 0
        Set_Position_001.inputs[1].default_value = True
        Vector_Math_001.inputs[1].default_value = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Vector_Math_002.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
