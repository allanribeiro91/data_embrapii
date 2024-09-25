from django.shortcuts import render
from data_embrapii.models import ProdutoInformacional
from setup.choices import STATUS_PRIVACIDADE, SETORES_EMBRAPII, FERRAMENTAS, FONTES_DADOS

def dashboards(request):
    infoprodutos = ProdutoInformacional.objects.filter(del_status=False).order_by('titulo')
    conteudo = {
        'infoprodutos': infoprodutos,
        'choices_status_privacidade': STATUS_PRIVACIDADE,
        'choices_ferramentas': FERRAMENTAS,
        'choices_dono_produto': SETORES_EMBRAPII,
        'choices_fontes_dados': FONTES_DADOS,
    }
    return render(request, 'data_embrapii/dashboards/index.html', conteudo)
