import bpy

def debug_node_group_api():
    """Debug script to check Blender 4.3 API structure"""
    
    print("\n" + "="*80)
    print("BLENDER 4.3 NODE GROUP API DEBUG")
    print("="*80)
    
    # Get a sample node group (first one found)
    if len(bpy.data.node_groups) == 0:
        print("No node groups found!")
        return
    
    ng = bpy.data.node_groups[0]
    print(f"\nAnalyzing Node Group: {ng.name}")
    print(f"Type: {ng.bl_idname}")
    
    # Check interface structure
    print("\n" + "-"*80)
    print("INTERFACE STRUCTURE:")
    print("-"*80)
    
    if hasattr(ng, 'interface'):
        print(f"✓ Has 'interface' attribute")
        
        if hasattr(ng.interface, 'items_tree'):
            print(f"✓ Has 'items_tree' attribute")
            print(f"  Number of items: {len(ng.interface.items_tree)}")
            
            for i, item in enumerate(ng.interface.items_tree[:3]):  # First 3 items
                print(f"\n  Item {i}:")
                print(f"    Type: {type(item)}")
                print(f"    Dir: {[attr for attr in dir(item) if not attr.startswith('_')]}")
                
                # Check common attributes
                for attr in ['item_type', 'name', 'identifier', 'socket_type', 'in_out', 'description']:
                    if hasattr(item, attr):
                        value = getattr(item, attr)
                        print(f"    {attr}: {value} (type: {type(value).__name__})")
        else:
            print("✗ No 'items_tree' - checking alternatives...")
            print(f"  Interface dir: {[attr for attr in dir(ng.interface) if not attr.startswith('_')]}")
    
    # Check nodes
    print("\n" + "-"*80)
    print("NODES STRUCTURE:")
    print("-"*80)
    
    if len(ng.nodes) > 0:
        node = ng.nodes[0]
        print(f"\nSample Node: {node.name}")
        print(f"Type: {node.type}")
        print(f"bl_idname: {node.bl_idname}")
        
        # Check name and label
        print(f"\nName attributes:")
        print(f"  node.name: {repr(node.name)} (type: {type(node.name).__name__})")
        print(f"  node.label: {repr(node.label)} (type: {type(node.label).__name__})")
        
        # Check if there are any None names
        print(f"\nChecking all nodes for None names:")
        for n in ng.nodes:
            if n.name is None:
                print(f"  ⚠ Found None name: {n}")
            if n.label is None:
                print(f"  ⚠ Found None label: {n}")
    
    # Check sockets - new API in 4.3
    print("\n" + "-"*80)
    print("SOCKET API CHECK:")
    print("-"*80)
    
    # Try both old and new API
    socket_found = False
    
    # New API (4.3+)
    if hasattr(ng.interface, 'items_tree'):
        for item in ng.interface.items_tree:
            if hasattr(item, 'in_out'):  # This is a socket
                print(f"\nSocket found (new API):")
                print(f"  Name: {item.name if hasattr(item, 'name') else 'N/A'}")
                print(f"  Socket type: {item.socket_type if hasattr(item, 'socket_type') else 'N/A'}")
                print(f"  Direction: {item.in_out if hasattr(item, 'in_out') else 'N/A'}")
                
                # Check all attributes
                attrs = [attr for attr in dir(item) if not attr.startswith('_')]
                print(f"  Available attributes: {attrs}")
                socket_found = True
                break
    
    if not socket_found:
        print("  No sockets found via items_tree")
    
    # Check frames
    print("\n" + "-"*80)
    print("FRAME NODES CHECK:")
    print("-"*80)
    
    frames = [n for n in ng.nodes if n.type == 'FRAME']
    if frames:
        frame = frames[0]
        print(f"\nSample Frame:")
        print(f"  name: {repr(frame.name)} (type: {type(frame.name).__name__})")
        print(f"  label: {repr(frame.label)} (type: {type(frame.label).__name__})")
        
        if hasattr(frame, 'text'):
            print(f"  text: {repr(frame.text)} (type: {type(frame.text).__name__})")
    else:
        print("  No frame nodes found")
    
    # Check links
    print("\n" + "-"*80)
    print("LINKS CHECK:")
    print("-"*80)
    
    if len(ng.links) > 0:
        link = ng.links[0]
        print(f"\nSample Link:")
        print(f"  from_node.name: {repr(link.from_node.name)} (type: {type(link.from_node.name).__name__})")
        print(f"  to_node.name: {repr(link.to_node.name)} (type: {type(link.to_node.name).__name__})")
        print(f"  from_socket.name: {repr(link.from_socket.name)} (type: {type(link.from_socket.name).__name__})")
        print(f"  to_socket.name: {repr(link.to_socket.name)} (type: {type(link.to_socket.name).__name__})")
    
    print("\n" + "="*80)
    print("DEBUG COMPLETE")
    print("="*80 + "\n")

# Run debug
debug_node_group_api()