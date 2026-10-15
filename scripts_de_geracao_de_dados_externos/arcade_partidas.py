import json
import os
import random
from faker import Faker

# Inicializa a Biblioteca Faker para geração de Informações Fictícias
fake = Faker('pt_BR')

while True:
    try:
        qtd_dados = int(input("Digite quantos Dados de Arcade deseja gerar: "))

        if qtd_dados <= 0:
            print("Digite uma quantidade maior que zero.")
            continue
        break
        
    except ValueError:
        print("Digite apenas um número inteiro.")

# Declara a Constante "DIRETORIO_ATUAL" e a usa para navegar para a Pasta Anterior e adentrar na Pasta "pasta_dados_desordenados" esse caminho então fica armazenado na Constante "CAMINHO_PASTA", a partir dela declara o Caminho do Arquivo em "NOME_DO_ARQUIVO" com o nome esperado "jogadores_arcade.json"
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PASTA = os.path.join(DIRETORIO_ATUAL, "..", "pasta_dados_desordenados")
NOME_DO_ARQUIVO = os.path.join(CAMINHO_PASTA, "jogadores_arcade.json")

print(f"Iniciando a geração de {qtd_dados} dados...")

# Inicializa a Lista "jogadores"
jogadores = []

# Loop que Gera os Dados por meio da Biblioteca Faker e os Insere na Lista através de ".append" ao final de cada Loop
for i in range (1, qtd_dados + 1):
    jogador = {
        "nome_jogador": fake.user_name(),
        "pontuacao": random.randint(0, 99999999),
        "tempo_partida_seg": random.randint(10, 3600),
        "venceu_partida": random.choice([True, False])
    }
    jogadores.append(jogador)

print("Gravando dados...")

# Salva os Dados em um Novo Arquivo
with open(NOME_DO_ARQUIVO, "w", encoding = "utf-8") as f:
    json.dump(jogadores, f, ensure_ascii = False, indent = 2)

print(f"Todos os {qtd_dados} dados foram gravados com sucesso em um arquivo .json!")