#coding=utf-8
from django.contrib import admin
from django.db import models

from automaticPort.models.modelAmbiente import Ambiente
from automaticPort.models.modelUsuario import Usuario
from django.contrib.auth.models import Group


class UsuarioAmbiente(models.Model):
    AUTORIZACAO_CHOICES = (
        ("Liberado", 'Liberado'),
        ("Aguardando", 'Aguardando'),
        ("Analisando", 'Analisando'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    autorizacao = models.CharField('Autorização', max_length=50, choices=AUTORIZACAO_CHOICES)

    def __unicode__(self):
        return "{}|{}".format(self.ambiente.bloco.nome, self.ambiente.nome)



class UsuarioAmbienteAdmin(admin.ModelAdmin):
    exclude = "autorizacao"

