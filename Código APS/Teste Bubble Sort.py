import random
import time

# 1. Função de Algoritmo de Ordenação Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    # Cria uma cópia para não alterar o vetor original na memória
    arr = lista.copy() # Uma Lista Dinâmica em Python, mas a gente chama de Array pois ele vai se comportar como um nesse programa
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# X. Função de Algoritmo de Ordenação Insertion Sort
# ------
# X. Função de Algoritmo de Ordenação Quick Sort
# ------

# 2. Geração de Dados Aleatórios Internos
tamanho_vetor = int(input("Digite um número inteiro positivo para definir a quantidade de dados a ser gerada: "))

# 3. Execução e Medição de Tempo Isolada
if tamanho_vetor > 0:
    dados_aleatorios = random.sample(range(1, 1000000), tamanho_vetor)

    inicio = time.perf_counter()
    dados_ordenados = bubble_sort(dados_aleatorios)
    fim = time.perf_counter()
    tempo_execucao = fim - inicio

    print(f"\nQuantidade de dados: {tamanho_vetor}")
    print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")

    print("-" * 50)
    print("[Visualização dos Dados Ordenados]")
    print("-" * 50, "\n")

    print(f"Ordem dos primeiros 10 dados: {dados_ordenados[:10]}")
    print(f"Ordem dos últimos 10 dados: {dados_ordenados[-10:]}")

# 4. Tratamento de Exceção
else:
    print("A quantidade de dados a ser gerada deve ser maior que zero! Por favor, execute o programa novamente com o valor correto.")

