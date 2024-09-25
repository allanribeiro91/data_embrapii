from django.shortcuts import render

abas_meus_dados = {
    'meus_dados': 'Meus Dados',
    'meus_logs': 'Meus Logs'
}

def meus_dados(request):
    conteudo = {
        'abas': abas_meus_dados,
    }
    return render(request, 'data_embrapii/mais_opcoes/meus_dados/index.html', conteudo)

def meus_logs(request):
    conteudo = {
        'abas': abas_meus_dados,
    }
    return render(request, 'data_embrapii/mais_opcoes/meus_logs/index.html', conteudo)
