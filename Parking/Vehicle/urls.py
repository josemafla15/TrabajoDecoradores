from django.urls import path

from .views import vehicleApiView

urlpatterns = [
    path ('crear-vehiculo', vehicleApiView.as_view()),
    path ('list', vehicleApiView.as_view()),
    path ('actualizar-vehiculo/<int:pkid>', vehicleApiView.as_view(), name="actulizar_vehiculo")
]



