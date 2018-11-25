from django.urls import path
from apps.app1.views import *


urlpatterns = [
    path(r'', login),
    path(r'login', logout),
    path(r'alumno', perfil_alumno_vista_docente),
    path(r'perfil', perfil_propio),
    path(r'homeEquipoDocente', home_profesor),
    path(r'home', home_alumno),
    path(r'fichaCoevaluacion', ficha_coevaluacion_alumno, name='ficha_coevaluacion'),
    path(r'fichaCurso/docente', ficha_curso_docente),
]
