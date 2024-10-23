import json
from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from Vehicle.models import vehicle
from .serializer import vehicle_serializer 
from django.shortcuts import get_object_or_404

from .decorators import is_authenticated

class vehicleApiView(APIView):
    
    
    def get(self, request, *args, **kwargs):
        lista_vehiculos = vehicle.objects.all()
        serializer_vehiculos = vehicle_serializer(lista_vehiculos, many=True)
        return Response(serializer_vehiculos.data, status=status.HTTP_200_OK)

    @is_authenticated
    def post(self, request, *args, **kwargs):
        data = {
            'placa': request.data.get('placa'),
            'marca': request.data.get('marca'),
            'color_vehiculo': request.data.get('color'),
            'modelo': request.data.get('modelo')
        }
        serializador = vehicle_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    @is_authenticated
    def put(self, request, pkid):
        mivehiculo = vehicle.objects.filter(id=pkid).update(
            placa=request.data.get('placa'),
            marca=request.data.get('marca'),
            color_vehiculo=request.data.get('color'),
            modelo=request.data.get('modelo')
        )

        return Response(mivehiculo, status=status.HTTP_200_OK)
