from django.db import models

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
        if self.data_inicio and self.data_termino:
            return (self.data_termino - self.data_inicio).days
        return None
