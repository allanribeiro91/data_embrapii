from django.urls import path
from data_embrapii.views.dashboards_views import dashboards

urlpatterns = [
    path('dashboards', dashboards, name='dashboards'),
]
