# Generated by Django 2.1.3 on 2018-11-22 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coevaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('estado', models.CharField(choices=[('abierta', 'abierta'), ('cerrada', 'cerrada'), ('publicada', 'publicada')], default='cerrada', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionEnCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('profesor', 'profesor'), ('auxiliar', 'auxiliar'), ('ayudante', 'ayudante'), ('alumno', 'alumno')], default='alumno', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=300)),
                ('ponderacion', models.FloatField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='participaciónencurso',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='participaciónencurso',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='participaciónencurso',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='personanatural',
            name='usuario_ptr',
        ),
        migrations.AddField(
            model_name='curso',
            name='semestre',
            field=models.CharField(choices=[('1', 'otoño'), ('2', 'primavera')], default='otoño', max_length=10),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='integrante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('codigo', 'seccion', 'año', 'semestre')},
        ),
        migrations.DeleteModel(
            name='ParticipaciónEnCurso',
        ),
        migrations.DeleteModel(
            name='PersonaNatural',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='participacionencurso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Curso'),
        ),
        migrations.AddField(
            model_name='participacionencurso',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='participacionencurso',
            unique_together={('persona', 'curso')},
        ),
    ]