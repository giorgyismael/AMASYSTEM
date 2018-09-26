#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from automaticPort.models.modelUsuario import Usuario
from automaticPort.serializer import ResponseUsuarioSerializer
from automaticPort.extras.moduloMensagem import MessengerError,MessengerSucess
from ipware.ip import get_ip

class viewRequestArduino(View):
    template = "visitante/index/index.html"
    conteudo = {'response': False}

    def get(self, request, codeRFID=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        if (codeRFID):
            usuario = Usuario.objects.filter(cataoRFID=codeRFID)
            if len(usuario) == 1:
                serializer = ResponseUsuarioSerializer(
                    usuario,
                    many=True,
                    context={'ip_microcontrolador': get_ip(request)})
                self.conteudo.update({"response": serializer.data})

            else:
                return render(request, self.template, {"messengerError": MessengerError().Usuario()})
        else:
            return render(request, self.template, {"messengerError":MessengerError().Usuario()})

        return HttpResponse(self.conteudo.items())

    def post(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        render(request, self.template, {"messengerError": MessengerError().Usuario()})