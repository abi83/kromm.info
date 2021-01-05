from django.urls import path


from . import views

urlpatterns = [
    path('', views.ads_maker, name="ads_maker")
]