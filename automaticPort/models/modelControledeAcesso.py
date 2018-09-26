#coding=utf-8
from django.db import models
from automaticPort.models.modelUsuarioAmbiente import UsuarioAmbiente

class ControledeAcesso(models.Model):
    MANHA = 'Manha'
    TARDE = 'Tarde'
    NOITE = 'Noite'

    HORARIO_CHOICES = (
        (MANHA, 'Manha'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    )

    SEGUNDA = 'Segunda'
    TERCA = 'Terca'
    QUARTA = 'Quarta'
    QUINTA = 'Quinta'
    SEXTA = 'Sexta'

    DIA_CHOICES = (
        (SEGUNDA, 'Segunda-Feira'),
        (TERCA, 'Terça-Feira'),
        (QUARTA, 'Quarta-Feira'),
        (QUINTA, 'Quinta-Feira'),
        (SEXTA, 'Sexta-Feira'),
    )

    UsuarioAmbiente = models.ForeignKey(UsuarioAmbiente, on_delete=models.CASCADE)
    turno = models.CharField(max_length=10, choices=HORARIO_CHOICES)
    data = models.CharField(max_length=255, choices=DIA_CHOICES)
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()


    def __unicode__(self):
        return self.data




