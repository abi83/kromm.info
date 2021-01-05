from django.urls import path


from . import views

urlpatterns = [
    path('', views.ads_maker, name="ads-maker-index"),
    path('<int:pk>/', views.SiteDetail.as_view(), name='site-detail')
]