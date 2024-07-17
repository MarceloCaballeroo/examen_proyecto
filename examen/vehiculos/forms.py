from django import forms
from .models import Vehiculoo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculoo
        fields = ['nombre', 'descripcion', 'precio', 'imagen']