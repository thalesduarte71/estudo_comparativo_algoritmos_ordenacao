import os
import json
import unicodedata

# Para organizar por Ordem Alfabética sem conflito de Acentuação
def normalizar_texto(texto):
    if isinstance(texto, str):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').casefold()
    return texto

# Escolha da Ordem de Ordenação
def escolher_ordem():
    while True:
        try:
            print("\nEscolha a ordem de ordenação:")
            print("1. Crescente")
            print("2. Decrescente")
            opcao_ordem = int(input())
            
            if opcao_ordem == 1:
                return False # Não é decrescente
            elif opcao_ordem == 2:
                return True  # É decrescente
            else:
                print("\nOpção inválida! Escolha 1 ou 2.")
        except ValueError:
            print("\nErro: Digite apenas números inteiros!")

# Função de Algoritmo de Ordenação Bubble Sort
def bubble_sort(lista, key = lambda x: x):
    # Uma Lista Dinâmica em Python, mas a gente chama de Array pois ele vai se comportar como um nesse programa
    n = len(lista)
    # Cria uma cópia para não alterar o vetor original na memória
    arr = lista.copy() 
    for i in range(n):
        # O 'n - i - 1' evita comparar os elementos que já foram "flutuados" para o fim da lista
        for j in range(0, n - i - 1):
            # Se o elemento atual for maior que o próximo, eles trocam de posição
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Função de Algoritmo de Ordenação Insertion Sort
def insertion_sort(lista, key = lambda x: x):
    n = len(lista)
    arr = lista.copy()
    for i in range(1, len(arr)): # Começa-se a Leitura a partir do segundo elemento, de índice 1
        chave = arr[i]
        j = i - 1
        # Compara-se o Valor Chave com os Valores à sua esquerda, verificando se é maior ou menor, o que for maior, desloca-se para a direita, abrindo espaço para inserir a chave na posição correta depois.
        while j >= 0 and key(arr[j]) > key(chave):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr
 
# Função de Algoritmo de Ordenação Quick Sort
def quick_sort (lista, key = lambda x: x):
    # Caso base da recursão: se a lista tiver 0 ou 1 elemento, ela já está ordenada
    if len(lista) <=1:
        return lista
    # Escolhe o elemento central da lista como o Pivô para dividir o problema
    pivo = lista[len(lista)//2]
    # Particionamento: divide a lista em três sublistas baseadas na comparação com o pivô
    menores = [x for x in lista if key(x) < key(pivo)]
    iguais = [x for x in lista if key(x) == key(pivo)]
    maiores = [x for x in lista if key(x) > key(pivo)]
    # Conquista e Combinação: ordena recursivamente as sublistas e junta os resultados com os iguais no meio
    return quick_sort(menores, key) + iguais + quick_sort(maiores, key)

# Função para Visualização de Dados
def visualizar(tamanho_vetor, tempo_execucao, dados_ordenados):
    print("\n")
    print("-" * 50)
    print("[Visualização dos Dados Ordenados]")
    print("-" * 50)
    print(f"Quantidade de dados: {tamanho_vetor}")
    print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
    print(f"Ordem dos primeiros(até 10) dados: {dados_ordenados[:10]}")
    print(f"Ordem dos últimos(até 10) dados: {dados_ordenados[-10:]}\n")
    
# Define o Nome e Caminho do Novo Arquivo de Dados Ordenados    
def tracar_caminho(caminho_arquivo, dados_ordenados, tempo_execucao):
    pasta_origem = os.path.dirname(os.path.abspath(caminho_arquivo))
    nome_arquivo_original = os.path.basename(caminho_arquivo)
    nome_base, extensao = os.path.splitext(nome_arquivo_original)

    pasta_destino = os.path.join(pasta_origem, "..", "pasta_dados_ordenados")

    # Garante que a pasta de destino existe
    os.makedirs(pasta_destino, exist_ok = True)

    # Nome base inicial de saída
    nome_arquivo_saida = f"{nome_base}_ordenado{extensao}"
    caminho_saida = os.path.join(pasta_destino, nome_arquivo_saida)

    # Controle de versão seguro: se o arquivo já existe, incrementa um contador
    contador = 1
    while os.path.exists(caminho_saida):
        nome_arquivo_saida = f"{nome_base}_ordenado_{contador}{extensao}"
        caminho_saida = os.path.join(pasta_destino, nome_arquivo_saida)
        contador += 1

    # Salva os dados no novo caminho seguro
    with open(caminho_saida, "w", encoding = "utf-8") as f:
        json.dump(dados_ordenados, f, ensure_ascii = False, indent = 2)

    print(f"\nSucesso! Arquivo ordenado salvo em: {caminho_saida}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos\n")