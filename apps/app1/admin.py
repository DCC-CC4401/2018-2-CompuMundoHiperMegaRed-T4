from django.contrib import admin
from apps.app1.models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Curso)
admin.site.register(ParticipacionEnCurso)
admin.site.register(Grupo)
admin.site.register(RelCursoGrupo)
admin.site.register(Coevaluacion)
admin.site.register(Pregunta)
