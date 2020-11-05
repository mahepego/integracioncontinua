from django.urls import path

from ubicacion import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ubicacion/<int:pk>/', views.UbicacionDetailView.as_view(), name='ubicacion_detail'),
    path('ubicacion/create/', views.UbicacionCreateView.as_view(), name='ubicacion_create'),
    path('ubicacion/update/<int:pk>/', views.UbicacionUpdateView.as_view(), name='ubicacion_update'),
    path('ubicacion/delete/<int:pk>/', views.UbicacionDeleteView.as_view(), name='ubicacion_delete')
]