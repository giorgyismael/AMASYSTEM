#coding: utf-8

from django.shortcuts import render
from django.views.generic.base import View
from automaticPort.views.loginrequired import LoginRequiredMixin
from automaticPort.extras.moduloMensagem import MessengerError,MessengerSucess
from automaticPort.models.modelUsuarioAmbiente import UsuarioAmbiente
from automaticPort.models.modelMicrocontrolador import Microcontrolador
import requests as rqts


class viewAmbienteAutorizado(LoginRequiredMixin,View):
    template = "usuario/ambiente/ambienteAutorizado.html"
    conteudo = {
        'controleMenu':'Ambiente',
    }
    def get(self, request, id_ambiente=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if id_ambiente:
            self.conteudo.update({'messengerSucess': MessengerError().Usuario(3),})

        try:
            pesquisa_usuario = UsuarioAmbiente.objects.filter(usuario=request.user.id).order_by("ambiente__bloco__nome")
            self.conteudo.update({"ambientes": pesquisa_usuario})
        except UsuarioAmbiente.DoesNotExist:
            self.conteudo.update({'messengerSucess': MessengerError().Usuario(4),})

        return render(request, self.template, self.conteudo)

    def post(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if request.POST.get("id_ambiente"):
            id_ambiente = request.POST.get("id_ambiente")
            pesquisa_ambiente = UsuarioAmbiente.objects.get(ambiente=id_ambiente, usuario=request.user.id)
            microcontrolador = Microcontrolador.objects.get(ambiente=pesquisa_ambiente.ambiente.id)

            if pesquisa_ambiente.usuario.id == request.user.id:
                context = {
                    'command': 'openthedoor',
                    'secretKey':microcontrolador.secretKey ,
                    'ipAddress':microcontrolador.ipAddress,
                    'port':microcontrolador.port}

                try:
                    response = rqts.get(
                        "http://{}:{}/automaticport/resquestarduinoteste/{}/{}".format(
                            context.get('ipAddress'),
                            context.get('port'),
                            context.get('command'),
                            context.get('secretKey')), timeout=5,)
                    self.conteudo.update({'messengerSucess': MessengerSucess().Usuario(1),})

                except:
                    self.conteudo.update({'messengerSucess': MessengerError().Usuario(5),})

            else:
                pesquisa_ambiente = None
                self.conteudo.update({'messengerSucess': MessengerError().Usuario(3),})

        return render(request, self.template, self.conteudo)