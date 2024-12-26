''' Autores todas las urls'''
from django.urls import path

from books.views.autores_views import (
    AutorDetailView,
    AutorListView,
    AutorCreateView,
    AutorUpdateView,
    AutorDeleteView,
)


app_name = 'autores'

urlpatterns = [

    path("list/", AutorListView.as_view(), name='list'),
    path("detail/<pk>/", AutorDetailView.as_view(), name='detail'),
    path("create/", AutorCreateView.as_view(), name='create'),
    path("update/<pk>/", AutorUpdateView.as_view(), name='update'),
    path("delete/<pk>/", AutorDeleteView.as_view(), name='delete'),
]
