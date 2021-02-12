from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemaps import sitemaps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path(r'tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap, sitemaps,
         name='django.contrib.sitemaps.views.sitemap')
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
