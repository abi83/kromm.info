# import requests
# import datetime
import logging
import re

from django.db import models
from django.contrib import messages

import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
# from sitemapparser import SiteMapParser

logger = logging.getLogger('kromm_info')


class WSite(models.Model):
    url = models.URLField(unique=True, null=False)
    status = models.CharField(max_length=3, null=False, default='xxx')
    short_desc = models.TextField(max_length=1023, verbose_name='Some Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    HEADERS = {'user-agent': 'ads_maker 0.1'}

    class Meta:
        ordering = ('-updated_at',)

    def check_status(self):
        """
        Populates 'status' field except connection error
        """
        try:
            resp = requests.head(self.url, headers=self.HEADERS, allow_redirects=True)
        except ConnectionError as error:
            logger.error(f'Could not connect to {self.url}. Error: {error}')
            self.status = 'xxx'
            return
        self.status = resp.status_code
        self.url = resp.url  # if redirects: save the final URL

    def check_info(self):
        r = requests.get(str(self.url), headers=self.HEADERS,
                         allow_redirects=False)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.short_desc = soup.title.string
        self.status = r.status_code

    def find_sitemaps_in_robots(self):
        r = requests.get(self.url + 'robots.txt')
        if r.ok:
            sitemaps_position = [m.start() for m in re.finditer('\sSitemap:', r.text)]
            for position in sitemaps_position:
                sitemap_url = r.text[position+10:].split('\n', 1)[0].strip()
                logger.debug(f'Found sitemap in robots.txt: {sitemap_url}')
                yield sitemap_url
        else:
            return []

    def is_homepage(self):
        """
        HTTP://WWW.AC54.RU/UDALENIE-ZAPAHOV
        We should search something after a slash after the last point.
        """
        return True

    def find_sitemaps(self):
        """
        Add default sitemap path to found in robots.txt if was not found
        """
        answer = list(self.find_sitemaps_in_robots())
        answer.append(self.url + 'sitemap.xml')
        answer.append(self.url + 'sitemap_index.xml')
        answer.append(self.url + 'sitemap1.xml')
        return set(answer)

    def get_sitemaps(self, request):
        # TODO: Рекурсивно оббегать все сайтмэпы
        logger.info(f'Parse sitemaps started at {self.url}')
        count = 0
        for page in self.find_sitemaps():
            r = requests.get(page, headers=self.HEADERS, allow_redirects=True)
            logger.debug(f'Trying to parse {page}. Response code: {r.status_code}.')
            if r.ok:
                soup = BeautifulSoup(r.content, 'xml')
                count_urls = len(soup.find_all('url'))
                count_sitemaps = len(soup.find_all('sitemap'))
                try:
                    sitemap = SiteMap.objects.get(url=r.url)
                    sitemap.save()
                    logger.debug(f'Successfully updated sitemap: {r.url}')
                except SiteMap.DoesNotExist:
                    self.sitemaps.create(url=r.url,
                                         is_sm_index=count_sitemaps > count_urls,
                                         count_urls=count_urls,
                                         count_sitemaps=count_sitemaps,
                                         )
                    logger.debug(f'Successfully created sitemap: {page}')
                count += 1
            else:
                logger.warning(f'Parse sitemap {page} failed. Status {r.status_code}')
        if count > 0:
            messages.success(request, f'Successfully proceeded {count} sitemaps')
        else:
            messages.warning(request, 'No sitemaps was found')



    def __str__(self):
        return self.url


class SiteMap(models.Model):
    url = models.URLField(unique=True, help_text='Sitemaps URL')
    count_sitemaps = models.IntegerField(default=0)
    count_urls = models.IntegerField(default=0)
    site = models.ForeignKey(WSite, blank=False, on_delete=models.CASCADE, related_name="sitemaps")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sm_index = models.BooleanField(null=True)



