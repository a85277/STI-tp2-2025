import json
import os
import random

FICHEIRO = "dados.json"
def carregar_db():
    if not os.path.exists(FICHEIRO):
        dados = {
            "estoque": {},
            "fotos": {},
            "historico": {},
            "carrinhos": {},
            "2fa": {}
        }
        guardar_db(dados)
        return dados

    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_db(dados):
    with open(FICHEIRO, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar_produto(nome, preco, qtd, categoria="", marca="", tamanho="", cor="", disponivel=True):
    dados = carregar_db()
    dados["estoque"][nome] = {
        "preco": preco,
        "quantidade": qtd,
        "categoria": categoria,
        "marca": marca,
        "tamanho": tamanho,
        "cor": cor,
        "disponivel": disponivel
    }
    guardar_db(dados)

def atualizar_estoque(nome, qtd_delta):
    dados = carregar_db()
    if nome in dados["estoque"]:
        dados["estoque"][nome]["quantidade"] += qtd_delta
        guardar_db(dados)
        return True
    return False


def filtrar_produtos(categoria=None, preco_max=None, marca=None, tamanho=None, cor=None, disponivel=None):
    dados = carregar_db()
    resultados = []

    for nome, p in dados["estoque"].items():
        if categoria and p["categoria"] != categoria:
            continue
        if preco_max and p["preco"] > preco_max:
            continue
        if marca and p["marca"] != marca:
            continue
        if tamanho and p["tamanho"] != tamanho:
            continue
        if cor and p["cor"] != cor:
            continue
        if disponivel is not None and p["disponivel"] != disponivel:
            continue

        resultados.append((nome, p))

    return resultados


def anexar_foto(produto, foto_nome):
    dados = carregar_db()

    if produto not in dados["fotos"]:
        dados["fotos"][produto] = []

    dados["fotos"][produto].append(foto_nome)
    guardar_db(dados)


def registrar_evento(evento):
    dados = carregar_db()

    if "global" not in dados["historico"]:
        dados["historico"]["global"] = []

    dados["historico"]["global"].append(evento)
    guardar_db(dados)

def obter_historico():
    dados = carregar_db()
    return dados["historico"].get("global", [])


def adicionar_carrinho(cliente, produto, qtd=1):
    dados = carregar_db()

    if cliente not in dados["carrinhos"]:
        dados["carrinhos"][cliente] = {}

    dados["carrinhos"][cliente][produto] = dados["carrinhos"][cliente].get(produto, 0) + qtd
    guardar_db(dados)

def finalizar_compra(cliente, endereco, pagamento):
    dados = carregar_db()

    if cliente not in dados["carrinhos"] or not dados["carrinhos"][cliente]:
        return False, "Carrinho vazio."

    total = 0

    for produto, qtd in dados["carrinhos"][cliente].items():
        preco = dados["estoque"][produto]["preco"]
        total += preco * qtd

        dados["estoque"][produto]["quantidade"] -= qtd

    registrar_evento(f"Cliente {cliente} finalizou compra. Total: {total}€.")

    dados["carrinhos"][cliente] = {}
    guardar_db(dados)

    return True, total

def gerar_2fa(cliente):
    dados = carregar_db()
    codigo = str(random.randint(100000, 999999))
    dados["2fa"][cliente] = codigo
    guardar_db(dados)
    return codigo

def validar_2fa(cliente, codigo):
    dados = carregar_db()
    return dados["2fa"].get(cliente) == codigo
