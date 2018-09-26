#coding=utf-8
import unittest
from django.test.client import Client
from django.test import TestCase
from automaticPort.models import Usuario


class TestViewLogin(TestCase):
    'base de dados teste sendo carregada'
    #fixtures = ['initial_data.json',]

    def setUp(self):
        'Inicialização co cliente web'
        self.client = Client()

    def testLoginErrorUserAndPassword(self):
        'Mensagem de erro que deve ser apresentada quando usuário ou senha estiverem errdos'
        response = self.client.post('/automaticport/login/', {'username': 'giorgy', 'password': 'senhaerrada'})
        context = (dict(response.context))

        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(context.get('messengerError'), u"Usuario ou senha incorretos")
        self.failUnlessEqual(context.get('messengerSucess'), "")
        self.failUnlessEqual(context.get('controleMenu'), "login")

    def testLoginSucessUserAndPassword(self):
        'Teste para quando usuario e senha estiverem certos'
        response = self.client.post('/automaticport/login/', {'username': 'giorgy', 'password': '1234abcd'})
        context = (dict(response.context))

        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(context.get('messengerError'), "")
        self.failUnlessEqual(context.get('messengerSucess'), "")
        self.failUnlessEqual(context.get('controleMenu'), "login")