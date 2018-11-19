from django.db import models


# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=50)
    isAdminChoices = (('yes', 'yes'), ('no', 'no'),)
    isAdmin = models.CharField(max_length=3, choices=isAdminChoices, default='no')


class PersonaNatural(Usuario):
    nombre = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)


class Curso(models.Model):
    codigo = models.CharField(max_length=7)
    seccion = models.IntegerField()
    año = models.IntegerField()
    semestreChoices = (('otoño', 'otoño'), ('primavera', 'primavera'),)
    semestre = models.CharField(max_length=10, choices=semestreChoices, default="otoño")
    nombre = models.CharField(max_length=100)

    class Meta:
        unique_together = ["codigo", "seccion", "año", "semestre"]


class ParticipacionEnCurso(models.Model):
    persona = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rolChoices = (("profesor", "profesor"), ("auxiliar", "auxiliar"), ("ayudante", "ayudante"), ("alumno", "alumno"))
    rol= models.CharField(max_length=10, choices=rolChoices, default="alumno")

    class Meta:
        unique_together = ["persona", "curso"]


class Grupo(models.Model):
    integrante = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)


class RelCursoGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class Coevaluacion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estadoChoices = (('abierta', 'abierta'), ('cerrada', 'cerrada'),)
    estado = models.CharField(max_length=9, choices=estadoChoices, default="cerrada")


class Pregunta(models.Model):
    contenido= models.TextField(max_length=300)
    ponderacion= models.FloatField()
