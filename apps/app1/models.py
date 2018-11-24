from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    codigo = models.CharField(max_length=7)
    seccion = models.IntegerField()
    año = models.IntegerField()
    semestreChoices = (('1', 'otoño'), ('2', 'primavera'),)
    semestre = models.CharField(max_length=10, choices=semestreChoices, default="otoño")
    nombre = models.CharField(max_length=100)

    class Meta:
        unique_together = ["codigo", "seccion", "año", "semestre"]

    def complete(self):
        complete_name = "{0}-{1}"
        return complete_name.format(self.nombre, self.seccion)

    def __str__(self):
        return self.complete()


class ParticipacionEnCurso(models.Model):
    persona = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rolChoices = (("profesor", "profesor"), ("auxiliar", "auxiliar"), ("ayudante", "ayudante"), ("alumno", "alumno"))
    rol = models.CharField(max_length=10, choices=rolChoices, default="alumno")

    class Meta:
        unique_together = ["persona", "curso"]

    def complete(self):
        complete_name = "{0} --> {1}"
        return complete_name.format(self.persona, self.curso)

    def __str__(self):
        return self.complete()


class Grupo(models.Model):
    integrante = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def complete(self):
        complete_name = "{0}"
        return complete_name.format(self.nombre)

    def __str__(self):
        return self.complete()


class RelCursoGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["grupo", "curso"]

    def complete(self):
        complete_name = "{0} --> {1}"
        return complete_name.format(self.grupo, self.curso)

    def __str__(self):
        return self.complete()


class Coevaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estadoChoices = (('Abierta', 'abierta'), ('Cerrada', 'cerrada'), ('Publicada', 'publicada'),)
    estado = models.CharField(max_length=9, choices=estadoChoices, default="cerrada")

    def complete(self):
        complete_name = "{0} ({1})"
        return complete_name.format(self.nombre, self.curso)

    def __str__(self):
        return self.complete()


class Pregunta(models.Model):
    contenido = models.TextField(max_length=300)
    ponderacion = models.FloatField()

