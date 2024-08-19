from django.urls import path
from data_embrapii.views import login, home, dashboards, projetos, unidades_embrapii, centros_competencias, analises_tecnicas, bases_dados, documentos, mais_opcoes

urlpatterns = [
    path('', login, name='login'),
    path('home', home, name='home'),
    path('dashboards', dashboards, name='dashboards'),
    path('projetos', projetos, name='projetos'),
    path('unidades_embrapii', unidades_embrapii, name='unidades_embrapii'),
    path('centros_competencias', centros_competencias, name='centros_competencias'),
    path('analises_tecnicas', analises_tecnicas, name='analises_tecnicas'),
    path('bases_dados', bases_dados, name='bases_dados'),
    path('documentos', documentos, name='documentos'),
    path('mais_opcoes', mais_opcoes, name='mais_opcoes'),
]