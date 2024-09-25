from django.urls import path, include

urlpatterns = [
    path('', include('data_embrapii.urls.geral_urls')),
    path('', include('data_embrapii.urls.dashboards_urls')),
    path('', include('data_embrapii.urls.meus_dados_urls')),
]
