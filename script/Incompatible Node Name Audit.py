import bpy
import re
from collections import defaultdict

# Python identifier regex
PY_IDENTIFIER = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')

report = defaultdict(lambda: {
    "nodes": [],
    "labels": [],
    "inputs": [],
    "outputs": []
})

total_nodes = 0

def is_bad(name: str) -> bool:
    if not name:
        return True
    return not PY_IDENTIFIER.match(name)

# --------------------------------------------------
# Scan all node groups
# --------------------------------------------------
for ng in bpy.data.node_groups:
    for node in ng.nodes:
        total_nodes += 1

        # NODE NAME
        if is_bad(node.name):
            report[ng.name]["nodes"].append(node.name)

        # NODE LABEL (label có thể rỗng, chỉ check nếu tồn tại)
        if node.label and is_bad(node.label):
            report[ng.name]["labels"].append(f"{node.name} :: {node.label}")

        # INPUT SOCKETS
        for sock in node.inputs:
            if is_bad(sock.name):
                report[ng.name]["inputs"].append(
                    f"{node.name} :: {sock.name}"
                )

        # OUTPUT SOCKETS
        for sock in node.outputs:
            if is_bad(sock.name):
                report[ng.name]["outputs"].append(
                    f"{node.name} :: {sock.name}"
                )

# --------------------------------------------------
# PRINT SUMMARY
# --------------------------------------------------
print("\n" + "=" * 90)
print("PYTHON-INCOMPATIBLE NODE NAME AUDIT")
print("=" * 90)

print(f"Total nodes scanned: {total_nodes}")

for ng_name, data in report.items():
    if not any(data.values()):
        continue

    print("\n" + "-" * 70)
    print(f"Node Group: {repr(ng_name)}")

    if data["nodes"]:
        print("  ❌ Node names:")
        for n in sorted(set(data["nodes"])):
            print(f"    - {repr(n)}")

    if data["labels"]:
        print("  ⚠️ Node labels:")
        for l in sorted(set(data["labels"])):
            print(f"    - {repr(l)}")

    if data["inputs"]:
        print("  ❌ Input sockets:")
        for s in sorted(set(data["inputs"])):
            print(f"    - {repr(s)}")

    if data["outputs"]:
        print("  ❌ Output sockets:")
        for s in sorted(set(data["outputs"])):
            print(f"    - {repr(s)}")

print("\n✓ Audit completed.")
