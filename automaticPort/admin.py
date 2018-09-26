from django.contrib import admin
from automaticPort.models import Microcontrolador, Bloco, Ambiente, UsuarioAmbiente, ControledeAcesso, Usuario, Sensor

class ControledeAcessoline(admin.TabularInline):
    model = ControledeAcesso
    extra = 1

class Microcontroladorline(admin.TabularInline):
    model = Microcontrolador
    extra = 1

class Sensorline(admin.TabularInline):
    model = Sensor
    extra = 1

class ControledeAcessoAdmin(admin.ModelAdmin):
    inlines = (ControledeAcessoline,)

class MicrocontroladorAdmin(admin.ModelAdmin):
    inlines = (Microcontroladorline,)

class SensorAdmin(admin.ModelAdmin):
    inlines = (Sensorline,)

admin.site.register(Bloco)
admin.site.register(Usuario)
admin.site.register(Microcontrolador, SensorAdmin)
admin.site.register(Ambiente, MicrocontroladorAdmin)
admin.site.register(UsuarioAmbiente, ControledeAcessoAdmin)



