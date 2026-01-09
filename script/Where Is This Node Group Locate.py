import bpy

TARGET_GROUP_NAME = "Specular Dot.001" #Your Node Group Name Here

used_in_node_groups = []
used_in_materials = []

# --------------------------------------------------
# 1. Scan all node groups
# --------------------------------------------------
for ng in bpy.data.node_groups:
    for node in ng.nodes:
        if node.type == 'GROUP' and node.node_tree:
            if node.node_tree.name == TARGET_GROUP_NAME:
                used_in_node_groups.append(ng.name)
                break

# --------------------------------------------------
# 2. Scan all materials
# --------------------------------------------------
for mat in bpy.data.materials:
    if not mat.use_nodes or not mat.node_tree:
        continue

    for node in mat.node_tree.nodes:
        if node.type == 'GROUP' and node.node_tree:
            if node.node_tree.name == TARGET_GROUP_NAME:
                used_in_materials.append(mat.name)
                break

# --------------------------------------------------
# REPORT
# --------------------------------------------------
print("\n" + "=" * 70)
print(f"USAGE REPORT FOR NODE GROUP: {TARGET_GROUP_NAME}")
print("=" * 70)

if used_in_node_groups:
    print("\nUsed in Node Groups:")
    for name in used_in_node_groups:
        print(f"  - {name}")
else:
    print("\nNot used in any Node Group.")

if used_in_materials:
    print("\nUsed in Materials:")
    for name in used_in_materials:
        print(f"  - {name}")
else:
    print("\nNot used in any Material.")

print("\n✓ Scan completed.")
