from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from registro.models import Registro

# Create your views here.

class HomeView(ListView):
    model = Registro
    template_name = 'registro/index.html'
    paginate_by = 10


class RegistroDetailView(DetailView):
    model = Registro
    template_name = 'registro/registro_detail.html'


class RegistroCreateView(CreateView):
    model = Registro
    template_name = 'registro/registro_create.html'
    fields = ['persona', 'evento']


class RegistroUpdateView(UpdateView):
    model = Registro
    template_name = 'registro/registro_create.html'
    fields = ['persona', 'evento']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class RegistroDeleteView(DeleteView):
    model = Registro
    success_url = reverse_lazy('registro:homeRegistro')
    template_name = 'registro/confirm_registro_deletion.html'