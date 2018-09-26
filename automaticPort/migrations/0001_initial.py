# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('capacidade', models.IntegerField(verbose_name=b'Capacidade')),
            ],
        ),
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('tipo', models.CharField(max_length=50, verbose_name=b'Tipo', choices=[(b'Administrativo', b'Administrativo'), (b'Educacional', b'Educacional'), (b'Juridico', b'Jur\xc3\xaddico'), (b'Esportivo', b'Esportivo'), (b'Auditorio', b'Audit\xc3\xb3rio')])),
            ],
        ),
        migrations.CreateModel(
            name='ControledeAcesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=10, choices=[(b'Manha', b'Manha'), (b'Tarde', b'Tarde'), (b'Noite', b'Noite')])),
                ('data', models.CharField(max_length=255, choices=[(b'Segunda', b'Segunda-Feira'), (b'Terca', b'Ter\xc3\xa7a-Feira'), (b'Quarta', b'Quarta-Feira'), (b'Quinta', b'Quinta-Feira'), (b'Sexta', b'Sexta-Feira')])),
                ('hora_entrada', models.TimeField()),
                ('hora_saida', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FaleConosco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=254, verbose_name=b'E-mail')),
                ('descricao', models.TextField(max_length=2000, verbose_name=b'Descricao')),
                ('data', models.DateField(verbose_name=b'Data Solicita\xc3\xa7\xc3\xa3o')),
                ('status', models.CharField(max_length=50, verbose_name=b'Status')),
            ],
        ),
        migrations.CreateModel(
            name='Microcontrolador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome', choices=[(b'ESP', b'ESP'), (b'Arduino', b'Arduino'), (b'Raspberry', b'Raspberry')])),
                ('tipo', models.CharField(max_length=50, verbose_name=b'Tipo')),
                ('ipAddress', models.GenericIPAddressField(verbose_name=b'Endere\xc3\xa7o IP')),
                ('port', models.IntegerField(verbose_name=b'Porta de Acesso')),
                ('netmask', models.GenericIPAddressField(default=b'255.255.255.255', verbose_name=b'Mascara de Rede')),
                ('gateway', models.GenericIPAddressField(null=True, verbose_name=b'Gateway', blank=True)),
                ('macAddress', models.GenericIPAddressField(null=True, verbose_name=b'Endere\xc3\xa7o MAC', blank=True)),
                ('secretKey', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=50, verbose_name=b'Status de Atividade', choices=[(b'Ativo', b'Ativo'), (b'Inativo', b'Inativo'), (b'Manutencao', b'Manutencao')])),
                ('ambiente', models.ForeignKey(to='automaticPort.Ambiente')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('tipo', models.CharField(max_length=50, verbose_name=b'Tipo', choices=[(b'Distancia', b'Dist\xc3\xa2ncia'), (b'Umidade e Temperatura', b'Umidade e Temperatura'), (b'Umidade', b'Umidade'), (b'Gas', b'G\xc3\xa1s'), (b'Fluxo de Agua', b'Fluxo de \xc3\x81gua'), (b'Movimento', b'Movimento'), (b'Umidade do Solo', b'Umidade do Solo'), (b'Nivel de Agua', b'N\xc3\xadvel de \xc3\x81gua'), (b'Vibracao', b'Vibra\xc3\xa7\xc3\xa3o'), (b'Peso', b'Peso'), (b'Chuva', b'Chuva'), (b'Obstaculo', b'Obst\xc3\xa1culo'), (b'Luz', b'Luz'), (b'Velocidade', b'Velocidade'), (b'Raio Ultravioleta', b'Raio Ultravioleta'), (b'Ultrassonico', b'Ultrass\xc3\xb4nico'), (b'Temperatura', b'Temperatura'), (b'Luminosidade', b'Luminosidade')])),
                ('status', models.CharField(max_length=50, verbose_name=b'Status', choices=[(b'Sensor', b'Sensor'), (b'Atuador', b'Atuador')])),
                ('microcontrolador', models.ForeignKey(to='automaticPort.Microcontrolador')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=14, unique=True, null=True, verbose_name=b'CPF', blank=True)),
                ('dataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento', blank=True)),
                ('cataoRFID', models.CharField(max_length=50, null=True, verbose_name=b'Numero Cart\xc3\xa3o RFID', blank=True)),
                ('siape', models.IntegerField(unique=True, null=True, verbose_name=b'Siape', blank=True)),
                ('matricula', models.IntegerField(unique=True, null=True, verbose_name=b'Matricula', blank=True)),
                ('chaveAtivacaoUsuario', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioAmbiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autorizacao', models.CharField(max_length=50, verbose_name=b'Autoriza\xc3\xa7\xc3\xa3o', choices=[(b'Liberado', b'Liberado'), (b'Aguardando', b'Aguardando'), (b'Analisando', b'Analisando')])),
                ('ambiente', models.ForeignKey(to='automaticPort.Ambiente')),
                ('usuario', models.ForeignKey(to='automaticPort.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='controledeacesso',
            name='UsuarioAmbiente',
            field=models.ForeignKey(to='automaticPort.UsuarioAmbiente'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='bloco',
            field=models.ForeignKey(to='automaticPort.Bloco'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='usuarioAmbiente',
            field=models.ManyToManyField(to='automaticPort.Usuario', through='automaticPort.UsuarioAmbiente'),
        ),
    ]
