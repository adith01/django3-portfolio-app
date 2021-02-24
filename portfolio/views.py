from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    print(request.headers)
    return render(request, 'portfolio/home.html', {'projects': projects})
