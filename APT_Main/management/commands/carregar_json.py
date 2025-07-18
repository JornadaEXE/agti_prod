from django.core.management.base import BaseCommand
from APT_Main.models import JsonResponseMaxi

class Command(BaseCommand):
    help = 'Carrega um JSON de exemplo no banco de dados'

    def handle(self, *args, **kwargs):
        JsonResponseMaxi.objects.create(
            nome="retorno_padrao",
            payload={
                "status": "ok",
                "mensagem": "Este é o JSON de exemplo",
                "itens": [1, 2, 3]
            }
        )
        self.stdout.write(self.style.SUCCESS('JSON carregado com sucesso!'))