from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.views.decorators.csrf import csrf_protect

from iuptec_site.models import Veiculos


@csrf_protect
def registro(request):
    if request.method == 'POST':  # Verifica se o método é POST, se for, pega os dados do formulário
        usuario = request.POST['usuario']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        senha = request.POST['senha']
        confirma_senha = request.POST['confirma_senha']

        if em_branco(usuario):
            messages.error(request, 'O campo usuário é obrigatório')
            return redirect('registro')

        if usuario_existente(usuario):
            messages.error(request, 'Este usuário já está cadastrado')
            return redirect('registro')

        if em_branco(nome):
            messages.error(request, 'O campo nome é obrigatório')
            return redirect('registro')

        if not nome_valido(nome):  # Verifica se o campo nome tem números
            messages.error(request, 'O campo nome não pode ter números')
            return redirect('registro')

        if email_valido(email):
            messages.error(request, 'Por favor, digite um email válido')
            return redirect('registro')

        if telefone_valido(telefone):
            messages.error(request, 'Por favor, digite um telefone válido')
            return redirect('registro')

        if em_branco(senha):
            messages.error(request, 'O campo senha é obrigatório')
            return redirect('registro')

        if senhas_diferentes(senha, confirma_senha):
            messages.error(request, 'As senhas não são iguais')
            return redirect('registro')

        if email_existente(email):
            messages.error(request, 'Este email já está cadastrado')
            return redirect('registro')

        if nome_existente(nome):
            messages.error(request, 'Este nome já está cadastrado')
            return redirect('registro')

        user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)  # Cria o usuário no banco de dados
        user.save()  # Salva o usuário no banco de dados

        messages.success(request, 'Cadastrado efetuado com sucesso')
        return redirect('login')

    else:
        return render(request, 'usuarios/registro.html')


@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email_login_vazio(request, email, senha):
            return redirect('login')

        if User.objects.filter(email=email).exists():
            usuario = User.objects.filter(email=email).values_list('username', flat=True).get()  # Pega o username do usuário no banco de dados pelo email
            user = auth.authenticate(request, username=usuario, password=senha)  # Autentica o usuário
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')

        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect('login')

    return render(request, 'usuarios/login.html')


@csrf_protect
def dashboard(request):
    if request.user.is_authenticated:
        usuario = get_object_or_404(User, pk=request.user.id)  # Pega o usuário logado

        veiculos = Veiculos.objects.all().filter(pessoa=request.user.id)  # Pega todos os veículos do usuário logado

        dados = {
            'veiculos': veiculos,
            'nome': usuario.first_name
        }

        return render(request, 'usuarios/dashboard.html', dados)


def logout(request):
    auth.logout(request)
    return redirect('index')


@csrf_protect
def cadastro_veiculo(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        ano = request.POST['ano']
        placa = request.POST['placa']
        cor = request.POST['cor']

        if em_branco(modelo):
            messages.error(request, 'O campo modelo não pode ficar em branco')
            return redirect('cadastro_veiculo')

        if em_branco(marca):
            messages.error(request, 'O campo marca não pode ficar em branco')
            return redirect('cadastro_veiculo')

        if em_branco(ano):
            messages.error(request, 'O campo ano não pode ficar em branco')
            return redirect('cadastro_veiculo')

        if em_branco(placa):
            messages.error(request, 'O campo placa não pode ficar em branco')
            return redirect('cadastro_veiculo')

        if not placa_valida(placa):
            messages.error(request, 'Por favor, digite uma placa válida')
            return redirect('cadastro_veiculo')

        if em_branco(cor):
            messages.error(request, 'O campo cor não pode ficar em branco')
            return redirect('cadastro_veiculo')

        user = User.objects.get(id=request.user.id)  # Pega o usuário logado
        veiculo = Veiculos.objects.create(pessoa=user, modelo=modelo, marca=marca, ano=ano, placa=placa, cor=cor)  # Cria o veículo no banco de dados
        veiculo.save()  # Salva o veículo no banco de dados

        return redirect('dashboard')
    return render(request, 'usuarios/cadastro_veiculo.html')


@csrf_protect
def editar_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculos, pk=veiculo_id)  # Pega o veículo pelo id
    veiculo_a_editar = {
        'veiculo': veiculo
    }
    return render(request, 'usuarios/editar_veiculo.html', veiculo_a_editar)


@csrf_protect
def atualiza_veiculo(request, veiculo_id):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        ano = request.POST['ano']
        placa = request.POST['placa']
        cor = request.POST['cor']

        if em_branco(modelo):
            messages.error(request, 'O campo modelo não pode ficar em branco')
            return redirect('editar_veiculo', veiculo_id)

        if em_branco(marca):
            messages.error(request, 'O campo marca não pode ficar em branco')
            return redirect('editar_veiculo', veiculo_id)

        if em_branco(ano):
            messages.error(request, 'O campo ano não pode ficar em branco')
            return redirect('editar_veiculo', veiculo_id)

        if em_branco(placa):
            messages.error(request, 'O campo placa não pode ficar em branco')
            return redirect('editar_veiculo', veiculo_id)

        if not placa_valida(placa):
            messages.error(request, 'Por favor, digite uma placa válida')
            return redirect('editar_veiculo', veiculo_id)

        if em_branco(cor):
            messages.error(request, 'O campo cor não pode ficar em branco')
            return redirect('editar_veiculo', veiculo_id)

        veiculo = get_object_or_404(Veiculos, pk=veiculo_id)  # Pega o veículo pelo id
        veiculo.modelo = modelo  # Atualiza o modelo do veículo
        veiculo.marca = marca  # Atualiza a marca do veículo
        veiculo.ano = ano  # Atualiza o ano do veículo
        veiculo.placa = placa  # Atualiza a placa do veículo
        veiculo.cor = cor  # Atualiza a cor do veículo
        veiculo.save()  # Salva o veículo no banco de dados

        return redirect('dashboard')


@csrf_protect
def excluir_veiculo(veiculo_id):
    veiculo = get_object_or_404(Veiculos, pk=veiculo_id)  # Pega o veículo pelo id
    veiculo.delete()  # Deleta o veículo
    return redirect('dashboard')


def em_branco(campo):  # Verifica se o campo está em branco
    return not campo.strip()


def senhas_diferentes(senha, senha2):  # Verifica se as senhas são diferentes
    return senha != senha2


def email_valido(email):  # Verifica se o email é válido
    return em_branco(email) or '@' not in email or '.' not in email


def email_existente(email):  # Verifica se o email já existe no banco de dados
    return User.objects.filter(email=email).exists()


def telefone_valido(telefone):  # Verifica se o telefone é válido
    return em_branco(telefone) or len(telefone) < 11 or len(telefone) > 11 or telefone.isalpha()


def placa_valida(placa):  # Verifica se a placa é válida
    return len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric()


def nome_valido(nome):  # Verifica se o nome é válido
    # Retorna True se os caracteres forem alfabéticos ou espaços
    return all(char.isalpha() or char.isspace() for char in nome)


def nome_existente(nome):  # Verifica se o nome já existe no banco de dados
    return User.objects.filter(username=nome).exists()


def email_login_vazio(request, email, senha):  # Verifica se o email e a senha estão em branco no login
    if em_branco(email):
        return messages.error(request, 'O campo email não pode ficar em branco')

    if em_branco(senha):
        return messages.error(request, 'O campo senha não pode ficar em branco')


def usuario_existente(usuario):
    return User.objects.filter(username=usuario).exists()