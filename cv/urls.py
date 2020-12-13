from django.urls import path

from . import views

urlpatterns = [
    path('cv/',
         views.study_view,
         name='study')
]