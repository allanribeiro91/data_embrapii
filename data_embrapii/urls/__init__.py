from .geral_urls import urlpatterns as geral_urls
from .produtos_informacionais import urlpatterns as produtos_informacionais_urls
from .meus_dados_urls import urlpatterns as meus_dados_urls
from .relacoes_mercado_urls import urlpatterns as relacoes_mercado_urls



# Combine todas as listas de URLs em uma só
urlpatterns = geral_urls + produtos_informacionais_urls + meus_dados_urls + relacoes_mercado_urls
