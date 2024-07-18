from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import VehiculoForm
from .models import Vehiculoo, Cart, CartItem

def catalogo(request):
    vehiculos = Vehiculoo.objects.all()
    return render(request, 'vehiculos/catalogo.html', {'vehiculos': vehiculos})

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    else:
        cart = None
    return render(request, 'vehiculos/cart_detail.html', {'cart': cart})

def add_to_cart(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculoo, pk=vehiculo_id)
    
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = get_object_or_404(Cart, pk=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    
    cart.add(vehiculo=vehiculo)
    
    return redirect('cart_detail')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
    
    return redirect('cart_detail')




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

def checkout(request):
    cart = get_cart_or_create(request)  # Función para obtener el carrito actual del usuario

    context = {
        'cart': cart,
    }
    return render(request, 'vehiculos/checkout.html', context)

def get_cart_or_create(request):

    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:

            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id  # Actualiza el cart_id en la sesión
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id  # Guarda el cart_id en la sesión

    return cart

