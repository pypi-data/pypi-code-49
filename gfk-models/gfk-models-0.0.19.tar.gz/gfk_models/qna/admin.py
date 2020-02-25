from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.StackedInline):
    fk_name = 'question'
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    exclude = ['last_update']
    list_display = ['title', 'author','last_update']

    inlines = [AnswerInline]

    model = Question

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['author', 'last_update', 'created_at']
    model = Answer

admin.site.register(Answer, AnswerAdmin)


# class AnswerAdmin(admin.ModelAdmin):
#     exclude = ['last_update']
#     list_display = ['author','last_update']
#     model = Answer
#
# admin.site.register(Answer, AnswerAdmin)
