''' Formulario de busqueda'''
from django import forms


class SearchForms(forms.Form):
    ''' crea un objeto de tipo texto'''
    q = forms.CharField(
        label="Introduce Cualquier Cadena de Texto",
        max_length=100,
    )
