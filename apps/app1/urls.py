from django.urls import path
from apps.app1.views import *


urlpatterns = [
    path(r'', login),
    path(r'alumno', perfil_alumno_vista_docente),
    path(r'perfil', perfil_propio),
    path(r'homeEquipoDocente', home_profesor)
]
