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


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Enter a value from 1 to 100")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
