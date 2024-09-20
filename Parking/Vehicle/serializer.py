from Vehicle.models import vehicle
from rest_framework import serializers

class vehicle_serializer(serializers.ModelSerializer):
    class Meta:
        model=vehicle
        fields=['id', 'placa', 'marca', 'color_vehiculo', 'modelo']
