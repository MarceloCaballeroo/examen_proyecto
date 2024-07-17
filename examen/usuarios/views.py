from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, UserEditForm
from .models import UserProfile
from django.core.paginator import Paginator

def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            first_name = user_form.cleaned_data.get('first_name')
            last_name = user_form.cleaned_data.get('last_name')
            user.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
    return render(request, 'usuarios/register.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'usuarios/profile_list.html', {'profiles': profiles})

@login_required
def profile_add(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('profile_list')
    else:
        user_form = UserForm()
    return render(request, 'usuarios/profile_add.html', {
        'user_form': user_form,
    })

@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=profile.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile_list')
    else:
        user_form = UserEditForm(instance=profile.user)
    return render(request, 'usuarios/profile_edit.html', {
        'user_form': user_form,
    })

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.user.delete()
        return redirect('profile_list')
    return render(request, 'usuarios/profile_delete.html', {'profile': profile})
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.user.delete()
        return redirect('profile_list')
    return render(request, 'usuarios/profile_delete.html', {'profile': profile})
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        # Borrar el perfil
        profile.user.delete()
        return redirect('profile_list')
    context = {
        'profile': profile,
    }
    return render(request, 'usuarios/profile_delete.html', context)