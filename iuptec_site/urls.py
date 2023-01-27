from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_veiculo', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('editar', views.editar, name='editar'),
]