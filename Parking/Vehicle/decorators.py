from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import get_authorization_header

def is_authenticated(func):
    def wrapper(self, request, *args, **kwargs):
        # Verifica si el usuario está autenticado
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Si se utiliza autenticación por token, valida el header de autorización
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return Response({'detail': 'Invalid token header. No credentials provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        return func(self, request, *args, **kwargs)
    return wrapper 