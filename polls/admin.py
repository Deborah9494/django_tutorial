from django.contrib import admin
from .models import Choice, Question

#class ChoiceInline(admin.StackedInline):
# tabular way of displaying inline related objects
class ChoiceInline(admin.TabularInline):    
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # adds the previous class
    # so each Question admin page will include the related Choices directly 
    # below the Question form

    # list of field names to display, as columns
    list_display = ["question_text", "pub_date", "was_published_recently"]

admin.site.register(Question, QuestionAdmin)
