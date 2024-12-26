''' formulario de libro'''
from django import forms
from django.forms import ModelForm
from books.models import Libro


class Librocreate(forms.Form):
    '''crear un objeto libro'''
    class Meta:
        '''hereda del modelo libro'''
        model = Libro
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


class LibroModelFormCreate(ModelForm):
    ''' crear un objeto libro'''
    class Meta:
        '''hereda del modelo libro'''
        model = Libro
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
