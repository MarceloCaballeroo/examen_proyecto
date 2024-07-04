from django import forms
from django.core.exceptions import ValidationError
from .models import Usuarios, Region, Comuna

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'correo', 'password', 'region', 'comuna']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre Completo',
            'correo': 'Correo Electrónico',
            'password': 'Contraseña',
        }
        help_texts = {
            'password': 'Tu contraseña debe contener al menos 8 caracteres.',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.all()
        self.fields['comuna'].queryset = Comuna.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # Manejo de excepción inválida o tipo incorrecto; el queryset vacío será usado

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Usuarios.objects.filter(correo=correo).exists():
            raise ValidationError("El correo electrónico ya está en uso.")
        return correo

    def clean(self):
        cleaned_data = super().clean()
        region = cleaned_data.get('region')
        comuna = cleaned_data.get('comuna')

        # Asegúrate de que la comuna seleccionada pertenezca a la región seleccionada
        if comuna and comuna.region != region:
            self.add_error('comuna', "La comuna seleccionada no pertenece a la región indicada.")

        return cleaned_data