# Register your models here.
from .models import Question, Choice
from django.contrib import admin
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)