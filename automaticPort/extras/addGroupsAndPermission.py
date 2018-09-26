#coding:utf-8

import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internetOfThings.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def createGruops():
    listaGrupos = ["visitante", "discente", "docente"]
    for grupo in listaGrupos:
        result, status=Group.objects.get_or_create(
            name=grupo,
        )
        result.save()

def createPermission():
    modelUsuarioAmbiente = ContentType.objects.filter(model="usuarioambiente")
    modelControledeAcesso = ContentType.objects.filter(model="controledeacesso")

    PermissionOne = Permission.objects.filter(content_type_id=modelUsuarioAmbiente)
    PermissionTwo = Permission.objects.filter(content_type_id=modelControledeAcesso)

    PermissionOne = PermissionOne.get(codename__startswith="add_")
    PermissionTwo = PermissionTwo.get(codename__startswith="add_")

    Group.objects.get(name='visitante').permissions.add(PermissionOne, PermissionTwo)
    Group.objects.get(name='discente').permissions.add(PermissionOne, PermissionTwo)

    for permission in Permission.objects.all():
        Group.objects.get(name='docente').permissions.add(permission)


def createGroupAndPermission():
    print ("Inicio da Migração")
    createGruops()
    createPermission()
    print ("Finalizando a Migração")

if __name__ == "__main__":
    createGroupAndPermission()