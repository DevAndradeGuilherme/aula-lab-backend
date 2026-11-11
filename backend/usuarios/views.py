from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET'])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def buscar_usuario(request, id):
    usuario = Usuario.objects.filter(id=id).first()
    if usuario is None:
        return Response(
            {"erro: Usuário não encontrado"},
            status = 404
        )
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)