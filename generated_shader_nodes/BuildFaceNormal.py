import bpy
from ..utils import ShaderNode


class ShaderNodeBuildFaceNormal(ShaderNode):
    bl_label = "Build Face Normal"
    bl_icon = "NONE"

    def init(self, context):
        self.getNodetree(self.name + "_node_tree")

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new("." + name, "ShaderNodeTree")
        nt.color_tag = "CONVERTER"
        nt.description = ""

        # Output sockets
            Normal_socket = nt.interface.new_socket(
                name="Normal",
                in_out="OUTPUT",
                socket_type="NodeSocketVector"
            )
        
        Normal_socket.default_value = (0.0, 0.0, 0.0)
        Normal_socket.subtype = "NONE"

        # Input sockets
            Face_Value_socket = nt.interface.new_socket(
                name="Face Value",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Value_socket.default_value = 0.5
        Face_Value_socket.min_value = -10000.0
        Face_Value_socket.max_value = 10000.0
        Face_Value_socket.subtype = "NONE"
            Face_Map_socket = nt.interface.new_socket(
                name="Face Map",
                in_out="INPUT",
                socket_type="NodeSocketFloat"
            )
        
        Face_Map_socket.default_value = 0.5
        Face_Map_socket.min_value = -10000.0
        Face_Map_socket.max_value = 10000.0
        Face_Map_socket.subtype = "NONE"
            Face_To_X_socket = nt.interface.new_socket(
                name="Face To X",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Face_To_X_socket.default_value = False
            Face_To_Y_socket = nt.interface.new_socket(
                name="Face To Y",
                in_out="INPUT",
                socket_type="NodeSocketBool"
            )
        
        Face_To_Y_socket.default_value = False

        # Create nodes
        Math = nt.nodes.new("ShaderNodeMath")
        Math.location = (-209.134521484375, -46.846229553222656)
        Math.operation = "GREATER_THAN"
        Math.inputs["Value"].default_value = 0.5
        Group_Output = nt.nodes.new("NodeGroupOutput")
        Group_Output.location = (897.3662109375, 14.525022506713867)
        Group_Input = nt.nodes.new("NodeGroupInput")
        Group_Input.location = (-427.303955078125, -12.794715881347656)
        Frame_004 = nt.nodes.new("NodeFrame")
        Frame_004.location = (1064.32861328125, 217.2521209716797)
        Reroute_006 = nt.nodes.new("NodeReroute")
        Reroute_006.location = (-246.9525146484375, -70.42658996582031)
        Reroute_003 = nt.nodes.new("NodeReroute")
        Reroute_003.location = (-246.9525146484375, -48.3992919921875)
        Combine_XYZ = nt.nodes.new("ShaderNodeCombineXYZ")
        Combine_XYZ.location = (704.9998168945312, 4.611240386962891)
        Combine_XYZ.inputs["Z"].default_value = 1.0
        Mix = nt.nodes.new("ShaderNodeMix")
        Mix.location = (518.7147827148438, -111.54592895507812)
        Mix.data_type = "FLOAT"
        Mix.blend_type = "MIX"
        Mix.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001 = nt.nodes.new("ShaderNodeMix")
        Mix_001.location = (520.7042846679688, 67.40652465820312)
        Mix_001.data_type = "FLOAT"
        Mix_001.blend_type = "MIX"
        Mix_001.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_001.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_001.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_001.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002 = nt.nodes.new("ShaderNodeMix")
        Mix_002.location = (134.796630859375, 173.7809295654297)
        Mix_002.data_type = "FLOAT"
        Mix_002.blend_type = "MIX"
        Mix_002.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_002.inputs["A"].default_value = -1.0
        Mix_002.inputs["B"].default_value = 1.0
        Mix_002.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_002.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_002.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003 = nt.nodes.new("ShaderNodeMix")
        Mix_003.location = (134.796630859375, -8.746414184570312)
        Mix_003.data_type = "FLOAT"
        Mix_003.blend_type = "MIX"
        Mix_003.inputs["Factor"].default_value = (0.5, 0.5, 0.5)
        Mix_003.inputs["A"].default_value = 1.0
        Mix_003.inputs["B"].default_value = -1.0
        Mix_003.inputs["A"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["B"].default_value = (0.0, 0.0, 0.0)
        Mix_003.inputs["A"].default_value = (0.5, 0.5, 0.5, 1.0)
        Mix_003.inputs["B"].default_value = (0.5, 0.5, 0.5, 1.0)
        Reroute = nt.nodes.new("NodeReroute")
        Reroute.location = (-37.6383056640625, -57.37171173095703)
        Reroute_001 = nt.nodes.new("NodeReroute")
        Reroute_001.location = (-37.6383056640625, 65.1427001953125)
        Reroute_002 = nt.nodes.new("NodeReroute")
        Reroute_002.location = (-37.6383056640625, -118.19062042236328)
        Reroute_004 = nt.nodes.new("NodeReroute")
        Reroute_004.location = (-213.8873291015625, -91.64509582519531)
        Reroute_005 = nt.nodes.new("NodeReroute")
        Reroute_005.location = (-246.8050537109375, -113.26799774169922)
        Reroute_008 = nt.nodes.new("NodeReroute")
        Reroute_008.location = (-213.8873291015625, -239.9164276123047)
        Reroute_009 = nt.nodes.new("NodeReroute")
        Reroute_009.location = (-246.8050537109375, -261.5393371582031)
        Reroute_010 = nt.nodes.new("NodeReroute")
        Reroute_010.location = (423.4469299316406, -239.9164276123047)
        Reroute_011 = nt.nodes.new("NodeReroute")
        Reroute_011.location = (441.6839904785156, -261.5393371582031)
        Reroute_012 = nt.nodes.new("NodeReroute")
        Reroute_012.location = (423.4469299316406, -41.1976318359375)
        Reroute_013 = nt.nodes.new("NodeReroute")
        Reroute_013.location = (441.6839904785156, -221.3079071044922)
        Reroute_014 = nt.nodes.new("NodeReroute")
        Reroute_014.location = (-186.6171112060547, 452.4814453125)
        Reroute_014.inputs["Input"].default_value = 0.0
        # Create links
        nt.links.new(Reroute_006.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Combine_XYZ.outputs["Vector"], Group_Output.inputs["Normal"])
        nt.links.new(Group_Input.outputs["Face Map"], Reroute_006.inputs["Input"])
        nt.links.new(Reroute_003.outputs["Output"], Math.inputs["Value"])
        nt.links.new(Group_Input.outputs["Face Value"], Reroute_003.inputs["Input"])
        nt.links.new(Mix_001.outputs["Result"], Combine_XYZ.inputs["X"])
        nt.links.new(Mix.outputs["Result"], Combine_XYZ.inputs["Y"])
        nt.links.new(Mix_002.outputs["Result"], Mix_001.inputs["A"])
        nt.links.new(Mix_003.outputs["Result"], Mix_001.inputs["B"])
        nt.links.new(Mix_002.outputs["Result"], Mix.inputs["A"])
        nt.links.new(Mix_003.outputs["Result"], Mix.inputs["B"])
        nt.links.new(Math.outputs["Value"], Reroute.inputs["Input"])
        nt.links.new(Reroute.outputs["Output"], Reroute_001.inputs["Input"])
        nt.links.new(Reroute_001.outputs["Output"], Mix_002.inputs["Factor"])
        nt.links.new(Reroute.outputs["Output"], Reroute_002.inputs["Input"])
        nt.links.new(Reroute_002.outputs["Output"], Mix_003.inputs["Factor"])
        nt.links.new(Group_Input.outputs["Face To X"], Reroute_004.inputs["Input"])
        nt.links.new(Group_Input.outputs["Face To Y"], Reroute_005.inputs["Input"])
        nt.links.new(Reroute_005.outputs["Output"], Reroute_009.inputs["Input"])
        nt.links.new(Reroute_004.outputs["Output"], Reroute_008.inputs["Input"])
        nt.links.new(Reroute_008.outputs["Output"], Reroute_010.inputs["Input"])
        nt.links.new(Reroute_009.outputs["Output"], Reroute_011.inputs["Input"])
        nt.links.new(Reroute_011.outputs["Output"], Reroute_013.inputs["Input"])
        nt.links.new(Reroute_010.outputs["Output"], Reroute_012.inputs["Input"])
        nt.links.new(Reroute_013.outputs["Output"], Mix.inputs["Factor"])
        nt.links.new(Reroute_012.outputs["Output"], Mix_001.inputs["Factor"])