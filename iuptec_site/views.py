from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def cadastro_veiculo(request):
    return render(request, 'cadastro_veiculo.html')


def editar(request):
    return render(request, 'editar.html')