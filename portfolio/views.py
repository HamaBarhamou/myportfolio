from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from django.core.paginator import Paginator
from .models import Project, Service, Skill, About, SocialLink, VisitorCount


def home(request):
    visitor_count = VisitorCount.objects.first()
    project_list = Project.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    social_links = SocialLink.objects.all()
    paginator = Paginator(project_list, 6)  # 6 projets par page

    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)

    return render(
        request,
        "portfolio/home.html",
        {
            "visitor_count": visitor_count.count if visitor_count else 0,
            "projects": projects,
            "skills": skills,
            "services": services,
            "social_links": social_links,
        },
    )


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "portfolio/project_detail.html", {"project": project})


def about(request):
    about_content = About.objects.first()
    return render(
        request,
        "portfolio/about.html",
        {"about": about_content, "social_links": SocialLink.objects.all()},
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(
                    f"Message from {name}",
                    message,
                    email,
                    ["hamabarhamou@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except ConnectionRefusedError:
                return HttpResponse(
                    "Failed to connect to the email server. Please try again later."
                )
            return render(request, "portfolio/contact_success.html")
    else:
        form = ContactForm()
    return render(
        request,
        "portfolio/contact.html",
        {"form": form, "social_links": SocialLink.objects.all()},
    )
