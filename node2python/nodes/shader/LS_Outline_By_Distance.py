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


class GeometryNodeLS_Outline_By_Distance(GeometryNode):
    bl_idname = 'GeometryNodeLS_Outline_By_Distance'
    bl_label = "LS Outline By Distance"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Ratio"].default_value = 0.0
        self.inputs["Max Outline Thickness"].default_value = 0.019999999552965164
        self.inputs["Affected Vertex"].default_value = False

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'GeometryNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'LS Outline By Distance'

        # Create output sockets
        nt.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')

        # Create input sockets
        nt.interface.new_socket('Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
        nt.interface.new_socket('Camera', in_out='INPUT', socket_type='NodeSocketObject')
        nt.interface.new_socket('Outlined Material', in_out='INPUT', socket_type='NodeSocketMaterial')
        input_socket = nt.interface.new_socket('Ratio', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.0
        input_socket = nt.interface.new_socket('Max Outline Thickness', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 0.019999999552965164
        input_socket = nt.interface.new_socket('Affected Vertex', in_out='INPUT', socket_type='NodeSocketBool')
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

        Frame = nt.nodes.new('NodeFrame')
        Frame.location = (-1648.00537109375, -79.04597473144531)
        Frame.label = "Make Thickness Between Camera and object"
        Frame.name = "Frame"

        Frame_001 = nt.nodes.new('NodeFrame')
        Frame_001.location = (-846.3800048828125, -256.55792236328125)
        Frame_001.label = "Make Object Extend alone with normal"
        Frame_001.name = "Frame.001"

        Set_Material = nt.nodes.new('GeometryNodeSetMaterial')
        Set_Material.location = (-238.66311645507812, -106.72352600097656)
        Set_Material.name = "Set Material"

        Reroute_002 = nt.nodes.new('NodeReroute')
        Reroute_002.location = (295.6165771484375, -395.34124755859375)
        Reroute_002.name = "Reroute.002"

        Reroute_003 = nt.nodes.new('NodeReroute')
        Reroute_003.location = (295.6165771484375, -204.86428833007812)
        Reroute_003.name = "Reroute.003"

        Reroute_001 = nt.nodes.new('NodeReroute')
        Reroute_001.location = (-511.20068359375, -395.34124755859375)
        Reroute_001.name = "Reroute.001"

        Position = nt.nodes.new('GeometryNodeInputPosition')
        Position.location = (-431.945068359375, -124.85385131835938)
        Position.name = "Position"

        Object_Info = nt.nodes.new('GeometryNodeObjectInfo')
        Object_Info.location = (-431.945068359375, -182.7223663330078)
        Object_Info.name = "Object Info"

        Math = nt.nodes.new('ShaderNodeMath')
        Math.location = (426.227294921875, -74.77542114257812)
        Math.name = "Math"
        Math.operation = 'MAXIMUM'

        Normal = nt.nodes.new('GeometryNodeInputNormal')
        Normal.location = (-111.53131103515625, -84.91717529296875)
        Normal.name = "Normal"

        Vector_Math = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math.location = (91.91107177734375, 28.883590698242188)
        Vector_Math.name = "Vector Math"
        Vector_Math.operation = 'SCALE'

        Math_002 = nt.nodes.new('ShaderNodeMath')
        Math_002.location = (-837.0912475585938, -128.90017700195312)
        Math_002.label = "Invert"
        Math_002.name = "Math.002"
        Math_002.operation = 'SUBTRACT'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-15.0728759765625, -97.79779052734375)
        Math_001.name = "Math.001"
        Math_001.operation = 'MULTIPLY'

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (-239.056640625, -105.02786254882812)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'DISTANCE'

        Reroute = nt.nodes.new('NodeReroute')
        Reroute.location = (-511.20068359375, -291.2296447753906)
        Reroute.name = "Reroute"

        Reroute_004 = nt.nodes.new('NodeReroute')
        Reroute_004.location = (-75.1748046875, -311.9986572265625)
        Reroute_004.name = "Reroute.004"

        Reroute_005 = nt.nodes.new('NodeReroute')
        Reroute_005.location = (-75.1748046875, -230.07603454589844)
        Reroute_005.name = "Reroute.005"

        Set_Position = nt.nodes.new('GeometryNodeSetPosition')
        Set_Position.location = (-448.4311218261719, -68.22897338867188)
        Set_Position.name = "Set Position"

        Flip_Faces = nt.nodes.new('GeometryNodeFlipFaces')
        Flip_Faces.location = (-14.683799743652344, -80.92935180664062)
        Flip_Faces.name = "Flip Faces"

        Join_Geometry = nt.nodes.new('GeometryNodeJoinGeometry')
        Join_Geometry.location = (360.168212890625, 20.218700408935547)
        Join_Geometry.name = "Join Geometry"

        # Create internal links
        nt.links.new(Join_Geometry.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Set_Position.outputs[0], Set_Material.inputs[0])
        nt.links.new(GroupInput.outputs[0], Set_Position.inputs[0])
        nt.links.new(Set_Material.outputs[0], Flip_Faces.inputs[0])
        nt.links.new(GroupInput.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(Flip_Faces.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(Normal.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Position.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Object_Info.outputs[1], Vector_Math_001.inputs[1])
        nt.links.new(GroupInput.outputs[1], Object_Info.inputs[0])
        nt.links.new(Math_001.outputs[0], Math.inputs[0])
        nt.links.new(GroupInput.outputs[4], Reroute.inputs[0])
        nt.links.new(Reroute.outputs[0], Reroute_001.inputs[0])
        nt.links.new(Reroute_001.outputs[0], Reroute_002.inputs[0])
        nt.links.new(Reroute_002.outputs[0], Reroute_003.inputs[0])
        nt.links.new(Reroute_003.outputs[0], Math.inputs[1])
        nt.links.new(Vector_Math.outputs[0], Set_Position.inputs[3])
        nt.links.new(Math_002.outputs[0], Set_Position.inputs[1])
        nt.links.new(GroupInput.outputs[2], Set_Material.inputs[2])
        nt.links.new(Math.outputs[0], Vector_Math.inputs[3])
        nt.links.new(GroupInput.outputs[5], Math_002.inputs[1])
        nt.links.new(Vector_Math_001.outputs[1], Math_001.inputs[0])
        nt.links.new(GroupInput.outputs[3], Reroute_004.inputs[0])
        nt.links.new(Reroute_004.outputs[0], Reroute_005.inputs[0])
        nt.links.new(Reroute_005.outputs[0], Math_001.inputs[1])
        nt.links.new(Math_002.outputs[0], Set_Material.inputs[1])
        nt.links.new(Math_002.outputs[0], Flip_Faces.inputs[1])

        # Set default values
        Object_Info.inputs[1].default_value = False
        Math.inputs[2].default_value = 0.5
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Math_002.inputs[0].default_value = 1.0
        Math_002.inputs[2].default_value = 0.5
        Math_001.inputs[2].default_value = -0.19999992847442627
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[3].default_value = 1.0
        Set_Position.inputs[2].default_value = (0.0, 0.0, 0.0)

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
