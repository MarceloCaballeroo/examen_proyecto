
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('usuarios/', include('usuarios.urls')), 
    path('profiles/', include('usuarios.urls')),# 'usuarios/' is the namespace
    path('socio/', TemplateView.as_view(template_name="socio.html"), name='socio'),
    path('sucursal/', TemplateView.as_view(template_name="sucursal.html"), name='sucursal'),
    path('vehiculo/', TemplateView.as_view(template_name="vehiculo.html"), name='vehiculo'),
    path('admin/', admin.site.urls),
    path('vehiculos/', include('vehiculos.urls')),
]   