from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Enfermedades
#from .forms import

# Create your views here.
def home(request):
    return render(request,'index.html')