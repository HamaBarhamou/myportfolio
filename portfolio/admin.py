from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "demo_link", "source_code_link")
    search_fields = ("title", "description")
