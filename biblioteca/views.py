from django.shortcuts import render

# Vistas generales de la Aplicaciòn 
def home_view(request):
    return render(request,"home.html") # la funsion render necesita 2 parametros un request y un archivo para renderizar 


def contact_view(request):
    return render(request,"contacto.html")