# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        password = request.POST['password']
        region = request.POST['region']
        comuna = request.POST['comuna']

        if User.objects.filter(email=correo).exists():
            return render(request, 'usuarios/register.html', {
                'error': 'El correo electrónico ya está en uso.'
            })

        user = User.objects.create_user(
            username=correo,  # Puedes usar alguna otra lógica para generar el nombre de usuario si lo prefieres
            first_name=nombre,
            email=correo,
            password=password
        )
        # Crear perfil del usuario
        Profile.objects.create(
            user=user,
            region=region,
            comuna=comuna
        )

        user = authenticate(username=correo, password=password)
        auth_login(request, user)
        return redirect('index')

    return render(request, 'usuarios/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'usuarios/login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')
