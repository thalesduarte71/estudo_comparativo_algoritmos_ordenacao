import json
import os
import string
import random

qtd_dados = int(input("Digite quantos Dados deseja gerar: "))
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_NOME = os.path.join(DIRETORIO_ATUAL, "jogadores_arcade.json")

print(f"Iniciando a geração de {qtd_dados} dados...")

jogadores = []

for i in range (1, qtd_dados + 1):
    sigla = "".join(random.choices(string.ascii_uppercase, k = 3))

    jogador = {
        "nome_jogador": sigla,
        "pontuacao": random.randint(0, 99999999),
        "tempo_partida_seg": random.randint(10, 3600),
        "venceu_partida": random.choice([True, False])
    }
    jogadores.append(jogador)

print("Gravando dados...")
with open(ARQUIVO_NOME, "w", encoding="utf-8") as f:
    json.dump(jogadores, f, ensure_ascii = False, indent = 2)

print(f"Todos os {qtd_dados} dados foram gravados com sucesso em um arquivo .json!")