import bpy
from ..utils import ShaderNode


class ShaderNodeBuildRampFromMap(ShaderNode):
    bl_label = "Build Ramp From Map"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            UV_socket = nt.interface.new_socket(
                name="UV",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        UV_socket.default_value = (0.0, 0.0, 0.0)
        UV_socket.subtype = "NONE"

        # Input sockets
            Toon_socket = nt.interface.new_socket(
                name="Toon",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Toon_socket.default_value = 0.0
        Toon_socket.min_value = -3.4028234663852886e+38
        Toon_socket.max_value = 3.4028234663852886e+38
        Toon_socket.subtype = "NONE"
            Ramp_Size_socket = nt.interface.new_socket(
                name="Ramp Size",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Ramp_Size_socket.default_value = 0.5
        Ramp_Size_socket.min_value = -10000.0
        Ramp_Size_socket.max_value = 10000.0
        Ramp_Size_socket.subtype = "NONE"

        # Create nodes
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (190.0, 0.0)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (-249.54733276367188, 9.415594100952148)
        Combine_XYZ.inputs["Y"].default_value = 1.0
        Combine_XYZ.inputs["Z"].default_value = 0.0
        Map_Range = nt.nodes.new("ShaderNodeMapRange")
        Map_Range.location = (-463.28900146484375, 70.53758239746094)
        Map_Range.data_type = "FLOAT"
        Map_Range.interpolation_type = "LINEAR"
        Map_Range.inputs["From Min"].default_value = -1.0
        Map_Range.inputs["To Min"].default_value = 0.0
        Map_Range.inputs["To Max"].default_value = 1.0
        Map_Range.inputs["Steps"].default_value = 4.0
        Map_Range.inputs["Vector"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["From Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["To Min"].default_value = (0.0, 0.0, 0.0)
        Map_Range.inputs["To Max"].default_value = (1.0, 1.0, 1.0)
        Map_Range.inputs["Steps"].default_value = (4.0, 4.0, 4.0)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-855.5357666015625, -28.377593994140625)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (-398.85986328125, 197.03111267089844)
        # Create links
        nt.links.new(Combine_XYZ.outputs["Vector"], Group_Output.inputs["UV"])
        nt.links.new(Group_Input.outputs["Toon"], Map_Range.inputs["Value"])
        nt.links.new(Map_Range.outputs["Result"], Combine_XYZ.inputs["X"])
        nt.links.new(Group_Input.outputs["Ramp Size"], Map_Range.inputs["From Max"])