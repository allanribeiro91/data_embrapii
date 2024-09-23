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
    user_registro = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='produtoinfo_user_registro')
    user_atualizacao = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='produtoinfo_user_atualizacao')
    
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
    


class PortFolio(models.Model):
    codigo_projeto = models.CharField(max_length=255, null=False, blank=False, unique=True)
    unidade_embrapii = models.CharField(max_length=255, null=True, blank=True)
    data_contrato = models.DateField(null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_termino = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    tipo_projeto = models.TextField(null=True, blank=True)
    parceria_programa = models.CharField(max_length=255, null=True, blank=True)
    call = models.CharField(max_length=255, null=True, blank=True)
    cooperacao_internacional = models.CharField(max_length=255, null=True, blank=True)
    modalidade_financiamento = models.CharField(max_length=255, null=True, blank=True)
    uso_recurso_obrigatorio = models.CharField(max_length=255, null=True, blank=True)
    tecnologia_habilitadora = models.CharField(max_length=255, null=True, blank=True)
    missoes_cndi = models.CharField(max_length=255, null=True, blank=True)
    area_aplicacao = models.CharField(max_length=255, null=True, blank=True)
    projeto = models.CharField(max_length=255, null=True, blank=True)
    trl_inicial = models.CharField(max_length=255, null=True, blank=True)
    trl_final = models.CharField(max_length=255, null=True, blank=True)
    valor_embrapii = models.FloatField(null=True, blank=True)
    valor_empresa = models.FloatField(null=True, blank=True)
    valor_unidade_embrapii = models.FloatField(null=True, blank=True)
    titulo = models.CharField(max_length=255, null=True, blank=True)
    titulo_publico = models.CharField(max_length=255, null=True, blank=True)
    objetivo = models.TextField(null=True, blank=True)
    descricao_publica = models.TextField(null=True, blank=True)
    data_avaliacao = models.DateField(null=True, blank=True)
    nota_avaliacao = models.CharField(max_length=255, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    data_extracao_dados = models.DateField(null=True, blank=True)
    status_view = models.BooleanField(null=False, blank=False)

    def total_dias(self):
        if self.data_inicio and self.data_termino:  # Verifica se ambas as datas estão presentes
            return (self.data_termino - self.data_inicio).days
        return None
