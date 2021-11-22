from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from EnfAuditivas import views as enfermedades_view

urlpatterns = [
    path('', enfermedades_view.index, name='index'),
    path('home/', enfermedades_view.home, name='home'),
    path('acerca/', enfermedades_view.acerca, name='acerca'),
    path('instrucciones/', enfermedades_view.instrucciones, name='instrucciones'),
    path('autores/', enfermedades_view.autores, name='autores'),   
]