from django.urls import path
from .views import register, login_view, logout_view
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profiles/<int:pk>/editar/', views.profile_edit, name='profile_edit'),
    path('profiles/<int:pk>/borrar/', views.profile_delete, name='profile_delete'),
]
