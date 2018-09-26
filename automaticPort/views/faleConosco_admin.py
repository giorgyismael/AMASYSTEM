from automaticPort.models.modelFaleConosco import FaleConosco
from django.views.generic.base import View
from django.shortcuts import render


class FaleConosco_admin(View):
    template = "usuario/faleConosco/fale_conosco.html"


    def get (self,request):

        todos_fale_connosco = FaleConosco.objects.all()
        total_fales = len(todos_fale_connosco)


        return render(request,self.template,{"todos_fale_connosco":todos_fale_connosco, "total_fales":total_fales})





