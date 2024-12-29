'''inicio y busqueda'''
from django.shortcuts import render

from books.models import Autor, Libro, Editorial
from books.forms import SearchForms
from .form import ContactForms

# Vistas generales de la Aplicaciòn


def home_view(request):

    # la funsion render necesita 2 parametros un request y un archivo para renderizar
    return render(request, "general/home.html")


# def search_view(request):
#     if request.GET:
#         busqueda = request.GET['q']

#         autores = Autor.objects.filter(nombre__icontains=busqueda)
#         editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
#         libros = Libro.objects.filter(titulo__icontains=busqueda)

#         context = {
#             'autores': autores,
#             'editoriales': editoriales,
#             'libros': libros
#         }
#         return render(request, "general/search.html", context)


#     return render(request, "general/search.html")

def search_view(request):
    '''busqueda'''
    if request.GET:
        formulario = SearchForms(request.GET)

        busqueda = request.GET['q']

        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)

        context = {
            'autores': autores,
            'editoriales': editoriales,
            'libros': libros,
            'formulario': formulario
        }

    else:
        formulario = SearchForms()

    context = {
        'formulario': formulario
    }

    return render(request, "general/search.html", context)


def contact_view(request):
    ''' formulario de contacto'''
    if request.POST:
        formulario = ContactForms(request.POST)

        if formulario.is_valid():

            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            print(f'Se ha enviado un email de {nombre}, procedente de {
                  email} con el comentario:{comentario}')
            context = {
                'formulario': formulario,
                'success': True
            }

            return render(request, "general/search.html", context)

        else:
            context = {
                'formulario': formulario,
                'success': True
            }

            return render(request, "general/search.html", context)

    formulario = ContactForms()
    context = {
        'formulario': formulario
    }
    return render(request, "general/contacto.html", context)
