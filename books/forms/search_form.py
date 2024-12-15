from django import forms

class SearchForms(forms.Form):
    q = forms.CharField(
        label = "Introduce Cualquier Cadena de Texto",
        max_length=100, 
        )