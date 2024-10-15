from django.shortcuts import render
import requests
from django.http import HttpResponse

def home(request):
    # URL do relatório Power BI
    url = "https://app.powerbi.com/view?r=eyJrIjoiOWQ0ZDY2MDMtY2IwOC00ZTllLWE4ZjQtZWZlZWIyYTMzYTJiIiwidCI6IjhmYjM0NGY0LTA3NDAtNGU1YS1iMmMxLTUzODU4YzBjNzMyZiJ9&pageName=0aa796dc0c21df30fa3b"

    # Fazer uma requisição HTTP ao Power BI
    response = requests.get(url)

    # Conteúdo para renderizar no template
    conteudo = {
        'powerbi_url': url,  # Armazenando a URL para renderização no template
    }

    # Renderiza o template 'home.html' com o contexto necessário
    return render(request, 'data_embrapii/home.html', conteudo)

    # powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiOWQ0ZDY2MDMtY2IwOC00ZTllLWE4ZjQtZWZlZWIyYTMzYTJiIiwidCI6IjhmYjM0NGY0LTA3NDAtNGU1YS1iMmMxLTUzODU4YzBjNzMyZiJ9&pageName=0aa796dc0c21df30fa3b"
    # conteudo = {
    #     'powerbi_url': powerbi_url,
    # }

def unidades_embrapii(request):
    return render(request, 'data_embrapii/unidades_embrapii.html')

def centros_competencias(request):
    return render(request, 'data_embrapii/centros_competencias.html')

def bases_dados(request):
    return render(request, 'data_embrapii/bases_dados.html')

def documentos(request):
    return render(request, 'data_embrapii/documentos/index.html') 