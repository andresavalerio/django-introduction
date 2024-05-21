from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
    This class represents the Choice model in a tabular form.

    It allows the admin to add, change, and delete instances of Choice
    directly from the Question page.
    """

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    This class customizes the admin form of the Question model.

    It defines the layout of the admin form, the fields to be displayed in the
    change list, and the filters that can be used in the change list page.
    """

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
