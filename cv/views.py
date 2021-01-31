from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Study, Project
from .forms import ContactForm


def study_view(request):
    nsu = Study.objects.get(pk=1)
    return render(request, 'index.html', {'uni': nsu})


class ProjectList(ListView):

    model = Project
    template_name = 'index_page.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['form'] = ContactForm(self.request.POST or None)
        return context

    def post(self, request):
        form = ContactForm(request.POST)
        breakpoint()
        if not form.is_valid():
            # return render(request, 'index_page.html', self.get_context_data())
            return redirect('index')
        email = EmailMessage(
            subject='New message from ContactForm',
            body=f'Form data {form.data}',
            to=['vladimir@kromm.info', ],
        )
        email.send()

        return redirect('index')


