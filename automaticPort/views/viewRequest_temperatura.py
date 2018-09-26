#coding:utf-8

from django.views.generic.base import View
from django.shortcuts import render



class viewRequest_temperatura(View):
    template = "usuario/Mostar_temperatura/Mostrar_temperatura.html"
    conteudo = {'response': False}

    def get(self,request,t=None):
        self.conteudo.update({'messengerSucess': '', 'messengerError': ''})

