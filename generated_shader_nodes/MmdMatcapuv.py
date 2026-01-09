import bpy
from ..utils import ShaderNode


class ShaderNodeMmdMatcapuv(ShaderNode):
    bl_label = "MMD: MatCapUV"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "VECTOR"
        nt.description = ""

        # Output sockets
            ToonUV_socket = nt.interface.new_socket(
                name="ToonUV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        ToonUV_socket.default_value = (0.0, 0.0, 0.0)
        ToonUV_socket.subtype = "NONE"
            SphereUV_socket = nt.interface.new_socket(
                name="SphereUV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        SphereUV_socket.default_value = (0.0, 0.0, 0.0)
        SphereUV_socket.subtype = "NONE"

        # Input sockets

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (365.29498291015625, 0.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-375.2950134277344, 0.0)
        Texture_Coordinate = nt.nodes.new("ShaderNodeTexCoord")
        Texture_Coordinate.location = (-175.29501342773438, 1.52587890625e-05)
        Vector_Transform = nt.nodes.new("ShaderNodeVectorTransform")
        Vector_Transform.location = (-8.140594482421875, -5.4357452392578125)
        Vector_Transform.vector_type = "NORMAL"
        Vector_Transform.convert_from = "OBJECT"
        Vector_Transform.convert_to = "CAMERA"
        Mapping = nt.nodes.new("ShaderNodeMapping")
        Mapping.location = (175.2949981689453, 5.4357452392578125)
        Mapping.vector_type = "POINT"
        Mapping.inputs["Location"].default_value = (0.5, 0.5, 0.0)
        Mapping.inputs["Rotation"].default_value = (0.0, 0.0, 0.0)
        Mapping.inputs["Scale"].default_value = (0.5, 0.5, 1.0)
        # Create links
        nt.links.new(Vector_Transform.outputs["Vector"], Mapping.inputs["Vector"])
        nt.links.new(Texture_Coordinate.outputs["Normal"], Vector_Transform.inputs["Vector"])
        nt.links.new(Mapping.outputs["Vector"], Group_Output.inputs["ToonUV"])
        nt.links.new(Mapping.outputs["Vector"], Group_Output.inputs["SphereUV"])