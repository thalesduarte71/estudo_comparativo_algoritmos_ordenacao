import json
import os
import unicodedata
from mapa_campos import campos_contexto

def chave_inteligente(item, campo_escolhido):
    valor = item[campo_escolhido]
    
    if isinstance(valor, (int, float)):
        return (0, valor)
        
    if isinstance(valor, str):
        try:
            if "." in valor:
                return (0, float(valor))
            return (0, int(valor))
        except ValueError:
            pass
            
    texto_normalizado = unicodedata.normalize('NFKD', str(valor)).casefold()
    return (1, texto_normalizado)

def gerar_semi_ordenado():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    pasta_desordenados = os.path.join(diretorio_atual, "..", "pasta_dados_desordenados")
    
    print("\nEscolha o Contexto do Arquivo:")
    print("1. Satélite")
    print("2. Arcade")
    print("3. Spotify")
    
    try:
        contexto_escolhido = int(input("\nQual será o Contexto Escolhido?: "))
        if contexto_escolhido not in campos_contexto:
            print("\nContexto Inválido!")
            return
    except ValueError:
        print("\nErro: Digite um Número Válido!")
        return

    campos_do_contexto = campos_contexto[contexto_escolhido]

    nome_arquivo = input("\nDigite o Nome do Arquivo JSON Base (ex: jogadores_arcade.json): ")
    if not nome_arquivo.endswith(".json"):
        nome_arquivo += ".json"
        
    caminho_entrada = os.path.join(pasta_desordenados, nome_arquivo)
    
    if not os.path.exists(caminho_entrada):
        print(f"\nErro: O Arquivo '{nome_arquivo}' não foi Encontrado na Pasta de Arquivos Desordenados!")
        return

    with open(caminho_entrada, "r", encoding="utf-8") as f:
        dados = json.load(f)
        
    if not dados or not isinstance(dados, list):
        print("\nErro: O Arquivo JSON está Vazio ou não contém uma Lista Válida.")
        return

    print("\nEscolha o Parâmetro de Ordenação Desejado:")
    opcoes_chaves = []
    for idx, (nome_amigavel, chave_tecnica) in campos_do_contexto.items():
        print(f"{idx}. {nome_amigavel}")
        opcoes_chaves.append(chave_tecnica)
        
    try:
        escolha = int(input("\nEscolha o Número do Campo: "))
        if not (1 <= escolha <= len(opcoes_chaves)):
            print("\nOpção Inválida!")
            return
        campo_escolhido = opcoes_chaves[escolha - 1]
    except ValueError:
        print("\nErro: Digite um Número Válido!")
        return

    try:
        percentual = float(input("Digite a Porcentagem dos Dados que ficará Ordenada (ex: 0.7 para 70%): "))
        if not (0 < percentual < 1):
            print("\nO Valor deve estar entre 0 e 1 (ex: 0.5 para 50%).")
            return
    except ValueError:
        print("\nErro: Digite um Número Válido para a Porcentagem!")
        return

    try:
        opcao_inverter = int(input('''Deseja Inverter a Ordem para Decrescente?
1. Sim
2. Não
\n'''))
        
        if opcao_inverter == 1:
            inverter = True
        elif opcao_inverter == 2:
            inverter = False
        else:
            print("\nOpção Inválida! Assumindo Ordem Crescente (Não).")
            inverter = False
            
    except ValueError:
        print("\nErro: Digite um Número Válido! Assumindo Ordem Crescente (Não).")
        inverter = False

    print(f"\nProcessando... Ordenando Parcialmente pelo Campo '{campo_escolhido}' ({int(percentual*100)}%)...")
    
    tamanho = len(dados)
    corte = int(tamanho * percentual)
    
    parte_ordenada = sorted(dados[:corte], key=lambda x: chave_inteligente(x, campo_escolhido), reverse=inverter)
    parte_desordenada = dados[corte:]
    
    dados_semi = parte_ordenada + parte_desordenada
    
    nome_saida = f"semi_{nome_arquivo}"
    caminho_saida = os.path.join(pasta_desordenados, nome_saida)
    
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(dados_semi, f, ensure_ascii=False, indent=2)
        
    print(f"\nSucesso! Arquivo Semi-Ordenado gerado com êxito como: {nome_saida}")

if __name__ == "__main__":
    gerar_semi_ordenado()