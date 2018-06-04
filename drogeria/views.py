from django.http import HttpResponse
from django.shortcuts import render
from drogeria.models import Sede, Medicamento,Paciente
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def first_view(request):
    return render(request, 'bienvenido.html')

#buscar
class BuscarView(TemplateView):
    def post(self,request, *arg, **kwargs):
        buscar=request.POST['buscalo']
        medicamento = Medicamento.objects.filter(nombre__contains=buscar)
        if medicamento:
            print(medicamento)
            return render(request,'drogeria/buscar.html',{'medicamentos':medicamento,'medicamento':True})
        else:
            paciente=Paciente.objects.filter(nombres__contains=buscar)
            return render(request,'drogeria/buscar.html',{'pacientes':paciente,'paciente':True})

#lista
class SedeListView(ListView):
    model = Sede
class SedeDetailView(DetailView):
    model = Sede

class MedicamentoListView(ListView):
    model = Medicamento
class MedicamentoDetailView(DetailView):
    model = Medicamento

class PacienteListView(ListView):
    model = Paciente
class PacienteDetailView(DetailView):
    model = Paciente


#create
class SedeCreate(CreateView):
    model = Sede
    fields='__all__'
class MedicamentoCreate(CreateView):
    model = Medicamento
    fields='__all__'
class PacienteCreate(CreateView):
    model = Paciente
    fields='__all__'

#update
class SedeUpdate(UpdateView):
    model = Sede
    fields='__all__'
class MedicamentoUpdate(UpdateView):
    model = Medicamento
    fields='__all__'
class PacienteUpdate(UpdateView):
    model = Paciente
    fields='__all__'



#delete
class SedeDelete(DeleteView):
    model = Sede
    success_url = reverse_lazy('sede-list')
class MedicamentoDelete(DeleteView):
    model = Medicamento
    success_url = reverse_lazy('medicamento-list')
class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('paciente-list')
