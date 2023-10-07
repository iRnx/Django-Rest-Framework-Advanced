from usuarios.models import Usuario
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['post', 'get']
    # permission_classes = [IsAuthenticated]
