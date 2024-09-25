from django.shortcuts import render
from data_embrapii.models import PortFolio

def projetos(request):
    projetos = PortFolio.objects.filter(status_view=True).order_by('-data_contrato')[:100]
    conteudo = {
        'projetos': projetos,
    }
    return render(request, 'data_embrapii/projetos/index.html', conteudo)
