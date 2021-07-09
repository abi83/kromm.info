from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import ContactForm
from .models import Project, CV, Cover


def price_view(request):
    form = ContactForm(request.POST or None)
    if request.POST:
        if not form.is_valid():
            messages.warning(
                request,
                _('Сообщение не было отправлено. В форме есть ошибки.'),
                extra_tags='alert-warning'
            )
            return render(request, 'cv/prices.html', {
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

    return render(request, 'cv/prices.html', {'form': form})


class ProjectList(ListView):
    model = Project
    template_name = 'index_page.html'
    context_object_name = 'projects'
    queryset = Project.objects.filter(active=True).prefetch_related('images')

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


class ProjectDetail(DetailView):
    model = Project
    template_name = 'cv/project.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: this is absolutely wrong!
        context['next'] = Project.objects.filter(pk=self.kwargs.get('pk')+1).first()
        context['previous'] = Project.objects.filter(pk=self.kwargs.get('pk')-1).first()

        return context


class CVDetail(DetailView):
    model = CV
    template_name = 'cv/cv_detail.html'
    context_object_name = 'cv'


class CVList(ListView):
    model = CV
    template_name = 'cv/cv_list.html'
    context_object_name = 'cvs'
    queryset = CV.objects.all()


class TicTacToe(View):
    def get(self, request):
        return render(request, 'cv/tic_tac_toe.html', {})


class CoverDetail(DetailView):
    model = Cover
    template_name = 'cv/cover.html'
    context_object_name = 'cover'
    queryset = Cover.objects.all()
