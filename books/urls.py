
from django.urls import path


from .views import (
    editoriales_view,
    autores_view,
    libros_view,
    autor_detail,
    editorial_create,
    editorial_detail,
    )

app_name = 'books' 

urlpatterns = [
    
    path("autores/",autores_view,name='autor_list'),
    path("autores/<int:id>/",autor_detail,name='autor_detail'), #todas las urs que coincidan con "autores/<un_numero>" 
    path("editorial/detalle/<int:id>/",editorial_detail,name='editorial_detail'),
    path("editoriales/",editoriales_view,name='editorial_list'),
    path("editoriales/create/",editorial_create,name='editorial_create'),
    path("libros/",libros_view,name='libros_list'),

  
]

