from django.shortcuts import render

ABAS = {
    'rm_eventos': 'Eventos',
    'rm_interacoes': 'Interações'
}

BOTOES_INDEX = ['Download', 'Inserir']

ABAS_FICHA_EVENTOS = {
    'rm_eventos': 'voltar',
    '#': 'Ficha do evento',
}

ABAS_FICHA_INTERACOES = {
    'rm_interacoes': 'voltar',
    '#': 'Ficha da interaçao',
}

BOTOES_FICHA = ['Cancelar', 'Salvar']

#Eventos
def rm_eventos(request):   
    conteudo = {
        'abas': ABAS,
        'botoes': BOTOES_INDEX,
    }
    return render(request, 'data_embrapii/relacoes_mercado/eventos/index.html', conteudo)

def rm_eventos_novo(request):
    conteudo = {
        'abas': ABAS_FICHA_EVENTOS,
        'botoes': BOTOES_FICHA,
    }
    return render(request, 'data_embrapii/relacoes_mercado/eventos/ficha.html', conteudo)


#Interações
def rm_interacoes(request):
    conteudo = {
        'abas': ABAS,
        'botoes': BOTOES_INDEX,
    }
    return render(request, 'data_embrapii/relacoes_mercado/interacoes/index.html', conteudo)

def rm_interacoes_novo(request):
    conteudo = {
        'abas': ABAS_FICHA_INTERACOES,
        'botoes': BOTOES_FICHA,
    }
    return render(request, 'data_embrapii/relacoes_mercado/interacoes/ficha.html', conteudo)