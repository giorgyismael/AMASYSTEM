#coding=utf-8
from django.db import models
from datetime import datetime



class FaleConosco(models.Model):
    nome = models.CharField('Nome', max_length=50,)
    email = models.EmailField('E-mail',)
    descricao = models.TextField("Descricao", max_length=2000,)
    data = models.DateField('Data Solicitação', )
    status = models.CharField('Status', max_length=50, )


    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.data=datetime.now().date()
        self.status = 'Pendente'
        super(FaleConosco, self).save(*args, **kwargs)


