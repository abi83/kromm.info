from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import info_dict

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path(r'tinymce/', include('tinymce.urls')),
    # path(r'^tinymce/', include('tinymce.urls')), # original, but with warning
    path('sitemap.xml', sitemap, {'sitemaps': {'projects': GenericSitemap(info_dict, priority=1.0)}}, name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += i18n_patterns(
    path('', include('cv.urls')),
)

urlpatterns += [
    path('ads_maker/', include('ads_maker.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
