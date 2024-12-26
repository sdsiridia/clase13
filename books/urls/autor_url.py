
from django.urls import path


# from views import (
#     editoriales_view,
#     autores_view,
#     libros_view,
#     autor_detail,
#     editorial_create,
#     editorial_detail,
#     EditorialList,
#     EditorialDetails,
#     LibroCreateView,
#     LibrosListView,
#     LibroUpdateView,
#     LibroDeleteView,
#     )


app_name = 'autor' 

urlpatterns = [
    
    # path("autores/",autores_view,name='autor_list'),
    # path("autores/<int:id>/",autor_detail,name='autor_detail'), #todas las urs que coincidan con "autores/<un_numero>" 
    # path("editorial/detalle/ccbv/<pk>/",EditorialDetails.as_view(),name='editorial_detail_ccbv'),
    # path("editorial/detalle/<int:id>/",editorial_detail,name='editorial_detail'),
    # path("editoriales/",editoriales_view,name='editorial_list'),
    # path("editoriales/lista/",EditorialList.as_view(),name='editorial_lista_ccbv'),
    # path("editoriales/create/",editorial_create,name='editorial_create'),
    # path("libros/",LibrosListView.as_view(),name='libros_list'),
    # path("libros/nuevo",LibroCreateView.as_view(),name='libro_create'),
    # path("libros/editar/<pk>/",LibroUpdateView.as_view(),name='libro_update'),
    # path("libros/eliminar/<pk>/",LibroDeleteView.as_view(),name='libro_delete'),
]

