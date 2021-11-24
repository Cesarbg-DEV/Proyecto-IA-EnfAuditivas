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

    # E N F E R M E D A D E S #
    path('EnfTaponesCerumen/', enfermedades_view.EnfTaponesCerumen, name='EnfTaponesCerumen'),
    path('EnfTinnitus/',enfermedades_view.EnfTinnitus, name='EnfTinnitus'),
    path('EnfOtosclerosis/',enfermedades_view.EnfOtosclerosis, name='EnfOtosclerosis'), 
    path('EnfOtematoma/',enfermedades_view.EnfOtematoma,name="EnfOtematoma"),
    path('EnfDermatitisSeborreica/',enfermedades_view.EnfDermatitisSeborreica,name="EnfDermatitisSeborreica"),
    path('EnfOtitisExterna/',enfermedades_view.EnfOtitisExterna,name="EnfOtitisExterna"),
    path('EnfPresbiacusia/',enfermedades_view.EnfPresbiacusia, name="EnfPresbiacusia"),
    path('EnfCofosis/',enfermedades_view.EnfCofosis, name="EnfCofosis"),
    path('EnfPericondritis/',enfermedades_view.EnfPericondritis, name="EnfPericondritis"),

    # C A S O S  E S P E C I A L E S #
    path('EnfTraumatismosAcusticos/', enfermedades_view.EnfTraumatismosAcusticos, name="EnfTraumatismosAcusticos"),
    path('EnfTaponesPresbiacusia/', enfermedades_view.EnfTaponesPresbiacusia, name="EnfTaponesPresbiacusia"),
    path('EnfTinnitusOtosclerosis/', enfermedades_view.EnfTinnitusOtosclerosis, name="EnfTinnitusOtosclerosis"),
    path('EnfNoEnfermedades/', enfermedades_view.EnfNoEnfermedades, name="EnfNoEnfermedades"),
    path('EnfPeligro/', enfermedades_view.EnfPeligro, name="EnfPeligro"),
    path('EnfOtro/',enfermedades_view.EnfOtro, name="EnfOtro"), 

]