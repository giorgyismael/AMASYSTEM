#coding=utf-8
from django.db import models

from automaticPort.models.modelBloco import Bloco
from automaticPort.models.modelUsuario import Usuario


class Ambiente(models.Model):
    nome = models.CharField('Nome', max_length=50,)
    capacidade = models.IntegerField('Capacidade',)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    usuarioAmbiente = models.ManyToManyField(Usuario, through='UsuarioAmbiente')




    def __unicode__(self):
        return (self.nome)


