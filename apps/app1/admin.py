from django.contrib import admin
from apps.app1.models import *
from django.contrib.auth.models import User


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'seccion', 'año', 'semestre')


class ParticipacionEnCursoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'curso', 'rol')


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'integrante', 'curso')


class CoevaluacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso', 'estado')


admin.site.register(Curso, CursoAdmin)
admin.site.register(ParticipacionEnCurso, ParticipacionEnCursoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Coevaluacion, CoevaluacionAdmin)
admin.site.register(Pregunta)
admin.site.register(Notas)
