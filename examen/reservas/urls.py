from django.urls import path
from .views import socio_view, reserva_lista, eliminar_reserva

urlpatterns = [
    path('socio/', socio_view, name='socio'),
    path('reservas/', reserva_lista, name='reserva_lista'),
    path('eliminar/<int:pk>/', eliminar_reserva, name='eliminar_reserva'),
]