from django.contrib import admin

from .models import Author, Choice, Log, Question, Quote


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuoteInLine(admin.TabularInline):
    model = Quote
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ["path", "method", "timestamp"]
    fields = ['path', 'method']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [QuoteInLine]
    list_display = ['first_name', 'last_name', 'date_of_birth', 'about']
