from django.core.management.base import BaseCommand
from data_embrapii.models import PortFolio

class Command(BaseCommand):
    help = 'Deleta todos os registros da tabela PortFolio'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando a limpeza dos dados...'))
        
        # Deletar todos os registros do modelo PortFolio
        total_registros = PortFolio.objects.count()  # Contar registros antes de deletar
        PortFolio.objects.all().delete()
        
        # Exibir uma mensagem informando quantos registros foram deletados
        self.stdout.write(self.style.SUCCESS(f'{total_registros} registros deletados com sucesso.'))
