from rest_framework import serializers
from .models import Ciudad

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        # '__all__' le dice a Django que traduzca absolutamente todos 
        # los campos de la tabla Ciudad a JSON.
        fields = '__all__'