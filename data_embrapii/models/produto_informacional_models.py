from django.db import models
from django.contrib.auth.models import User
from setup.choices import STATUS_PRIVACIDADE, SETORES_EMBRAPII, FONTES_DADOS, FERRAMENTAS

class ProdutoInformacional(models.Model):
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    user_registro = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='produtoinfo_user_registro')
    user_atualizacao = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='produtoinfo_user_atualizacao')
    titulo = models.CharField(max_length=255, null=False, blank=False, unique=True)
    tipo_produto = models.CharField(max_length=255, null=True, blank=True)
    dono_produto = models.CharField(max_length=255, choices=SETORES_EMBRAPII, null=True, blank=True)
    status_privacidade = models.CharField(max_length=255, choices=STATUS_PRIVACIDADE, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateField(null=True, blank=True)
    fonte_dados = models.CharField(max_length=255, choices=FONTES_DADOS, null=True, blank=True)
    ferramenta = models.CharField(max_length=255, choices=FERRAMENTAS, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.tipo_produto}) (ID: {self.id})"
