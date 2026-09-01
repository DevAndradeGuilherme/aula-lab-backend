from django.urls import path
from .views import listar_transacoes, listar_transacoes_pendentes

urlpatterns = [
    path('transacoes/', listar_transacoes),
    path('transacoes/pendentes/', listar_transacoes_pendentes),
]