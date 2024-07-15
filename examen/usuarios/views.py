# usuarios/views.py

from django.shortcuts import render, redirect , get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.core.paginator import Paginator


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
        return redirect('home')

    return render(request, 'usuarios/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'usuarios/login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def profile_list(request):
    profiles = Profile.objects.all()

    # Filtro por nombre de usuario
    nombre_filter = request.GET.get('nombre')
    if nombre_filter:
        profiles = profiles.filter(user__username__icontains=nombre_filter)

    # Configuración de paginación
    paginator = Paginator(profiles, 10)  # Mostrar 10 perfiles por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'profiles': page_obj,
        'nombre_filter': nombre_filter,  # Para mantener el valor del filtro en el formulario
    }
    return render(request, 'usuarios/profile_list.html', context)

@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {
        'profile': profile,
    }
    return render(request, 'usuarios/profile_detail.html', context)

@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        # Actualizar el perfil
        profile.region = request.POST.get('region')
        profile.comuna = request.POST.get('comuna')
        profile.save()
        return redirect('profile_list')
    context = {
        'profile': profile,
    }
    return render(request, 'usuarios/profile_edit.html', context)

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        # Borrar el perfil
        profile.user.delete()
        return redirect('profile_list')
    context = {
        'profile': profile,
    }
    return render(request, 'usuarios/profile_delete.html', context)




