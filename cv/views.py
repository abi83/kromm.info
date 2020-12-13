from django.shortcuts import render
from .models import Study

def study_view(request):
    nsu = Study.objects.get(pk=1)
    return render(request, 'index.html', {'uni': nsu})