#coding:utf-8
from django import forms
from django.db import models
from automaticPort.models import Bloco
from automaticPort.models import ControledeAcesso

class FormUsuarioAmbiente(forms.ModelForm):
    bloco = forms.ModelChoiceField(
        empty_label="Selecione Bloco",
        required=True,
        queryset=Bloco.objects.all(),
        widget=forms.Select(attrs={"onchange":"requestAmbiente()",}))

    ambiente = forms.ChoiceField(
        widget=forms.Select(),
        required=True,
        choices=([('', '--------')]))


    class Meta:
        model = ControledeAcesso
        fields = ('bloco','ambiente','turno','hora_entrada','hora_saida','data')
        widgets = {
            'turno': forms.Select(attrs={'disabled':True}),
            'data': forms.SelectMultiple(attrs={'disabled':True}),
            'hora_entrada': forms.TextInput(
                attrs={'placeholder': 'Horario de Entrada','disabled':True, "onfocus": "(this.type='time')",
                       "onblur": "(this.type='text')"}),
            'hora_saida': forms.TextInput(
                attrs={'placeholder': 'Horario de Saída','disabled':True, "onfocus": "(this.type='time')",
                       "onblur": "(this.type='text')"}),
        }

