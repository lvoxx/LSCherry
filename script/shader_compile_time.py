import time
import bpy
import platform
import multiprocessing
import datetime
import os
import csv

# ==========================
# Config
# ==========================
MATERIAL_NAME = "LSCherry"   # Material chính để test
NODE_GROUP = "Make Toon"     # Node group chính (nếu có)
ENGINE = "BLENDER_EEVEE_NEXT"  # Có thể đổi sang 'CYCLES' hoặc 'BLENDER_EEVEE'
LSCHERRY_VERSION = "1.2.6"

# ==========================
# CPU Info
# ==========================
cpu_model = platform.processor()
cpu_cores = multiprocessing.cpu_count()
cpu_info = f"{cpu_model} ({cpu_cores} cores)"

# ==========================
# Benchmark directory
# ==========================
BENCHMARK_DIR = os.path.join(os.path.dirname(bpy.data.filepath), "benchmark")
os.makedirs(BENCHMARK_DIR, exist_ok=True)

# ==========================
# Ensure engine
# ==========================
bpy.context.scene.render.engine = ENGINE

# ==========================
# Force reload material (clear cache trick)
# ==========================
obj = bpy.context.object
material = bpy.data.materials.get(MATERIAL_NAME)

if not obj or not material:
    raise ValueError(f"Object or material '{MATERIAL_NAME}' not found!")

# Tạm detach rồi attach lại để ép Blender treat như material mới
obj.active_material = None
bpy.context.view_layer.update()
obj.active_material = material
bpy.context.view_layer.update()

# ==========================
# Benchmark
# ==========================
start_time = time.time()

# Render 1 frame (không lưu file) để ép compile shader thật sự
bpy.ops.render.render(write_still=False)

compile_time = time.time() - start_time

# ==========================
# Format kết quả
# ==========================
time_unit = "ms" if compile_time < 1 else "s"
compile_time_display = compile_time * 1000 if time_unit == "ms" else compile_time
compile_time_str = f"{compile_time_display:.2f} {time_unit}"

print(f"[Benchmark] Material={MATERIAL_NAME}, NodeGroup={NODE_GROUP}, "
      f"Compile Time={compile_time_str}, CPU={cpu_info}")

# ==========================
# Save CSV
# ==========================
now = datetime.datetime.now()
file_name = f"{MATERIAL_NAME}-{NODE_GROUP.replace(' ', '-')}-{LSCHERRY_VERSION}-{now.strftime('%Y%m%d_%H%M%S')}.csv"
file_path = os.path.join(BENCHMARK_DIR, file_name)

results = [{
    "Material": MATERIAL_NAME,
    "Node Group": NODE_GROUP,
    "Compile Time": compile_time_str,
    "CPU Info": cpu_info
}]

with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Results saved to: {file_path}")