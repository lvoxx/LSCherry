import bpy
from ..utils import ShaderNode


class ShaderNodeExperimental(ShaderNode):
    bl_label = "Experimental"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "OUTPUT"
        nt.description = ""

        # Output sockets
            Unstable_socket = nt.interface.new_socket(
                name="Unstable",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        
            DO_NOT_USE_FOR_PRODUCTION_socket = nt.interface.new_socket(
                name="DO NOT USE FOR PRODUCTION",
                in_out="OUTPUT",
                socket_type="NodeSocketShader"
            )
        

        # Input sockets
            Unstable_socket = nt.interface.new_socket(
                name="Unstable",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        
            DO_NOT_USE_FOR_PRODUCTION_socket = nt.interface.new_socket(
                name="DO NOT USE FOR PRODUCTION",
                in_out="INPUT",
                socket_type="NodeSocketShader"
            )
        

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (209.28079223632812, 92.1033935546875)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-190.71923828125, 92.1033935546875)
        Frame = nt.nodes.new("NodeFrame")
        Frame.location = (11.932327270507812, -13.32492446899414)
        Frame_001 = nt.nodes.new("NodeFrame")
        Frame_001.location = (18.357421875, -90.05806732177734)
        Frame_002 = nt.nodes.new("NodeFrame")
        Frame_002.location = (-13.707847595214844, 195.10861206054688)
        # Create links
        nt.links.new(Group_Input.outputs["Unstable"], Group_Output.inputs["Unstable"])
        nt.links.new(Group_Input.outputs["DO NOT USE FOR PRODUCTION"], Group_Output.inputs["DO NOT USE FOR PRODUCTION"])