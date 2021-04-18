from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.ProjectList.as_view(),
         name='index'),
    path('price/',
         views.price_view,
         name='price'),
    path('project/<int:pk>/',
         views.ProjectDetail.as_view(),
         name='project-detail'),
    path('tic-tac-toe/',
         views.TicTacToe.as_view(),
         name='tic-tac-toe'),
    path('cv/<int:pk>',
         views.CVDetail.as_view(),
         name='cv-detail'),
    path('cv/',
         views.CVList.as_view(),
         name='cv-list'),
]
