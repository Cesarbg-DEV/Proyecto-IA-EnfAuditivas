from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from EnfAuditivas import views as enfermedades_view

urlpatterns = [
    path('', enfermedades_view.home, name='Home'),
]