from django.db import models
from django.contrib.auth.models import User

from setup.choices import STATUS_PRIVACIDADE, SETORES_EMBRAPII, FONTES_DADOS, FERRAMENTAS

class Usuario(models.Model): 
    #relacionamento
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_relacionado')
    
    #log
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    #dados pessoais (dp)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)

    #contato (ctt)
    celular = models.CharField(max_length=17, null=True, blank=True)
    email_pessoal = models.EmailField(max_length=40, null=True, blank=True)

    #usuario está ativo
    usuario_is_ativo = models.BooleanField(default=True, null=False, blank=False, db_index=True)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.cpf} - {self.nome_completo} (ID: {self.id})"
    
    def primeiro_ultimo_nome(self):
        partes_nome = self.nome_completo.split()
        primeiro_nome = partes_nome[0]
        ultimo_nome = partes_nome[-1] if len(partes_nome) > 1 else ''
        return f"{primeiro_nome} {ultimo_nome}"


class ProdutoInformacional(models.Model): 
    
    #log
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    user_registro = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_registro')
    user_atualizacao = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_atualizacao')
    
    #dados pessoais (dp)
    titulo = models.CharField(max_length=255, null=False, blank=False, unique=True)
    tipo_produto = models.CharField(max_length=255, null=True, blank=True)
    dono_produto = models.CharField(max_length=255, choices=SETORES_EMBRAPII, null=True, blank=True)
    status_privacidade = models.CharField(max_length=255, choices=STATUS_PRIVACIDADE, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateField(null=True, blank=True)
    fonte_dados = models.CharField(max_length=255, choices=FONTES_DADOS, null=True, blank=True)
    ferramenta = models.CharField(max_length=255, choices=FERRAMENTAS, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    
    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.tipo_produto}) (ID: {self.id})"
    
