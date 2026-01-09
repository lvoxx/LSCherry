import bpy


class Node:
    """Base node class with common utilities"""

    def draw_buttons(self, context, layout):
        pass

    def createNodetree(self, name):
        pass

    def getNodetree(self, name):
        self.createNodetree(name)

    def addSocket(self, is_output, sockettype, name):
        if is_output == True:
            socket = self.node_tree.interface.new_socket(
                name, in_out="OUTPUT", socket_type=sockettype
            )
        else:
            socket = self.node_tree.interface.new_socket(
                name, in_out="INPUT", socket_type=sockettype
            )
        return socket

    def addNode(self, nodetype, attrs):
        node = self.node_tree.nodes.new(nodetype)
        for attr in attrs:
            self.value_set(node, attr, attrs[attr])
        return node

    def getNode(self, nodename):
        if self.node_tree.nodes.find(nodename) > -1:
            return self.node_tree.nodes[nodename]
        return None

    def innerLink(self, socketin, socketout):
        SI = self.node_tree.path_resolve(socketin)
        SO = self.node_tree.path_resolve(socketout)
        self.node_tree.links.new(SI, SO)

    def value_set(self, obj, path, value):
        if "." in path:
            path_prop, path_attr = path.rsplit(".", 1)
            prop = obj.path_resolve(path_prop)
        else:
            prop = obj
            path_attr = path
        setattr(prop, path_attr, value)

    def free(self):
        if self.node_tree.users == 1:
            bpy.data.node_groups.remove(self.node_tree, do_unlink=True)


class ShaderNode(Node, bpy.types.ShaderNodeCustomGroup):
    """Base class for custom shader nodes"""
    pass


class GeometryNode(Node, bpy.types.GeometryNodeCustomGroup):
    """Base class for custom geometry nodes"""
    pass