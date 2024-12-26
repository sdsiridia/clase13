from django.shortcuts import render
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
    success_url = reverse_lazy("books:libros_list")