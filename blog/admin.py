from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "category", "image"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
