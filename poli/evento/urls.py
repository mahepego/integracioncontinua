from django.urls import path

from django.conf.urls import url
from evento import views
from .views import ConsolidadoEvento

urlpatterns = [
    path('evento/', views.HomeView.as_view(), name='homeEvento'),
    path('evento/<int:pk>/', views.EventoDetailView.as_view(), name='evento_detail'),
    path('evento/create/', views.EventoCreateView.as_view(), name='evento_create'),
    path('evento/update/<int:pk>/', views.EventoUpdateView.as_view(), name='evento_update'),
    path('evento/delete/<int:pk>/', views.EventoDeleteView.as_view(), name='evento_delete'),
    url(r'^ConsolidadoEvento/', ConsolidadoEvento.as_view(), name='ConsolidadoEvento'),
]