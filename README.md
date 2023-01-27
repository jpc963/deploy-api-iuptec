Cria um sistema de cadastro de veículos com as seguintes funcionalidades:

[x] Cadastro de usuários
[x] Cadastro de veículos
[x] Listagem de veículos
[x] Edição de veículos
[x] Exclusão de veículos

## Como executar o projeto

1. Clone o repositório
2. Crie um ambiente virtual com o comando `python -m venv venv`
3. Ative o ambiente virtual com o comando `venv\Scripts\activate`
4. Instale as dependências com o comando `pip install -r requirements.txt`
5. Rode as migrações com o comando `python manage.py migrate`
6. Execute o servidor com o comando `python manage.py runserver`

## Como acessar o sistema

1. Acesse a url `http://localhost:8000/`
2. Clique em `Cadastrar` para criar um novo usuário
3. Faça login com o usuário e senha criados

## Como acessar o painel de administração

1. Crie um super usuário com o comando `python manage.py createsuperuser`
2. Acesse a url `http://localhost:8000/admin/`
3. Faça login com o usuário e senha criados
