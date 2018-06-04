from django.urls import path
from usuarios import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('usuarios',views.RegistroUsuario.as_view(), name="registrar"),
    path('usuarios/list',login_required(views.UsuariosListView.as_view()), name="usuarios-list"),
     #Update
    path('usuarios/list/<int:pk>/update/', login_required(views.UsuariosUpdate.as_view()), name='usuarios-update'),
    #Delete
    path('usuarios/list/sede/<int:pk>/delete/', login_required(views.UsuarioDelete.as_view()), name='usuarios-delete'),
]