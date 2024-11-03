
from django.urls import path


from .views import (
    editoriales_view,
    autores_view,
    libros_view
    )

urlpatterns = [
    
    path("autores/",autores_view),
    path("editoriales/",editoriales_view),
    path("libros/",libros_view),

  
]

