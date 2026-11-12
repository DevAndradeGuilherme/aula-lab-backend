from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Categoria
from .serializers import CategoriaSerializer

@api_view(['GET', 'POST'])
def categorias_lista(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def categoria_detalhe(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response({'detail': 'Categoria não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    if request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    parcial = request.method == 'PATCH'
    serializer = CategoriaSerializer(categoria, data=request.data, partial=parcial)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_categorias_despesas(request):
    categorias = Categoria.objects.filter(tipo='Despesa')
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)