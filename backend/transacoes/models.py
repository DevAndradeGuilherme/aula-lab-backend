from django.db import models
from categorias.models import Categoria
from usuarios.models import Usuario

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('RECEITA','Receita'),
        ('DESPESA','Despesa'),
    ]
    STATUS_CHOICES = [
        ('PENDENTE','Pendente'),
        ('PAGO','Pago'),
    ]

    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    data = models.DateField()
    observacao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10,choices=TIPO_CHOICES)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='PENDENTE')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.descricao} - {self.valor}"
