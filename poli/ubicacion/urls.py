from django.urls import path

from django.conf.urls import url
from ubicacion import views
from .views import ConsolidadoUbicacion

urlpatterns = [
    path('ubicacion/', views.HomeView.as_view(), name='homeUbicacion'),
    path('ubicacion/<int:pk>/', views.UbicacionDetailView.as_view(), name='ubicacion_detail'),
    path('ubicacion/create/', views.UbicacionCreateView.as_view(), name='ubicacion_create'),
    path('ubicacion/update/<int:pk>/', views.UbicacionUpdateView.as_view(), name='ubicacion_update'),
    path('ubicacion/delete/<int:pk>/', views.UbicacionDeleteView.as_view(), name='ubicacion_delete'),
    url(r'^ConsolidadoUbicacion/', ConsolidadoUbicacion.as_view(), name='ConsolidadoUbicacion'),
]