from django.urls import path

from .views import vehicleApiView

urlpatterns = [
    path ('list', vehicleApiView.as_view())
]
