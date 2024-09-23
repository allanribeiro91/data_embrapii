from datetime import datetime, timedelta
import openpyxl
from django.core.management.base import BaseCommand
from data_embrapii.models import PortFolio

class Command(BaseCommand):
    help = 'Importa dados do Excel para o modelo PortFolio'

    def handle(self, *args, **kwargs):
        file_path = 'dados/portfolio.xlsx'  # Ajuste o caminho do arquivo Excel
        self.import_from_excel(file_path)

    def import_from_excel(self, file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            projeto = PortFolio()

            projeto.codigo_projeto = row[0]
            projeto.unidade_embrapii = row[1]

            # Converter datas usando a função convert_date
            projeto.data_contrato = self.convert_date(row[2])
            projeto.data_inicio = self.convert_date(row[3])
            projeto.data_termino = self.convert_date(row[4])

            projeto.status = row[5]
            projeto.tipo_projeto = row[6]
            projeto.parceria_programa = row[7]
            projeto.call = row[8]
            projeto.cooperacao_internacional = row[9]
            projeto.modalidade_financiamento = row[10]
            projeto.uso_recurso_obrigatorio = row[11]
            projeto.tecnologia_habilitadora = row[12]
            projeto.missoes_cndi = row[13]
            projeto.area_aplicacao = row[14]
            projeto.projeto = row[15]
            projeto.trl_inicial = row[16]
            projeto.trl_final = row[17]
            projeto.valor_embrapii = row[18]
            projeto.valor_empresa = row[19]
            projeto.valor_unidade_embrapii = row[20]
            projeto.titulo = row[21]
            projeto.titulo_publico = row[22]
            projeto.objetivo = row[23]
            projeto.descricao_publica = row[24]

            projeto.data_avaliacao = self.convert_date(row[25])
            projeto.nota_avaliacao = row[26]
            projeto.observacoes = row[27]
            projeto.tags = row[28]
            projeto.data_extracao_dados = self.convert_date(row[29])

            projeto.status_view = True
            projeto.save()

    

    from datetime import datetime, timedelta

    def convert_date(self, date_value):
        """
        Converte datas em número serial do Excel ou strings numéricas para o formato de data.
        Se o valor for uma string no formato DD/MM/YYYY, converte também.
        Se for None ou vazio, retorna None.
        """
        # Tratar campos vazios ou nulos
        if not date_value:  # Verifica se o valor é None, vazio ou equivalente
            return None

        # Tratar números seriais do Excel ou strings numéricas
        if isinstance(date_value, (int, float)):
            try:
                base_date = datetime(1899, 12, 30)  # Data base do Excel (30/12/1899)
                return base_date + timedelta(days=date_value)
            except ValueError:
                self.stdout.write(self.style.ERROR(f"Data inválida (serial do Excel): {date_value}"))
                return None
        elif isinstance(date_value, str):
            # Tentar converter strings numéricas para número serial do Excel
            try:
                date_as_number = float(date_value)
                base_date = datetime(1899, 12, 30)
                return base_date + timedelta(days=date_as_number)
            except ValueError:
                # Se não for numérica, tenta tratar como string DD/MM/YYYY
                try:
                    return datetime.strptime(date_value, "%d/%m/%Y").date()
                except ValueError:
                    self.stdout.write(self.style.ERROR(f"Data inválida (string): {date_value}"))
                    return None
        
        return None  # Retornar None para qualquer caso não tratado

