'''para poder colocar en elfooter el año en todas las páginas'''
from datetime import datetime
from books.models import Libro, Editorial, Autor

# aunque marca error el request si lo quito no funciona


def get_current_year_context_processor(request):
    ''' en una funcion de normal haríamops el retur current_year, 
    pero vamos a devolver un diccionario
    con esto lo añadimos a nuestro array de 
    funciones de context processor en setting
    '''
    current_year = datetime.now().year

    return {
        'current_year': current_year
    }


def get_statistic_books(request):
    ''' contar cantidad de todo'''
    return {
        'n_books': Libro.objects.all().count(),
        'n_editorial': Editorial.objects.all().count(),
        'n_autor': Autor.objects.all().count(),
        'user_logged': request

    }
