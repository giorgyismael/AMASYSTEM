from django.conf.urls import  patterns, url, include
from django.contrib import admin
from rest_framework import routers
from automaticPort.views import *
from automaticPort.extras.moduloMensagem import MessengerSucess
from automaticPort.views import faleConosco_admin
from automaticPort.views.faleConosco_admin import FaleConosco_admin
from automaticPort.forms import FormLogin


router = routers.DefaultRouter()
router.register(r'usuarios', SerializerViewUsuario)




urlpatterns = patterns("",
        url(r'^admin/', include(admin.site.urls)),
        url(r'^rest', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

        url(r'^$', Index.as_view(), name="automaticindex"),
                        # Caso a URL esteja vazia, Django ira executar a view Index

        url(r'^cadastro/$', Cadastro.as_view(), name='cadastroUsuario'),



        url(r'^ativacadastro/(?P<chaveAtivacao>.+)/$', AtivaCadastro.as_view(), name='ativaCadatro'),

        url(r'^perfil/$', Perfil.as_view(), name='perfil'),

        url(r'^editarperfil/(?P<user_id>\d+)/$', Perfil.as_view(), name='editarPerfil'),

        url(r'^recuperarsenha/$', RecuperarSenha.as_view(), name='emailRecuperarSenha'),

        url(r'^recuperarsenhachave/(?P<chaveAtivacao>.+)/$', RecuperarSenha.as_view(), name='recuperarSenha'),

        url(r'^emailativacao/$', EmailAtivacao.as_view(), name='emailAtivacao'),

        url(r'^faleconosco/$', FaleConosco.as_view(), name='faleConosco'),

        url(r'^faleconosco_admin/$', FaleConosco_admin.as_view(), name='faleConosco_admin'),



        url(r'^controleacesso/(requestarduino?P<user_code>.+)/$', ControleAcesso.as_view(), name='ControleAcesso'),

        url(r'^requestarduino/(?P<codeRFID>.+)$', viewRequestArduino.as_view(), name='ResquestArduino'),
        url(r'^requestarduino/$', viewRequestArduino.as_view(), name='ResquestArduinoNotFound'),

        url(r'^requestTemperatura/(?P<t>.+)$', viewRequest_temperatura.as_view(), name='ResquestArduino'),



        url(r'^ambienteautorizado/$', viewAmbienteAutorizado.as_view(),name='ambienteAutorizado'),
        url(r'^solicitaacesso/$', viewSolicitaAcesso.as_view(),name='solicitaAcesso'),
        url(r'^requestambiente/$', ViewRequestAmbiente.as_view(),name='requestAmbiente'),





        url(r'^login/$', Login.as_view(),name='login'),

        url(r'^suporte/$', Suporte.as_view(),name='suporte'),

        url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'visitante/index/index.html', 'extra_context': {'form_login':FormLogin(),'controleMenu': 'logout', 'messengerSucess': MessengerSucess().Usuario(3)}}, name='logout'),
)
