from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'teacher', 'credits')
    search_fields = ('code', 'title', 'teacher')
    list_filter = ('credits', 'teacher')
    ordering = ('code',)
    list_per_page = 25
