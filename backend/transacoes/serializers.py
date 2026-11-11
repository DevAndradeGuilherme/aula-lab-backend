from rest_framework import serializers
from .models import Transacao

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id','descricao','valor', 'data', 'observacao', 'tipo', 'status', 'usuario', 'categoria']