from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from evento.models import Evento

# Create your views here.

class HomeView(ListView):
    model = Evento
    template_name = 'evento/index.html'
    paginate_by = 10


class EventoDetailView(DetailView):
    model = Evento
    template_name = 'evento/evento_detail.html'


class EventoCreateView(CreateView):
    model = Evento
    template_name = 'evento/evento_create.html'
    fields = ['codigo', 'nombre', 'tipo','duracion','descripcion']


class EventoUpdateView(UpdateView):
    model = Evento
    template_name = 'evento/evento_create.html'
    fields = ['codigo', 'nombre', 'tipo','duracion','descripcion']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class EventoDeleteView(DeleteView):
    model = Evento
    success_url = reverse_lazy('evento:homeEvento')
    template_name = 'evento/confirm_evento_deletion.html'