from django.urls import path
from . import views


app_name = "portfolio"

urlpatterns = [
    path("home", views.home, name="home"),
    path("project/<int:project_id>/", views.project_detail, name="project_detail"),
    path("", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("events/", views.event_list, name="event_list"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
    path("events/<int:event_id>/gallery/", views.event_gallery, name="event_gallery"),
    path("gallery/", views.gallery, name="gallery"),
]
