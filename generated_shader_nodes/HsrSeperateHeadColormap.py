import bpy
from ..utils import ShaderNode


class ShaderNodeHsrSeperateHeadColormap(ShaderNode):
    bl_label = "HSR: Seperate Head Colormap"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Blush_socket = nt.interface.new_socket(
                name="Blush",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Blush_socket.default_value = 0.0
        Blush_socket.min_value = -3.4028234663852886e+38
        Blush_socket.max_value = 3.4028234663852886e+38
        Blush_socket.subtype = "NONE"
            Mood_Down_socket = nt.interface.new_socket(
                name="Mood Down",
                in_out="OUTPUT",
                socket_type="NodeSocketFloat"
            )
        
        Mood_Down_socket.default_value = 0.0
        Mood_Down_socket.min_value = -3.4028234663852886e+38
        Mood_Down_socket.max_value = 3.4028234663852886e+38
        Mood_Down_socket.subtype = "NONE"

        # Input sockets
            Lightmap_socket = nt.interface.new_socket(
                name="Lightmap",
                in_out="INPUT",
                socket_type="NodeSocketColor"
            )
        
        Lightmap_socket.default_value = (1.0, 1.0, 1.0, 1.0)

        # Create nodes
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-249.63360595703125, -95.09207153320312)
        Group = nt.nodes.new("ShaderNodeGroup")
        Group.location = (0.0, 0.0)
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (682.076416015625, -5.7914509773254395)
        Frame_003 = nt.nodes.new("NodeFrame")
        Frame_003.location = (168.77728271484375, 146.44871520996094)
        # Create links
        nt.links.new(Group_Input.outputs["Lightmap"], Group.inputs["Lightmap"])
        nt.links.new(Group.outputs["Diffuse"], Group_Output.inputs["Mood Down"])
        nt.links.new(Group.outputs["Metal"], Group_Output.inputs["Blush"])