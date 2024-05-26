from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project


def home(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 5)  # 5 projets par page

    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)

    return render(request, "portfolio/home.html", {"projects": projects})
