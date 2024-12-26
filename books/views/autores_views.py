''' Definiciond e las vistas de autores'''
#########################################

# from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from books.models import Autor
# from books.forms import *

# Create your views here.


class AutorListView(ListView):
    '''lista de autores'''
    model = Autor
    template_name = 'autores/AutorList.html'
    context_object_name = 'autores'


class AutorDetailView(DetailView):
    ''' detalle autor'''
    model = Autor
    template_name = 'autores/AutorDetail.html'
    context_object_name = 'autor'


class AutorCreateView(CreateView):
    ''' creacion de autor'''
    model = Autor
    template_name = 'autores/AutorCreate.html'
    success_url = reverse_lazy('autor:list')
    fields = ['nombre',
              'apellido',
              'f_nac',
              'nacionalidad',
              'biografia',
              'premios',
              'telefono',
              'email',
              'sitio_web']


class AutorUpdateView(UpdateView):
    ''' modificar autor'''
    model = Autor
    template_name = 'autores/AutorUpdate.html'
    success_url = reverse_lazy('autor:list')
    fields = ['nombre',
              'apellido',
              'f_nac',
              'nacionalidad',
              'biografia',
              'premios',
              'telefono',
              'email',
              'sitio_web']


class AutorDeleteView(DeleteView):
    ''' borrar autor'''
    model = Autor
    template_name = 'autores/AutorDelete.html'
    success_url = reverse_lazy('autor:list')
