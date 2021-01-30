from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.flatpage, {'url': '/'}, name='index'),
    # path('', study_view, name='index'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    # path('/', include('django.contrib.flatpages.urls')),
    # path('', study_view, name='index'),
    path('', include('cv.urls')),
    # path('cv/', include('cv.urls')),
        # path('contact/', include("contact.urls")),
    # path("", include("movies.urls")),
)

urlpatterns += [
    path('ads_maker/', include('ads_maker.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)