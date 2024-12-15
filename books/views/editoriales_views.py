from django.shortcuts import render,redirect,reverse
from books.forms import EditorialCreate
from books.models import Editorial

# Create your views here.


def editoriales_view(request):
    editoriales = Editorial.objects.all()
    context = {
        'editoriales' : editoriales
    }
    return render(request,"editoriales/editoriales.html",context)

def editorial_detail(request,id):
       
    editorial = Editorial.objects.get(pk=id)

    context = {
        "editorial": editorial
    }
    return render(request, "editoriales/editorial_detail.html", context)


def editorial_create(request):
    if request.POST:
        form = EditorialCreate(request.POST)
        if form.is_valid():
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data['nombre'],
                direccion = form.cleaned_data['direccion'],
                email = form.cleaned_data['email'],
                fecha_fundacion = form.cleaned_data['fecha_fundacion']
            )
            # Redireccionamos a los datos de la nueva editorial creada
            return redirect(reverse('books:editorial_detail',kwargs={'id':nueva_editorial.pk}))
    else:    
        form = EditorialCreate()
    
    context ={
        'form':form
    }
    return render(request,"editoriales/editorial_create.html",context)