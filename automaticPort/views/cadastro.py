#coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View

from automaticPort.extras.moduloMensagem import MessengerSucess, MessengerError
from automaticPort.forms import FormLogin
from automaticPort.forms import FormUsuario
from automaticPort.models.modelUsuario import Usuario


class Cadastro(View):
    template = "visitante/cadastro/cadastro.html"
    conteudo = {
        'form_login': FormLogin(),
        'controleMenu':'cadastroUsuario',
    }

    def get(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        form_usuario = FormUsuario()
        self.conteudo.update({'form_usuario': form_usuario,})

        return render(request, self.template, self.conteudo)

    def post(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        form_usuario = FormUsuario(request.POST)
        if form_usuario.is_valid():
            dominio = request.get_host()
            form_usuario.save(dominio)
            self.conteudo.update({'messengerSucess': MessengerSucess().Cadastro(0),})
        else:
            self.conteudo.update({'form_usuario': form_usuario,})

        return render(request, self.template, self.conteudo)



class AtivaCadastro(View):
    template = 'visitante/index/index.html'
    conteudo = {
        'form_login': FormLogin(),
        'controleMenu': 'index',
    }

    def get(self, request, chaveAtivacao=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if (chaveAtivacao):
            try:
                usuario = Usuario.objects.get(chaveAtivacaoUsuario=str(chaveAtivacao))
            except:
                usuario=None

            if (usuario):
                if not (usuario.is_active):
                    usuario.is_active = True
                    usuario.save()
                    self.conteudo.update({'messengerSucess': MessengerSucess().Cadastro(1),})
                else:
                    self.conteudo.update({'messengerError': MessengerError().Cadastro(0),})

            else:
                self.conteudo.update({'messengerError': MessengerError().Cadastro(1),})
        else:
            self.conteudo.update({'messengerError': MessengerError().Cadastro(2),})

        return render(request, self.template, self.conteudo)