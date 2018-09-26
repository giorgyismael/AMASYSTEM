#coding:utf-8
import hashlib, os
from django import forms
from automaticPort.models import Usuario
from automaticPort.extras.moduloMensagem import  MessengerError
from django.contrib.auth.models import Group, Permission
from automaticPort.extras.moduloEmail import emailAtivacaoCadastro

class FormUsuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    def clean_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']

            if len(password) < 8:
                raise forms.ValidationError(MessengerError().Password(0))

            else:
                first_isalpha = password[0].isalpha()
                if all(c.isalpha() == first_isalpha for c in password):
                    raise forms.ValidationError(MessengerError().Password(1))
                else:
                    return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and Usuario.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(MessengerError().Email(0))
        return email

    def save(self, dominio=None, commit=True):
        usuario = super(FormUsuario, self).save(commit=False)
        usuario.chaveAtivacaoUsuario = hashlib.sha1(os.urandom(128)).hexdigest()
        usuario.set_password(self.cleaned_data.get('password'))
        usuario.is_active = False
        usuario.is_staff = True
        usuario.save()
        usuario.groups.add(Group.objects.get(name='visitante'))
        usuario.save()
        emailAtivacaoCadastro(usuario.first_name, usuario.email, "Ativacao de Cadastro", usuario.chaveAtivacaoUsuario, dominio)
        return usuario

    class Meta:
        model = Usuario
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'dataNascimento': forms.TextInput(attrs={'placeholder': 'Datan de Nascimento', "onfocus":"(this.type='date')", "onblur":"(this.type='text')"}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Matrícula'}),
            'siape': forms.TextInput(attrs={'placeholder': 'SIAPE'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome', 'required': ''}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuario', 'required': ''}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail', 'type':'email', 'required': ''}),
        }


        fields = ('first_name','email','cpf','dataNascimento','username', 'password',)

