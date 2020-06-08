import bpy
from bpy.props import StringProperty

bl_info = {
    'name': "Trevor's Blender Add-on",
    'blender': (2,80,0),
    'category': 'Interface'
}

class OperatorGoToFrame(bpy.types.Operator):
    bl_idname = 'scene.gotoframe'
    bl_label = 'Go / jump to specific frame'
    bl_property = 'frame'
    
    frame: StringProperty(default = '1', name = "Frame number")
    
    def execute(self, context):
        self.report({'INFO'}, 'Set frame number to {}'.format(self.frame))
        context.scene.frame_set(int(self.frame))
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(OperatorGoToFrame)

def unregister():
    bpy.utils.unregister_class(OperatorGoToFrame)

if __name__ == '__main__':
    register()
