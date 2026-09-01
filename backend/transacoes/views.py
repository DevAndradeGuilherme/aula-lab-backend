from django.http import JsonResponse
from .models import Transacao

def listar_transacoes(request):
    transacoes = Transacao.objects.all().values('descricao','valor','data','tipo', 'status', 'usuario', 'categoria')
    return JsonResponse(list(transacoes), safe=False)
def listar_transacoes_pendentes(request):
    transacoes = Transacao.objects.filter(status='PENDENTE').values('descricao','valor','data','tipo', 'status', 'usuario', 'categoria')
    return JsonResponse(list(transacoes), safe=False)