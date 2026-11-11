from django.urls import path
from .views import listar_usuarios, buscar_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuarios/<int:id>/', buscar_usuario),
]