from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Study, Project
from .forms import ContactForm
from django.utils.translation import ugettext_lazy as _


def study_view(request):
    nsu = Study.objects.get(pk=1)
    return render(request, 'index.html', {'uni': nsu})


def price_view(request):
    return render(request, 'prices.html', {})

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
        if not form.is_valid():
            messages.warning(
                request,
                _('Сообщение не было отправлено. В <a href="#contact-form"'
                  'class="alert-link">форме</a> есть ошибки.'),
                extra_tags='alert-warning'
            )
            return render(request, 'index_page.html', {
                    'projects': Project.objects.all(),
                    'form': form,
                })
        email = EmailMessage(
            subject='New message from ContactForm',
            body=f'Form data {form.data}',
            to=['vladimir@kromm.info', ],
        )
        email.send()
        messages.success(
            request, 'Your message was sent', extra_tags='alert-success')

        return render(request, 'index_page.html', {
            'projects': Project.objects.all(),
            'form': ContactForm(),
        })


class ProjecDetail(DetailView):
    model = Project
    template_name = 'cv/project.html'
    context_object_name = 'project'
