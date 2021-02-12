from django.contrib import sitemaps
from django.urls import reverse

from cv.models import Project


class ProjectsSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'weekly'
    i18n = True

    def items(self):
        return Project.objects.filter(active=True).order_by('pk')

    def location(self, item):
        return reverse('project-detail', args=[item.pk])


sitemaps = {'sitemaps': {'projects': ProjectsSitemap}}