from django.shortcuts import render

ABAS = {
    'pinfo_dashboards': 'Dashboards',
    'pinfo_relatorios': 'Relatórios',
    'pinfo_apresentacoes': 'Apresentações',
}

BOTOES_INDEX = ['Download', 'Inserir']

BOTOES_FICHA = ['Cancelar', 'Salvar']

#Dashboards
def pinfo_dashboards(request):   
    conteudo = {
        'abas': ABAS,
        'botoes': BOTOES_INDEX,
    }
    return render(request, 'data_embrapii/produtos_informacionais/dashboards/index.html', conteudo)

ABAS_FICHA_DASHBOARDS = {
    'pinfo_dashboards': 'voltar',
    '#': 'Ficha do dashboard',
}

def pinfo_dashboards_novo(request):
    conteudo = {
        'abas': ABAS_FICHA_DASHBOARDS,
        'botoes': BOTOES_FICHA,
    }
    return render(request, 'data_embrapii/produtos_informacionais/dashboards/ficha.html', conteudo)

#Relatórios
def pinfo_relatorios(request):   
    conteudo = {
        'abas': ABAS,
        'botoes': BOTOES_INDEX,
    }
    return render(request, 'data_embrapii/produtos_informacionais/relatorios/index.html', conteudo)

ABAS_FICHA_RELATORIOS = {
    'pinfo_relatorios': 'voltar',
    '#': 'Ficha do relatório',
}

def pinfo_relatorios_novo(request):
    conteudo = {
        'abas': ABAS_FICHA_RELATORIOS,
        'botoes': BOTOES_FICHA,
    }
    return render(request, 'data_embrapii/produtos_informacionais/relatorios/ficha.html', conteudo)

#Apresentações
def pinfo_apresentacoes(request):   
    conteudo = {
        'abas': ABAS,
        'botoes': BOTOES_INDEX,
    }
    return render(request, 'data_embrapii/produtos_informacionais/apresentacoes/index.html', conteudo)

ABAS_FICHA_APRESENTACOES = {
    'pinfo_apresentacoes': 'voltar',
    '#': 'Ficha do apresentação',
}

def pinfo_apresentacoes_novo(request):
    conteudo = {
        'abas': ABAS_FICHA_APRESENTACOES,
        'botoes': BOTOES_FICHA,
    }
    return render(request, 'data_embrapii/produtos_informacionais/apresentacoes/ficha.html', conteudo)