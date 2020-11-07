from django.urls import path

from persona import views
from django.conf.urls import url
from .views import ConsolidadoPersona

urlpatterns = [
    path('persona/', views.HomeView.as_view(), name='homePersona'),
    path('persona/<int:pk>/', views.PersonaDetailView.as_view(), name='persona_detail'),
    path('persona/create/', views.PersonaCreateView.as_view(), name='persona_create'),
    path('persona/update/<int:pk>/', views.PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/delete/<int:pk>/', views.PersonaDeleteView.as_view(), name='persona_delete'),
    url(r'^ConsolidadoPersona/', ConsolidadoPersona.as_view(), name='ConsolidadoPersona'),
]