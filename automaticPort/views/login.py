#coding:utf-8
from automaticPort.forms import FormLogin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from automaticPort.extras.moduloMensagem import MessengerSucess, MessengerError

class Login(View):
    # Esta é a View que controla o Login e a parte do formulário de Login.
    # É aqui que a "mágica" do Login acontece.
    template = "visitante/login/login.html"
    # Acima, a variável template recebe o endereço (DENTRO DO DJANGO) que será renderizado.
    conteudo = {
    # A variável conteúdo vai receber o formulário FormLogin.
        'form_login': FormLogin(),
        'controleMenu':'login',
    }

    def get(self, request):
        # Este trecho do código será executado sempre que o usuário entrar nas páginas Inicial, Suporte ou Login.
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        self.conteudo.update({'titulo_pagina': 'Login',})
        return render(request, self.template, self.conteudo) # <- Variável conteúdo aqui!
#                                       ^
#                             Variável Template aqui!

    def post(self, request):
        # Esse trecho do código será executado caso o usuário tente fazer login.
        # Basicamente, serve para enviar as informações e verificar se o usuário está cadastrado e ativado.
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario:
            if usuario.is_active:
                login(request, usuario)
                self.template = 'usuario/index/index.html'
                self.conteudo.update({'controleMenu': 'login'})

            else:
                self.conteudo.update({"messengerError":MessengerError().Usuario(0)})
        else:
            self.conteudo.update({"messengerError":MessengerError().Usuario(1)})

        return render(request, self.template, self.conteudo)