from django.shortcuts import redirect, render

# Importações do Django
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Importações do App
from data_embrapii.forms import LoginForm
from data_embrapii.models import ProdutoInformacional
from setup.choices import STATUS_PRIVACIDADE, SETORES_EMBRAPII, FERRAMENTAS, FONTES_DADOS

def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        cpf = form.cleaned_data['cpf']
        senha = form.cleaned_data['senha']

        usuario = auth.authenticate(request, username=cpf, password=senha)

        if not usuario:
            mensagem_erro = "Usuário ou senha inválido!"
        else:
            usuario_validacao = usuario.usuario_relacionado

            #Verificar status
            if not usuario_validacao.usuario_is_ativo or usuario_validacao.del_status:
                mensagem_erro = "Usuário inativado!"
            else:
                auth.login(request, usuario)
                return redirect('home')

        # Se qualquer uma das verificações falhar, setar o valor inicial de 'cpf' e renderizar novamente
        form.fields['cpf'].initial = cpf
        conteudo = {
            'form': form,
            'mensagem': mensagem_erro,
        }
        return render(request, 'data_embrapii/login/login.html', conteudo)

    conteudo = {
        'form': form,
    }

    logout(request)
    return render(request, 'data_embrapii/login/login.html', conteudo)


def home(request):
    return render(request, 'data_embrapii/home.html')

def projetos(request):
    return render(request, 'data_embrapii/projetos.html')

def unidades_embrapii(request):
    return render(request, 'data_embrapii/unidades_embrapii.html')

def centros_competencias(request):
    return render(request, 'data_embrapii/centros_competencias.html')

def dashboards(request):

    infoprodutos = ProdutoInformacional.objects.filter(del_status=False).order_by('titulo')
    conteudo = {
        'infoprodutos': infoprodutos,
        'choices_status_privacidade': STATUS_PRIVACIDADE,
        'choices_ferramentas': FERRAMENTAS,
        'choices_dono_produto': SETORES_EMBRAPII,
        'choices_fontes_dados': FONTES_DADOS,
    }
    return render(request, 'data_embrapii/dashboards.html', conteudo)

def analises_tecnicas(request):
    return render(request, 'data_embrapii/analises_tecnicas.html')

def bases_dados(request):
    return render(request, 'data_embrapii/bases_dados.html')

def documentos(request):
    return render(request, 'data_embrapii/documentos.html') 

def mais_opcoes(request):
    return render(request, 'data_embrapii/mais_opcoes.html') 