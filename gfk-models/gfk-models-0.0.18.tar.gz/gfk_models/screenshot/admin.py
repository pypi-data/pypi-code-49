from django.contrib import admin
from .models import Screenshot


class ScreenshotAdmin(admin.ModelAdmin):
    model = Screenshot

admin.site.register(Screenshot, ScreenshotAdmin)


# class ReviewListAdmin(admin.ModelAdmin):
#     model = ReviewList

# admin.site.register(ReviewList, ReviewListAdmin)
