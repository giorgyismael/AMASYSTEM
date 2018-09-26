#coding:utf-8
from django import forms

from automaticPort.models.modelUsuario import Usuario


class FormEmailAtivacao(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'E-mail',
        'type': 'email',
    }))

class FormEmailRecuperarSenha(forms.ModelForm):

    class Meta:
        model = Usuario
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail', 'type':'email', 'required': ''}),
        }

        fields = ('email',)


class FormRecuperarSenha(forms.ModelForm):

    def save(self, commit=True):
        usuario = super(FormRecuperarSenha, self).save(commit=False)
        usuario.set_password(self.cleaned_data.get('password'))
        usuario.save()

        return usuario

    class Meta:
        model = Usuario
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail','style': 'display:none;','type':'email', 'required': ''}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Novo Password'}),
            'chaveAtivacaoUsuario': forms.TimeInput(attrs={'style': 'display:none;'}),
        }

        fields = ('password','chaveAtivacaoUsuario')