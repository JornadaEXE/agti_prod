from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .forms import CredencialForm, FornecedorForm, LicencaForm, CadastroUserForm, LancamentoForm, EndEqpForm, CadTipForm, CadEqpForm, CadSetForm
from .models import t001log, t010for, t100lic, JsonResponseMaxi, t200ipc, t002set, t003tip, t004eqp
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'APT_Main/login.html') 

def cad_credenciais(request):
    return redirect('cadastro')

@login_required
def main_page(request):
    return render(request, 'APT_Main/main_page.html')

def login_old(request):
    if request.method == 'POST':
        login_input = request.POST.get('login')
        senha_input = request.POST.get('senha')

        try:
            usuario = t001log.objects.get(Q(susrlog=login_input) | Q(susrnam=login_input))

            if check_password(senha_input, usuario.susrsen):
                return redirect('main_page')
            else:
                return render(request, 'APT_Main/login.html', {'error': 'Senha incorreta.'})
        except t001log.DoesNotExist:
            return render(request, 'APT_Main/login.html', {'error': 'Usuário não encontrado'})    

    return render(request, 'APT_Main/login.html')

def insere_cred(request):
    if request.method == "POST":
        form = CredencialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = CredencialForm()
 
    return render(request, 'APT_Main/cad_credenciais.html', {'form': form})

def configuracao(request):
    return render(request, 'APT_Main/configuracao.html')

def cad_info(request):
    return render(request, 'APT_Main/cad_info.html')

def insere_for(request):
    mensagem = None

    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            instancia = form.save()
            print("Fornecedor salvo com ID:", instancia.id if hasattr(instancia, 'id') else instancia.pk)
            mensagem = "Fornecedor cadastrado com sucesso!"
            form = FornecedorForm()  # limpa o formulário
        else:
            print("ERROS DO FORMULÁRIO:")
            print("Erros no formulário:", form.errors.as_text())  # debug opcional
    else:
        form = FornecedorForm()
    
    fornecedores_lista = t010for.objects.order_by('-id')
    paginator = Paginator(fornecedores_lista, 5)  # 5 por página
    page_number = request.GET.get('page')
    fornecedores = paginator.get_page(page_number)

    return render(request, 'APT_Main/gtfor001.html', {'form': form,
                                                       'mensagem': mensagem,
                                                       'fornecedores': fornecedores})

def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(t010for, id=id)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('gtfor001')
    else:
        form = FornecedorForm(instance=fornecedor)

    return render(request, 'APT_Main/gtfor001.html', {'form': form, 'fornecedores': t010for.objects.order_by('-id')})

def excluir_fornecedor(request, id):
    fornecedor = get_object_or_404(t010for, id=id)
    fornecedor.delete()
    return redirect('gtfor001')

def insere_lic(request):

    # Definições de Variáveis -------------------#

    mensagem = None
    licenca_instance = None

    # Get -------------------------- #

    buscar_licenca = request.GET.get('buscar_licenca')
    if buscar_licenca:
        licenca_instance = t100lic.objects.filter(ncodlic=buscar_licenca).first() # Este é um comando originário do ORM, onde selecionamos o modelo.objects.filter, ou seja,
        # pegamos o objeto, o filtramos, através da condição entre parenteses, neste caso, se ncodlic = buscar_licenca, que dentro do HTML, vem do campo input licenca,
        # já o first, busca o primeiro registro apenas, para caso de diferentes campos

        if licenca_instance: # comparador, se está preenchido, prossegue
            form = LicencaForm(instance=licenca_instance) # é este comando que preenche o form com os dados do código acima
            mensagem = "Licença carregada com sucesso"
        else: # caso não encontre nenhuma licença com o código informado...
            form = LicencaForm() # Carrega o form sem dados, vazio
            mensagem = "Licença não encontrada"

    # Post ------------------------- # # O post serve para quando o usuário quer cadastrar ou atualizar

    elif request.method == "POST": # elif sendo chamado através do if buscar_licenca, quando o mesmo estiver vazio
        ncodlic = request.POST.get("ncodlic") # captura o codigo informado
        licenca_instance = t100lic.objects.filter(ncodlic=ncodlic).first() # busca novamente o codigo sendo preenchido dentro do banco

        if licenca_instance: # comparador, caso preenchido, edita, caso não, altera
            form = LicencaForm(request.POST, instance=licenca_instance) 
            mensagem = "Licença alterada com sucesso!"
        else: # quando não está preenchido...
            form = LicencaForm(request.POST) # aqui preenchemos o request.POST, dessa forma, estamos inserindo todas as variáveis do formulário
            mensagem = "Licença cadastrada com sucesso!"
        if form.is_valid(): # se o formulário for valido...
            instancia = form.save() # salva dentro do banco
            print("Licenca salva com ID:", instancia.id if hasattr(instancia, 'id') else instancia.pk)
            form = LicencaForm()  # limpa o formulário
        else:
            print("Erros no formulário:", form.errors.as_text())  # debug opcional
    else:
        form = LicencaForm() # Get vazio, deixando limpo o formulário

    # Paginator --------------------- #    
    
    licenca_lista = t100lic.objects.order_by('-id')
    paginator = Paginator(licenca_lista, 5)  # 5 por página
    page_number = request.GET.get('page')
    licencas = paginator.get_page(page_number)

    return render(request, 'APT_Main/inlic001.html', {'form': form,
                                                       'mensagem': mensagem,
                                                       'licencas': licencas})

def manutencao(request):
    return render(request, 'APT_Main/manutencao.html' )

def informacoes(request):
    return render(request, 'APT_Main/informacoes.html' )

def responder_json(request):
    try:
        dado = JsonResponseMaxi.objects.get(nome="retorno_padrao")
        return JsonResponse(dado.payload, safe=False)
    except JsonResponseMaxi.DoesNotExist:
        return JsonResponse({"erro": "JSON não encontrado"}, status=404)

def excluir_licenca(request, id):
    licenca = get_object_or_404(t100lic, id=id)
    licenca.delete()
    return redirect('inlic001')

@login_required
def log_sec(request):
    return render(request, 'APT_Main/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')  # Substitua pelo nome da sua página inicial
        else:
            return render(request, 'APT_Main/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'APT_Main/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha']
            )
            return redirect('login')
    else:
        form = CadastroUserForm()

    usuarios = User.objects.all()
    
    return render(request, 'APT_Main/cadastro.html', {'form': form, 'usuarios': usuarios})

def red_login(request):
    return render(request, 'APT_Main/login.html')

def lancamento_contrato(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            instancia = form.save()
            form = LancamentoForm()
    else:
        form = LancamentoForm()

    return render(request, 'APT_Main/gtlan001.html', {'form': form})

def cad_endip(request):
    if request.method == 'POST':
        form = EndEqpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('end_eqp')
    else:
        form = EndEqpForm()
    
    registros = t200ipc.objects.all()

    return render(request, 'APT_Main/inend001.html', {'form': form, 'registros' : registros})

def cad_tipo(request):
    if request.method == 'POST':
        form = CadTipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_tip')
    else:
        form = CadTipForm()

    registros = t003tip.objects.all()

    return render(request, 'APT_Main/ceqp001.html', {'form' : form, 'registros' : registros})

def cad_equipamento(request):
    if request.method == 'POST':
        form = CadEqpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_equipamento')
    else:
        form = CadEqpForm()

    registros = t004eqp.objects.all()

    return render(request, 'APT_Main/ceqp002.html', {'form' : form, 'registros' : registros})

def cad_setores(request):
    if request.method == 'POST':
        form = CadSetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_setores')
    else:
        form = CadSetForm()

    registros = t002set.objects.all()

    return render(request, 'APT_Main/cinfo001.html', {'form' : form, 'registros' : registros})