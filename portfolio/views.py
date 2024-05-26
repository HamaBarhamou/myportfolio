from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project


def home(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 6)  # 5 projets par page

    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)

    return render(request, "portfolio/home.html", {"projects": projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "portfolio/project_detail.html", {"project": project})
