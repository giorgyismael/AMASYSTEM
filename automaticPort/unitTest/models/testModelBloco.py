#coding=utf-8
from automaticPort.models.modelBloco import Bloco
import unittest

class TestModelBloco(unittest.TestCase):
    'Teste do modelo bloco'

    def setUp(self):
        'Inicializando 3 objetos do tipo bloco e persistindo do banco teste'
        Bloco.objects.create(nome="Bloco C", tipo="Educacional")
        Bloco.objects.create(nome="Bloco B", tipo="Juridico")
        Bloco.objects.create(nome="Bloco A", tipo="Esportivo")


    def testCreateObject(self):
        'Realizando um busca pelo Objetivo e verificando se retornou o  nome correto'
        self.bloco_c = Bloco.objects.get(nome="Bloco C")
        self.bloco_b = Bloco.objects.get(nome="Bloco B")
        self.bloco_a = Bloco.objects.get(nome="Bloco A")

        self.assertEquals(self.bloco_a.nome, "Bloco A")
        self.assertEquals(self.bloco_b.nome, "Bloco B")
        self.assertEquals(self.bloco_c.nome, "Bloco C")