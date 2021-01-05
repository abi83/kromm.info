"""
1. Я не хочу сохранять в базу один и тот же сайт дважды
2. http и https
"""

import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View
from django.core.exceptions import ValidationError
from django.contrib import messages


from .models import SiteMap, WSite
from .forms import NewSiteForm

logger = logging.getLogger('kromm_info')

def ads_maker(request):
    sites = WSite.objects.all()
    form = NewSiteForm(request.POST or None)
    paginator = Paginator(sites, 21)
    page_number = request.GET.get('page', default=1)
    sites = paginator.get_page(page_number)
    context = {
        'form': form,
        'sites': sites,
        'paginator': paginator,
    }
    if not form.is_valid():
        return render(request, 'ads_maker/index.html', context)

    site = WSite()
    site.url = form.cleaned_data['url']
    site.check_status()
    if site.status == 200:
        site.save()
        messages.success(request, 'Your website added successfully')
        sites = WSite.objects.all()
        paginator = Paginator(sites, 10)
        context['sites'] = paginator.get_page(1)

    else:
        form.add_error(None, 'Connection error')
    return render(request, 'ads_maker/index.html', context)


class SiteDetail(DetailView, View):
    model = WSite
    # queryset = WSite.objects.select_related('sitemaps').all()

    def post(self, request, pk):
        self.object = self.get_object()
        if 'update' in request.POST:
            self.object.check_info()
            self.object.save()
            context = self.get_context_data(object=self.object)
            return render(request, 'ads_maker/wsite_detail.html', context)
        if 'parse-sitemaps' in request.POST:
            self.object.get_sitemaps()
            context = self.get_context_data(object=self.object)
            return render(request, 'ads_maker/wsite_detail.html', context)
