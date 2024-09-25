from django.shortcuts import render

def home(request):
    return render(request, 'data_embrapii/home.html')

def unidades_embrapii(request):
    return render(request, 'data_embrapii/unidades_embrapii.html')

def centros_competencias(request):
    return render(request, 'data_embrapii/centros_competencias.html')

def analises_tecnicas(request):
    return render(request, 'data_embrapii/analises_tecnicas.html')

def bases_dados(request):
    return render(request, 'data_embrapii/bases_dados.html')

def documentos(request):
    return render(request, 'data_embrapii/documentos/index.html') 