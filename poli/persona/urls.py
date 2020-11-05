from django.urls import path

from persona import views

urlpatterns = [
    path('persona/', views.HomeView.as_view(), name='homePersona'),
    path('persona/<int:pk>/', views.PersonaDetailView.as_view(), name='persona_detail'),
    path('persona/create/', views.PersonaCreateView.as_view(), name='persona_create'),
    path('persona/update/<int:pk>/', views.PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/delete/<int:pk>/', views.PersonaDeleteView.as_view(), name='persona_delete')
]