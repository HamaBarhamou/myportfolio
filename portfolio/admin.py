from django.contrib import admin
from .models import Project, Skill, Service
from ckeditor.widgets import CKEditorWidget
from django import forms


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = "__all__"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ("title", "date_created", "demo_link", "source_code_link")
    search_fields = ("title", "description")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
