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
def insertion_sort(lista):
    n = len(lista)
    arr = lista.copy()
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr
 
# X. Função de Algoritmo de Ordenação Quick Sort
# ------

# 2. Geração de Dados Aleatórios Internos + Menu
while True:
    print("="*30)
    print("MENU DE ORDENAÇÃO")
    print("="*30)
    print('''Escolha um dos três Algoritmos de Ordenação ou saia do Programa: 
1. Bubble Sort
2. Insertion Sort
3. Quick Sort (Ainda a ser desenvolvido)
4. Sair do Programa''')

    try:
        opcao = int(input())

        if opcao == 4:
            print("\nEncerrando o programa...")
            break

        if opcao <= 0 or opcao > 4:
            print("\nOpção inválida, escolha um número entre 1 e 4.")
            continue

        tamanho_vetor = int(input("\nDigite um número inteiro positivo para definir a quantidade de dados a ser gerada: "))

        if tamanho_vetor <= 0:
            print("\nA quantidade de dados deve ser maior que zero!")
            continue

    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros!")
        continue

        
    # 3. Execução e Medição de Tempo Isolada Bubble Sort + Tratamento de Exceção
    match opcao:
        case 1:
            if tamanho_vetor > 0:
                dados_aleatorios = random.choices(range(1, 1000000), k=tamanho_vetor)

                inicio = time.perf_counter()
                dados_ordenados = bubble_sort(dados_aleatorios)
                fim = time.perf_counter()
                tempo_execucao = fim - inicio

                print("\n")
                print("-" * 50)
                print("[Visualização dos Dados Ordenados]")
                print("-" * 50)
                print(f"Quantidade de dados: {tamanho_vetor}")
                print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
                print(f"Ordem dos primeiros 10 dados: {dados_ordenados[:10]}")
                print(f"Ordem dos últimos 10 dados: {dados_ordenados[-10:]}\n")

            else:
                print("A quantidade de dados a ser gerada deve ser maior que zero! Por favor, execute o programa novamente com o valor correto.")

        case 2:
            if tamanho_vetor > 0:
                dados_aleatorios = random.choices(range(1, 1000000), k=tamanho_vetor)

                inicio = time.perf_counter()
                dados_ordenados = insertion_sort(dados_aleatorios)
                fim = time.perf_counter()
                tempo_execucao = fim - inicio

                print("\n")
                print("-" * 50)
                print("[Visualização dos Dados Ordenados]")
                print("-" * 50)
                print(f"Quantidade de dados: {tamanho_vetor}")
                print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
                print(f"Ordem dos primeiros 10 dados: {dados_ordenados[:10]}")
                print(f"Ordem dos últimos 10 dados: {dados_ordenados[-10:]}\n")

            else:
                print("A quantidade de dados a ser gerada deve ser maior que zero! Por favor, execute o programa novamente com o valor correto.")
        case 3:
            print("Quick Sort ainda está sendo desenvolvido.")