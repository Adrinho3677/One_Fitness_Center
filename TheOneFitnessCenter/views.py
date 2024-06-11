from django.shortcuts import render, redirect
from TheOneFitnessCenter.models import Assinatura
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import default_storage
from django.conf import settings

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('cadastro')
    else:
        assinatura = Assinatura.objects.order_by('data')
        return render(request, 'index.html', {'dados':assinatura})

def cadastro(request):

    print('entrou')

    if request.method == 'POST':
            
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            
            print(nome, email, senha, senha2)
        
            if senha == senha2:
            
                if User.objects.filter(email=email):
                
                    return redirect('login')
                
                else:
                
                    usuario = User.objects.create_user(email=email, password=senha, username=email ,first_name=nome)
                    usuario.save()
                
                    return redirect('login')
                
            else:
            
                return redirect('cadastro')
            
    return render(request, 'cadastro.html')

def login(request):

    print('entrou2')

    if request.method == 'POST':

        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        print(email, senha)

        usuario = auth.authenticate(
            request,
            username = email,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def assinatura(request):

    print('entrou3')

    if request.method == 'POST':
            
        nome = request.POST.get('nome')
        descricao = request.POST.get('desc')
        imagem = request.FILES.get('img')

        print(imagem)

        # Salvar a imagem no diretório de mídia
        if not imagem:
            
            imagem= '../static/blank.png'  
                
        assinatura = Assinatura(nome=nome, descricao=descricao, foto=imagem)
        assinatura.save()
                
        return redirect('assinatura')
            
    return render(request, 'assinatura.html')

def info(request, id):

    assinatura = Assinatura.objects.get(id = id)
    return render(request, 'info.html', {'dados':assinatura})

def info_delete(request, id):
    if request.method == 'POST':
        dado = Assinatura.objects.get(id = id)
        dado.delete()
    return redirect('index')