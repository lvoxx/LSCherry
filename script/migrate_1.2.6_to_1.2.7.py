import bpy
import os

#===========================
#    --- DEV ONLY ---
#===========================

def replace_linked_node_groups(target_blend_name="LS Cherry.blend"):
    """
    Thay thế các node groups được linked từ các file khác 
    bằng node groups cùng tên từ file target (LS Cherry.blend)
    
    Args:
        target_blend_name: Tên file blend đích (mặc định: "LS Cherry.blend")
    """
    
    # Lấy danh sách tất cả node groups hiện có
    existing_node_groups = list(bpy.data.node_groups)
    
    # Dictionary để lưu thông tin về node groups cần thay thế
    groups_to_replace = {}
    target_library_path = None
    
    # Bước 1: Tìm đường dẫn của LS Cherry.blend và các node groups cần thay thế
    for ng in existing_node_groups:
        if ng.library:  # Node group được linked
            library_filepath = ng.library.filepath
            library_filename = os.path.basename(library_filepath)
            
            # Tìm đường dẫn của LS Cherry.blend
            if library_filename == target_blend_name:
                if target_library_path is None:
                    target_library_path = library_filepath
                    print(f"Tìm thấy file đích: {library_filepath}")
            
            # Lưu các node groups từ file khác
            elif library_filename != target_blend_name:
                if ng.name not in groups_to_replace:
                    groups_to_replace[ng.name] = {
                        'old_group': ng,
                        'old_library': library_filepath
                    }
                    print(f"Cần thay thế: '{ng.name}' từ {library_filename}")
    
    if target_library_path is None:
        print(f"\nLỗi: Không tìm thấy node groups nào được linked từ '{target_blend_name}'")
        print("Hãy đảm bảo file hiện tại đã có ít nhất 1 node group từ LS Cherry.blend")
        return
    
    if not groups_to_replace:
        print("\nKhông tìm thấy node groups nào cần thay thế.")
        return
    
    print(f"\n{'='*60}")
    print(f"Tìm thấy {len(groups_to_replace)} node groups cần thay thế")
    
    if not groups_to_replace:
        print("\nKhông tìm thấy node groups nào cần thay thế.")
        return
    
    print(f"\n{'='*60}")
    print(f"Tìm thấy {len(groups_to_replace)} node groups cần thay thế")
    print(f"{'='*60}\n")
    
    replaced_count = 0
    not_found_count = 0
    missing_groups = []
    
    # Bước 2: Load các node groups từ LS Cherry.blend
    target_abs_path = bpy.path.abspath(target_library_path)
    
    print(f"Đang load node groups từ: {target_blend_name}...\n")
    
    with bpy.data.libraries.load(target_abs_path, link=True) as (data_from, data_to):
        # Load những node groups cần thiết
        available_groups = set(data_from.node_groups)
        needed_groups = [ng for ng in groups_to_replace.keys() if ng in available_groups]
        
        if needed_groups:
            data_to.node_groups = needed_groups
            print(f"✓ Đã load {len(needed_groups)} node groups từ {target_blend_name}")
        
        # Kiểm tra node groups không tồn tại
        for ng_name in groups_to_replace.keys():
            if ng_name not in available_groups:
                missing_groups.append(ng_name)
    
    if missing_groups:
        print(f"\n⚠ Cảnh báo: {len(missing_groups)} node groups không tồn tại trong {target_blend_name}:")
        for ng in missing_groups:
            print(f"  - {ng}")
        print()
    
    # Bước 3: Thay thế trong tất cả materials
    print("Đang thay thế trong Materials...")
    for mat in bpy.data.materials:
        if mat.use_nodes and mat.node_tree:
            for node in mat.node_tree.nodes:
                if node.type == 'GROUP' and node.node_tree:
                    node_group_name = node.node_tree.name
                    
                    if node_group_name in groups_to_replace:
                        # Tìm node group mới từ target file
                        new_group = None
                        for ng in bpy.data.node_groups:
                            if ng.name == node_group_name and ng.library:
                                lib_filename = os.path.basename(ng.library.filepath)
                                if lib_filename == target_blend_name:
                                    new_group = ng
                                    break
                        
                        if new_group:
                            old_lib = "Local"
                            if node.node_tree.library:
                                old_lib = os.path.basename(node.node_tree.library.filepath)
                            node.node_tree = new_group
                            replaced_count += 1
                            print(f"  ✓ Material '{mat.name}': '{node_group_name}' ({old_lib} → {target_blend_name})")
                        elif node_group_name not in missing_groups:
                            not_found_count += 1
    
    # Bước 4: Thay thế trong geometry nodes modifiers
    print("\nĐang thay thế trong Geometry Nodes Modifiers...")
    for obj in bpy.data.objects:
        if obj.modifiers:
            for mod in obj.modifiers:
                if mod.type == 'NODES' and mod.node_group:
                    node_group_name = mod.node_group.name
                    
                    if node_group_name in groups_to_replace:
                        new_group = None
                        for ng in bpy.data.node_groups:
                            if ng.name == node_group_name and ng.library:
                                lib_filename = os.path.basename(ng.library.filepath)
                                if lib_filename == target_blend_name:
                                    new_group = ng
                                    break
                        
                        if new_group:
                            old_lib = "Local"
                            if mod.node_group.library:
                                old_lib = os.path.basename(mod.node_group.library.filepath)
                            mod.node_group = new_group
                            replaced_count += 1
                            print(f"  ✓ Object '{obj.name}' modifier: '{node_group_name}' ({old_lib} → {target_blend_name})")
                        elif node_group_name not in missing_groups:
                            not_found_count += 1
                    
                    # Thay thế các node groups BÊN TRONG geometry node tree
                    if mod.node_group and hasattr(mod.node_group, 'nodes'):
                        for node in mod.node_group.nodes:
                            if node.type == 'GROUP' and node.node_tree:
                                nested_group_name = node.node_tree.name
                                
                                if nested_group_name in groups_to_replace:
                                    new_nested_group = None
                                    for ng in bpy.data.node_groups:
                                        if ng.name == nested_group_name and ng.library:
                                            lib_filename = os.path.basename(ng.library.filepath)
                                            if lib_filename == target_blend_name:
                                                new_nested_group = ng
                                                break
                                    
                                    if new_nested_group and node.node_tree != new_nested_group:
                                        old_lib = "Local"
                                        if node.node_tree.library:
                                            old_lib = os.path.basename(node.node_tree.library.filepath)
                                        node.node_tree = new_nested_group
                                        replaced_count += 1
                                        print(f"  ✓ Object '{obj.name}' → nested: '{nested_group_name}' ({old_lib} → {target_blend_name})")
    
    # Bước 5: Thay thế nested node groups trong TẤT CẢ node groups
    print("\nĐang thay thế nested node groups trong các Node Groups...")
    
    # Lặp lại nhiều lần để xử lý nested sâu
    max_iterations = 5
    for iteration in range(max_iterations):
        iteration_replaced = 0
        
        for ng in bpy.data.node_groups:
            if not hasattr(ng, 'nodes'):
                continue
                
            for node in ng.nodes:
                if node.type == 'GROUP' and node.node_tree:
                    node_group_name = node.node_tree.name
                    
                    if node_group_name in groups_to_replace:
                        # Kiểm tra xem đã đúng target chưa
                        current_is_target = False
                        if node.node_tree.library:
                            current_lib = os.path.basename(node.node_tree.library.filepath)
                            if current_lib == target_blend_name:
                                current_is_target = True
                        
                        if not current_is_target:
                            new_group = None
                            for ng_candidate in bpy.data.node_groups:
                                if ng_candidate.name == node_group_name and ng_candidate.library:
                                    lib_filename = os.path.basename(ng_candidate.library.filepath)
                                    if lib_filename == target_blend_name:
                                        new_group = ng_candidate
                                        break
                            
                            if new_group and node.node_tree != new_group:
                                old_lib = "Local"
                                if node.node_tree.library:
                                    old_lib = os.path.basename(node.node_tree.library.filepath)
                                node.node_tree = new_group
                                replaced_count += 1
                                iteration_replaced += 1
                                
                                ng_display_name = ng.name
                                if ng.library:
                                    ng_lib = os.path.basename(ng.library.filepath)
                                    ng_display_name = f"{ng.name} ({ng_lib})"
                                
                                print(f"  ✓ Inside '{ng_display_name}': '{node_group_name}' ({old_lib} → {target_blend_name})")
        
        # Nếu không còn gì để thay thế thì dừng
        if iteration_replaced == 0:
            if iteration > 0:
                print(f"  → Hoàn thành sau {iteration + 1} vòng lặp")
            break
    
    print(f"\n{'='*60}")
    print(f"KẾT QUẢ:")
    print(f"{'='*60}")
    print(f"✓ Đã thay thế thành công: {replaced_count} node groups")
    if missing_groups:
        print(f"⚠ Không tìm thấy trong {target_blend_name}: {len(missing_groups)}")
    if not_found_count > 0:
        print(f"✗ Lỗi khác: {not_found_count}")
    print(f"{'='*60}\n")
    print(f"💡 Tip: Lưu file và reload để cập nhật hoàn toàn!")


# Sử dụng script
if __name__ == "__main__":
    # Chỉ cần tên file, không cần đường dẫn đầy đủ
    # Script sẽ tự động tìm đường dẫn từ các node groups đã được linked
    replace_linked_node_groups("LS Cherry.blend")