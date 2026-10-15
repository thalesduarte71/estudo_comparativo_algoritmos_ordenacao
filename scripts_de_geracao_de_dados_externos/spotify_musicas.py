import json
import os
import random
from faker import Faker

# Inicializa a Biblioteca Faker para geração de Informações Fictícias
fake = Faker('pt_BR')

# Listas para gerar Nomes de Músicas Fictícias (Faker não possui esse Recurso)
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

# Função para gerar os Nomes das Músicas
def gerar_nome_musica():
    sub = random.choice(SUBSTANTIVOS)
    adj = random.choice(ADJETIVOS)
    verbo = random.choice(VERBOS)
    extra = random.choice(EXTRA)
    nome = f"{adj} {sub} {verbo}"
    return f"{nome} ({extra})" if extra else nome

# Verificação para Quantidade Válida de Músicas
while True:
    try:
        dados = int(input("Selecione a quantidade de Músicas a serem Geradas: "))

        if dados <= 0:
            print("Digite uma quantidade maior que zero.")
            continue
        break

    except ValueError:
        print("Digite apenas um número inteiro.")

# Declara a Constante "DIRETORIO_ATUAL" e a usa para navegar para a Pasta Anterior e adentrar na Pasta "pasta_dados_desordenados" esse caminho então fica armazenado na Constante "CAMINHO_PASTA", a partir dela declara o Caminho do Arquivo em "NOME_ARQUIVO" com o nome esperado "jogadores_arcade.json"
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PASTA = os.path.join(DIRETORIO_ATUAL, "..", "pasta_dados_desordenados")
NOME_ARQUIVO = os.path.join(CAMINHO_PASTA, "musicas_geradas.json")

print(f"Iniciando a geração de {dados} músicas.")

# Inicializa a Lista "musicas"
musicas = []

# Loop que Gera os Dados por meio da Biblioteca Faker e os Insere na Lista através de ".append" ao final de cada Loop
for i in range(1, dados + 1):
    musica = {
        "nome_musica": gerar_nome_musica(),
        "artista": f"{fake.first_name()} {fake.last_name()}",
        "visualizacoes": min(
            int(random.expovariate(1 / 100_000)),
            999999999
        ),
        "data_lancamento": str(fake.date_between(start_date='-5y', end_date='today')),
    }
    musicas.append(musica)

print("Exportando dados...")

# Salva os Dados em um Novo Arquivo
with open(NOME_ARQUIVO, "w", encoding = "utf-8") as f:
    json.dump(musicas, f, ensure_ascii = False, indent = 2)

print(f"\nSuas {dados} músicas foram gravadas com sucesso!")
print(f"Arquivo: {NOME_ARQUIVO}")