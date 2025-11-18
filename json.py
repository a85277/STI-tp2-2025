import json
import os

FICHEIRO = "dados.json"

def carregar_db():
    if not os.path.exists(FICHEIRO):
        dados = {
            "clientes": {},
            "trabalhadores": {
                "andre": {"password": "martins", "role": "balcao"},
                "joao": {"password": "silva", "role": "tecnico"},
                "afonso": {"password": "martins", "role": "tecnico"}
            }
        }
        guardar_db(dados)
        return dados

    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_db(dados):
    with open(FICHEIRO, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar_cliente(username, password):
    dados = carregar_db()

    if username in dados["clientes"]:
        return False

    dados["clientes"][username] = password
    guardar_db(dados)
    return True


def login_cliente(username, password):
    dados = carregar_db()
    return username in dados["clientes"] and dados["clientes"][username] == password

def adicionar_trabalhador(username, password, role):
    dados = carregar_db()

    if username in dados["trabalhadores"]:
        return False

    dados["trabalhadores"][username] = {
        "password": password,
        "role": role
    }

    guardar_db(dados)
    return True


def remover_trabalhador(username):
    dados = carregar_db()

    if username not in dados["trabalhadores"]:
        return False

    del dados["trabalhadores"][username]
    guardar_db(dados)
    return True


def atualizar_password(username, nova_password):
    dados = carregar_db()

    if username not in dados["trabalhadores"]:
        return False

    dados["trabalhadores"][username]["password"] = nova_password
    guardar_db(dados)
    return True


def atualizar_role(username, novo_role):
    dados = carregar_db()

    if username not in dados["trabalhadores"]:
        return False

    dados["trabalhadores"][username]["role"] = novo_role
    guardar_db(dados)
    return True


def login_trabalhador(username, password):
    dados = carregar_db()

    if username not in dados["trabalhadores"]:
        return None

    if dados["trabalhadores"][username]["password"] == password:
        return dados["trabalhadores"][username]["role"]

    return None


def obter_trabalhadores():
    dados = carregar_db()
    return dados["trabalhadores"]