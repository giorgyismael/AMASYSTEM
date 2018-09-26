#coding=utf-8
from automaticPort.models.modelUsuario import Usuario
from automaticPort.models.modelMicrocontrolador import Microcontrolador
from rest_framework import serializers

class ResponseUsuarioSerializer(serializers.ModelSerializer):

    authorization = serializers.SerializerMethodField('authorizationArduino')
    secretKey = serializers.SerializerMethodField('getSecretKey')

    def getSecretKey(self,key=None):
        try:
            key = Microcontrolador.objects.get(secretKey= self.context.get('ip_microcontrolador'))
        except :
            key ='Not Found key'
        return key

    def authorizationArduino(self, authorization=None):
        authorization = True
        return authorization

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cataoRFID', 'authorization', 'secretKey')
