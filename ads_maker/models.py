# import requests
# import datetime
from django.db import models
import requests
from requests.exceptions import ConnectionError


class Site(models.Model):  # TODO: Rename model!!!
    url = models.URLField(unique=True, null=False)
    status = models.CharField(max_length=3, null=False, default='xxx')
    short_desc = models.TextField(max_length=1023, verbose_name='Some Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def check_status(self):
        """
        Populates status field and handles possible url mistakes
        """
        headers = {'user-agent': 'ads_maker 0.1'}
        if not str(self.url).startswith('http://')\
                and not str(self.url).startswith('https://'):
            self.url = 'http://' + self.url
        try:
            r = requests.head(str(self.url), headers=headers,
                              allow_redirects=True)
        except ConnectionError:
            self.status = 'xxx'
            return
        self.status = r.status_code
        if r.history:
            self.url = r.url
            # save final URL

    def get_sitemap(self):
        sitemaps_list = []
        sitemaps_list.append()

    def __str__(self):
        return self.url


class SiteMap(models.Model):
    url = models.URLField(unique=True, help_text='Sitemaps URL')
    count = models.IntegerField
    site = models.ForeignKey(Site, blank=False, on_delete=models.CASCADE, related_name="site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sm_index = models.BooleanField(null=True)



