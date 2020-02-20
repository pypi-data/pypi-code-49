from django.contrib.admin.options import BaseModelAdmin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.admin.options import csrf_protect_m
from django.contrib.admin.options import TO_FIELD_VAR
from django.contrib.admin.options import unquote
from django.urls import reverse

class ReadEditSwitchAdminMixin(BaseModelAdmin):
    # Work together with templatetag readedit_switch_submit_row

    change_form_template = "admin/django_readedit_switch_admin_change_form.html"

    def is_edit_view(self, request):
        if "change" in request.path:
            ps = request.path.split("/")
            if len(ps) <= 2:
                return False
            pk = ps[-2]
            if not pk.isdigit():
                return False
            pk = int(pk)
            app_label = self.model._meta.app_label
            model_name = self.model._meta.model_name
            edit_view_url = reverse("admin:{}_{}_change".format(app_label, model_name), args=[pk])
            print(app_label, model_name, edit_view_url)
            if edit_view_url == request.path:
                return True
            else:
                return False
        return False

    def get_changing_object(self, request, object_id):
        if not object_id:
            return None
        else:
            to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
            obj = self.get_object(request, unquote(object_id), to_field)
            return obj

    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        obj = self.get_changing_object(request, object_id)
        extra_context = extra_context or {}
        extra_context["with_readeditmixin"] = True
        extra_context["has_change_permission_real"] = self.has_change_permission_real(request, obj)
        return super().changeform_view(request, object_id, form_url, extra_context)

    def has_change_permission(self, request, obj=None):
        result = super().has_change_permission(request, obj)
        if not self.is_edit_view(request):
            return result
        if hasattr(request, "readeditmixin_ignore_editflag"):
            return result
        else:
            if not request.GET.get("_edit_flag"):
                return False
            else:
                return result # Not True, result may be False

    def has_change_permission_real(self, request, obj=None):
        setattr(request, "readeditmixin_ignore_editflag", True)
        try:
            return self.has_change_permission(request, obj)
        finally:
            delattr(request, "readeditmixin_ignore_editflag")

    def has_add_permission(self, request):
        result = super().has_add_permission(request)
        if not self.is_edit_view(request):
            return result
        if hasattr(request, "readeditmixin_ignore_editflag"):
            return result
        else:
            if not request.GET.get("_edit_flag") and isinstance(self, InlineModelAdmin) and not request.path.endswith("/add/"):
                return False
            else:
                return result

    def has_add_permission_real(self, request):
        setattr(request, "readeditmixin_ignore_editflag", True)
        try:
            return self.has_add_permission(request)
        finally:
            delattr(request, "readeditmixin_ignore_editflag")

    def has_delete_permission(self, request, obj=None):
        result = super().has_delete_permission(request, obj)
        if not self.is_edit_view(request):
            return result
        if hasattr(request, "readeditmixin_ignore_editflag"):
            return result
        else:
            if not request.GET.get("_edit_flag") and isinstance(self, InlineModelAdmin):
                return False
            else:
                return result

    def has_delete_permission_real(self, request, obj=None):
        setattr(request, "readeditmixin_ignore_editflag", True)
        try:
            return self.has_delete_permission(request, obj)
        finally:
            delattr(request, "readeditmixin_ignore_editflag")

    class Media:
        css = {
            "all": [
                "admin/css/django_readedit_switch_admin.css",
            ]
        }
        js = [
            "admin/js/django_readedit_switch_admin.js",
        ]
