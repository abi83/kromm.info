from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.ProjectList.as_view(),
         name='index'),
    path('price/',
         views.price_view,
         name='price'),
    path('<int:pk>/',
         views.ProjecDetail.as_view(),
         name='project-detail')

]