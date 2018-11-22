from itertools import chain
from typing import Any, Union
from django.shortcuts import render
from django.template.smartif import key

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
    # obtener rut desde sesión:
    rut = request.session['usuario']
    contexto = {}
    # nombre del usuario:
    user = User.objects.filter(username=rut)
    nombre = user[0].first_name
    apellido = user[0].last_name
    contexto.update({'nombre': nombre + ' ' + apellido})
    # tabla de cursos:
    cursosTemp = []  # lista de cursos que se pasará al template
    cursos = ParticipacionEnCurso.objects.filter(persona__username=rut).order_by('-curso__año', '-curso__semestre')  # obtengo cursos del alumno
    for curso in cursos:
        idCurso = curso.id
        infocursos = Curso.objects.get(id=idCurso)
        cursosTemp.append(infocursos)
    contexto.update({'cursos': cursosTemp})
    # tabla de coevaluaciones:
    coevTemp = []  # lista de coevaluaciones que se pasará al template
    coevs = Coevaluacion.objects.none()
    for curso in cursos:
        idCurso = curso.id
        coevs = coevs | Coevaluacion.objects.filter(curso=idCurso)
    coevs.order_by('-fecha_inicio')
    for coev in coevs:
        coevTemp.append(coev)
    contexto.update({'coevs': coevTemp})
    return render(request, 'home-vista-alumno.html', contexto)


def perfil_alumno_vista_docente(request):
    return render(request, 'perfil-alumno-vista-docente.html')


def perfil_propio(request):

    rut = request.session['usuario']
    usuario = User.objects.get(username=rut)

    cursosTemp = []
    cursos = ParticipacionEnCurso.objects.filter(persona__username=rut)
    for curso in cursos:
        idCurso = curso.id
        infocursos = Curso.objects.get(id=idCurso)
        cursosTemp.append(infocursos)

    return render(request, 'perfil-vista-dueno.html', {'usuario': usuario , 'cursos': cursosTemp})


def home_profesor(request):
    return render(request, 'home-vista-profesor.html')


def ficha_coevaluacion_alumno(request):
    return render(request, 'coevaluacion-vista-alumno.html')
