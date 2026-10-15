import json
import os
import random
from faker import Faker

# Inicializa a Biblioteca Faker para geração de Informações Fictícias
fake = Faker('pt_BR')

while True:
    try:
        qtd_dados = int(input("Digite quantos Dados de Satélite deseja gerar: "))

        if qtd_dados <= 0:
            print("Digite uma quantidade maior que zero.")
            continue
        break
        
    except ValueError:
        print("Digite apenas um número inteiro.")

# Declara a Constante "DIRETORIO_ATUAL" e a usa para navegar para a Pasta Anterior e adentrar na Pasta "pasta_dados_desordenados" esse caminho então fica armazenado na Constante "CAMINHO_PASTA", a partir dela declara o Caminho do Arquivo em "ARQUIVO_NOME" com o nome esperado "jogadores_arcade.json"
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PASTA = os.path.join(DIRETORIO_ATUAL, "..", "pasta_dados_desordenados")
ARQUIVO_NOME = os.path.join(CAMINHO_PASTA, "fotos_satelite_amazonia.json")

# Dicionário com a Localização de algumas das Cidades do Norte do Brasil
CIDADES = {
    "Manaus":      {"lat": (-4.09, -2.09), "long": (-61.06, -59.06)},
    "Belém":       {"lat": (-2.46, -0.46), "long": (-49.51, -47.51)},
    "Macapá":      {"lat": (-0.96, 1.04),  "long": (-52.06, -50.06)},
    "Boa Vista":   {"lat": (1.82, 3.82),   "long": (-61.67, -59.67)},
    "Rio Branco":  {"lat": (-10.97, -8.97),"long": (-68.81, -66.81)},
    "Porto Velho": {"lat": (-9.75, -7.75), "long": (-64.91, -62.91)},
    "Santarém":    {"lat": (-3.44, -1.44), "long": (-55.71, -53.71)},
    "Marabá":      {"lat": (-6.37, -4.37), "long": (-50.13, -48.13)},
}

# Função que verifica se a Localização fornecida pela Latitude e Longitude encontram-se em um Intervalo Coincidente com as Cidades no Dicionário
def verificar_local(lat, long):
    for nome, intervalo in CIDADES.items():
        lat_min, lat_max = intervalo["lat"]
        long_min, long_max = intervalo["long"]
        if lat_min <= lat <= lat_max and long_min <= long <= long_max:
            return nome
    return "Floresta Amazônica"

print(f"Iniciando a geração de {qtd_dados} dados...")

# Inicializa a Lista "fotos"
fotos = []

# Loop que Gera os Dados por meio da Biblioteca Faker e os Insere na Lista através de ".append" ao final de cada Loop
for i in range(1, qtd_dados + 1):
    lat = round(random.uniform(-9.0, 5.0), 5)
    long = round(random.uniform(-74.0, -44.0), 5)
    local = verificar_local(lat, long)

    foto = {
        "local": local,
        "hora": fake.date_time_between(start_date='-1y', end_date='now').strftime("%Y-%m-%d %H:%M:%S"),
        "latitude": lat,
        "longitude": long
    }
    fotos.append(foto)

print("Gravando dados...")

# Salva os Dados em um Novo Arquivo
with open(ARQUIVO_NOME, "w", encoding = "utf-8") as f:
    json.dump(fotos, f, ensure_ascii = False, indent = 2)

print(f"Todos os {qtd_dados} dados foram gravados com sucesso em um arquivo .json!")