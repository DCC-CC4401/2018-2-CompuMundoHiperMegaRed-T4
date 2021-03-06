from django.contrib import admin
from apps.app1.models import *
from django.contrib.auth.models import User


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'seccion', 'año', 'semestre')


class ParticipacionEnCursoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'curso', 'rol')


class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'integrante')


class CoevaluacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso', 'estado')


class ContestadaAdmin(admin.ModelAdmin):
    list_display = ('coevaluacion', 'alumno_evaluador', 'alumno_a_evaluar', 'estado')

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso')

class NotasAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'nota', 'coevaluacion')


admin.site.register(Curso, CursoAdmin)
admin.site.register(ParticipacionEnCurso, ParticipacionEnCursoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Coevaluacion, CoevaluacionAdmin)
admin.site.register(Contestada, ContestadaAdmin)
admin.site.register(Pregunta)
admin.site.register(Notas, NotasAdmin)
