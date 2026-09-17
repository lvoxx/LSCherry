import bpy # type: ignore
import json
import os

# Chỉnh version tại đây
VERSION = "1.1.5.1"

# Lấy đường dẫn file .blend hiện tại
blend_path = bpy.data.filepath

if not blend_path:
    raise RuntimeError("❌ Chưa lưu file .blend, hãy Save trước khi export!")

# Project root = folder chứa file blend
PROJECT_ROOT = os.path.dirname(blend_path)

# Đường dẫn xuất JSON
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "src", "constants", "version")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_PATH = os.path.join(OUTPUT_DIR, f"{VERSION}.json")


def export_node_groups():
    export_data = {
        "version": VERSION,
        "node_groups": []
    }

    for ng in bpy.data.node_groups:
        export_data["node_groups"].append({
            "name": ng.name
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Exported LSCherry node groups to {OUTPUT_PATH}")


if __name__ == "__main__":
    export_node_groups()
