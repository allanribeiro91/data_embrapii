from django.urls import path
from data_embrapii.views.geral_views import (home, unidades_embrapii, 
                                 centros_competencias, analises_tecnicas, bases_dados, documentos,
                                 )
from data_embrapii.views.auth_views import login
from data_embrapii.views.projetos_views import projetos

urlpatterns = [
    path('', login, name='login'),
    path('home', home, name='home'),

    path('projetos', projetos, name='projetos'),
    path('unidades_embrapii', unidades_embrapii, name='unidades_embrapii'),
    path('centros_competencias', centros_competencias, name='centros_competencias'),
    path('analises_tecnicas', analises_tecnicas, name='analises_tecnicas'),
    path('bases_dados', bases_dados, name='bases_dados'),
    path('documentos', documentos, name='documentos'),
]