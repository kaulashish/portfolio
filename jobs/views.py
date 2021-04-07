from django.shortcuts import render
from .models import *
from django.views import View

# Create your views here.
def homepage(request):
    jobs = Job.objects.all()
    return render(request, "jobs/home.html", {"jobs": jobs})


def details(request):
    details = Detail.objects.all()
    return render(request, "jobs/base.html", {"details": details})


def education(request):
    education_items = Education.objects.all()
    return render(request, "jobs/education.html", {"education_items": education_items})


def projects(request):
    projects = Job.objects.all()
    return render(request, "jobs/projects.html", {"projects": projects})


def skills(request):
    skills = Skills.objects.all()
    return render(request, "jobs/base.html", {"skills": skills})