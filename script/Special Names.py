import bpy
import re
from collections import defaultdict

# Chỉ cho phép a-z A-Z 0-9 _
BAD_CHARS = re.compile(r'[^\w]')

summary = defaultdict(lambda: {
    "nodes": set(),
    "inputs": set(),
    "outputs": set()
})

total_nodes = 0
bad_nodes = 0
bad_sockets = 0

for ng in bpy.data.node_groups:
    for node in ng.nodes:
        total_nodes += 1

        # Check node name
        if BAD_CHARS.search(node.name):
            bad_nodes += 1
            summary[ng.name]["nodes"].add(node.name)

        # Check sockets
        for s in node.inputs:
            if BAD_CHARS.search(s.name):
                bad_sockets += 1
                summary[ng.name]["inputs"].add(f"{node.name} :: {s.name}")

        for s in node.outputs:
            if BAD_CHARS.search(s.name):
                bad_sockets += 1
                summary[ng.name]["outputs"].add(f"{node.name} :: {s.name}")

# ===== PRINT SUMMARY =====

print("\n" + "=" * 80)
print("NODE / SOCKET NAME SUMMARY")
print("=" * 80)

print(f"Total nodes scanned     : {total_nodes}")
print(f"Nodes with bad names    : {bad_nodes}")
print(f"Sockets with bad names  : {bad_sockets}")

for ng_name, data in summary.items():
    if not (data["nodes"] or data["inputs"] or data["outputs"]):
        continue

    print("\n" + "-" * 60)
    print(f"Node Group: {repr(ng_name)}")

    if data["nodes"]:
        print("  Nodes:")
        for n in sorted(data["nodes"]):
            print(f"    - {repr(n)}")

    if data["inputs"]:
        print("  Input Sockets:")
        for s in sorted(data["inputs"]):
            print(f"    - {repr(s)}")

    if data["outputs"]:
        print("  Output Sockets:")
        for s in sorted(data["outputs"]):
            print(f"    - {repr(s)}")

print("\n✓ Summary completed.")
