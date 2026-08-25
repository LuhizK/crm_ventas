from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Ciudad
from ..serializers import CiudadSerializer
from .api_auth import validar_token

# --------------------------------------------------------
# RUTA 1: Lista todas las ciudades (GET) o Crea una nueva (POST)
# --------------------------------------------------------
@api_view(['GET', 'POST'])
@validar_token
def ciudad_api_list(request):
    if request.method == 'GET':
        ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # Guarda en la base de datos
            # 201 Created: Nuevo recurso creado
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        # 400 Bad Request: Error de validación
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------
# RUTA 2: Detalle (GET), Actualizar (PUT), Eliminar (DELETE) de UNA ciudad
# --------------------------------------------------------
@api_view(['GET', 'PUT', 'DELETE'])
@validar_token
def ciudad_api_detail(request, pk):
    try:
        ciudad = Ciudad.objects.get(pk=pk)
    except Ciudad.DoesNotExist:
        # 404 Not Found: El recurso no existe
        return Response({'error': 'Ciudad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CiudadSerializer(ciudad)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CiudadSerializer(ciudad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ciudad.delete()
        # 204 No Content: Procesado con éxito, sin datos devueltos
        return Response(status=status.HTTP_204_NO_CONTENT)