# import requests
# import datetime
import logging

from django.db import models
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from sitemapparser import SiteMapParser

logger = logging.getLogger('kromm_info')


class WSite(models.Model):
    url = models.URLField(unique=True, null=False)
    status = models.CharField(max_length=3, null=False, default='xxx')
    short_desc = models.TextField(max_length=1023, verbose_name='Some Description', default='This site was not scaned yet')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    HEADERS = {'user-agent': 'ads_maker 0.1'}

    class Meta:
        ordering = ('-updated_at',)

    def check_status(self):
        """
        Populates status field and handles possible url mistakes
        """
        if not str(self.url).startswith('http://')\
                and not str(self.url).startswith('https://'):
            self.url = 'http://' + self.url
        try:
            r = requests.head(str(self.url), headers=self.HEADERS,
                              allow_redirects=True)
        except ConnectionError:
            self.status = 'xxx'
            return
        self.status = r.status_code
        if r.history:
            # if redirects: save final URL
            self.url = r.url

    def check_info(self):
        r = requests.get(str(self.url), headers=self.HEADERS,
                         allow_redirects=False)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.short_desc = soup.title.string

    def find_sitemaps(self):
        r = requests.get(self.url + 'sitemap.xml',
                         headers=self.HEADERS, allow_redirects=False)
        if r.ok:
            soup = BeautifulSoup(r.content, 'xml')
            for sitemap in soup.find_all('sitemap'):
                yield sitemap.find('loc').text
        else:
            return [self.url + 'sitemap.xml']

    def get_sitemaps(self):
        logger.debug(f'Parse sitemap started at {self.url}')
        for page in self.find_sitemaps():
            r = requests.get(page, headers=self.HEADERS, allow_redirects=False)
            if r.ok:
                soup = BeautifulSoup(r.content, 'xml')
                count_url = len(soup.find_all('url'))
                count_sitemaps = len(soup.find_all('sitemap'))
                logger.debug(f'Parsed sitemap {page}')
                self.sitemaps.create(url=page,
                                     is_sm_index=count_sitemaps > count_url,
                                     count=count_sitemaps+count_url,)


    def __str__(self):
        return self.url


class SiteMap(models.Model):
    url = models.URLField(unique=True, help_text='Sitemaps URL')
    count = models.IntegerField(default=0)
    site = models.ForeignKey(WSite, blank=False, on_delete=models.CASCADE, related_name="sitemaps")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sm_index = models.BooleanField(null=True)



