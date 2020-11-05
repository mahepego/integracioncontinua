from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ubicacion.models import Ubicacion

# Create your views here.

class HomeView(ListView):
    model = Ubicacion
    template_name = 'ubicacion/index.html'
    paginate_by = 10


class UbicacionDetailView(DetailView):
    model = Ubicacion
    template_name = 'ubicacion/ubicacion_detail.html'


class UbicacionCreateView(CreateView):
    model = Ubicacion
    template_name = 'ubicacion/ubicacion_create.html'
    fields = ['codigo', 'sector', 'nombre', 'capacidad']


class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    template_name = 'ubicacion/ubicacion_create.html'
    fields = ['codigo', 'sector', 'nombre', 'capacidad']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class UbicacionDeleteView(DeleteView):
    model = Ubicacion
    success_url = reverse_lazy('ubicacion:home')
    template_name = 'ubicacion/confirm_ubicacion_deletion.html'