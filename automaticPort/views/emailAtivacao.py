#coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from automaticPort.models import Usuario
from automaticPort.forms.formEmail import FormEmailAtivacao
from automaticPort.extras.moduloEmail import emailAtivacaoCadastro
from automaticPort.forms.formLogin import FormLogin
from automaticPort.extras.moduloMensagem import MessengerError, MessengerSucess


class EmailAtivacao(View):
    template = "visitante/suporte/formEmailAtivacao.html"
    conteudo = {
        'controleMenu':'suporte',
        'tituloPagina':'Redefinir Senha',
        'form_login': FormLogin(),
    }

    def get(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        self.conteudo.update({'formEmailAtivacao':FormEmailAtivacao()})

        return render(request, self.template, self.conteudo)

    def post(self, request):
        form = FormEmailAtivacao(request.POST)
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        self.conteudo.update({'formEmailAtivacao': form})

        if (form.is_valid()):
            try:
                usuario = Usuario.objects.get(email=form.cleaned_data.get('email'))

                if not usuario.is_active:
                    dominio = request.get_host()
                    emailAtivacaoCadastro(usuario.first_name, usuario.email, 'Ativação de Cadastro', usuario.chaveAtivacaoUsuario, dominio)
                    self.conteudo.update({'messengerSucess': MessengerSucess().Email(0, usuario.email)})
                else:
                    self.conteudo.update({'messengerError': MessengerError().Cadastro(3),})
            except:
                self.conteudo.update({'messengerError':  MessengerError().Cadastro(4),})

        return render(request, self.template, self.conteudo)