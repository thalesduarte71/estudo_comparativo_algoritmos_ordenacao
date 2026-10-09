import json
import os
import random
from faker import Faker

fake = Faker('pt_BR')

SUBSTANTIVOS = ["Sol", "Lua", "Mar", "Fogo", "Chuva", "Vento", "Coração", "Estrela",
                "Noite", "Dia", "Rio", "Céu", "Flor", "Sombra", "Luz", "Caminho",
                "Sonho", "Silêncio", "Trovão", "Deserto"]

ADJETIVOS = ["Eterno", "Selvagem", "Dourado", "Silencioso", "Profundo", "Perdido",
             "Infinito", "Solitário", "Ardente", "Distante", "Sagrado", "Fugaz",
             "Imortal", "Sereno", "Intenso"]

VERBOS = ["Que Arde", "Que Chora", "Que Dança", "Que Voa", "Que Grita", "Que Sonha",
          "Que Brilha", "Que Chega", "Que Parte", "Que Fica"]

EXTRA = ["Ao Vivo", "Remix", "Versão Acústica", "Remasterizado", "Instrumental",
         "Edição Especial", "No Verão", "À Meia-Noite", "Reinterpretação", ""]


def gerar_nome_musica():
    sub = random.choice(SUBSTANTIVOS)
    adj = random.choice(ADJETIVOS)
    verbo = random.choice(VERBOS)
    extra = random.choice(EXTRA)
    nome = f"{adj} {sub} {verbo}"
    return f"{nome} ({extra})" if extra else nome


while True:
    try:
        dados = int(input("Selecione a quantidade de músicas: "))

        if dados <= 0:
            print("Digite uma quantidade maior que zero.")
            continue

        break

    except ValueError:
        print("Digite apenas um número inteiro.")

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PASTA = os.path.join(DIRETORIO_ATUAL, "..", "pasta_dados_desordenados")
NOME_ARQUIVO = os.path.join(CAMINHO_PASTA, "musicas_geradas.json")

print(f"Iniciando a geração de {dados} músicas.")

musicas = []

for i in range(1, dados + 1):
    musica = {
        "nome_musica": gerar_nome_musica(),
        "Artista": f"{fake.first_name()} {fake.last_name()}",
        "Visualizações": min(
            int(random.expovariate(1 / 100_000)),
            999999999
        ),
        "Data_lancamento": str(fake.date_between(start_date='-5y', end_date='today')),
    }
    musicas.append(musica)

print("Exportando dados...")
with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
    json.dump(musicas, f, ensure_ascii=False, indent=2)

print(f"\nSuas {dados} músicas foram gravadas com sucesso!")
print(f"Arquivo: {NOME_ARQUIVO}")