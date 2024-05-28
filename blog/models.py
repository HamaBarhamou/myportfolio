from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="posts/", blank=True, null=True)

    def __str__(self):
        return self.title
