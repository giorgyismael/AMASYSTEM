#coding=utf-8
from automaticPort.models.modelUsuario import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Usuario
        fields = ('url','username', 'email', 'cataoRFID')

