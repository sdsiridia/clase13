'''clase de creacion de un nuebvo autor'''
from django import forms
from django.forms import ModelForm
from books.models import Autor


class AutorCreate(forms.Form):
    '''campos de la clase nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=300, required=False)
    ciudad = forms.CharField(max_length=100, required=False)
    estado = forms.CharField(max_length=100, required=False)
    pais = forms.CharField(max_length=100, required=False)
    codigo_postal = forms.CharField(max_length=20, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    sitio_web = forms.URLField(required=False)
    f_nac = forms.DateField(widget=forms.SelectDateWidget)'''

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


'''nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    premios = models.TextField(blank=True, null=True)'''
