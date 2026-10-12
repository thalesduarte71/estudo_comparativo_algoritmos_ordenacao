import json
import os
import random
from faker import Faker

fake = Faker('pt_BR')

qtd_dados = int(input("Digite quantos Dados deseja gerar: "))
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PASTA = os.path.join(DIRETORIO_ATUAL, "..", "pasta_dados_desordenados")
ARQUIVO_CAMINHO = os.path.join(CAMINHO_PASTA, "jogadores_arcade.json")

print(f"Iniciando a geração de {qtd_dados} dados...")

jogadores = []

for i in range (1, qtd_dados + 1):
    jogador = {
        "nome_jogador": fake.user_name(),
        "pontuacao": random.randint(0, 99999999),
        "tempo_partida_seg": random.randint(10, 3600),
        "venceu_partida": random.choice([True, False])
    }
    jogadores.append(jogador)

print("Gravando dados...")
with open(ARQUIVO_CAMINHO, "w", encoding="utf-8") as f:
    json.dump(jogadores, f, ensure_ascii = False, indent = 2)

print(f"Todos os {qtd_dados} dados foram gravados com sucesso em um arquivo .json!")