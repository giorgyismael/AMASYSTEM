#coding: utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from automaticPort.forms import FormLogin

class Suporte(View):
    template = "visitante/suporte/suporte.html"
    conteudo = {
        'form_login': FormLogin(),
        'controleMenu': 'suporte',
    }

    def get(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        return render(request, self.template, self.conteudo)

    def post(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        return render(request, self.template, self.conteudo)