from django.urls import path
from .views import register, login_view, logout_view, profile_list, profile_add, profile_edit, profile_delete

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profiles/', profile_list, name='profile_list'),
    path('profiles/add/', profile_add, name='profile_add'),
    path('profiles/edit/<int:pk>/', profile_edit, name='profile_edit'),
    path('profiles/delete/<int:pk>/', profile_delete, name='profile_delete'),
]
