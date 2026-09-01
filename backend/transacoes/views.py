from django.http import JsonResponse
from .models import Transacao

def listar_transacoes(request):
    transacoes = Transacao.objects.all().values('descricao','valor','data','tipo', 'status', 'usuario', 'categoria')
    return JsonResponse(list(Transacao), safe=False)