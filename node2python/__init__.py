bl_info = {
    "name": "Generated Node Groups Test",
    "author": "Auto-generated",
    "version": (1, 0, 0),
    "blender": (4, 3, 0),
    "location": "Node Editor > Add > Generated Nodes",
    "description": "Test addon for auto-generated custom nodes",
    "category": "Node",
}

import bpy
import sys
import importlib
from pathlib import Path

# Get addon directory and package name
addon_dir = Path(__file__).parent
package_name = __name__.split('.')[0] if '.' in __name__ else 'dist'

print(f"Addon dir: {addon_dir}")
print(f"Package name: {package_name}")

# Import using relative imports
try:
    # Import the shader module
    from .nodes import shader

    NODE_CLASSES = [
        getattr(shader, name)
        for name in dir(shader)
        if name.startswith("ShaderNode")
        and isinstance(getattr(shader, name), type)
    ]

    print(f"✓ Loaded {len(NODE_CLASSES)} node classes")
    NODES_LOADED = True
    
except Exception as e:
    print(f"✗ Error importing nodes.shader: {e}")
    import traceback
    traceback.print_exc()
    NODE_CLASSES = []
    NODES_LOADED = False


class NODE_MT_add_generated(bpy.types.Menu):
    """Menu for generated custom nodes"""
    bl_idname = "NODE_MT_add_generated"
    bl_label = "Generated Nodes"
    
    def draw(self, context):
        layout = self.layout
        
        if not NODES_LOADED or not NODE_CLASSES:
            layout.label(text="No nodes loaded", icon='ERROR')
            return
        
        # Sort by label
        sorted_nodes = sorted(NODE_CLASSES, key=lambda x: x.bl_label if hasattr(x, 'bl_label') else '')
        
        # Group by prefix for better organization (optional)
        layout.label(text=f"{len(NODE_CLASSES)} Custom Nodes:", icon='MATERIAL')
        
        for node_class in sorted_nodes:
            op = layout.operator(
                "node.add_custom_generated",
                text=node_class.bl_label if hasattr(node_class, 'bl_label') else node_class.__name__,
                icon='NODETREE'
            )
            op.node_type = node_class.__name__


class NODE_OT_add_custom_generated(bpy.types.Operator):
    """Add a custom generated node"""
    bl_idname = "node.add_custom_generated"
    bl_label = "Add Generated Node"
    bl_options = {'REGISTER', 'UNDO'}
    
    node_type: bpy.props.StringProperty()
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space and space.type == 'NODE_EDITOR' and space.edit_tree
    
    def execute(self, context):
        space = context.space_data
        tree = space.edit_tree
        
        # Find the node class
        node_class = None
        for cls in NODE_CLASSES:
            if cls.__name__ == self.node_type:
                node_class = cls
                break
        
        if not node_class:
            self.report({'ERROR'}, f"Node class not found: {self.node_type}")
            return {'CANCELLED'}
        
        # Add node using the registered bl_idname
        try:
            new_node = tree.nodes.new(node_class.__name__)
            new_node.location = space.cursor_location
            new_node.select = True
            
            # Deselect all other nodes
            for node in tree.nodes:
                if node != new_node:
                    node.select = False
            
            tree.nodes.active = new_node
            
            node_label = node_class.bl_label if hasattr(node_class, 'bl_label') else node_class.__name__
            self.report({'INFO'}, f"Added: {node_label}")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to add node: {str(e)}")
            import traceback
            traceback.print_exc()
            return {'CANCELLED'}


def menu_draw(self, context):
    """Add custom menu to Add menu"""
    layout = self.layout
    
    # Only show in Shader Editor
    space = context.space_data
    if space and space.tree_type == 'ShaderNodeTree':
        layout.separator()
        layout.menu("NODE_MT_add_generated", icon='NODETREE')


classes = (
    NODE_OT_add_custom_generated,
    NODE_MT_add_generated,
)


def register():
    print("\n" + "="*60)
    print("Registering Generated Node Classes...")
    print("="*60)
    
    if not NODES_LOADED:
        print("\n✗ ERROR: Could not load nodes.shader module")
        print("  Make sure 'nodes/shader/' folder exists with __init__.py")
        print("  and utils.py is in 'nodes/' folder")
    
    # Register node classes
    registered_count = 0
    for node_class in NODE_CLASSES:
        try:
            bpy.utils.register_class(node_class)
            print(f"✓ Registered: {node_class.bl_label if hasattr(node_class, 'bl_label') else node_class.__name__}")
            registered_count += 1
        except Exception as e:
            print(f"✗ Error registering {node_class.__name__}: {e}")
    
    # Register UI classes
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Add to menu
    bpy.types.NODE_MT_add.append(menu_draw)
    
    print("\n" + "="*60)
    print(f"✓ Addon registered with {registered_count} custom nodes")
    print("="*60 + "\n")


def unregister():
    # Remove from menu
    bpy.types.NODE_MT_add.remove(menu_draw)
    
    # Unregister UI classes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    # Unregister node classes
    for node_class in reversed(NODE_CLASSES):
        try:
            bpy.utils.unregister_class(node_class)
        except:
            pass


if __name__ == "__main__":
    register()