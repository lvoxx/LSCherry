bl_info = {
	"name": "VF Planar UV",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 5, 0),
	"blender": (2, 83, 0),
	"location": "Scene > VF Tools > Planar UV",
	"description": "Numerical planar projection of 3D meshes into UV space",
	"warning": "inexperienced developer, use at your own risk",
	"doc_url": "https://github.com/jeinselenVF/VF-BlenderPlanarUV",
	"tracker_url": "https://github.com/jeinselenVF/VF-BlenderPlanarUV/issues",
	"category": "3D View"}

# Based in part on basic code found here:
# https://blenderartists.org/t/set-face-uv-coordinates-while-in-edit-mode/1317947
# https://blender.stackexchange.com/questions/9399/add-uv-layer-to-mesh-add-uv-coords-with-python
# https://blender.stackexchange.com/questions/30421/create-a-radio-button-via-python
# https://gifguide2code.com/2017/05/14/python-how-to-loop-through-every-vertex-in-a-mesh/

import bpy
import bmesh
from mathutils import Vector

###########################################################################
# Main class

class vf_planar_uv(bpy.types.Operator):
	bl_idname = "vfplanaruv.set"
	bl_label = "Set UV Map"
	bl_description = "Numerical planar projection of 3D meshes into UV space"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		if not context.view_layer.objects.active.data.vertices:
			return {'CANCELLED'}
		
		# Set up local variables
		axis = context.scene.vf_planar_uv_settings.projection_axis
		world = True if context.scene.vf_planar_uv_settings.projection_space == "W" else False
		rotation = context.scene.vf_planar_uv_settings.projection_rotation
		flip = float(context.scene.vf_planar_uv_settings.projection_flip)
		align = float(context.scene.vf_planar_uv_settings.projection_align)
		centre = context.scene.vf_planar_uv_settings.projection_centre
		size = context.scene.vf_planar_uv_settings.projection_size
		
		# Prevent divide by zero errors
		size[0] = size[0] if size[0] > 0.0 else 1.0
		size[1] = size[1] if size[1] > 0.0 else 1.0
		size[2] = size[2] if size[2] > 0.0 else 1.0
		
		# Save current mode
		mode = context.active_object.mode
		# Switch to edit mode
		bpy.ops.object.mode_set(mode='EDIT')
		
		# Get object
		obj = context.active_object
		mat = obj.matrix_world
		bm = bmesh.from_edit_mesh(obj.data)
		# Get UV map
		uv_layer = bm.loops.layers.uv.verify()
		
		# Loop through faces
		U = 0.0
		V = 0.0
		for f in bm.faces:
			if f.select:
				for l in f.loops:
					# Process input coordinates
					# Use copy() to prevent changes to the source vertex coordinates
					pos = l.vert.co.copy()
					
					# Convert to world space if enabled
					if world:
						pos = mat @ pos
					
					pos[0] = (pos[0] - centre[0]) / size[0]
					pos[1] = (pos[1] - centre[1]) / size[1]
					pos[2] = (pos[2] - centre[2]) / size[2]
					
					# Projection Axis
					if axis == "X":
						U = pos[1]
						V = pos[2]
					elif axis == "Y":
						U = pos[0]
						V = pos[2]
					else: # axis == "Z"
						U = pos[0]
						V = pos[1]
					
					# Projection Rotation
					if "YX" in rotation:
						U, V = V, U
						U *= -1.0
					if "-" in rotation:
						U *= -1.0
						V *= -1.0
					
					# Projection Flip
					U *= flip
					
					# Set UV map values with image centre or zero point alignment
					l[uv_layer].uv = (U + align, V + align)
		
		# Update mesh
		bmesh.update_edit_mesh(obj.data)
		
		# Reset object mode to original
		bpy.ops.object.mode_set(mode=mode)
		
		# Done
		return {'FINISHED'}

class vf_load_selection(bpy.types.Operator):
	bl_idname = "vfloadselection.set"
	bl_label = "Load Selection Settings"
	bl_description = "Set the Centre and Size variables to the bounding box of the selected geometry"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		if not context.view_layer.objects.active.data.vertices:
			return {'CANCELLED'}
		
		# Save current mode
		mode = context.active_object.mode
		# Switch to edit mode
		bpy.ops.object.mode_set(mode='EDIT')
		
		# Get object data
		obj = context.active_object
		mat = obj.matrix_world
		mesh = bmesh.from_edit_mesh(obj.data)
		
		# Loop through selected vertices and find the minimum/maximum positions
		min_co = Vector((float("inf"), float("inf"), float("inf")))
		max_co = Vector((float("-inf"), float("-inf"), float("-inf")))
		for vert in mesh.verts:
			if vert.select:
				min_co.x = min(min_co.x, vert.co.x)
				min_co.y = min(min_co.y, vert.co.y)
				min_co.z = min(min_co.z, vert.co.z)
				max_co.x = max(max_co.x, vert.co.x)
				max_co.y = max(max_co.y, vert.co.y)
				max_co.z = max(max_co.z, vert.co.z)
		
		# Convert to world space if enabled
		if context.scene.vf_planar_uv_settings.projection_space == "W":
			min_co = mat @ min_co
			max_co = mat @ max_co
		
		# Calculate bounding box and centre point
		centr = (min_co + max_co) * 0.5
		max_co = max_co - min_co
		
		# Prevent zero scale entries
		if max_co.x == 0:
			max_co.x = 1.0
		if max_co.y == 0:
			max_co.y = 1.0
		if max_co.z == 0:
			max_co.z = 1.0
		
		# Set local variables
		context.scene.vf_planar_uv_settings.projection_centre = centr
		context.scene.vf_planar_uv_settings.projection_size = max_co
		
		# Reset object mode to original
		bpy.ops.object.mode_set(mode=mode)
		
		# Done
		return {'FINISHED'}

###########################################################################
# Project settings and UI rendering classes

class vfPlanarUvSettings(bpy.types.PropertyGroup):
	projection_axis: bpy.props.EnumProperty(
		name='Axis',
		description='Planar projection axis',
		items=[
			('X', 'X', 'X axis projection'),
			('Y', 'Y', 'Y axis projection'),
			('Z', 'Z', 'Z axis projection')
			],
		default='X')
	projection_centre: bpy.props.FloatVectorProperty(
		name="Centre",
		description="Centre of the planar projection mapping area",
		subtype="TRANSLATION",
		default=[0.0, 0.0, 0.0],
		step=1.25,
		precision=3)
	projection_size: bpy.props.FloatVectorProperty(
		name="Size",
		description="Size of the planar projection mapping area",
		subtype="TRANSLATION",
		default=[1.0, 1.0, 1.0],
		step=1.25,
		precision=3)
	projection_space: bpy.props.EnumProperty(
		name='Space',
		description='Planar projection coordinate space',
		items=[
			('L', 'Local', 'Projection using local space'),
			('W', 'World', 'Projection using world space')
			],
		default='L')
	projection_rotation: bpy.props.EnumProperty(
		name='Rotation',
		description='Planar projection axis',
		items=[
			('+XY', '0°', 'XY orientation projection'),
			('+YX', '90', 'YX orientation projection'),
			('-XY', '180', '-XY orientation projection'),
			('-YX', '270', '-YX orientation projection')
			],
		default='+XY')
	projection_flip: bpy.props.EnumProperty(
		name='Flip',
		description='Planar projection axis',
		items=[
			('1.0', 'Front', 'Projection from positive direction'),
			('-1.0', 'Back', 'Projection from negative direction')
			],
		default='1.0')
	projection_align: bpy.props.EnumProperty(
		name='Alignment',
		description='UV map alignment',
		items=[
			('0.5', 'Image', 'Align mapped geometry centre to UV 0.5, 0.5'),
			('0.0', 'Zero', 'Align mapped geometry centre to UV 0.0, 0.0')
			],
		default='0.5')

class VFTOOLS_PT_planar_uv(bpy.types.Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_category = 'VF Tools'
	bl_order = 10
	bl_options = {'DEFAULT_CLOSED'}
	
	@classmethod
	def poll(cls, context):
		return True

class VFTOOLS_PT_planar_uv_main(VFTOOLS_PT_planar_uv, bpy.types.Panel):
	bl_idname = "VFTOOLS_PT_planar_uv"
	bl_label = "Planar UV"
	
	def draw_header(self, context):
		try:
			layout = self.layout
		except Exception as exc:
			print(str(exc) + " | Error in VF Planar UV panel header")
	
	def draw(self, context):
		try:
			layout = self.layout
			layout.use_property_split = True
			layout.use_property_decorate = False # No animation
			layout.prop(context.scene.vf_planar_uv_settings, 'projection_axis', expand=True)
			
			col = layout.column()
			col.prop(context.scene.vf_planar_uv_settings, 'projection_centre')
			col = layout.column()
			col.prop(context.scene.vf_planar_uv_settings, 'projection_size')
			
			layout.prop(context.scene.vf_planar_uv_settings, 'projection_space', expand=True)
			
			button = layout.row()
			if not (context.view_layer.objects.active and context.view_layer.objects.active.type == "MESH"):
				button.active = False
				button.enabled = False
			button.operator(vf_planar_uv.bl_idname, icon="GROUP_UVS")
		except Exception as exc:
			print(str(exc) + " | Error in VF Planar UV panel")

class VFTOOLS_PT_planar_uv_advanced(VFTOOLS_PT_planar_uv, bpy.types.Panel):
	bl_idname = "VFTOOLS_PT_planar_uv_advanced"
	bl_parent_id = "VFTOOLS_PT_planar_uv"
	bl_label = "Advanced"
	bl_options = {'DEFAULT_CLOSED'}
	
	def draw_header(self, context):
		try:
			layout = self.layout
		except Exception as exc:
			print(str(exc) + " | Error in VF Planar UV panel header")
	
	def draw(self, context):
		try:
			layout = self.layout
			layout.use_property_split = True
			layout.use_property_decorate = False # No animation
			
			button = layout.row()
			if not (context.view_layer.objects.active and context.view_layer.objects.active.type == "MESH"):
				button.active = False
				button.enabled = False
			button.operator(vf_load_selection.bl_idname, icon="SHADING_BBOX")
			
			layout.prop(context.scene.vf_planar_uv_settings, 'projection_rotation', expand=True)
			layout.prop(context.scene.vf_planar_uv_settings, 'projection_flip', expand=True)
			layout.prop(context.scene.vf_planar_uv_settings, 'projection_align', expand=True)
		except Exception as exc:
			print(str(exc) + " | Error in VF Planar UV Advanced panel")

classes = (vf_planar_uv, vf_load_selection, vfPlanarUvSettings, VFTOOLS_PT_planar_uv_main, VFTOOLS_PT_planar_uv_advanced)

###########################################################################
# Addon registration functions

def register():
	for cls in classes:
		bpy.utils.register_class(cls)
	bpy.types.Scene.vf_planar_uv_settings = bpy.props.PointerProperty(type=vfPlanarUvSettings)

def unregister():
	for cls in reversed(classes):
		bpy.utils.unregister_class(cls)
	del bpy.types.Scene.vf_planar_uv_settings

if __name__ == "__main__":
	register()