from django.urls import path
from . import views
from .views import add_to_cart, cart_detail, remove_from_cart


urlpatterns = [
    path('', views.vehiculo_list, name='vehiculo_list'),
    path('nuevo/', views.vehiculo_add, name='vehiculo_add'),
    path('<int:pk>/editar/', views.vehiculo_edit, name='vehiculo_edit'),
    path('<int:pk>/borrar/', views.vehiculo_delete, name='vehiculo_delete'),
    path('catalogo', views.catalogo, name='catalogo'),

    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:vehiculo_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:vehiculo_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    
    path('checkout/', views.checkout, name='checkout'),
]