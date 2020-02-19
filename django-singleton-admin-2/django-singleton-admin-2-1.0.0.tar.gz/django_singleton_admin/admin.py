from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect

class SingletonModelAdmin(admin.ModelAdmin):
    change_form_template = "admin/django_singleton_admin/change_form.html"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        urls = super(SingletonModelAdmin, self).get_urls()

        model_name = self.model._meta.model_name
        self.model._meta.verbose_name_plural = self.model._meta.verbose_name
        url_name_prefix = '%(app_name)s_%(model_name)s' % {
            'app_name': self.model._meta.app_label,
            'model_name': model_name,
        }
        custom_urls = [
            url(r'^$',
                self.admin_site.admin_view(self.change_view),
                {'object_id': str(self.singleton_instance_id)},
                name='%s_change' % url_name_prefix),
        ]
        # By inserting the custom URLs first, we overwrite the standard URLs.
        return custom_urls + urls
    
    def response_change(self, request, obj):
        msg = '%s changed successfully' % obj
        self.message_user(request, msg)
        return HttpResponseRedirect("../../")

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.model.objects.get_or_create(pk=self.singleton_instance_id)
        return super(SingletonModelAdmin, self).change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )

    @property 
    def singleton_instance_id(self):
        return self.model.objects.all()[0].pk