#coding: utf-8

from django.shortcuts import render
from django.views.generic.base import View
from automaticPort.models import Usuario
from automaticPort.forms.formEmail import FormRecuperarSenha, FormEmailRecuperarSenha
from automaticPort.extras.moduloEmail import emailRecuperarSenha
from automaticPort.forms.formLogin import FormLogin
from automaticPort.extras.moduloMensagem import MessengerSucess,MessengerError


class RecuperarSenha(View):
    template = ''
    conteudo = {
        'controleMenu':'suporte',
        'tituloPagina':'Email de Ativacao',
        'form_login': FormLogin(),
    }

    def get(self, request, chaveAtivacao=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if chaveAtivacao:
            try:
                self.template = "visitante/suporte/formRecuperarSenha.html"
                usuario = Usuario.objects.get(chaveAtivacaoUsuario=str(chaveAtivacao))
                self.conteudo.update({'formRecuperarSenha': FormRecuperarSenha(instance=usuario)})
            except:
                self.template = "visitante/suporte/suporte.html"
                self.conteudo.update({'messengerError': 'Chave invalida!'})

        else:
            self.template = "visitante/suporte/formRecuperarSenha.html"
            self.conteudo.update({'formRecuperarSenha':FormEmailRecuperarSenha()})

        return render(request, self.template, self.conteudo)

    def post(self, request, chaveAtivacao=None):
        self.template = "visitante/suporte/suporte.html"
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if chaveAtivacao:
            usuario = Usuario.objects.get(chaveAtivacaoUsuario=str(chaveAtivacao))
            form = FormRecuperarSenha(instance=usuario, data=request.POST,)
            if (form.is_valid()):
                try:
                    if usuario.is_active:
                        form.save()
                        self.conteudo.update({'messengerSucess': 'Senha Alterada com Sucesso'})
                    else:
                        self.conteudo.update({'messengerError': 'Cadastro encontra-se Inativo.'})
                except:
                    self.conteudo.update({'messengerError': 'Cadastro não encontrado, informe e-mail válido'})
        else:

            form = FormEmailRecuperarSenha(request.POST)
            if form.is_valid:
                try:
                    usuario = Usuario.objects.get(email=form.data.get('email'))
                    if usuario.is_active:
                        dominio = request.get_host()
                        emailRecuperarSenha(usuario.first_name, usuario.email, 'Recuperar Senha', usuario.chaveAtivacaoUsuario, dominio)
                        self.conteudo.update({
                        'messengerSucess': 'E-mail enviado para {}.'.format(usuario.email),
                        })
                    else:
                        self.conteudo.update({'messengerSucess': 'Cadastro encontra-se Inativo.'})

                except:
                    self.conteudo.update({'messengerError': 'Cadastro não encontrado, informe email válido'})

        return render(request, self.template, self.conteudo)