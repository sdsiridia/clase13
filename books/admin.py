from django.contrib import admin


from books.models import Autor, Editorial, Libro
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class AutorResource(resources.ModelResource):

    class Meta:
        model = Autor
        fields = ('nombre', 'apellido','fecha_nacimiento')
        export_order = ('nombre', 'apellido','fecha_nacimiento')


class BookinLine(admin.StackedInline): # puedo usar TabularInline para mostrar horizontoal o StackedInline para que se vea en vertical
     model = Libro

@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin): # heredamos de ImportExportModelAdmin por que da mas funcionanlidades con la extension
    resources_class = AutorResource # hereda de la clase para saber que campos son los que puedo exportar
    list_display = ['pk','nombre','apellido', # permito en la web separar por columnas los datos 
                    'fecha_nacimiento',
                    'email',
                    'telefono'
                    ]
    ordering = ['apellido','nombre']
    

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre','ciudad', # permito en la web separar por columnas los datos 
                    'sitio_web',
                    'email',
                    'telefono',
                    'fecha_fundacion'
                    ]

    list_filter = ['fecha_fundacion']
    inlines=[
         BookinLine,
    ]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
      list_display = [
        "titulo",
        "editorial",
        "isbn",
        "is_out_of_stock",
        "fecha_publicacion",
        "numero_paginas",
        "idioma",
    ]
      list_filter = ['editorial','idioma']
      search_fields = ['titulo','autores__nombre'] # campos de busqueda, el el caso de autores con "__" hago referencia al campo por el cual buscar
      filter_horizontal = ('autores',)
   

