import bpy
import re

OLD_BASE = "Bright/Contrast"
NEW_BASE = "Bright or Contrast"

# Regex bắt:
# Bright/Contrast
# Bright/Contrast.001
# Bright/Contrast.123
PATTERN = re.compile(rf'^{re.escape(OLD_BASE)}(\.\d+)?$')

renamed = []

for ng in bpy.data.node_groups:
    for node in ng.nodes:
        name = node.name

        match = PATTERN.match(name)
        if not match:
            continue

        suffix = match.group(1) or ""
        new_name = f"{NEW_BASE}{suffix}"

        if new_name != name:
            renamed.append((ng.name, name, new_name))
            node.name = new_name

# --------------------------------------------------
# REPORT
# --------------------------------------------------
print("\n" + "=" * 80)
print("NODE RENAME REPORT")
print("=" * 80)

if renamed:
    print(f"Renamed {len(renamed)} node(s):")
    for ng_name, old, new in renamed:
        print(f"  Node Group : {repr(ng_name)}")
        print(f"    {repr(old)} -> {repr(new)}")
else:
    print("No matching nodes found.")

print("\n[OK] Rename completed.")
