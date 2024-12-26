'''clase de creacion de un nuebvo autor'''
from django import forms
from django.forms import ModelForm
from books.models import Autor


class AutorCreate(forms.Form):
    ''' objeto nuevo autor'''
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    f_nac = forms.DateField()
    nacionalidad = forms.CharField(max_length=100)
    biografia = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20, blank=True, null=True)
    sitio_web = forms.URLField(blank=True, null=True)
    premios = forms.CharField(blank=True, null=True)

    def clean_nombre(self):
        '''restriccion en el nombre'''
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError(
                "El nombre debe tener al menos 5 caracteres")
        return nombre


class AutorModelFormCreate(ModelForm):
    '''no se bien que '''
    class Meta:
        ''' clase meta'''
        model = Autor
        fields = ['nombre', 'direccion', 'email', 'f_nac']
