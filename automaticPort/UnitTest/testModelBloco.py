import unittest
from automaticPort.models.modelBloco import Bloco

class testeModelBloco(unittest.TestCase):
    def setUp(self):
        self.blocoA = Bloco.objects.create(nome="")