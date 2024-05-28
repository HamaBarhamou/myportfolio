from django.contrib import admin
from .models import Category, Tag, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "category", "image"]
    search_fields = ["title", "content"]
    list_filter = ["created_at", "category", "tags"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "post", "created_at", "active"]
    list_filter = ["active", "created_at"]
    search_fields = ["name", "email", "body"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
