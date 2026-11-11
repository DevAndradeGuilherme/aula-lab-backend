from django.urls import path
from .views import listar_transacoes, listar_transacoes_pendentes, listar_transacoes_pagas

urlpatterns = [
    path('transacoes/', listar_transacoes),
    path('transacoes/pendentes/', listar_transacoes_pendentes),
    path('transacoes/pagas/', listar_transacoes_pagas),
]