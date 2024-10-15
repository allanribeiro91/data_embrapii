from django.urls import path
from data_embrapii.views.produtos_informacionais_views import (pinfo_dashboards, pinfo_relatorios, pinfo_apresentacoes,
                                                               pinfo_dashboards_novo, pinfo_relatorios_novo, pinfo_apresentacoes_novo)

urlpatterns = [

    #Dashboards
    path('pinfo_dashboards', pinfo_dashboards, name='pinfo_dashboards'),
    path('pinfo_dashboards/novo', pinfo_dashboards_novo, name='pinfo_dashboards_novo'),

    #Relatórios
    path('pinfo_relatorios', pinfo_relatorios, name='pinfo_relatorios'),
    path('pinfo_relatorios/novo', pinfo_relatorios_novo, name='pinfo_relatorios_novo'),

    #Apresentações
    path('pinfo_apresentacoes', pinfo_apresentacoes, name='pinfo_apresentacoes'),
    path('pinfo_apresentacoes/novo', pinfo_apresentacoes_novo, name='pinfo_apresentacoes_novo'),
]
