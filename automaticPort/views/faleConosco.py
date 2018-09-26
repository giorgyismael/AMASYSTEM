#coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from automaticPort.forms.formFaleConosco import FormFaleConosco
from automaticPort.forms.formLogin import FormLogin
from automaticPort.extras.moduloMensagem import MessengerSucess


class FaleConosco(View):
    template = "visitante/suporte/formFaleConosco.html"
    conteudo = {
        'controleMenu':'suporte',
        'tituloPagina':'Fale Conosco',
        'form_login': FormLogin(),
    }

    def get(self, request):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})
        self.conteudo.update({'formFaleConosco':FormFaleConosco()})

        return render(request, self.template, self.conteudo)

    def post(self, request):
        form = FormFaleConosco(request.POST)
        self.conteudo.update({'formEmailAtivacao': form})
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

        if (form.is_valid()):
            form.save()
            self.conteudo.update({'messengerSucess': MessengerSucess().FaleConosco(0)})

        return render(request, self.template, self.conteudo)