from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Enfermedades
#from .forms import

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')

def acerca(request):
    return render(request, 'acerca.html')

def instrucciones(request):
    return render(request, 'instrucciones.html')

def autores(request):
    return render(request, 'autores.html')

# ENFERMEDADES

def EnfTaponesCerumen(request):
    return render(request, 'EnfTaponesCerumen.html')

def EnfTinnitus(request):
    return render(request,'EnfTinnitus.html')

def EnfOtosclerosis(request):
    return render(request,'EnfOtosclerosis.html')

def EnfOtematoma(request):
    return render(request,'EnfOtematoma.html')

def EnfDermatitisSeborreica(request):
    return render(request,'EnfDermatitisSeborreica.html')

def EnfOtitisExterna(request):
    return render(request,'EnfOtitisExterna.html')

def EnfPresbiacusia(request):
    return render(request,'EnfPresbiacusia.html')

def EnfCofosis(request):
    return render(request,'EnfCofosis.html')

def EnfPericondritis(request):
    return render(request,'EnfPericondritis.html')

def EnfTraumatismosAcusticos(request):
    return render(request,'EnfTraumatismosAcusticos.html')

# C A S O S  E S P E C I A L E S #
def EnfTaponesPresbiacusia(request):
    return render(request,'EnfTaponesPresbiacusia.html')

def EnfTinnitusOtosclerosis(request):
    return render(request,'EnfTinnitusOtosclerosis.html')

def EnfNoEnfermedades(request):
    return render(request,'EnfNoEnfermedades.html')

def EnfPeligro(request):
    return render(request,'EnfPeligro.html')

def EnfOtro(request):
    return render(request,'EnfOtro.html')