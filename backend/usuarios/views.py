from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all().values('id','nome','email','data_cadastro')
    return JsonResponse(list(usuarios), safe=False)