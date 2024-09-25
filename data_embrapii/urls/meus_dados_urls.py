from django.urls import path
from data_embrapii.views.meus_dados_views import meus_dados, meus_logs

urlpatterns = [
    path('meus_dados', meus_dados, name='meus_dados'),
    path('meus_logs', meus_logs, name='meus_logs'),
]
