#coding=utf-8
from django.db import models

class Bloco(models.Model):

    ADMINISTRATIVO = 'Administrativo'
    EDUCACIONAL = 'Educacional'
    JURIDICO = 'Juridico'
    ESPORTIVO = 'Esportivo'
    AUDITORIO = 'Auditorio'

    TIPOS_CHOICES = (
        (ADMINISTRATIVO, 'Administrativo'),
        (EDUCACIONAL, 'Educacional'),
        (JURIDICO, 'Jurídico'),
        (ESPORTIVO, 'Esportivo'),
        (AUDITORIO, 'Auditório'),
    )


    nome = models.CharField('Nome', max_length=50,)
    tipo = models.CharField('Tipo', max_length=50, choices=TIPOS_CHOICES)



    def __unicode__(self):
        return self.nome


