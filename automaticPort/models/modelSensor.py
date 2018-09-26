#coding=utf-8
from django.db import models
from automaticPort.models.modelMicrocontrolador import Microcontrolador

class Sensor(models.Model):


    TIPOS_CHOICES = (
        ("Distancia", 'Distância'),
        ("Umidade e Temperatura", 'Umidade e Temperatura'),
        ("Umidade", 'Umidade'),
        ("Gas", 'Gás'),
        ("Fluxo de Agua", 'Fluxo de Água'),
        ("Movimento", 'Movimento'),
        ("Umidade do Solo", 'Umidade do Solo'),
        ("Nivel de Agua", 'Nível de Água'),
        ("Vibracao", 'Vibração'),
        ("Peso", 'Peso'),
        ("Chuva", 'Chuva'),
        ("Obstaculo", 'Obstáculo'),
        ("Luz", 'Luz'),
        ("Velocidade", 'Velocidade'),
        ("Raio Ultravioleta", 'Raio Ultravioleta'),
        ("Ultrassonico", 'Ultrassônico'),
        ("Temperatura", 'Temperatura'),
        ("Luminosidade", 'Luminosidade'),
    )

    STATUS_CHOICES = (
        ("Sensor", 'Sensor'),
        ("Atuador", 'Atuador'),
    )


    nome = models.CharField('Nome', max_length=50,)
    tipo = models.CharField('Tipo', max_length=50, choices=TIPOS_CHOICES)
    status = models.CharField('Status', max_length=50, choices=STATUS_CHOICES)
    microcontrolador = models.ForeignKey(Microcontrolador, on_delete=models.CASCADE)




    def __unicode__(self):
        return self.nome


