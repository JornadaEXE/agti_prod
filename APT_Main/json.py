from .models import JsonResponseMaxi

JsonResponseMaxi.objects.create(
    nome="retorno_padrao",
    payload={
        "status": "ok",
        "mensagem": "Este é o JSON de exemplo",
        "itens": [1, 2, 3]
    }
)