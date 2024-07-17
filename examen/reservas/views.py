from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.decorators import login_required

@login_required
def socio_view(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            if request.user.is_authenticated:
                reserva.usuario = request.user
                reserva.email = request.user.email
                reserva.nombre = request.user.username
            else:
                reserva.email = request.POST.get('email')
                reserva.nombre = request.POST.get('nombre')
            reserva.save()
            return redirect('reserva_lista')
    else:
        form = ReservaForm()
    return render(request, 'reservas/socio.html', {'form': form, 'user': request.user})


@login_required
def reserva_lista(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

@login_required
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva_lista')
    return render(request, 'reservas/confirmar_eliminacion.html', {'reserva': reserva})
