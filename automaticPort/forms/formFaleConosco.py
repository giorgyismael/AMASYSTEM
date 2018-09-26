#coding:utf-8
from django import forms
from automaticPort.extras.moduloEmail import emailFaleConosco
from automaticPort.models.modelFaleConosco import FaleConosco

class FormFaleConosco(forms.ModelForm):

    class Meta:
        model = FaleConosco
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome', 'type': 'text', 'required': ''}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail', 'type': 'email', 'required': ''}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descricao', 'type': 'text', 'required': ''}),
        }

        fields = ('nome','email','descricao')

    def save(self, commit=True):

        emailFaleConosco(
                nomeUsuario=self.cleaned_data.get('nome'),
                emailUsuario=self.cleaned_data.get('email'),
                assunto='Fale Conosco',
                descricao=self.cleaned_data.get('descricao')
            )
        super(FormFaleConosco, self).save()



