from django.urls import path
from . import views

# Caminhos para as páginas com as funções que serão executadas
urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cadastro_veiculo', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('excluir_veiculo/<int:veiculo_id>', views.excluir_veiculo, name='excluir_veiculo'),
    path('editar_veiculo/<int:veiculo_id>', views.editar_veiculo, name='editar_veiculo'),
    path('atualiza_veiculo/<int:veiculo_id>', views.atualiza_veiculo, name='atualiza_veiculo'),
]