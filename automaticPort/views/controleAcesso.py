#coding:utf-8
from django.http import HttpResponse
from django.views.generic.base import View

from automaticPort.forms import FormLogin


class ControleAcesso(View):
    template = "index/index.html"
    conteudo = {
        'form_login': FormLogin(),
        'controleMenu': 'home',
    }

    def get(self, request, user_code=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        print("Recebi o codigo {}".format(user_code))
        return HttpResponse(user_code)

    def post(self, request,user_code=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        return HttpResponse(user_code)