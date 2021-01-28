from django.test import TestCase
from ads_maker.forms import NewSiteForm


class FormsTests(TestCase):
    def test_clean_url(self):
        urls = {
            'www.site.com': True,
            'site.com': True,
            'blog.site.com': True,
            'www.blog.site.com': True,

            'www.site.com/': True,
            'site.com/': True,
            'blog.site.com/': True,
            'www.blog.site.com/': True,

            'http://www.site.com': True,
            'http://site.com': True,
            'http://blog.site.com': True,
            'http://www.blog.site.com': True,

            'https://www.site.com': True,
            'https://site.com': True,
            'https://blog.site.com': True,
            'https://www.blog.site.com': True,

            'site.com/page': False,
            'site.com/page/': False,
            'site.com/index.html': False,
        }

        for url, result in urls.items():
            with self.subTest(url=url):
                form = NewSiteForm({'url': url, })
                self.assertEqual(form.is_valid(), result,
                                 f'Test failed in {url}')
