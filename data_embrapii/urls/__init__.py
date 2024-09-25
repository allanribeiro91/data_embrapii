from .geral_urls import urlpatterns as geral_urls
from .dashboards_urls import urlpatterns as dashboards_urls
from .meus_dados_urls import urlpatterns as meus_dados_urls



# Combine todas as listas de URLs em uma só
urlpatterns = geral_urls + dashboards_urls + meus_dados_urls
