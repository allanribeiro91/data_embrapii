from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import logout
from data_embrapii.forms import LoginForm

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

            if not usuario_validacao.usuario_is_ativo or usuario_validacao.del_status:
                mensagem_erro = "Usuário inativado!"
            else:
                auth.login(request, usuario)
                return redirect('home')

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
