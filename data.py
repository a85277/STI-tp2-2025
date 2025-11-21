# json.py

import json

# ---------------------------------------
# User Stories – Clientes
# ---------------------------------------
user_stories_clientes = [
    "Como cliente, quero acompanhar o status do reparo do meu equipamento para saber em que etapa ele está (orçamento, conserto, pronto, etc.).",
    "Como utilizador gostava de poder ver o histórico das minhas compras.",
    "Como utilizador gostava de deixar uma avaliação sobre os produtos comprados.",
    "Como cliente gostaria de receber recibo.",
    "Como utilizador gostava de poder escolher o método de pagamento (cartão, PayPal, MB Way, etc.).",
    "Como utilizador gostava de receber um e-mail de confirmação da compra."
]

# ---------------------------------------
# User Stories – Administrador / Funcionário / Dono
# ---------------------------------------
user_stories_admin = [
    "Como funcionário, quero poder enviar os recibos dos produtos para facilitar o atendimento ao cliente.",
    "Como administrador gostava de visualizar os pedidos realizados por cada cliente.",
    "Como administrador gostava de aceder a relatórios de vendas e estatísticas.",
    "Como administrador gostava de definir descontos e promoções temporárias nos produtos.",
    "Como administrador gostava de gerir métodos de pagamento disponíveis no sistema.",
    "Como dono, quero poder definir permissões de acesso dos funcionários para controlar o que cada um pode fazer."
]

# Estrutura final tipo JSON
user_stories = {
    "clientes": [{"id": i+1, "descricao": desc} for i, desc in enumerate(user_stories_clientes)],
    "administrador": [{"id": i+1, "descricao": desc} for i, desc in enumerate(user_stories_admin)]
}

# Função para exportar para JSON (opcional)
def salvar_como_json(nome_arquivo="user_stories.json"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(user_stories, f, ensure_ascii=False, indent=4)
