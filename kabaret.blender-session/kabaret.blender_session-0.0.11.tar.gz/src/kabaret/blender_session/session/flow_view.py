from __future__ import print_function

import json
import random
import bpy

import kabaret
from kabaret.app.ui.view import ViewMixin


#
#   PROPERTIES
#


class MappedItem(bpy.types.PropertyGroup):
    oid: bpy.props.StringProperty(name="oid")
    name: bpy.props.StringProperty(name="name")


class OpenStateProperties(bpy.types.PropertyGroup):

    name: bpy.props.StringProperty(name="name")
    open: bpy.props.BoolProperty(default=False)


_FIELDS_VALUE_CACHE = {}


class FlowFieldProperties(bpy.types.PropertyGroup):
    def on_map_expand_changed(self, context):
        if self.is_map_expanded:
            self.ensure_mapped_items_loaded()

    def _get_value(self):
        global _FIELDS_VALUE_CACHE
        try:
            value = _FIELDS_VALUE_CACHE[self.oid]
        except KeyError:
            pass
        else:
            print("Using cache", value, self.oid)
            return value

        print("GET VALUE FOR", self.oid)
        try:
            value = kabaret.session.cmds.Flow.get_value(self.oid)
        except Exception as err:
            print("!!!! Error getting value for {}: {}".format(self.oid, err))
            value = "!!! ERROR: " + str(err)

        _FIELDS_VALUE_CACHE[self.oid] = value
        return self._py_value_cache

    def _set_value(self, value):
        kabaret.session.cmds.Flow.set_value(self.oid, value)

    def touch_value(self):
        global _FIELDS_VALUE_CACHE
        del _FIELDS_VALUE_CACHE[self.oid]
        return

    def get_value(self):
        value = self._get_value()
        if isinstance(value, str):
            return value
        else:
            return repr(value)

    def get_bool_value(self):
        return self._get_value() and True or False

    def get_int_value(self):
        return int(self._get_value())

    def get_float_value(self):
        return float(self._get_value())

    def on_set(self, value):
        self._set_value(value)

    def on_bool_set(self, value):
        self._set_value(value)

    def on_int_set(self, value):
        self._set_value(value)

    def on_float_set(self, value):
        self._set_value(value)

    def ensure_mapped_items_loaded(self):
        if self.mapped_items:
            return
        print("================ !!FACKE!! FETCH MAPPED ITEMS", self.oid)
        oid = self.oid
        for i in range(random.randrange(10, 20)):
            item = self.mapped_items.add()
            name = "Item%i" % (i,)
            item.oid = oid + "/" + name
            item.name = name

    # Flow
    oid: bpy.props.StringProperty(default="Unknown")
    relation_type: bpy.props.StringProperty()
    is_action: bpy.props.BoolProperty()
    is_map: bpy.props.BoolProperty()
    is_map_expanded: bpy.props.BoolProperty(default=False, update=on_map_expand_changed)
    mapped_items: bpy.props.CollectionProperty(type=MappedItem)
    current_mapped_item: bpy.props.IntProperty()

    # UI
    icon: bpy.props.StringProperty(name="icon", default="")
    editor_type: bpy.props.StringProperty(name="editor_type", default="")
    editable: bpy.props.BoolProperty(name="editable")
    label: bpy.props.StringProperty(name="label", default="")
    group: bpy.props.StringProperty(name="label", default="")
    hidden: bpy.props.BoolProperty(name="hidden")
    tooltip: bpy.props.StringProperty(name="tooltip", default="")

    # Value
    # value_cache : bpy.props.StringProperty(name="value_cache")
    # value_cache_dirty : bpy.props.BoolProperty(name="value_cache_dirty", default=True)

    value: bpy.props.StringProperty(name="value", get=get_value, set=on_set)
    bool_value: bpy.props.BoolProperty(
        name="value", get=get_bool_value, set=on_bool_set
    )
    int_value: bpy.props.IntProperty(name="value", get=get_int_value, set=on_int_set)
    float_value: bpy.props.FloatProperty(
        name="value", get=get_float_value, set=on_float_set
    )


class FlowPageProperties(bpy.types.PropertyGroup):
    def update_all_VIEW_3D_TOOLS(self):
        all_3d_areas = []
        for screen in bpy.data.screens:
            # print('1', screen)
            for area in screen.areas:
                # print('2  ', area)
                for space in area.spaces:
                    # print('3  ', space)
                    if space.type == "VIEW_3D":
                        # print('+++AREA', area)
                        all_3d_areas.append(area)
                        break

        for area in all_3d_areas:
            if 0:
                # this does not redraw:
                for region in area.regions:
                    if region.type == "TOOLS":
                        # print(">>>>>>>>>>", region)
                        region.tag_redraw()
            else:
                # but this does:
                area.tag_redraw()

    def update_VIEW_3D(self, context):
        """ tag redraw on VIEW_3D areas"""
        type = "VIEW_3D"
        if not context.screen:
            return
        areas = [a for a in context.screen.areas if a.type == type]
        for area in areas:
            area.tag_redraw()

    def on_current_oid_changed(self, context):
        global _FIELDS_VALUE_CACHE
        _FIELDS_VALUE_CACHE.clear()
        bpy.context.window_manager.flow_page.fields.clear()
        oid = self.current_oid
        self.is_action = kabaret.session.cmds.Flow.is_action(oid)
        if self.is_action:
            self.action_buttons = json.dumps(None)
            self.action_needs_dialog = kabaret.session.cmds.Flow.action_needs_dialog(
                oid
            )
            if self.action_needs_dialog:
                self.action_buttons = json.dumps(
                    kabaret.session.cmds.Flow.get_action_buttons(oid)
                )
        related_list, mapped_names = kabaret.session.cmds.Flow.ls(
            oid or None, context="Blender.details"
        )
        group_name = set()
        for related in related_list:
            name, relation_type, is_action, is_map, ui = related
            field = bpy.context.window_manager.flow_page.fields.add()
            field.name = name
            # Flow
            field.oid = oid + "/" + name
            field.relation_type = relation_type
            field.is_action = is_action
            field.is_map = is_map
            # UI
            field.icon = ui.get("icon") or ""
            field.editor_type = ui.get("editor_type") or ""
            field.editable = ui.get("editable") or True
            field.label = ui.get("label") or name.replace("_", " ").title()
            group_name = ui.get("group") or ""
            field.group = group_name
            field.hidden = ui.get("hidden") or False
            field.tooltip = ui.get("tooltip") or ""

        self.update_VIEW_3D(context)

    home_oid: bpy.props.StringProperty(
        name="Flow Home oid",
        description="OID of the Tools Home page",
        update=update_VIEW_3D,
    )
    current_oid: bpy.props.StringProperty(
        name="Flow Page Current OID",
        description="The oid of the displayed tool",
        update=on_current_oid_changed,
    )
    is_action: bpy.props.BoolProperty(
        name="Flow Page Is Action", description="What name says",
    )
    action_needs_dialog: bpy.props.BoolProperty(name="Flow Page Is Action w/ dialog")
    action_buttons: bpy.props.StringProperty(name="Flow Page Is Action w/ Buttons",)
    open_states: bpy.props.CollectionProperty(
        type=OpenStateProperties,
        name="Page Groups Open States",
        description="what name says",
        # option={'SKIP_SAVE'},
    )
    fields: bpy.props.CollectionProperty(
        type=FlowFieldProperties,
        name="Flow Page Fields",
        description="Current Page (string param) Fields",
        # option={'SKIP_SAVE'},
    )


#
#   OPERATORS
#


class KABARET_OT_GotoRelated(bpy.types.Operator):
    """
    Goto there.
    """

    bl_idname = "kabaret.flow_page_goto_related"
    bl_label = "kabaret.flow.Goto"
    bl_options = {"REGISTER"}  # , 'UNDO'}

    parent_oid: bpy.props.StringProperty(name="parent oid")
    name: bpy.props.StringProperty(name="name")

    def execute(self, context):
        oid = kabaret.session.cmds.Flow.resolve_path(self.parent_oid + "/" + self.name)
        context.window_manager.flow_page.current_oid = oid
        return {"FINISHED"}


class KABARET_OT_GotoMappedItem(bpy.types.Operator):
    """Quick jump to Item"""

    bl_idname = "kabaret.flow_page_goto_mapped_item"
    bl_label = "kabaret.flow.goto_mapped_item"
    bl_property = "item_name"

    def get_item_names(self, context):
        field = bpy.context.window_manager.flow_page.fields[self.field_index]
        field.ensure_mapped_items_loaded()
        ret = []
        for item in field.mapped_items:
            ret.append((item.oid, item.name, "Mapped Item: %s" % (item.oid,)))
        return ret

    field_index: bpy.props.IntProperty()
    item_name: bpy.props.EnumProperty(items=get_item_names, options={"SKIP_SAVE"})

    def execute(self, context):
        self.report({"INFO"}, "Selected: %s" % self.item_name)
        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {"FINISHED"}


class KABARET_OT_RunAction(bpy.types.Operator):
    """
    Run this action.
    """

    bl_idname = "kabaret.flow_page_run_action"
    bl_label = "kabaret.flow.Run"
    bl_options = {"REGISTER"}  # , 'UNDO'}

    action_oid: bpy.props.StringProperty(name="parent oid")
    from_oid: bpy.props.StringProperty(name="flow_oid")
    page_is_dialog: bpy.props.BoolProperty(
        name="the current page is the action dialog", default=False,
    )
    button: bpy.props.StringProperty(name="clicked button")

    def goto_oid(self, oid, context):
        context.window_manager.flow_page.current_oid = oid
        return {"FINISHED"}

    def execute(self, context):
        if not self.page_is_dialog:
            needs_dialog = kabaret.session.cmds.Flow.action_needs_dialog(
                self.action_oid
            )
            if needs_dialog:
                # self.report({'ERROR'}, 'Cannot run action with dialog (yet)')
                # return {'CANCELLED'}
                self.goto_oid(self.action_oid, context)
                return {"FINISHED"}

        result = kabaret.session.cmds.Flow.run_action(self.action_oid, self.button)
        result = result or {}

        if "goto" in result:
            self.goto_oid(result["goto"], context)
        elif result.get("close", True):
            self.goto_oid(self.from_oid, context)

        self.report({"WARNING"}, "Action {} result: {}".format(self.action_oid, result))

        return {"FINISHED"}


#
#   MENU
#
class KABARET_MT_NavigatorMenu(bpy.types.Menu):
    bl_idname = "KABARET_MT_NavigatorMenu"
    bl_label = "Goto"

    def draw(self, context):
        flow_page = context.window_manager.flow_page
        layout = self.layout
        home_oid = flow_page.home_oid

        parts = kabaret.session.cmds.Flow.split_oid(
            flow_page.current_oid, skip_maps=True, up_to_oid=home_oid
        )
        icon = "FILE_REFRESH"
        for label, oid in reversed(parts):
            if not oid.startswith(home_oid):
                continue
            parent_oid, name = oid.rsplit("/", 1)
            goto_op = layout.operator(
                KABARET_OT_GotoRelated.bl_idname, text=label, icon=icon
            )
            goto_op.name = name
            goto_op.parent_oid = parent_oid
            icon = "LOOP_BACK"

        goto_op = layout.operator(
            KABARET_OT_GotoRelated.bl_idname, text="Home", icon="WORLD_DATA"
        )
        goto_op.parent_oid = flow_page.home_oid
        goto_op.name = "."


#
#   PANEL
#


class KABARET_PT_flow_page(bpy.types.Panel):

    bl_idname = "KABARET_PT_flow_page"

    bl_order = -1

    # bl_space_type = 'PROPERTIES'
    # bl_region_type = 'WINDOW'
    # bl_context = "object"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "Kabaret"
    bl_label = "Flow Tools"

    def draw(self, context):
        flow_page = context.window_manager.flow_page
        current_oid = flow_page.current_oid
        home_oid = flow_page.home_oid

        path = current_oid
        if current_oid.startswith(home_oid):
            path = "Home" + current_oid[len(home_oid) :]
        self.layout.menu(
            KABARET_MT_NavigatorMenu.bl_idname, text=path,
        )

        parent_oid = current_oid

        # parents_lo = self.layout.row()
        lo = self.layout.column()
        lo.use_property_split = True
        lo.use_property_decorate = False

        fields = bpy.context.window_manager.flow_page.fields
        is_action = bpy.context.window_manager.flow_page.is_action
        action_buttons_json = bpy.context.window_manager.flow_page.action_buttons

        last_group = ""
        for field_index, (name, field) in enumerate(fields.items()):
            group = field.group
            open = True
            if group:
                state = bpy.context.window_manager.flow_page.open_states.get(group)
                if state is None:
                    state = bpy.context.window_manager.flow_page.open_states.add()
                    state.name = group
                    state.open = False
                open = state.open

            if group != last_group:
                last_group = group
                if group:
                    lo = self.layout.box()
                    lo.prop(
                        state,
                        "open",
                        text=group,
                        icon="DISCLOSURE_TRI_DOWN" if open else "DISCLOSURE_TRI_RIGHT",
                        emboss=False,
                        translate=False,
                        toggle=1,
                        icon_only=True,
                    )
                    if not open:
                        continue
                    lo = lo.column()
                    lo.use_property_split = True
                    lo.use_property_decorate = False
                else:
                    lo = self.layout.column()
                    lo.use_property_split = True
                    lo.use_property_decorate = False

            if not open:
                continue

            if name.startswith("_") or field.hidden:
                continue

            relation_type = field.relation_type
            if relation_type in ("Param", "Computed"):
                row = lo.row()
                if not field.editable or relation_type == "Computed":
                    row.enabled = False
                value_prop_name = "value"
                if field.editor_type == "bool":
                    value_prop_name = "bool_value"
                elif field.editor_type == "int":
                    value_prop_name = "int_value"
                elif field.editor_type == "float":
                    value_prop_name = "float_value"

                row.prop(
                    data=field,
                    property=value_prop_name,
                    text=field.label,
                    translate=False,
                )

            elif field.is_map:
                icon = "ALIGN_JUSTIFY"
                row = lo.row()
                row.prop(
                    field,
                    "is_map_expanded",
                    icon="TRIA_DOWN" if field.is_map_expanded else "TRIA_RIGHT",
                    icon_only=True,
                    emboss=False,
                )
                goto_op = row.operator(
                    KABARET_OT_GotoRelated.bl_idname, text=field.label, icon=icon
                )
                goto_op.name = field.name
                goto_op.parent_oid = parent_oid

                select_op = row.operator(
                    KABARET_OT_GotoMappedItem.bl_idname, text="", icon="VIEWZOOM"
                )
                select_op.field_index = field_index

                if field.is_map_expanded:
                    row = lo.row()
                    row.separator()
                    row.template_list(
                        "UI_UL_list",
                        field.oid,
                        field,
                        "mapped_items",
                        field,
                        "current_mapped_item",
                    )

            elif field.is_action:
                icon = "PREFERENCES"
                action_op = lo.operator(
                    KABARET_OT_RunAction.bl_idname, text=field.label, icon=icon
                )
                action_op.from_oid = current_oid
                action_op.action_oid = field.oid
                action_op.page_is_dialog = False

            elif relation_type in ("Child",):
                icon = "FORWARD"
                goto_op = lo.operator(
                    KABARET_OT_GotoRelated.bl_idname, text=field.label, icon=icon
                )
                goto_op.name = field.name
                goto_op.parent_oid = parent_oid

            elif relation_type in ("Parent",):
                icon = "LOOP_BACK"
                goto_op = lo.operator(
                    KABARET_OT_GotoRelated.bl_idname, text=field.label, icon=icon
                )
                goto_op.name = field.name
                goto_op.parent_oid = parent_oid

            else:
                lo.label("???" + field.oid)
                goto_op = self.layout.operator(
                    KABARET_OT_GotoRelated.bl_idname, text=field.label
                )
                goto_op.name = field.name
                goto_op.parent_oid = parent_oid

        if is_action:
            buttons = json.loads(action_buttons_json)
            if buttons is None:
                # Action without dialog/button are triggered from their parent
                # this should never happen !
                lo.label("WHHHHHHAT ?!? Current oid is an action w/o dialog ??")
            for button in buttons:
                icon = "PREFERENCES"
                action_op = lo.operator(
                    KABARET_OT_RunAction.bl_idname, text=button, icon=icon
                )
                action_op.from_oid = current_oid.rsplit("/", 1)[0]
                action_op.action_oid = current_oid
                action_op.page_is_dialog = True
                action_op.button = button


#
#   VIEW
#
class FlowView(ViewMixin):
    def __init__(self, *args, **kwargs):
        super(FlowView, self).__init__(*args, **kwargs)

        bpy.utils.register_class(MappedItem)
        bpy.utils.register_class(OpenStateProperties)
        bpy.utils.register_class(FlowFieldProperties)
        bpy.utils.register_class(FlowPageProperties)
        bpy.types.WindowManager.flow_page = bpy.props.PointerProperty(
            type=FlowPageProperties,
            name="Page Properties",
            description="Current Page Properties",
            # option={'SKIP_SAVE'},
        )

        bpy.utils.register_class(KABARET_OT_GotoMappedItem)
        bpy.utils.register_class(KABARET_OT_GotoRelated)
        bpy.utils.register_class(KABARET_OT_RunAction)
        bpy.utils.register_class(KABARET_MT_NavigatorMenu)
        bpy.utils.register_class(KABARET_PT_flow_page)

        from bpy.app.handlers import persistent

        @persistent
        def kablender_on_scene_load(dummy):
            bpy.context.window_manager.flow_page.home_oid = self.session.home_oid
            bpy.context.window_manager.flow_page.current_oid = self.session.home_oid

        self._scene_load_handler = kablender_on_scene_load
        bpy.app.handlers.load_post.append(self._scene_load_handler)

    def receive_event(self, event, data):
        print("FlowView receive_event", event, data)
        if event == "flow_touched":
            oid = data["oid"]

            if not oid.startswith(
                bpy.context.window_manager.flow_page.current_oid + "/"
            ):
                print("   touched oid not under current page oid")
                print("      touched: " + oid)
                print(
                    "      current: ",
                    bpy.context.window_manager.flow_page.current_oid + "/",
                )
                return

            for field in bpy.context.window_manager.flow_page.fields:
                if field.oid == oid:
                    print("     UPDATING VALUE FOR:", field)
                    field.touch_value()
                    bpy.context.window_manager.flow_page.update_all_VIEW_3D_TOOLS()

    def delete_view(self):
        bpy.utils.unregister_class(KABARET_PT_flow_page)
        bpy.utils.unregister_class(KABARET_MT_NavigatorMenu)
        bpy.utils.unregister_class(KABARET_OT_RunAction)
        bpy.utils.unregister_class(KABARET_OT_GotoRelated)
        bpy.utils.unregister_class(KABARET_OT_GotoMappedItem)

        del bpy.types.WindowManager.flow_page
        bpy.utils.unregister_class(FlowPageProperties)
        bpy.utils.unregister_class(FlowFieldProperties)
        bpy.utils.unregister_class(OpenStateProperties)
        bpy.utils.unregister_class(MappedItem)

        bpy.app.handlers.load_post.remove(self._scene_load_handler)
        super(FlowView, self).delete_view()
