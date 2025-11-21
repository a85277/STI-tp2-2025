# --------------------------------------
# USER STORIES (CLIENTES)
# --------------------------------------

user_stories_clientes = [
    {
        "eu_como": "utilizador",
        "quero": "poder ver o percurso da minha encomenda",
        "para": "acompanhar o estado do envio"
    },
    {
        "eu_como": "utilizador",
        "quero": "poder criar uma conta",
        "para": "aceder ao sistema e receber serviços"
    },
    {
        "eu_como": "utilizador",
        "quero": "receber notificações (promoções ou avisos de produtos)",
        "para": "ficar informado sobre novidades"
    },
    {
        "eu_como": "utilizador",
        "quero": "ter uma página principal",
        "para": "navegar facilmente no sistema"
    },
    {
        "eu_como": "utilizador",
        "quero": "ver uma página só com o produto que selecionei",
        "para": "ver detalhes específicos"
    },
    {
        "eu_como": "utilizador",
        "quero": "ver especificações detalhadas dos produtos",
        "para": "poder comparar e decidir melhor"
    },
    {
        "eu_como": "cliente",
        "quero": "solicitar um orçamento de conserto online",
        "para": "saber quanto vou pagar"
    }
]

# --------------------------------------
# USER STORIES (ADMIN / TRABALHADORES)
# --------------------------------------

user_stories_admin = [
    {
        "eu_como": "admin",
        "quero": "anexar fotos e descrever o diagnóstico técnico",
        "para": "deixar o histórico do conserto claro"
    },
    {
        "eu_como": "administrador",
        "quero": "gerar uma ordem de serviço com assinatura do cliente",
        "para": "formalizar a solicitação de reparo"
    },
    {
        "eu_como": "dono",
        "quero": "fazer uma cópia de segurança dos dados",
        "para": "evitar perdas em caso de erros ou falhas"
    },
    {
        "eu_como": "funcionário",
        "quero": "ver o histórico das encomendas do cliente",
        "para": "ajudar em casos de dúvidas"
    },
    {
        "eu_como": "funcionário",
        "quero": "poder atualizar o estado de reparação do produto",
        "para": "manter o cliente informado"
    }
]

# --------------------------------------
# EXPORTAR COMO JSON
# --------------------------------------

import json

def exportar_json():
    estrutura = {
        "clientes": user_stories_clientes,
        "admin": user_stories_admin
    }

    with open("user_stories.json", "w", encoding="utf-8") as f:
        json.dump(estrutura, f, ensure_ascii=False, indent=4)

    print("Ficheiro 'user_stories.json' criado com sucesso!")
