import bpy

TARGET_SUBSTRING = "idv.lvoxx."

removed = []

for ng in bpy.data.node_groups:
    # Thu thập trước, không xóa trực tiếp khi đang iterate
    frames_to_remove = []

    for node in ng.nodes:
        if node.type == 'FRAME':
            label = node.label or ""
            if TARGET_SUBSTRING in label:
                frames_to_remove.append(node)

    # Xóa frame
    for frame in frames_to_remove:
        removed.append((ng.name, frame.name, frame.label))
        ng.nodes.remove(frame)

# --------------------------------------------------
# REPORT
# --------------------------------------------------
print("\n" + "=" * 80)
print("FRAME CLEANUP REPORT")
print("=" * 80)

if removed:
    print(f"Removed {len(removed)} frame(s):")
    for ng_name, frame_name, frame_label in removed:
        print(f"  - Node Group: {repr(ng_name)}")
        print(f"    Frame     : {repr(frame_name)}")
        print(f"    Label     : {repr(frame_label)}")
else:
    print("No matching frames found.")

print("\n[OK] Cleanup completed.")
