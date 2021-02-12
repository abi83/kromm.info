from django.urls import path


from . import views

urlpatterns = [
    path('', views.ads_maker, name="ads-maker-index"),
    path('site/<int:pk>/', views.SiteDetail.as_view(), name='site-detail'),
    path('site/<int:site_pk>/sitemap/<int:pk>/', views.SitemapDetail.as_view(), name='sitemap-detail')
]