from django.urls import path
from . import views


app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("project/<int:project_id>/", views.project_detail, name="project_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("events/", views.event_list, name="event_list"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
]
