from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from persona.models import Persona

# Create your views here.

class HomeView(ListView):
    model = Persona
    template_name = 'persona/index.html'
    paginate_by = 10


class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'persona/persona_detail.html'


class PersonaCreateView(CreateView):
    model = Persona
    template_name = 'persona/persona_create.html'
    fields = ['numIdentificacion', 'tipoIdentificacion', 'apellidoPaterno','apellidoMaterno','nombres','fechaNacimiento','sexo','telefono','direccion','email','evento']


class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = 'persona/persona_create.html'
    fields = ['numIdentificacion', 'tipoIdentificacion', 'apellidoPaterno','apellidoMaterno','nombres','fechaNacimiento','sexo','telefono','direccion','email','evento']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('persona:homePersona')
    template_name = 'persona/confirm_persona_deletion.html'