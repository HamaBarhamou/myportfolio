from django.contrib import admin
from .models import Project, Skill, Service, About, SocialLink, Event
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
    list_display = ("name", "proficiency", "image")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")


class AboutAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = About
        fields = "__all__"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm
    list_display = ("title", "image")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "icon_class")


admin.site.register(Event)
