#coding=utf-8
from django.db import models
from automaticPort.models.modelAmbiente import Ambiente
import hashlib, os

class Microcontrolador(models.Model):

    ESP = 'ESP'
    ARDUINO = 'Arduino'
    RASPBERRY = 'Raspberry'

    NOME_CHOICES = (
        (ESP, 'ESP'),
        (ARDUINO, 'Arduino'),
        (RASPBERRY, 'Raspberry'),
    )

    STATUS_CHOICES = (
        ("Ativo", 'Ativo'),
        ("Inativo", 'Inativo'),
        ("Manutencao", 'Manutencao'),
    )

    nome = models.CharField('Nome', max_length=50, choices=NOME_CHOICES)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo', max_length=50,)
    ipAddress = models.GenericIPAddressField('Endereço IP', )
    port = models.IntegerField('Porta de Acesso', )
    netmask = models.GenericIPAddressField('Mascara de Rede', default='255.255.255.255')
    gateway = models.GenericIPAddressField('Gateway',null=True, blank=True)
    macAddress = models.GenericIPAddressField('Endereço MAC',null=True, blank=True)
    secretKey = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField('Status de Atividade', max_length=50, choices=STATUS_CHOICES)



    def __unicode__(self):
        return ("{} - {}").format(self.nome,self.tipo)

    def save(self, *args, **kwargs):
        if not self.secretKey:
            self.secretKey = hashlib.sha1(os.urandom(128)).hexdigest()


        super(Microcontrolador, self).save(*args, **kwargs)


