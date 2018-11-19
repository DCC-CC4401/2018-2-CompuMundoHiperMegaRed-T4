from django.contrib import admin
from apps.app1.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(PersonaNatural)
admin.site.register(Curso)
admin.site.register(ParticipacionEnCurso)
admin.site.register(Grupo)
admin.site.register(RelCursoGrupo)
admin.site.register(Coevaluacion)
admin.site.register(Pregunta)
