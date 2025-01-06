from django import forms
from django.utils.translation import gettext_lazy as _lazy

class ContactForms(forms.Form):
   nombre = forms.CharField(max_length=140, label=_lazy("Nombre"))
   email = forms.EmailField(label=_lazy("Correo"))
   comentario = forms.CharField(max_length=1000, label=_lazy("Comentario"), widget=forms.Textarea)

   # puedo definir funciones con clean_<nombre_del_campo> para realizar validaciones, ejemplo:

   def clean_nombre(self):
      nombre = self.cleaned_data.get('nombre')
      if len(nombre)<5:
         raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
      return nombre
   
   # otro ejemplo para el campo email

   """ def clean_email(self):
      email = self.cleaned_data.get('email')
      if 'prueba' in email:
         raise forms.ValidationError("El email no puede contener la palabra PRUEBA")
      return email """