# Copyright (C) 2007-2020, Raffaele Salmaso <raffaele@salmaso.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# EmailAdmin/AttachmentInlineAdmin adapted from https://github.com/stefanfoulis/django-database-email-backend
# Copyright (C) 2011 Stefan Foulis and contributors.

from functools import update_wrapper

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.http import HttpResponse
from django.template.defaultfilters import linebreaks_filter
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.translation import gettext_lazy as _
from fluo import admin, forms
from fluo.urls import reverse

from .models import Attachment, Email, EmailTemplate, EmailTemplateTranslation

MAX_LANGUAGES = len(settings.LANGUAGES)


class CopyEmail(admin.CopyObject):
    def update(self, request, instance, original):
        instance.name = "{name} [new {count}]".format(
            name=original.name, count=EmailTemplate.objects.filter(name__istartswith=original.name).count(),
        )


class EmailTemplateTranslationForm(forms.ModelForm):
    pass


class EmailTemplateTranslationInline(admin.StackedInline):
    model = EmailTemplateTranslation
    form = EmailTemplateTranslationForm
    extra = 0
    max_num = MAX_LANGUAGES


class EmailTemplateAdminForm(forms.ModelForm):
    pass


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    actions = [CopyEmail()]
    form = EmailTemplateAdminForm
    inlines = [EmailTemplateTranslationInline]


class AttachmentInlineAdmin(admin.TabularInline):
    model = Attachment
    extra = 0
    can_delete = False
    max_num = 0
    readonly_fields = ["filename", "mimetype", "content", "file_link"]
    fields = ["file_link", "mimetype"]

    def file_link(self, obj):
        if obj.pk is None:
            return ""
        url_name = "%s:%s_email_attachment" % (self.admin_site.name, self.model._meta.app_label)
        kwargs = {
            "email_id": str(obj.email_id),
            "attachment_id": str(obj.id),
            "filename": str(obj.filename),
        }
        url = reverse(url_name, kwargs=kwargs)
        return mark_safe('<a href="%(url)s">%(filename)s</a>' % {"filename": obj.filename, "url": url})


class EmailAdmin(admin.ModelAdmin):
    list_display = ["from_email", "to_emails", "subject", "body_stripped", "created_at", "attachment_count"]
    date_hierarchy = "created_at"
    search_fields = ["from_email", "to_emails", "subject", "body", "body_html"]
    exclude = ["raw", "body"]
    readonly_fields = [
        "created_at",
        "all_recipients",
        "from_email",
        "to_emails",
        "cc_emails",
        "bcc_emails",
        "headers",
        "subject",
        "body",
        "body_br",
    ]
    inlines = [AttachmentInlineAdmin]

    def queryset(self, request):
        queryset = super().queryset(request)
        return queryset.annotate(attachment_count_cache=Count("attachments"))

    def attachment_count(self, obj):
        return obj.attachment_count

    attachment_count.short_description = _("attachment count")
    attachment_count.admin_order_field = "attachment_count_cache"

    def body_stripped(self, obj):
        return Truncator(obj).chars(120, truncate="...")

    body_stripped.short_description = _("body")
    body_stripped.admin_order_field = "body"

    def get_urls(self):
        urlpatterns = super().get_urls()
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            return update_wrapper(wrapper, view)

        appname = self.model._meta.app_label

        urlpatterns = [
            url(
                r"^(?P<email_id>\d+)/attachments/(?P<attachment_id>\d+)/(?P<filename>[\w.]+)$",
                wrap(self.serve_attachment),
                name="%s_email_attachment" % appname,
            )
        ] + urlpatterns
        return urlpatterns

    def serve_attachment(self, request, email_id, attachment_id, filename, extra_context=None):
        if not self.has_change_permission(request, None):
            raise PermissionDenied
        attachment = Attachment.objects.get(email__id=email_id, id=attachment_id, filename=filename)
        response = HttpResponse(attachment.content, content_type=attachment.mimetype or "application/octet-stream")
        response["Content-Length"] = len(attachment.content)
        return response

    def body_br(self, obj):
        return mark_safe(linebreaks_filter(obj.body))

    body_br.short_description = _("body html")
    body_br.admin_order_field = "body html"


if settings.EMAIL_BACKEND == "emails.backend.EmailBackend":
    admin.site.register(Email, EmailAdmin)
