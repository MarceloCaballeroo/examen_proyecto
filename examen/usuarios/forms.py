# usuarios/forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Region, Comuna

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'nombre', 'correo', 'password1', 'password2', 'region', 'comuna')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Nombre de Usuario',
            'nombre': 'Nombre Completo',
            'correo': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.all()
        self.fields['comuna'].queryset = Comuna.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('nombre')
            except (ValueError, TypeError):
                pass

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if get_user_model().objects.filter(correo=correo).exists():
            raise ValidationError("El correo electrónico ya está en uso.")
        return correo

    def clean(self):
        cleaned_data = super().clean()
        region = cleaned_data.get('region')
        comuna = cleaned_data.get('comuna')

        if comuna and comuna.region != region:
            self.add_error('comuna', "La comuna seleccionada no pertenece a la región indicada.")

        return cleaned_data
