#coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from automaticPort.views.loginrequired import LoginRequiredMixin
from automaticPort.extras.moduloMensagem import MessengerError,MessengerSucess
from automaticPort.forms import FormUsuarioAmbiente
from automaticPort.models import Usuario


class viewSolicitaAcesso(LoginRequiredMixin,View):
    template = "usuario/ambiente/solicitaAcesso.html"
    conteudo = {'controleMenu':'SolicitaAcesso'}

    def get(self, request, user_id=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        if user_id:
            usuario = Usuario.objects.get(id=request.user.id)
            form = FormUsuarioAmbiente(instance=usuario)

        self.conteudo.update({'formUsuarioAmbiente':FormUsuarioAmbiente()})

        return render(request, self.template, self.conteudo)

    def post(self, request, user_id=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        form = FormUsuarioAmbiente(request.POST)
        if form.is_valid():
            form.save(request.user.id, form.cleaned_data.get("UsuarioAmbiente"))
        self.conteudo.update({'formUsuarioAmbiente':form})
        return render(request, self.template, self.conteudo)