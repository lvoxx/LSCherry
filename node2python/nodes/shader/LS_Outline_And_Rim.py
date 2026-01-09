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


class GeometryNodeLS_Outline_And_Rim(GeometryNode):
    bl_idname = 'GeometryNodeLS_Outline_And_Rim'
    bl_label = "LS Outline And Rim"
    bl_icon = "NODETREE"

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs["Ratio"].default_value = 1.2000000476837158
        self.inputs["Affected Vertex"].default_value = False

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new('.'+name, 'GeometryNodeTree')
        nt.color_tag = 'CONVERTER'
        nt.description = 'LS Outline And Rim'

        # Create output sockets
        nt.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')

        # Create input sockets
        nt.interface.new_socket('Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
        nt.interface.new_socket('Outlined Material', in_out='INPUT', socket_type='NodeSocketMaterial')
        nt.interface.new_socket('Rim Material', in_out='INPUT', socket_type='NodeSocketMaterial')
        input_socket = nt.interface.new_socket('Ratio', in_out='INPUT', socket_type='NodeSocketFloat')
        input_socket.default_value = 1.2000000476837158
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
        Join_Geometry.location = (431.1681823730469, 20.218700408935547)
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

        Set_Material_001 = nt.nodes.new('GeometryNodeSetMaterial')
        Set_Material_001.location = (-167.66311645507812, -433.09808349609375)
        Set_Material_001.name = "Set Material.001"

        Set_Position_001 = nt.nodes.new('GeometryNodeSetPosition')
        Set_Position_001.location = (-377.43115234375, -394.6035461425781)
        Set_Position_001.name = "Set Position.001"

        Vector_Math_001 = nt.nodes.new('ShaderNodeVectorMath')
        Vector_Math_001.location = (162.9110565185547, -198.07589721679688)
        Vector_Math_001.name = "Vector Math.001"
        Vector_Math_001.operation = 'SCALE'

        Math_001 = nt.nodes.new('ShaderNodeMath')
        Math_001.location = (-38.2884635925293, -152.33050537109375)
        Math_001.name = "Math.001"
        Math_001.operation = 'DIVIDE'

        Math_003 = nt.nodes.new('ShaderNodeMath')
        Math_003.location = (-203.1246795654297, -152.33050537109375)
        Math_003.name = "Math.003"
        Math_003.operation = 'MULTIPLY'

        Flip_Faces_001 = nt.nodes.new('GeometryNodeFlipFaces')
        Flip_Faces_001.location = (56.316192626953125, -342.9420166015625)
        Flip_Faces_001.name = "Flip Faces.001"

        Math_004 = nt.nodes.new('ShaderNodeMath')
        Math_004.location = (-383.57550048828125, -3.863555908203125)
        Math_004.name = "Math.004"
        Math_004.operation = 'MULTIPLY'

        # Create internal links
        nt.links.new(Join_Geometry.outputs[0], GroupOutput.inputs[0])
        nt.links.new(Set_Position.outputs[0], Set_Material.inputs[0])
        nt.links.new(GroupInput.outputs[0], Set_Position.inputs[0])
        nt.links.new(Set_Material.outputs[0], Flip_Faces.inputs[0])
        nt.links.new(GroupInput.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(Flip_Faces.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(Normal.outputs[0], Vector_Math.inputs[0])
        nt.links.new(Vector_Math.outputs[0], Set_Position.inputs[3])
        nt.links.new(Math_002.outputs[0], Set_Position.inputs[1])
        nt.links.new(GroupInput.outputs[1], Set_Material.inputs[2])
        nt.links.new(GroupInput.outputs[4], Math_002.inputs[1])
        nt.links.new(Math.outputs[0], Vector_Math.inputs[3])
        nt.links.new(Set_Position_001.outputs[0], Set_Material_001.inputs[0])
        nt.links.new(GroupInput.outputs[0], Set_Position_001.inputs[0])
        nt.links.new(GroupInput.outputs[2], Set_Material_001.inputs[2])
        nt.links.new(Math_001.outputs[0], Vector_Math_001.inputs[3])
        nt.links.new(Math_004.outputs[0], Math_003.inputs[0])
        nt.links.new(Math_003.outputs[0], Math_001.inputs[0])
        nt.links.new(Normal.outputs[0], Vector_Math_001.inputs[0])
        nt.links.new(Vector_Math_001.outputs[0], Set_Position_001.inputs[3])
        nt.links.new(Set_Material_001.outputs[0], Flip_Faces_001.inputs[0])
        nt.links.new(Flip_Faces_001.outputs[0], Join_Geometry.inputs[0])
        nt.links.new(Math_002.outputs[0], Set_Position_001.inputs[1])
        nt.links.new(GroupInput.outputs[3], Math_004.inputs[0])
        nt.links.new(Math_004.outputs[0], Math.inputs[0])
        nt.links.new(Math_002.outputs[0], Set_Material.inputs[1])
        nt.links.new(Math_002.outputs[0], Flip_Faces.inputs[1])
        nt.links.new(Math_002.outputs[0], Set_Material_001.inputs[1])
        nt.links.new(Math_002.outputs[0], Flip_Faces_001.inputs[1])

        # Set default values
        Math_002.inputs[0].default_value = 1.0
        Math_002.inputs[2].default_value = 0.5
        Set_Position.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math.inputs[2].default_value = (0.0, 0.0, 0.0)
        Math.inputs[1].default_value = 1000.0
        Math.inputs[2].default_value = 0.5
        Set_Position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
        Vector_Math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
        Math_001.inputs[1].default_value = 1000.0
        Math_001.inputs[2].default_value = 0.5
        Math_003.inputs[1].default_value = 0.5
        Math_003.inputs[2].default_value = 0.5
        Math_004.inputs[1].default_value = 2.0
        Math_004.inputs[2].default_value = 0.5

    def duplicate(self):
        self.node_tree = self.node_tree.copy()
