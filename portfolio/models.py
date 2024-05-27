from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to="projects/")
    demo_link = models.URLField(max_length=200, blank=True)
    source_code_link = models.URLField(max_length=200, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
