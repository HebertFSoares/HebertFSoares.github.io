from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Perfil
from django.http import HttpResponse
import time
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
import re

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirma_senha = request.POST.get("confirma_senha")
        data_nascimento_str = request.POST.get("data_nascimento")
        user_type = request.POST.get("user_type")
        estado_civil = request.POST.get("estado_civil")
        cpf_estudante = request.POST.get("cpf")
        cpf_anfitriao = request.POST.get("cpf_anfitriao")
        telefone = request.POST.get("telefone")
        nome_pai = request.POST.get("nome_pai")
        nome_mae = request.POST.get("nome_mae")
        instituicao = request.POST.get("instituicao")
        periodo = request.POST.get("periodo")
        resumo_academico = request.POST.get("resumo_academico")
        endereco = request.POST.get("endereco")
        descricao_espaco = request.POST.get("descricao_espaco")
        comodidades = request.POST.get("comodidades")
        
        # Verificações
        data_nascimento = None
        idade_minima = 17
        
        if not data_nascimento_str:
            messages.error(request, 'A data de nascimento é obrigatória.')
            return redirect(reverse('cadastro'))

        try:
            data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'A data de nascimento possui um formato inválido.')
            return redirect(reverse('cadastro'))

        if data_nascimento is None or data_nascimento.year is None:
            messages.error(request, 'A data de nascimento é inválida.')
            return redirect(reverse('cadastro'))

        idade = datetime.now().date().year - data_nascimento.year
        
        if idade < idade_minima:
            messages.add_message(request, constants.ERROR, 'Você deve ter pelo menos 17 anos para se cadastrar.')
            return redirect(reverse('cadastro'))
        
        if not usuario or not email or not senha or not confirma_senha or not data_nascimento:
            messages.add_message(request, constants.ERROR, 'A campos obrigatórios vazios.')
            return redirect(reverse('cadastro'))
        
        if User.objects.filter(username=usuario).exists():
            messages.add_message(request, constants.ERROR, 'O nome de usuário já está em uso por outro usuário.')
            return redirect(reverse('cadastro'))

        if not (senha == confirma_senha):
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect(reverse('cadastro'))
        
        if len(senha) < 8:
            messages.add_message(request, constants.ERROR, 'A senha deve conter pelo menos 8 caracteres.')
            return redirect(reverse('cadastro'))
        
        if not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'\d', senha):
            messages.add_message(request, constants.ERROR, 'A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um dígito.')
            return redirect(reverse('cadastro'))
        
        usuarios = User.objects.filter(email=email)
        if usuarios.exists():
            messages.add_message(request, constants.ERROR, 'O email já está em uso por outro usuário.')
            return redirect(reverse('cadastro'))
       
        if user_type == 'estudante':
            if not cpf_estudante:
                messages.add_message(request, constants.ERROR, 'O campo CPF do estudante é obrigatório.')
                return redirect(reverse('cadastro'))
            if len(cpf_estudante) != 11:
                messages.add_message(request, constants.ERROR, 'CPF do estudante inválido.')
                return redirect(reverse('cadastro'))
            if Perfil.objects.filter(cpf_estudante=cpf_estudante).exists():
                messages.add_message(request, constants.ERROR, 'Cpf Inválido.')
                return redirect(reverse('cadastro'))
        
        if user_type == 'anfitriao':
            if not cpf_anfitriao:
                messages.add_message(request, constants.ERROR, 'O campo CPF do anfitrião é obrigatório.')
                return redirect(reverse('cadastro'))
            if len(cpf_anfitriao) != 11:
                messages.add_message(request, constants.ERROR, 'CPF do anfitrião inválido.')
                return redirect(reverse('cadastro'))
            if Perfil.objects.filter(cpf_anfitriao=cpf_anfitriao).exists():
                messages.add_message(request, constants.ERROR, 'Cpf Inválido.')
                return redirect(reverse('cadastro'))
        
        # Cria um novo usuário
        
        username = usuario
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        
        # Cria o perfil do usuário com os campos extras
         
        perfil = Perfil.objects.create(
            usuario=user,
            data_nascimento=data_nascimento,
            user_type=user_type,
            estado_civil=estado_civil,
            cpf_estudante=cpf_estudante,
            telefone_estudante=telefone,
            nome_pai=nome_pai,
            nome_mae=nome_mae,
            instituicao=instituicao,
            periodo=periodo,
            resumo_academico=resumo_academico,
            cpf_anfitriao=cpf_anfitriao,
            telefone_anfitriao=telefone,
            endereco=endereco,
            descricao_espaco=descricao_espaco,
            comodidades=comodidades
        )
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso.')
        return redirect(reverse('login'))
    
    elif request.method == "GET":
        return render(request, 'cadastro.html')

def is_estudante(user):
    try:
        perfil = Perfil.objects.get(usuario=user)
        return perfil.user_type == 'estudante'
    except Perfil.DoesNotExist:
        return False

def is_anfitriao(user):
    try:
        perfil = Perfil.objects.get(usuario=user)
        return perfil.user_type == 'anfitriao'
    except Perfil.DoesNotExist:
        return False

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        
        if not usuario or not senha:
            messages.add_message(request, constants.ERROR, 'Por favor, preencha todos os campos.')
            return redirect(reverse('login'))
        
        user = auth.authenticate(username=usuario, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        
        # Verificar o tipo de usuário e redirecionar para a página correta
        if is_estudante(user):
            return redirect(reverse('home_estudante'))
        
        if is_anfitriao(user):
            return redirect(reverse('anfitriao_home'))


    
def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.SUCCESS, 'obrigado pela visita. até breve!')
    return redirect(reverse('login'))


