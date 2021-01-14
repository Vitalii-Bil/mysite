from django.contrib import admin

from .models import Lecturer, Rector, Student, University


class RectorInlineModelAdmin(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Rector


class LecturerInlineModelAdmin(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Lecturer


class StudentInlineModelAdmin(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Student


class UniversityAdmin(admin.ModelAdmin):
    fields = ['name', 'date_of_found']
    inlines = [RectorInlineModelAdmin, LecturerInlineModelAdmin, StudentInlineModelAdmin]


admin.site.register(University, UniversityAdmin)
