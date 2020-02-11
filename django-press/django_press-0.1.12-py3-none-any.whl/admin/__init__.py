from django.contrib import admin

from .context import ContextAdmin
from .page import PageAdmin
from .Inquiry import InquiryAdmin, ContactAdmin
from django_press.models import Page, Context, BaseInquiry, Contact, TabElement, ImageFile, Service, Product

admin.site.register(Page, PageAdmin)
admin.site.register(Context, ContextAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(BaseInquiry, InquiryAdmin)
admin.site.register(TabElement)
admin.site.register(ImageFile)
admin.site.register(Service)
admin.site.register(Product)