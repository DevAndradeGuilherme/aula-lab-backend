from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transacao
from .serializers import TransacaoSerializer

@api_view(['GET'])
def listar_transacoes(request):
    transacoes = Transacao.objects.all()
    serializer = TransacaoSerializer(transacoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_transacoes_pendentes(request):
    transacoes = Transacao.objects.filter(status='Pendente')
    serializer = TransacaoSerializer(transacoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_transacoes_pagas(request):
    transacoes = Transacao.objects.filter(status='Pago')
    serializer = TransacaoSerializer(transacoes, many=True)
    return Response(serializer.data)