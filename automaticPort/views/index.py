#coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from automaticPort.forms import FormLogin

class Index(View):
    '''
    form_login = Inclusão do FormLogin() no dicionário Conteudo
    template = Endereço (NO DJANGO, NÃO NA URL) do Template que será renderizado
    '''
    template = "visitante/index/index.html"
    conteudo = {
        'form_login': FormLogin(),
        'controleMenu': 'home',
        # Inclusão do Controle de Menu. Se não existir Controle de Menu, a página perde a estrutura
    }

    def get(self, request):

        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        # Inclui os dois tipos de mensagens no conteudo, sem excluir as chaves e os registros que já estão no conteudo
        print(self.conteudo)
        return render(request, self.template, self.conteudo) # Renderização do Template, usando a variável template; conteudo é context

    def post(self, request):

        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        # Inclui os dois tipos de mensagens no conteudo, sem excluir as chaves e os registros que já estão no conteudo
        return render(request, self.template, self.conteudo)
        # Renderização do Template, usando a variável template; conteudo é context
