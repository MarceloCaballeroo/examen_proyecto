from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from vehiculos import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('quienes_somos/', TemplateView.as_view(template_name="quienes_somos.html"), name='quienes_somos'),
    path('sucursal/', TemplateView.as_view(template_name="sucursal.html"), name='sucursal'),

    path('vehiculos/', include('vehiculos.urls')),

    path('reservas/', include('reservas.urls')),
]
