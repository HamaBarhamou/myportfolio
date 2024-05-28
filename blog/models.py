from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

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
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
