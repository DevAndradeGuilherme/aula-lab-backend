from django.urls import path
from .views import listar_transacoes

urlpatterns = [
    path('transacoes/', listar_transacoes),
]