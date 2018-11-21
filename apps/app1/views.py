from typing import Any, Union
from django.shortcuts import render
from apps.app1.forms import *
from apps.app1.models import *
from django.contrib.auth import authenticate
# Create your views here.


def login(request):
    context = {'form': Login(), 'bad': False}
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = form.cleaned_data['rut']
            clave = form.cleaned_data['password']
            registrado = authenticate(username=user, password=clave)
            if registrado:
                request.session['usuario'] = user
                return home_alumno(request)
            else:
                context.update({'bad': True})
            return render(request, 'login.html', context)
        else:
            context.update({'bad': True})
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def home_alumno(request):
    codigos = {}
    seccion = {}
    año = {}
    semestre = {}
    rut = request.session['usuario']
    cursos = ParticipacionEnCurso.objects.filter(persona__username=rut)
    for curso in cursos:
        infocursos = Curso.objects.filter(curso=curso['curso'])
        codigos.update({})


    return render(request, 'home-vista-alumno.html')


def perfil_alumno_vista_docente(request):
    return render(request, 'perfil-alumno-vista-docente.html')


def perfil_propio(request):
    return render(request, 'perfil-vista-dueno.html')


def home_profesor(request):
    return render(request, 'home-vista-profesor.html')


def ficha_coevaluacion_alumno(request):
    return render(request, 'coevaluacion-vista-alumno.html')

