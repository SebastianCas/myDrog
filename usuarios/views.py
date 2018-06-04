from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from usuarios.forms import RegistroForm
# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "registrar.html"
    form_class = UserCreationForm 
    #form_class = RegistroForm
    success_url = reverse_lazy('base')

#list
class UsuariosListView(ListView):
    model = User

#update
class UsuariosUpdate(UpdateView):
    model = User
    fields='__all__'

#delete
class UsuarioDelete(DeleteView):
    model = User
    success_url = reverse_lazy('usuarios-list')