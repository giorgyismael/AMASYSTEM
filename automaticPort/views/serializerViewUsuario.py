#coding:utf-8
from rest_framework import viewsets
from automaticPort.models.modelUsuario import Usuario
from automaticPort.serializer.serializerUsuario import UsuarioSerializer


class SerializerViewUsuario(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer