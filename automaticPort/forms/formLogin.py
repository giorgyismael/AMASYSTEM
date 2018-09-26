#coding:utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class FormLogin(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}), max_length=254)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return username

    def login(self):
        usuario = super(FormLogin, self).save(commit=False)
        return usuario


    class Meta:
        model = User
        fields = ('username', 'password',)