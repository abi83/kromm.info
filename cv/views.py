from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Study, Project

def study_view(request):
    nsu = Study.objects.get(pk=1)
    return render(request, 'index.html', {'uni': nsu})


class ProjectList(ListView):

    model = Project
    template_name = 'index_page.html'
    context_object_name = 'projects'

