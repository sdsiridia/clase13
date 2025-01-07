"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include # , re_path
from debug_toolbar.toolbar import debug_toolbar_urls


# from django.urls import include

# importamos la funsion que esta en el otro archivo
from .views import home_view, contact_view, search_view #, SetLanguageView



# urlpatterns = [
#     path('grappelli/', include('grappelli.urls')),  # grappelli URLS
#     re_path(r'^rosetta/', include('rosetta.urls')),
#     path('set-language/', SetLanguageView.as_view(),name='set_language'),
#     path("", home_view, name='home'),

#     # path("",include('books.urls',namespace='books')), # en esta parte path(""  entre las ""
#     # puede escribir cualuier cosa, es para que las urs en la barra esten
#     # dentro de una subcategoria, si no pongo nada solo cambia la url
#
#
#     path('editorial/', include('books.urls.editorial_url', namespace='editorial')),
#     path('autor/', include('books.urls.autor_url', namespace='autor')),
#     path('libro/', include('books.urls.libro_url', namespace='libro')),

#     path("contacto/", contact_view, name='contacto'),
#     path('admin/', admin.site.urls),
# ] + debug_toolbar_urls()


# urlpatterns +=i18n_patterns[
#             path("buscar/", search_view, name='search'),
# ]

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Incluir la vista 'set_language'
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("buscar/", search_view, name="search"),
    path("", home_view, name="home"),
    path('editorial/', include('books.urls.editorial_url', namespace='editorial')),
    path('autor/', include('books.urls.autor_url', namespace='autor')),
    path('libro/', include('books.urls.libro_url', namespace='libro')),

    path("contacta-con-nosotros/", contact_view, name="contacto"),
)

# si rosatta esta instalado anade las urls de rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
                    ]