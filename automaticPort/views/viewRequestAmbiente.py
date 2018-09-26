#coding:utf-8
import json
from django.http import HttpResponse
from django.views.generic import View
from automaticPort.models.modelAmbiente import Ambiente

class ViewRequestAmbiente(View):
    def get(self, request):
        return HttpResponse(
            json.dumps({"Nada para Mostrar": "Está Página não deve ser acessada Assim"}),
            content_type="application/json"
        )

    def post(self, request):
        id_bloco = request.POST.get('id_bloco')
        response_data = {}

        ambientes = Ambiente.objects.filter(bloco_id=id_bloco)
        if (ambientes):
            for i, ambiente in enumerate(ambientes):
                response_data[i] = {"nome":ambiente.nome, "id":ambiente.id}
                response_data["length"] = i
        else:
            response_data["0"] = {"nome":"Não Existem Ambientes", "id":"00"}
            response_data["length"] = 0

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json")