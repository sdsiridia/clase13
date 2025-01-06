'''inicio y busqueda'''
from django.shortcuts import render
from django.contrib import messages

from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.views.generic import View
from django.utils import translation
from django.http import HttpResponseRedirect

from books.models import Autor, Libro, Editorial
from books.forms import SearchForms
from .form import ContactForms

# Vistas generales de la Aplicaciòn

class SetLanguageView(View):
    def post(self,request,*args,**kwargs):
        # Obtenemos el idioma seleccionado del formulario
        language = request.POST.get('language',None)

        # Si se selecciona un idioma lo activamos
        if language:
            translation.activate(language)
            #request.session(translation.LANGUAGE_SESSION_KEY) == language

        # redireccionamos a la pagina donde se hio la petición
        next_url = request.POST.get('next','/')
        return HttpResponseRedirect(next_url)


def home_view(request):
    messages.error(request,'Prueba de mensaje de error')
    messages.info(request,'Prueba de mensaje de info') 
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
            print(_(f'Se ha enviado un email de {nombre}, procedente de {email} con el comentario:{comentario}'))
            context = {
                'formulario': formulario
            }
            messages.info(request,_('Correo enviado correctamente'))
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


