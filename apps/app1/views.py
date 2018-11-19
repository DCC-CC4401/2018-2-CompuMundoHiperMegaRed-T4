from django.shortcuts import render
# Create your views here.


def login(request):
    return render(request, 'login.html')


def perfil_alumno_vista_docente(request):
    return render(request, 'perfil-alumno-vista-docente.html')


def perfil_propio(request):
    return render(request, 'perfil-vista-dueno.html')

def home_profesor(request):
    return render(request, 'home-vista-profesor.html')
