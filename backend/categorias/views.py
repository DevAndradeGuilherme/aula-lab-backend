from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria
from .serializers import CategoriaSerializer

@api_view(['GET'])
def listar_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)