from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehiculo_list, name='vehiculo_list'),
    path('<int:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('nuevo/', views.vehiculo_add, name='vehiculo_add'),
    path('<int:pk>/editar/', views.vehiculo_edit, name='vehiculo_edit'),
    path('<int:pk>/borrar/', views.vehiculo_delete, name='vehiculo_delete'),
]