#coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from automaticPort.forms import FormPerfil
from automaticPort.models import Usuario
from automaticPort.views.loginrequired import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from automaticPort.extras.moduloMensagem import MessengerError,MessengerSucess


class Perfil(LoginRequiredMixin,View):
    template = "usuario/perfil/perfil.html"
    conteudo = {
        'form_usuario': FormPerfil(),
        'controleMenu':'Edit',
    }
    def get(self, request, user_id=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        if user_id:
            usuario = Usuario.objects.get(id=user_id)
            form = FormPerfil(instance=usuario)

        else:
            form = FormPerfil()
            self.template='index/index.html',
            self.conteudo.update({
                'messengerError': MessengerError().Usuario(2)
            })

        self.conteudo.update({
            'form_usuario': form,
            'titulo_pagina': 'Editar perfil',
        })

        return render(request, self.template, self.conteudo)

    def post(self, request, user_id=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if user_id:
            usuario = Usuario.objects.get(id=user_id)
            form = FormPerfil(instance=usuario, data=request.POST)
        else:
            form = FormPerfil(request.POST)

        self.conteudo.update({
            'form_usuario': form,
            'titulo_pagina': 'Editar perfil',
        })

        if form.is_valid():
            form.save(request)
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),)

            if user is not None:
                if user.is_active:
                    login(request, user)


            self.template = 'usuario/perfil/perfil.html'
            self.conteudo.update({
                'form': '',
                'controleMenu': 'index',
                'messengerSucess': MessengerSucess().Usuario(0),
            })

        return render(request, self.template, self.conteudo)