from django.urls import path
from drogeria import views 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.first_view), name='base'),

    path('sede/', login_required(views.SedeListView.as_view()), name='sede-list'),
    path('sede/<int:pk>/detail/', login_required(views.SedeDetailView.as_view()), name='sede-detail'),
    path('sede/api/', login_required(views.SedeListViewApi.as_view()), name='sede-list-Api'),

    path('medicamento/', login_required(views.MedicamentoListView.as_view()), name='medicamento-list'),
    path('medicamento/<int:pk>/detail/', login_required(views.MedicamentoDetailView.as_view()), name='medicamento-detail'),
    path('medicamento/api/', login_required(views.MedicamentoListViewApi.as_view()), name='medicamento-list-Api'),

    path('paciente/', login_required(views.PacienteListView.as_view()), name='paciente-list'),
    path('paciente/<int:pk>/detail/', login_required(views.PacienteDetailView.as_view()), name='paciente-detail'),
    path('paciente/api', login_required(views.PacienteListViewApi.as_view()), name='paciente-list-api'),

    path('medicamentos/buscar/', login_required(views.BuscarView.as_view()), name='buscar'),

    #Create
    path('sede/create/', login_required(views.SedeCreate.as_view()), name='sede-create'),
    path('medicamento/create/', login_required(views.MedicamentoCreate.as_view()), name='medicamento-create'),
    path('paciente/create/', login_required(views.PacienteCreate.as_view()), name='paciente-create'),

    #Update
    path('sede/<int:pk>/update/', login_required(views.SedeUpdate.as_view()), name='sede-update'),
    path('medicamento/<int:pk>/update/', login_required(views.MedicamentoUpdate.as_view()), name='medicamento-update'),
    path('paciente/<int:pk>/update/', login_required(views.PacienteUpdate.as_view()), name='paciente-update'),

    #Delete
    path('sede/<int:pk>/delete/', login_required(views.SedeDelete.as_view()), name='sede-delete'),
    path('medicamento/<int:pk>/delete/', login_required(views.MedicamentoDelete.as_view()), name='medicamento-delete'),
    path('paciente/<int:pk>/delete/', login_required(views.PacienteDelete.as_view()), name='paciente-delete'),
]