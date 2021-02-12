"""
1. Я не хочу сохранять в базу один и тот же сайт дважды
2. http и https
"""

import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
        try:
            site = WSite.objects.get(url=site.url)
            messages.success(request, 'Your website updated successfully', extra_tags='alert-success')
        except WSite.DoesNotExist:
            site = WSite(url=site.url, status=site.status)
            messages.success(request, 'Your website added successfully', extra_tags='alert-success')
        site.save()
        logger.info(f'Site {site.url} proceed successfully')
        sites = WSite.objects.all()
        paginator = Paginator(sites, 10)
        context['sites'] = paginator.get_page(1)
    else:
        form.add_error(None, 'Connection error')

    return render(request, 'ads_maker/index.html', context)


class SiteDetail(DetailView, View):
    model = WSite
    template_name = 'ads_maker/site_detail.html'

    def post(self, request, pk):
        self.object = self.get_object()
        if 'update' in request.POST:
            self.object.check_info()
            self.object.save()
            context = self.get_context_data(object=self.object)
            return render(request, self.template_name, context)
        if 'parse-sitemaps' in request.POST:
            self.object.get_sitemaps(request)
            context = self.get_context_data(object=self.object)
            return render(request, self.template_name, context)


class SitemapDetail(DetailView):
    model = SiteMap
    template_name = 'ads_maker/sitemap_detail.html'

    def get_object(self):
        site = get_object_or_404(WSite, pk=self.kwargs.get('site_pk'))
        return get_object_or_404(SiteMap, pk=self.kwargs.get('pk'), site=site)