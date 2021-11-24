"""proyectoIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from EnfAuditivas import views as enfermedades_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', enfermedades_view.index),
    path('', include('EnfAuditivas.urls')),
    path('home/', enfermedades_view.home),
    path('acerca/', enfermedades_view.acerca),
    path('instrucciones/', enfermedades_view.instrucciones),
    path('autores/', enfermedades_view.autores),

    # E N F E R M E D A D E S #
    path('EnfTaponesCerumen/', enfermedades_view.EnfTaponesCerumen),
    path('EnfTinnitus/', enfermedades_view.EnfTinnitus),
    path('EnfOtosclerosis/', enfermedades_view.EnfOtosclerosis),
    path('EnfOtematoma/',enfermedades_view.EnfOtematoma,name="EnfOtematoma"),
    path('EnfDermatitisSeborreica/', enfermedades_view.EnfDermatitisSeborreica),
    path('EnfOtitisExterna/',enfermedades_view.EnfOtitisExterna,name="EnfOtitisExterna"),
    path('EnfPresbiacusia/',enfermedades_view.EnfPresbiacusia, name="EnfPresbiacusia"),
    path('EnfCofosis/',enfermedades_view.EnfCofosis, name="EnfCofosis"),
    path('EnfPericondritis/',enfermedades_view.EnfPericondritis, name="EnfPericondritis"),
    path('EnfTraumatismosAcusticos/',enfermedades_view.EnfTraumatismosAcusticos, name="EnfTraumatismosAcusticos"),

    # C A S O S  E S P E C I A L E S #
    path('EnfTaponesPresbiacusia/',enfermedades_view.EnfTaponesPresbiacusia, name="EnfTaponesPresbiacusia"),
    path('EnfNoEnfermedades/',enfermedades_view.EnfNoEnfermedades, name="EnfNoEnfermedades"),
    path('EnfPeligro/',enfermedades_view.EnfPeligro, name="EnfPeligro"),
    path('EnfOtro/',enfermedades_view.EnfOtro, name="EnfOtro"), 

    
    
]
