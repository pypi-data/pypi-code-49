import bpy

from kabaret.app.session import KabaretSession

from .flow_view import FlowView


class BlenderEmbeddedSession(KabaretSession):
    def __init__(self, home_oid, session_name, debug=False):
        super(BlenderEmbeddedSession, self).__init__(session_name, debug)
        self.home_oid = home_oid

    def register_view_types(self):
        super(BlenderEmbeddedSession, self).register_view_types()

        type_name = self.register_view_type(FlowView)
        self.add_view(type_name)

    def _blender_tick(self):
        self.tick()
        return 0.1

    def start(self):
        print("Starting KaBlender")
        self.register_view_types()

        bpy.app.timers.register(self._blender_tick, persistent=True)
        print(
            ">>>>> KaBlender Started", bpy.app.timers.is_registered(self._blender_tick)
        )
