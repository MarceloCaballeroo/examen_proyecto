from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import VehiculoForm

from django.shortcuts import render
from .models import Vehiculoo  # Asegúrate de importar el modelo correcto


def vehiculo_list(request):
    vehiculos_list = Vehiculoo.objects.all().order_by('nombre')  # Ordenar por nombre
    
    # Filtrar por búsqueda
    query = request.GET.get('q')
    if query:
        vehiculos_list = vehiculos_list.filter(
            nombre__icontains=query
        )

    # Paginar los resultados
    paginator = Paginator(vehiculos_list, 10)  # 10 vehículos por página
    page = request.GET.get('page')
    try:
        vehiculos = paginator.page(page)
    except PageNotAnInteger:
        vehiculos = paginator.page(1)
    except EmptyPage:
        vehiculos = paginator.page(paginator.num_pages)

    return render(request, 'vehiculos/vehiculo_list.html', {'vehiculos': vehiculos, 'query': query})


def vehiculo_add(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def vehiculo_edit(request, pk):
    vehiculo = get_object_or_404(Vehiculoo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculoo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo_list')
    return render(request, 'vehiculos/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})