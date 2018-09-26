#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



class Usuario(User):
    cpf = models.CharField('CPF', max_length=14, unique=True, null=True, blank=True)
    dataNascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    cataoRFID = models.CharField("Numero Cartão RFID", max_length=50, null=True, blank=True)
    siape = models.IntegerField('Siape', unique=True, null=True, blank=True )
    matricula = models.IntegerField('Matricula', unique=True,null=True, blank=True)
    chaveAtivacaoUsuario = models.CharField(max_length=255)

    def __unicode__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.cpf:
            self.cpf = None

        if not self.siape:
            self.siape = None

        if not self.matricula:
            self.matricula = None

        super(Usuario, self).save(*args, **kwargs)


    def __str__(self):
        return self.first_name
