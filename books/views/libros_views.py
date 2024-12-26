'''from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from books.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.

def libros_view(request):
    return render(request,"libros/libros.html")


class LibrosListView(ListView):
    model = Libro
    template_name = "libros/libros.html"
    context_object_name = 'libros'

class LibroCreateView(CreateView):
    model = Libro
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas"      
              ]
    template_name='libros/libros_create.html'
    success_url = reverse_lazy('books:libros_list')


class LibroUpdateView(UpdateView):
    model = Libro
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas"      
              ]
    template_name='libros/libros_update.html'
    success_url = reverse_lazy('books:libros_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name='libros/libro_delete.html'
    success_url = reverse_lazy("books:libros_list")'''

# from django.shortcuts import render, redirect, reverse
# from books.forms import EditorialCreate, EditorialModelFormCreate

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from books.models import Libro


# Create your views here.


class LibroListView(ListView):
    ''' lista de libros'''
    model = Libro
    template_name = 'libros/LibroList.html'
    context_object_name = 'libros'


class LibroDetailView(DetailView):
    '''detalle libro'''
    model = Libro
    template_name = 'libros/LibroDetail.html'
    context_object_name = 'libro'


class LibroCreateView(CreateView):
    ''' nuevo libro'''
    model = Libro
    template_name = 'libros/LibroCreate.html'
    success_url = reverse_lazy('libro:list')
    fields = ['titulo',
              'isbn',
              'fecha_publicacion',
              'numero_paginas',
              'idioma',
              'descripcion',
              'editorial',
              'autores',
              'genero',
              'precio',
              'is_out_of_stock'
              ]


class LibroUpdateView(UpdateView):
    '''modificar un libro'''
    model = Libro
    template_name = 'libros/LibroUpdate.html'
    success_url = reverse_lazy('libro:list')
    fields = ['titulo',
              'isbn',
              'fecha_publicacion',
              'numero_paginas',
              'idioma',
              'descripcion',
              'editorial',
              'autores',
              'genero',
              'precio',
              'is_out_of_stock'
              ]
    # widgets = {'LANGS_CHOICES': forms.CheckboxSelectMultiple,  # Usar casillas de verificación
    #           }


class LibroDeleteView(DeleteView):
    ''' eliminar un libro'''
    model = Libro
    template_name = 'libros/LibroDelete.html'
    success_url = reverse_lazy('libro:list')
