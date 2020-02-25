from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    exclude = ['last_update']
    list_display = ['author', 'rating','last_update']
    model = Review

admin.site.register(Review, ReviewAdmin)


# class ReviewListAdmin(admin.ModelAdmin):
#     model = ReviewList

# admin.site.register(ReviewList, ReviewListAdmin)
