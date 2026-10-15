import json
import os
import unicodedata
from mapa_campos import campos_contexto

# Função para extrair o Valor do Parâmetro escolhido e Normalizá-lo, vale destacar o uso de Tuplas em return ((0, valor) e (1, texto_normalizado), para evitar o erro que Python dá quando tenta comparar número com texto diretamente.
def extrair_chave_ordenacao(item, campo_escolhido): # "item" é de fato um Item Inteiro da Lista, "campo_escolhido" é o campo/parâmetro, como "pontuacao" por exemplo.
    valor = item[campo_escolhido]

    # Reconhece se o Parâmetro selecionado na Lista é Numérico
    if isinstance(valor, (int, float)):
        return (0, valor)

    # Reconhece se o Parâmetro selecionado na Lista é String(Caso tenho um número com "." na String, converte o número de String para Float, se não, para Inteiro)
    if isinstance(valor, str):
        try:
            if "." in valor:
                return (0, float(valor))
            return (0, int(valor))
        except ValueError:
            pass

    # Variável com o Texto Normalizado
    texto_normalizado = unicodedata.normalize('NFKD', str(valor)).casefold()
    return (1, texto_normalizado)

# O Core do Script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_desordenados = os.path.join(diretorio_atual, "..", "pasta_dados_desordenados")

# Validação do Contexto
while True:
    print('''\nEscolha o Contexto do Arquivo:
1. Satélite
2. Arcade
3. Spotify
''')
    
    try:
        contexto_escolhido = int(input("\nQual será o Contexto Escolhido?: "))
        if contexto_escolhido not in campos_contexto:
            print("\nContexto Inválido! Tente novamente.")
            continue
        break
    except ValueError:
        print("\nErro: Digite um Número Válido!")

campos_do_contexto = campos_contexto[contexto_escolhido] # "campos_contexto" é todo o Dicionário "mapa_campos" e "contexto_excolhido", o seu parâmetro

# Validação do Arquivo
while True:
    nome_arquivo = input("\nDigite o Nome do Arquivo JSON Base (ex: jogadores_arcade.json): ")
    if not nome_arquivo.endswith(".json"):
        nome_arquivo += ".json"
        
    caminho_entrada = os.path.join(pasta_desordenados, nome_arquivo)
    
    if not os.path.exists(caminho_entrada):
        print(f"\nErro: O Arquivo '{nome_arquivo}' não foi Encontrado na Pasta de Arquivos Desordenados! Tente novamente.")
        continue
    break

with open(caminho_entrada, "r", encoding="utf-8") as f:
    dados = json.load(f)
    
if not dados or not isinstance(dados, list):
    print("\nErro: O Arquivo JSON está Vazio ou não contém uma Lista Válida.")
    exit()

print("\nEscolha o Parâmetro de Ordenação Desejado:")
# "opcoes_chaves" Salva em formato de Lista as "chave_tecnica", onde os índices começam no 0, na prática fica: ["nome_jogador", "pontuacao", ...] 
opcoes_chaves = []
for idx, (nome, chave_tecnica) in campos_do_contexto.items():
    print(f"{idx}. {nome}")
    opcoes_chaves.append(chave_tecnica)

# É aqui que o Programa Seleciona o Campo de Acordo com a Escolha do Usuário
while True:
    try:
        escolha = int(input("\nEscolha o Campo: "))
        if not (1 <= escolha <= len(opcoes_chaves)):
            print("\nOpção Inválida! Tente novamente.")
            continue
        campo_escolhido = opcoes_chaves[escolha - 1]
        break
    except ValueError:
        print("\nErro: Digite um Número Válido!")

# Cálculo e Armazenamento do Percentual a ser Ordenado em Variável
while True:
    try:
        percentual = float(input("Digite a Porcentagem dos Dados que ficará Ordenada (ex: 0.7 para 70%): "))
        if not (0 < percentual < 1):
            print("\nO Valor deve estar entre 0 e 1 (ex: 0.5 para 50%). Tente novamente.")
            continue
        break
    except ValueError:
        print("\nErro: Digite um Número Válido para a Porcentagem!")

# Se Deseja Inverter a Ordem da Lista no Arquivo
while True:
    try:
        opcao_inverter = int(input('''Deseja Inverter a Ordem para Decrescente?
1. Sim
2. Não
\n'''))
        
        if opcao_inverter == 1:
            inverter = True
            break
        elif opcao_inverter == 2:
            inverter = False
            break
        else:
            print("\nOpção Inválida! Tente novamente.")
            
    except ValueError:
        print("\nErro: Digite um Número Válido!")

tamanho = len(dados)
corte = int(tamanho * percentual) # Variável utilizada para o Splicing(Selecionar os arquivos do início até o Número indicado por essa Variável)

# "parte_ordenada" usa Sorted para Ordenar desde o Início da Lista até o valor do "corte", key usa lambda para acessar a função de normalização "extrair_chave_ordenacao" e "reverse" define se Inverte ou não
parte_ordenada = sorted(dados[:corte], key = lambda x: extrair_chave_ordenacao(x, campo_escolhido), reverse = inverter)

# "parte_desordenada" pega desde o índice do "corte" até o Fim do Arquivo
parte_desordenada = dados[corte:]

# Concatenação das Duas Partes
dados_semi = parte_ordenada + parte_desordenada

# Gera/Salva o Arquivo
nome_saida = f"semi_{nome_arquivo}"
caminho_saida = os.path.join(pasta_desordenados, nome_saida)

with open(caminho_saida, "w", encoding="utf-8") as f:
    json.dump(dados_semi, f, ensure_ascii=False, indent=2)
    
print(f"\nSucesso! Arquivo Semi-Ordenado gerado com êxito como: {nome_saida}")