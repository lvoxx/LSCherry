import bpy
import os
import re
from pathlib import Path

class NodeGroupPluginGenerator:
    """Generate standalone Python files from Blender node groups"""
    
    # Node types that should be treated as inputs
    INPUT_NODE_TYPES = {
        'ShaderNodeTexImage': 'image',
        'ShaderNodeUVMap': 'uv',
        'ShaderNodeAttribute': 'attribute',
        'GeometryNodeImageTexture': 'image',
        'GeometryNodeInputNamedAttribute': 'attribute',
        'FunctionNodeInputVector': 'vector',
        'FunctionNodeInputColor': 'color',
    }
    
    def __init__(self):
        self.generated_code = []
        
    def sanitize_var_name(self, name):
        """Convert any string to valid Python variable name"""
        if not name:
            return 'var'
        
        # Replace all non-alphanumeric chars with underscore
        var_name = re.sub(r'\W+', '_', name)
        
        # Remove leading/trailing underscores
        var_name = var_name.strip('_')
        
        # Ensure doesn't start with number
        if var_name and var_name[0].isdigit():
            var_name = 'node_' + var_name
        
        # Ensure not empty
        if not var_name:
            var_name = 'var'
        
        return var_name
    
    def get_socket_type(self, socket):
        """Get socket type identifier"""
        type_map = {
            'NodeSocketFloat': 'Float',
            'NodeSocketFloatFactor': 'Float',
            'NodeSocketInt': 'Int',
            'NodeSocketBool': 'Bool',
            'NodeSocketVector': 'Vector',
            'NodeSocketVectorXYZ': 'Vector',
            'NodeSocketColor': 'Color',
            'NodeSocketShader': 'Shader',
            'NodeSocketGeometry': 'Geometry',
            'NodeSocketMaterial': 'Material',
            'NodeSocketImage': 'Image',
            'NodeSocketString': 'String',
            'NodeSocketClosure': 'Closure',
        }
        
        # Blender 4.0+ interface sockets have socket_type instead of bl_idname
        if hasattr(socket, 'socket_type'):
            socket_type = socket.socket_type
            # Remove 'NodeSocket' prefix if present
            if socket_type.startswith('NodeSocket'):
                return socket_type.replace('NodeSocket', '')
            return type_map.get(socket_type, 'Value')
        elif hasattr(socket, 'bl_idname'):
            return type_map.get(socket.bl_idname, 'Value')
        else:
            # Fallback: try to get type from class name
            class_name = socket.__class__.__name__
            if 'Float' in class_name:
                return 'Float'
            elif 'Int' in class_name:
                return 'Int'
            elif 'Vector' in class_name:
                return 'Vector'
            elif 'Color' in class_name:
                return 'Color'
            return 'Value'
    
    def is_empty_input_node(self, node):
        """Check if node should be treated as external input"""
        node_type = node.bl_idname
        
        # Image nodes without image data
        if node_type == 'ShaderNodeTexImage':
            return node.image is None
        
        # Geometry Image Texture without image
        if node_type == 'GeometryNodeImageTexture':
            return not hasattr(node, 'image') or node.image is None
        
        # UV Map without specific UV layer
        if node_type == 'ShaderNodeUVMap':
            return node.uv_map == ''
        
        # Attribute without name (check for different attribute properties in Blender 4.x)
        if node_type == 'ShaderNodeAttribute':
            return hasattr(node, 'attribute_name') and node.attribute_name == ''
        
        # Geometry Named Attribute (Blender 4.3+)
        if node_type == 'GeometryNodeInputNamedAttribute':
            if hasattr(node, 'inputs') and len(node.inputs) > 0:
                name_socket = node.inputs.get('Name')
                if name_socket:
                    if hasattr(name_socket, 'default_value'):
                        return name_socket.default_value == ''
                    return True
            if hasattr(node, 'attribute_name'):
                return node.attribute_name == ''
            return False
        
        return False
    
    def generate_socket_variable_name(self, socket_name):
        """Generate valid Python variable name from socket name"""
        # Replace invalid characters with underscore
        var_name = socket_name.replace(" ", "_").replace(".", "_").replace("-", "_")
        var_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in var_name)
        
        # Ensure doesn't start with number
        if var_name and var_name[0].isdigit():
            var_name = 'socket_' + var_name
        
        # Ensure not empty
        if not var_name:
            var_name = 'socket'
        
        return var_name
        """Get socket type identifier"""
        type_map = {
            'NodeSocketFloat': 'Float',
            'NodeSocketFloatFactor': 'Float',
            'NodeSocketInt': 'Int',
            'NodeSocketBool': 'Bool',
            'NodeSocketVector': 'Vector',
            'NodeSocketVectorXYZ': 'Vector',
            'NodeSocketColor': 'Color',
            'NodeSocketShader': 'Shader',
            'NodeSocketGeometry': 'Geometry',
            'NodeSocketMaterial': 'Material',
            'NodeSocketImage': 'Image',
            'NodeSocketString': 'String',
            'NodeSocketClosure': 'Closure',
        }
        
        # Blender 4.0+ interface sockets have socket_type instead of bl_idname
        if hasattr(socket, 'socket_type'):
            socket_type = socket.socket_type
            # Remove 'NodeSocket' prefix if present
            if socket_type.startswith('NodeSocket'):
                return socket_type.replace('NodeSocket', '')
            return type_map.get(socket_type, 'Value')
        elif hasattr(socket, 'bl_idname'):
            return type_map.get(socket.bl_idname, 'Value')
        else:
            # Fallback: try to get type from class name
            class_name = socket.__class__.__name__
            if 'Float' in class_name:
                return 'Float'
            elif 'Int' in class_name:
                return 'Int'
            elif 'Vector' in class_name:
                return 'Vector'
            elif 'Color' in class_name:
                return 'Color'
            return 'Value'
    
    def get_default_value(self, socket):
        """Get default value for socket"""
        try:
            if hasattr(socket, 'default_value'):
                val = socket.default_value
                if hasattr(val, '__iter__') and not isinstance(val, str):
                    return tuple(val)
                return val
        except:
            pass
        
        # Try to get from default_value attribute for interface sockets
        try:
            if hasattr(socket, 'default_value'):
                return socket.default_value
        except:
            pass
            
        return None
    
    def analyze_node_group(self, node_group):
        """Analyze node group and identify inputs/outputs"""
        inputs = []
        outputs = []
        internal_nodes = []
        empty_input_nodes = []
        
        # Analyze nodes
        for node in node_group.nodes:
            if node.bl_idname == 'NodeGroupInput':
                continue
            elif node.bl_idname == 'NodeGroupOutput':
                continue
            elif self.is_empty_input_node(node):
                # Store empty input node info
                empty_input_nodes.append({
                    'type': node.bl_idname,
                    'name': node.label or node.name,
                    'node': node
                })
            else:
                internal_nodes.append(node)
        
        # Get outputs from group output node
        for node in node_group.nodes:
            if node.bl_idname == 'NodeGroupOutput':
                for input_socket in node.inputs:
                    if input_socket.is_linked:
                        outputs.append({
                            'name': input_socket.name,
                            'type': self.get_socket_type(input_socket)
                        })
        
        # Get inputs from interface (Blender 4.0+)
        if hasattr(node_group, 'interface') and hasattr(node_group.interface, 'items_tree'):
            try:
                for item in node_group.interface.items_tree:
                    # Check if item is a socket (not a panel or other type)
                    if hasattr(item, 'in_out'):
                        if item.in_out == 'INPUT':
                            socket_type = self.get_socket_type(item)
                            default_val = None
                            try:
                                if hasattr(item, 'default_value'):
                                    val = item.default_value
                                    if hasattr(val, '__iter__') and not isinstance(val, str):
                                        default_val = tuple(val)
                                    else:
                                        default_val = val
                            except:
                                pass
                            
                            inputs.append({
                                'name': item.name,
                                'type': socket_type,
                                'default': default_val
                            })
            except Exception as e:
                print(f"Warning: Could not read interface items: {e}")
        
        # Fallback: Get inputs from NodeGroupInput node
        if not inputs:
            for node in node_group.nodes:
                if node.bl_idname == 'NodeGroupInput':
                    for output in node.outputs:
                        if output.is_linked and output.name != '':
                            inputs.append({
                                'name': output.name,
                                'type': self.get_socket_type(output),
                                'default': self.get_default_value(output)
                            })
        
        # Fallback: Get outputs from NodeGroupOutput node if empty
        if not outputs:
            for node in node_group.nodes:
                if node.bl_idname == 'NodeGroupOutput':
                    for input_socket in node.inputs:
                        if input_socket.name != '':
                            outputs.append({
                                'name': input_socket.name,
                                'type': self.get_socket_type(input_socket)
                            })
        
        return inputs, outputs, internal_nodes, empty_input_nodes
    
    def generate_node_construction_code(self, node_group):
        """Generate code to reconstruct node group structure"""
        code = []
        node_var_map = {}
        var_counter = 0
        
        # Create internal nodes
        for node in node_group.nodes:
            if node.bl_idname in ['NodeGroupInput', 'NodeGroupOutput']:
                continue
            
            # Sanitize node name for variable
            base_name = self.sanitize_var_name(node.name if node.name else f"node_{var_counter}")
            var_name = f"{base_name}"
            
            # Ensure unique variable name
            original_var = var_name
            counter = 1
            while var_name in node_var_map.values():
                var_name = f"{original_var}_{counter}"
                counter += 1
            
            node_var_map[node] = var_name
            var_counter += 1
            
            code.append(f"        {var_name} = nt.nodes.new('{node.bl_idname}')")
            code.append(f"        {var_name}.location = ({node.location.x}, {node.location.y})")
            
            if node.label:
                # Escape quotes in label
                label_escaped = node.label.replace("\\", "\\\\").replace('"', '\\"')
                code.append(f"        {var_name}.label = \"{label_escaped}\"")
            if node.name:
                # Escape quotes in name
                name_escaped = node.name.replace("\\", "\\\\").replace('"', '\\"')
                code.append(f"        {var_name}.name = \"{name_escaped}\"")
            
            # Set node properties
            if hasattr(node, 'operation') and node.operation:
                code.append(f"        {var_name}.operation = '{node.operation}'")
            if hasattr(node, 'blend_type') and node.blend_type:
                code.append(f"        {var_name}.blend_type = '{node.blend_type}'")
            if hasattr(node, 'color_space') and node.color_space:
                code.append(f"        {var_name}.color_space = '{node.color_space}'")
            if hasattr(node, 'interpolation') and node.interpolation:
                code.append(f"        {var_name}.interpolation = '{node.interpolation}'")
            
            # Special handling for specific node types
            if node.bl_idname == 'ShaderNodeTangent' and hasattr(node, 'direction_type'):
                code.append(f"        {var_name}.direction_type = '{node.direction_type}'")
            if node.bl_idname == 'ShaderNodeVectorTransform' and hasattr(node, 'convert_to'):
                code.append(f"        {var_name}.convert_to = '{node.convert_to}'")
            if node.bl_idname in ['GeometryNodeRepeatInput', 'GeometryNodeRepeatOutput']:
                # Will handle pairing later
                pass
            
            code.append("")
        
        # Handle RepeatInput/Output pairing
        repeat_pairs = []
        for node in node_group.nodes:
            if node.bl_idname == 'GeometryNodeRepeatInput':
                repeat_input_var = node_var_map.get(node)
                # Find corresponding output
                for other_node in node_group.nodes:
                    if other_node.bl_idname == 'GeometryNodeRepeatOutput':
                        repeat_output_var = node_var_map.get(other_node)
                        repeat_pairs.append((repeat_input_var, repeat_output_var, node, other_node))
                        break
        
        # Generate repeat pairing code
        for input_var, output_var, input_node, output_node in repeat_pairs:
            code.append(f"        # Pair repeat nodes")
            code.append(f"        {input_var}.pair_with_output({output_var})")
            # Add repeat items from output node
            if hasattr(output_node, 'repeat_items'):
                for item in output_node.repeat_items:
                    code.append(f"        {output_var}.repeat_items.new('{item.socket_type}', '{item.name}')")
            code.append("")
        
        # Create links
        code.append("        # Create internal links")
        for link in node_group.links:
            from_node = link.from_node
            to_node = link.to_node
            
            if from_node.bl_idname == 'NodeGroupInput':
                from_ref = "GroupInput"
            elif from_node in node_var_map:
                from_ref = node_var_map[from_node]
            else:
                continue
            
            if to_node.bl_idname == 'NodeGroupOutput':
                to_ref = "GroupOutput"
            elif to_node in node_var_map:
                to_ref = node_var_map[to_node]
            else:
                continue
            
            from_socket_idx = list(from_node.outputs).index(link.from_socket)
            to_socket_idx = list(to_node.inputs).index(link.to_socket)
            
            code.append(f"        nt.links.new({from_ref}.outputs[{from_socket_idx}], {to_ref}.inputs[{to_socket_idx}])")
        
        # Set default values for unconnected inputs
        code.append("")
        code.append("        # Set default values")
        for node in node_group.nodes:
            if node.bl_idname in ['NodeGroupInput', 'NodeGroupOutput']:
                continue
            if node not in node_var_map:
                continue
                
            var_name = node_var_map[node]
            for idx, input_socket in enumerate(node.inputs):
                if not input_socket.is_linked:
                    try:
                        default_val = self.get_default_value(input_socket)
                        if default_val is not None:
                            code.append(f"        {var_name}.inputs[{idx}].default_value = {repr(default_val)}")
                    except:
                        pass
        
        return "\n".join(code)
    
    def generate_node_class(self, node_group, tree_type):
        """Generate complete node class file"""
        inputs, outputs, internal_nodes, empty_nodes = self.analyze_node_group(node_group)
        
        safe_name = "".join(c if c.isalnum() else "_" for c in node_group.name)
        class_name = f"ShaderNode{safe_name}" if tree_type == 'ShaderNodeTree' else f"GeometryNode{safe_name}"
        
        # Determine base class
        base_class = "ShaderNode" if tree_type == 'ShaderNodeTree' else "GeometryNode"
        
        # Generate properties for empty input nodes
        properties = []
        for empty_node in empty_nodes:
            if empty_node['type'] == 'ShaderNodeTexImage':
                properties.append({
                    'name': 'image',
                    'type': 'PointerProperty',
                    'prop_type': 'bpy.types.Image',
                    'label': 'Image'
                })
            elif empty_node['type'] == 'ShaderNodeUVMap':
                properties.append({
                    'name': 'uv_map',
                    'type': 'StringProperty',
                    'label': 'UV Map',
                    'default': ''
                })
        
        code = [
            "import bpy",
            "import sys",
            "from pathlib import Path",
            "",
            "# Import utils (handle both relative and absolute imports)",
            "try:",
            "    from ..utils import ShaderNode" if tree_type == 'ShaderNodeTree' else "    from ..utils import GeometryNode",
            "except ImportError:",
            "    # Fallback for direct execution",
            "    import importlib.util",
            "    utils_path = Path(__file__).parent.parent / 'utils.py'",
            "    spec = importlib.util.spec_from_file_location('utils', utils_path)",
            "    utils = importlib.util.module_from_spec(spec)",
            "    spec.loader.exec_module(utils)",
            "    ShaderNode = utils.ShaderNode" if tree_type == 'ShaderNodeTree' else "    GeometryNode = utils.GeometryNode",
            "",
            "",
            f"class {class_name}({base_class}):",
            f"    bl_idname = '{class_name}'",
            f"    bl_label = \"{node_group.name}\"",
            "    bl_icon = \"NODETREE\"",
            "",
        ]
        
        # Add properties
        for prop in properties:
            if prop['type'] == 'PointerProperty':
                code.extend([
                    f"    {prop['name']}: bpy.props.PointerProperty(",
                    f"        name=\"{prop['label']}\",",
                    f"        type={prop['prop_type']},",
                    f"        description=\"{prop['label']} for this node\",",
                    "        update=lambda self, context: self.valuesUpdate(context),",
                    "    )",
                    ""
                ])
            elif prop['type'] == 'StringProperty':
                code.extend([
                    f"    {prop['name']}: bpy.props.StringProperty(",
                    f"        name=\"{prop['label']}\",",
                    f"        description=\"{prop['label']} for this node\",",
                    f"        default=\"{prop.get('default', '')}\",",
                    "        update=lambda self, context: self.valuesUpdate(context),",
                    "    )",
                    ""
                ])
        
        # Generate init method
        code.extend([
            "    def init(self, context):",
            "        self.getNodetree(self.name + '_node_tree')",
        ])
        
        # Set default values for inputs
        for inp in inputs:
            if 'default' in inp and inp['default'] is not None:
                code.append(f"        self.inputs[\"{inp['name']}\"].default_value = {repr(inp['default'])}")
        
        code.append("")
        
        # Generate draw_buttons if properties exist
        if properties:
            code.extend([
                "    def draw_buttons(self, context, layout):",
                "        super().draw_buttons(context, layout)",
            ])
            for prop in properties:
                if prop['name'] == 'image':
                    code.append(f"        layout.template_ID(self, \"{prop['name']}\", open=\"image.open\")")
                elif prop['name'] == 'uv_map':
                    code.extend([
                        "        if context.active_object and context.active_object.data and hasattr(context.active_object.data, 'uv_layers'):",
                        f"            layout.prop_search(self, \"{prop['name']}\", context.active_object.data, \"uv_layers\", text=\"UV Map\")",
                        "        else:",
                        f"            layout.prop(self, \"{prop['name']}\", text=\"UV Map\")",
                    ])
            code.append("")
        
        # Generate createNodetree method
        code.extend([
            "    def createNodetree(self, name):",
            f"        nt = self.node_tree = bpy.data.node_groups.new('.'+name, '{tree_type}')",
            "        nt.color_tag = 'CONVERTER'",
            f"        nt.description = '{node_group.name}'",
            "",
        ])
        
        # Add outputs
        code.append("        # Create output sockets")
        for out in outputs:
            socket_type = f"NodeSocket{out['type']}"
            code.append(f"        nt.interface.new_socket('{out['name']}', in_out='OUTPUT', socket_type='{socket_type}')")
        
        code.append("")
        
        # Add inputs
        code.append("        # Create input sockets")
        for inp in inputs:
            socket_type = f"NodeSocket{inp['type']}"
            if 'default' in inp and inp['default'] is not None:
                code.append(f"        input_socket = nt.interface.new_socket('{inp['name']}', in_out='INPUT', socket_type='{socket_type}')")
                code.append(f"        input_socket.default_value = {repr(inp['default'])}")
            else:
                code.append(f"        nt.interface.new_socket('{inp['name']}', in_out='INPUT', socket_type='{socket_type}')")
        
        code.extend([
            "",
            "        # Build node tree",
            "        self.rebuildNodetree(None)",
        ])
        
        if properties:
            code.append("        self.valuesUpdate(None)")
        
        code.extend([
            "",
            "    def rebuildNodetree(self, context):",
            "        if context is not None:",
            "            if self.node_tree.users > 1:",
            "                self.duplicate()",
            "",
            "        nt = self.node_tree",
            "",
            "        # Clear existing nodes",
            "        for node in list(nt.nodes):",
            "            nt.nodes.remove(node)",
            "",
            "        # Create group input/output",
            "        GroupInput = nt.nodes.new('NodeGroupInput')",
            "        GroupInput.location = (-400, 0)",
            "        GroupOutput = nt.nodes.new('NodeGroupOutput')",
            "        GroupOutput.location = (400, 0)",
            "",
        ])
        
        # Add node construction code (already properly indented)
        construction = self.generate_node_construction_code(node_group)
        code.append(construction)
        
        # Add duplicate method
        code.extend([
            "",
            "    def duplicate(self):",
            "        self.node_tree = self.node_tree.copy()",
            ""
        ])
        
        # Add valuesUpdate if properties exist
        if properties:
            code.extend([
                "    def valuesUpdate(self, context):",
                "        if self.node_tree.users > 1:",
                "            self.duplicate()",
                "",
                "        for node in self.node_tree.nodes:",
            ])
            
            for prop in properties:
                if prop['name'] == 'image':
                    code.extend([
                        "            if node.type == 'TEX_IMAGE':",
                        f"                node.image = self.{prop['name']}",
                    ])
                elif prop['name'] == 'uv_map':
                    code.extend([
                        f"            if hasattr(node, 'uv_map') and self.{prop['name']}:",
                        f"                node.uv_map = self.{prop['name']}",
                    ])
            code.append("")
        
        return "\n".join(code)
    
    def generate_file(self, output_path):
        """Generate complete Python file with all node groups"""
        
        processed_groups = []
        
        # Process all node groups
        for node_tree in bpy.data.node_groups:
            tree_type = node_tree.bl_idname
            
            if tree_type in ['ShaderNodeTree', 'GeometryNodeTree']:
                try:
                    node_code = self.generate_node_class(node_tree, tree_type)
                    
                    safe_name = "".join(c if c.isalnum() else "_" for c in node_tree.name)
                    file_name = f"{safe_name}.py"
                    file_path = os.path.join(output_path, file_name)
                    
                    # Write individual file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(node_code)
                    
                    processed_groups.append({
                        'name': node_tree.name,
                        'tree_type': tree_type,
                        'file_name': file_name,
                        'class_name': f"ShaderNode{safe_name}" if tree_type == 'ShaderNodeTree' else f"GeometryNode{safe_name}"
                    })
                except Exception as e:
                    print(f"Error processing {node_tree.name}: {str(e)}")
                    import traceback
                    traceback.print_exc()
        
        # Generate __init__.py for the shader module
        self.generate_init_file(output_path, processed_groups)
        
        return processed_groups
    
    def generate_init_file(self, output_path, processed_groups):
        """Generate __init__.py that imports all node classes"""
        init_code = ['"""Auto-generated node modules"""', '', '# Import all generated node classes']
        
        # Add imports
        for group in processed_groups:
            module_name = group['file_name'].replace('.py', '')
            class_name = group['class_name']
            init_code.append(f"from .{module_name} import {class_name}")
        
        # Add __all__
        init_code.extend(['', '__all__ = ['])
        for group in processed_groups:
            init_code.append(f'    "{group["class_name"]}",')
        init_code.append(']')
        
        # Write __init__.py
        init_path = os.path.join(output_path, '__init__.py')
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(init_code))
        
        print(f"✓ Generated __init__.py with {len(processed_groups)} imports")


# ============================================
# QUICK TEST EXECUTION
# ============================================

def run_generator():
    """Quick test function - run directly in Blender"""
    
    print("="*60)
    print("DEBUG: Starting node group analysis...")
    print("="*60)
    
    # Debug: Check all node groups
    print(f"\nTotal node groups in file: {len(bpy.data.node_groups)}")
    
    valid_types = ['ShaderNodeTree', 'GeometryNodeTree', 'CompositorNodeTree']
    print(f"\nNode groups by type:")
    type_counts = {}
    for ng in bpy.data.node_groups:
        ng_type = ng.bl_idname
        type_counts[ng_type] = type_counts.get(ng_type, 0) + 1
    
    for ng_type, count in type_counts.items():
        print(f"  - {ng_type}: {count}")
    
    valid_count = sum(1 for ng in bpy.data.node_groups if ng.bl_idname in ['ShaderNodeTree', 'GeometryNodeTree'])
    print(f"\nValid node groups for export: {valid_count}")
    
    if valid_count == 0:
        print("\n✗ ERROR: No valid node groups found!")
        print("  Valid types are: ShaderNodeTree, GeometryNodeTree")
        return
    
    # Get current blend file directory
    blend_file = bpy.data.filepath
    if not blend_file:
        print("\n✗ ERROR: Please save your .blend file first!")
        return
    
    blend_dir = os.path.dirname(blend_file)
    
    # Create dist/shader folder
    dist_folder = os.path.join(blend_dir, "dist", "nodes", "shader")
    os.makedirs(dist_folder, exist_ok=True)
    print(f"\nOutput folder: {dist_folder}")
    
    # Generate
    generator = NodeGroupPluginGenerator()
    
    try:
        processed = generator.generate_file(dist_folder)
        
        print("\n" + "="*60)
        print(f"✓ SUCCESS!")
        print(f"✓ Generated {len(processed)} node class files")
        print("="*60)
        
        print("\nGenerated files:")
        for item in processed:
            print(f"  - {item['file_name']} ({item['class_name']})")
        
        print("\n" + "="*60)
        print("Next steps:")
        print("  1. Copy the generated files to your addon's nodes/shader folder")
        print("  2. Make sure utils.py is in the parent folder")
        print("  3. Import in your addon using NodeLib")
        print("="*60)
        
    except Exception as e:
        print("="*60)
        print(f"✗ ERROR: {str(e)}")
        print("="*60)
        import traceback
        traceback.print_exc()


# Run the generator immediately when script is executed
if __name__ == "__main__":
    run_generator()