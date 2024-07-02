
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('register/', TemplateView.as_view(template_name="register.html"), name='register'),
    path('socio/', TemplateView.as_view(template_name="socio.html"), name='socio'),
    path('sucursal/', TemplateView.as_view(template_name="sucursal.html"), name='sucursal'),
    path('vehiculo/', TemplateView.as_view(template_name="vehiculo.html"), name='vehiculo'),
]