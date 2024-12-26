'''from django.shortcuts import render
from datetime import date
from books.models import Autor

# Create your views here.


def autores_view(request):

    autores = Autor.objects.all()
    context =   {
            'autores': autores,
            'titulo': 'Hola esto es una prueba'

                }
    
    
    
    
    return render(request,"autores/autores.html",context)


def autor_detail(request,id):
    autores = [
        {
            'id':1,
            'nombre':'Antonio',
            'f_nac':date(1980,8,1)

        },
        {
            'id':2,
            'nombre':'Felipe',
            'f_nac':date(1985,10,1)

        },
        {
            'id':3,
            'nombre':'Matilde',
            'f_nac':date(1990,5,6)

        },
            
            ]
    
    context = {
            'autor':None
                   }

    for autor in autores:
        
        if autor['id'] == id:
            context['autor'] = autor
            break   



    return render(request,'autores/autor_detail.html',context)

'''

# from django.shortcuts import render
# from datetime import date

# from books.models import Autor


# def autores_view(request):
#     autores = Autor.objects.all()

#     context = {
#         "autores": autores,
#         "titulo": "Hola esto es otra prueba de paso de contexto",
#     }

#     return render(request, "autores/autores.html", context)


# def autor_detail(request, id):

#     autores = [
#         {"id": 1, "nombre": "Antonio", "f_nac": date(1980, 8, 1)},
#         {"id": 2, "nombre": "Felipe", "f_nac": date(1985, 10, 1)},
#         {"id": 3, "nombre": "Matilde", "f_nac": date(1990, 11, 5)},
#     ]

#     context = {
#         "autor": None,
#     }
#     for autor in autores:
#         if autor["id"] == id:
#             context["autor"] = autor
#             break

#     return render(request, "autores/autor_detail.html", context)
#########################################

# from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from books.models import Autor
from books.forms import *

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
