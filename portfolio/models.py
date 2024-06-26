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
    image = models.ImageField(upload_to="skills/", blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    icon_class = models.CharField(
        max_length=50,
        help_text="Enter the CSS class for the icon (e.g., 'fab fa-twitter')",
    )

    def __str__(self):
        return self.name


class VisitorCount(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.count)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="events/", blank=True, null=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    event = models.ForeignKey(
        Event, related_name="gallery_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f"Image for {self.event.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
