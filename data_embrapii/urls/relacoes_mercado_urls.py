from django.urls import path
from data_embrapii.views.relacoes_mercado_views import rm_eventos, rm_eventos_novo, rm_interacoes, rm_interacoes_novo

urlpatterns = [

    # Eventos
    path('rm/eventos', rm_eventos, name='rm_eventos'),
    path('rm/eventos/novo', rm_eventos_novo, name='rm_eventos_novo'),

    # Interações
    path('rm/interacoes', rm_interacoes, name='rm_interacoes'),
    path('rm/interacoes/novo', rm_interacoes_novo, name='rm_interacoes_novo'),
    
]
