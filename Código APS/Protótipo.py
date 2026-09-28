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

# 2. Função de Algoritmo de Ordenação Insertion Sort
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
 
# 3. Função de Algoritmo de Ordenação Quick Sort
def quick_sort (lista):
    if len(lista) <=1:
        return lista
    pivo = lista[len(lista)//2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

# 4. Geração de Dados Aleatórios Internos
while True:
    try:
        tamanho_vetor = int(input("\nDigite um número inteiro positivo para definir a quantidade de dados a ser gerada: "))
        if tamanho_vetor <= 0:
            print("\nA quantidade de dados deve ser maior que zero!")
            continue
        break
    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros.")

print(f"Gerando dados aleatórios em um vetor de {tamanho_vetor} valores.")
dados_aleatorios = random.choices(range(1, 1000000), k=tamanho_vetor)

# 5. variavéis para Comparação Futura de Tempos de Ordenação
tempo_bubble = None
tempo_insertion = None
tempo_quick = None

# 6. Menu de Execução    
while True:
    print("="*30)
    print("MENU DE ORDENAÇÃO")
    print("="*30)
    print('''Escolha um dos três Algoritmos de Ordenação ou saia do Programa: 
1. Bubble Sort
2. Insertion Sort
3. Quick Sort
4. Comparar Tempo
5. Sair do Programa''')

    try:
        opcao = int(input())

        if opcao == 5:
            print("\nEncerrando o programa...")
            break

        if opcao <= 0 or opcao > 5:
            print("\nOpção inválida, escolha um número de 1 a 5.")
            continue

    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros!")
        continue


    match opcao:
    # 7. Execução e Medição de Tempo Bubble Sort
        case 1:
            inicio = time.perf_counter()
            dados_ordenados = bubble_sort(dados_aleatorios)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_bubble = tempo_execucao

            print("\n")
            print("-" * 50)
            print("[Visualização dos Dados Ordenados]")
            print("-" * 50)
            print(f"Quantidade de dados: {tamanho_vetor}")
            print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
            print(f"Ordem dos primeiros(até 10) dados: {dados_ordenados[:10]}")
            print(f"Ordem dos últimos(até 10) dados: {dados_ordenados[-10:]}\n")

    # 8. Execução e Medição de Tempo Insertion Sort
        case 2:
            inicio = time.perf_counter()
            dados_ordenados = insertion_sort(dados_aleatorios)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_insertion = tempo_execucao

            print("\n")
            print("-" * 50)
            print("[Visualização dos Dados Ordenados]")
            print("-" * 50)
            print(f"Quantidade de dados: {tamanho_vetor}")
            print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
            print(f"Ordem dos primeiros(até 10) dados: {dados_ordenados[:10]}")
            print(f"Ordem dos últimos(até 10) dados: {dados_ordenados[-10:]}\n")

    # 9. Execução e Medição de Tempo Quick Sort
        case 3:
            inicio = time.perf_counter()
            dados_ordenados = quick_sort(dados_aleatorios) 
            fim = time.perf_counter()
            tempo_execucao = fim - inicio 
            tempo_quick = tempo_execucao

            print("\n")
            print("-" * 50)
            print("[Visualização dos Dados Ordenados]")
            print("-" * 50)
            print(f"Quantidade de dados: {tamanho_vetor}")
            print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
            print(f"Ordem dos primeiros(até 10) dados: {dados_ordenados[:10]}")
            print(f"Ordem dos últimos(até 10) dados: {dados_ordenados[-10:]}\n")

    # 10. Comparação Tempo de Ordenação 
        case 4:
            print("\n" + "-" * 50)
            print("COMPARAÇÃO DOS TEMPOS DE EXECUÇÃO")
            print("-" * 50)

            if tempo_bubble is not None:
                print(f"Bubble Sort: {tempo_bubble:.6f} segundos")
            else:
                print("Bubble Sort: Ainda não executado")

            if tempo_insertion is not None:
                print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
            else:
                print("Insertion Sort: Ainda não executado")

            if tempo_quick is not None:
                print(f"Quick Sort: {tempo_quick:.6f} segundos")
            else:
                print("Quick Sort: Ainda não executado")

            print("\n")