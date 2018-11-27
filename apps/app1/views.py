from itertools import chain
from typing import Any, Union
from django.shortcuts import render, redirect
from django.template.backends import django
from django.template.smartif import key

from apps.app1.forms import *
from apps.app1.models import *
from django.contrib.auth import authenticate


# Create your views here.

log = False


def login(request):
    global log
    context = {'form': Login(), 'bad': False}
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = form.cleaned_data['rut']
            clave = form.cleaned_data['password']
            registrado = authenticate(username=user, password=clave)
            if registrado:
                request.session['usuario'] = user
                log = True
                return redirect('/home')
            else:
                context.update({'bad': True})
            return render(request, 'login.html', context)
        else:
            context.update({'bad': True})
            return render(request, 'login.html', context)
    else:
        if log:
            return redirect('/home')
        else:
            return render(request, 'login.html', context)


def logout(request):
    global log
    log = False
    return login(request)


def home_alumno(request):
    # copiar siguientes 3 lineas en las otras vistas:
    global log
    if not log:
        return redirect('/')
    # obtener rut desde sesión:

    rut = request.session['usuario']
    contexto = {}
    # nombre del usuario:
    user = User.objects.filter(username=rut)
    nombre = user[0].first_name
    apellido = user[0].last_name
    contexto.update({'nombre': nombre + ' ' + apellido})
    # tabla de cursos:
    cursosTemp = []  # lista de cursos que se pasara al template
    cursos = ParticipacionEnCurso.objects.filter(persona__username=rut).order_by('-curso__año', '-curso__semestre')  # obtengo cursos del alumno
    for curso in cursos:
        idCurso = curso.id
        infocursos = Curso.objects.get(id=idCurso)
        cursosTemp.append(infocursos)
    contexto.update({'cursos': cursosTemp})
    # tabla de coevaluaciones:
    coevTemp = []  # lista de coevaluaciones que se pasara al template
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
    bad1 = False
    bad2 = False

    form = CambioPassword()
    if request.method == 'POST':
        form = CambioPassword(request.POST)
        if form.is_valid():
            previous = form.cleaned_data['previous']
            actual = usuario.password

            if authenticate(request, username = rut, password = previous) != None:
                new = form.cleaned_data['new']
                confirmation = form.cleaned_data['confirmation']
                if new == confirmation:
                    usuario.set_password(new)
                    usuario.save()
                else:
                    bad2 = True

            else:
                bad1 = True

    coevals = []
    cursosTemp = []
    cursos = ParticipacionEnCurso.objects.filter(persona__username=rut)
    for curso in cursos:
        idCurso = curso.id
        infocursos = Curso.objects.get(id=idCurso)
        cursosTemp.append(infocursos)

        infocoev = Coevaluacion.objects.filter(curso = infocursos, estado='Publicada')
        for c in infocoev:
            coevals.append(c)

    notas = []
    for coeval in coevals:
        notaInfo = Notas.objects.get(coevaluacion= coeval, alumno = usuario)
        notas.append(notaInfo)

    return render(request, 'perfil-vista-dueno.html', {'usuario': usuario , 'cursos': cursosTemp, 'coevaluaciones': coevals, 'notas': notas, 'passwordForm': form, 'bad1': bad1, 'bad2': bad2})


def home_profesor(request):
    return render(request, 'home-vista-profesor.html')


def ficha_coevaluacion_alumno(request):

    data = {}
    rut = request.session['usuario']
    user = User.objects.filter(username=rut)
    nombre = user[0].first_name
    apellido = user[0].last_name
    data.update({'nombre': nombre + ' ' + apellido})

    coev_nombre = request.POST.get('coev_nombre', False)
    curso_codigo = request.POST.get('curso_codigo', False)
    curso_seccion = request.POST.get('curso_seccion', False)
    curso_ano = request.POST.get('curso_ano', False)
    curso_semestre = request.POST.get('curso_semestre', False)

    curso = Curso.objects.get(codigo=curso_codigo, seccion=curso_seccion, año=curso_ano, semestre=curso_semestre)
    data.update({'curso': curso})

    coevaluacion = Coevaluacion.objects.get(curso=curso, nombre=coev_nombre)
    data.update({'coev': coevaluacion})

    estados = Contestada.objects.filter(coevaluacion=coevaluacion, alumno_evaluador=user[0])
    data.update({'estados': estados})

    return render(request, 'coevaluacion-vista-alumno.html', data)


def ficha_curso(request):
    # copiar siguientes 3 lineas en las otras vistas:
    global log
    if not log:
        return redirect('/')
    # obtener rut desde sesión:
    rut = request.session['usuario']
    data = {}
    # nombre del usuario:
    user = User.objects.filter(username=rut)
    nombre = user[0].first_name
    apellido = user[0].last_name
    data.update({'nombre': nombre + ' ' + apellido})

    curso_codigo = request.POST.get('curso_codigo', False)
    curso_seccion = request.POST.get('curso_seccion', False)
    curso_ano = request.POST.get('curso_ano', False)
    curso_semestre = request.POST.get('curso_semestre', False)

    curso = Curso.objects.get(codigo=curso_codigo, seccion=curso_seccion, año=curso_ano, semestre=curso_semestre)
    data.update({'curso': curso})

    coevaluaciones = Coevaluacion.objects.filter(curso=curso).order_by('-fecha_inicio')
    data.update({'coevs': coevaluaciones})

    coevaluaciones_publicadas = Coevaluacion.objects.filter(curso=curso, estado='Publicada').order_by('-fecha_inicio')
    data.update({'coevslistas': coevaluaciones_publicadas})

    grupos = Grupo.objects.filter(curso=curso)

    lista_grupos = []
    for grupo in grupos:
        nombre = grupo.nombre
        integrantes = Asignacion.objects.filter(grupo=grupo)
        lista1 = []
        for integrante in integrantes:
            alumno = integrante.integrante
            notas = Notas.objects.filter(alumno=integrante.integrante)
            aux = [alumno, notas]
            lista1.append(aux)
        aux2 = [nombre, lista1]
        lista_grupos.append(aux2)

    data.update({'grupos': lista_grupos})
    rol = ParticipacionEnCurso(persona=user[0], curso=curso)
    if rol.rol == "alumno":
        return render(request, 'curso-vista-alumno.html', data)
    else:
        return render(request, 'curso-vista-docente.html', data)