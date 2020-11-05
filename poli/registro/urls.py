from django.urls import path

from registro import views

urlpatterns = [
    path('registro/', views.HomeView.as_view(), name='homeRegistro'),
    path('registro/<int:pk>/', views.RegistroDetailView.as_view(), name='registro_detail'),
    path('registro/create/', views.RegistroCreateView.as_view(), name='registro_create'),
    path('registro/update/<int:pk>/', views.RegistroUpdateView.as_view(), name='registro_update'),
    path('registro/delete/<int:pk>/', views.RegistroDeleteView.as_view(), name='registro_delete')
]