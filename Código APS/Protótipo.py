# Bibliotecas
import random
import time
import os
import json

# Função de Algoritmo de Ordenação Bubble Sort
def bubble_sort(lista):
    # Uma Lista Dinâmica em Python, mas a gente chama de Array pois ele vai se comportar como um nesse programa
    n = len(lista)
    # Cria uma cópia para não alterar o vetor original na memória
    arr = lista.copy() 
    for i in range(n):
        # O 'n - i - 1' evita comparar os elementos que já foram "flutuados" para o fim da lista
        for j in range(0, n - i - 1):
            # Se o elemento atual for maior que o próximo, eles trocam de posição
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Função de Algoritmo de Ordenação Insertion Sort
def insertion_sort(lista):
    n = len(lista)
    arr = lista.copy()
    for i in range(1, len(arr)): # Começa-se a Leitura a partir do segundo elemento, de índice 1
        chave = arr[i]
        j = i - 1
        # Compara-se o Valor Chave com os Valores à sua esquerda, verificando se é maior ou menor, o que for maior, desloca-se para a direita, abrindo espaço para inserir a chave na posição correta depois.
        while j >= 0 and arr[j] > chave:
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
def visualizar():
    print("\n")
    print("-" * 50)
    print("[Visualização dos Dados Ordenados]")
    print("-" * 50)
    print(f"Quantidade de dados: {tamanho_vetor}")
    print(f"Tempo de ordenação: {tempo_execucao:.6f} segundos")
    print(f"Ordem dos primeiros(até 10) dados: {dados_ordenados[:10]}")
    print(f"Ordem dos últimos(até 10) dados: {dados_ordenados[-10:]}\n")

# Geração de Dados Aleatórios Internos
while True:
    try:
        tamanho_vetor = int(input("\nDigite um número inteiro positivo para definir a quantidade de dados a ser gerada: "))
        if tamanho_vetor <= 0:
            print("\nA quantidade de dados deve ser maior que zero!")
            continue
        break
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.\n")

print(f"Dados aleatórios em um vetor de {tamanho_vetor} valores gerados com êxito.\n")
dados_aleatorios = random.choices(range(1, 1000000), k=tamanho_vetor)

# Variavéis para Comparação Futura de Tempos de Ordenação
tempo_bubble = None
tempo_insertion = None
tempo_quick = None

# Menu de Execução    
while True:
    print("="*50)
    print("MENU DE ORDENAÇÃO")
    print("="*50)
    print('''Escolha um dos três Algoritmos de Ordenação, selecione um Arquivo Externo ou Saia do Programa: 
1. Bubble Sort
2. Insertion Sort
3. Quick Sort
4. Comparar Tempo
5. Selecionar Arquivo .json Externo
6. Sair do Programa
''')

    try:
        opcao = int(input())

        if opcao == 6:
            print("Encerrando o programa...")
            break

        if opcao <= 0 or opcao > 6:
            print("Opção inválida, escolha um número de 1 a 6.")
            continue

    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros!")
        continue


    match opcao:
        # Execução e Medição de Tempo Bubble Sort
        case 1:
            inicio = time.perf_counter()
            dados_ordenados = bubble_sort(dados_aleatorios)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_bubble = tempo_execucao

            visualizar()

        # Execução e Medição de Tempo Insertion Sort
        case 2:
            inicio = time.perf_counter()
            dados_ordenados = insertion_sort(dados_aleatorios)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_insertion = tempo_execucao

            visualizar()

        # Execução e Medição de Tempo Quick Sort
        case 3:
            inicio = time.perf_counter()
            dados_ordenados = quick_sort(dados_aleatorios) 
            fim = time.perf_counter()
            tempo_execucao = fim - inicio 
            tempo_quick = tempo_execucao

            visualizar()

        # Comparação entre os Tempos de Ordenação
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

        # Leitura e Ordenação de Arquivo Externo por Contexto
        case 5:
            # Escolha do Contexto para Arquivo Externo
            while True:
                # Variavéis para Comparação Futura de Tempos de Ordenação para Arquivo Externo
                tempo_bubble_ex = None
                tempo_insertion_ex = None
                tempo_quick_ex = None

                chave_busca = None
                print('''Qual será o Contexto Escolhido?: 
1. Satélite
2. Arcade
3. Spotify
4. Retornar
''')
                # Necessário para definir qual Parâmetro será utilizado na Ordenação
                try:
                    escolha = int(input())
                    if escolha == 4:
                        break
                    if escolha == 1:
                        chave_busca = "---"
                    elif escolha == 2:
                        chave_busca = "pontuacao"
                    elif escolha == 3:
                        chave_busca = "---"
                    else:
                        print("\nOpção inválida! Escolha de 1 a 4.")
                        continue

                    # Seleção do Arquivo pelo Usuário e sua Leitura por with open... json.load(f) + Tratamento de Exceção
                    caminho_arquivo = input("Digite o caminho do arquivo JSON (ex: jogadores_arcade.json): ")

                    with open(caminho_arquivo, "r", encoding="utf-8") as f:
                        dados_externos = json.load(f)

                    print("\nArquivo carregado com sucesso!")

                except ValueError:
                    print("\nErro: Digite apenas números inteiros!")
                    continue
                except FileNotFoundError:
                    print("\nErro: Arquivo não encontrado! Verifique o caminho digitado.")
                    continue

                # Menu de Execução para Arquivo Externo
                while True:
                    print("\n")
                    print("="*50)
                    print("MENU DE ORDENAÇÃO PARA ARQUIVO EXTERNO")
                    print("="*50)
                    print('''Escolha um dos três Algoritmos de Ordenação ou Retorne: 
1. Bubble Sort
2. Insertion Sort
3. Quick Sort
4. Comparar Tempo
5. Retornar
''')
                    
                    try:
                        opcao_ex = int(input())
                
                        if opcao_ex == 5:
                            break
                
                        if opcao_ex <= 0 or opcao_ex > 5:
                            print("\nOpção inválida, escolha um número de 1 a 5.")
                            continue
                
                    except ValueError:
                        print("\nErro: Por favor, digite apenas números inteiros!")
                        continue


                    match opcao_ex:
                        # Execução e Medição de Tempo Quick Sort para Arquivo Externo
                        case 3:
                            inicio = time.perf_counter()
                            # Aqui se mostra o uso de key = lambda, para Recursão da Função.
                            dados_ordenados = quick_sort(dados_externos, key = lambda x: x[chave_busca])
                            # Inverte a Lista para ordená-la de forma Decrescente
                            dados_ordenados.reverse()
                            fim = time.perf_counter()
                            tempo_execucao = fim - inicio
                            tempo_quick_ex = tempo_execucao

                            pasta_origem = os.path.dirname(os.path.abspath(caminho_arquivo))
                            nome_arquivo_original = os.path.basename(caminho_arquivo)
                            nome_base, extensao = os.path.splitext(nome_arquivo_original)
                            nome_arquivo_saida = f"{nome_base}_ordenado{extensao}"
                            caminho_saida = os.path.join(pasta_origem, nome_arquivo_saida)

                            with open(caminho_saida, "w", encoding="utf-8") as f:
                                json.dump(dados_ordenados, f, ensure_ascii = False, indent = 2)

                            print(f"\nSucesso! Arquivo ordenado salvo em: {caminho_saida}")
                            print(f"Tempo de execução: {tempo_execucao:.6f} segundos\n")

                        # Comparação entre os Tempos de Ordenação para Arquivo Externo
                        case 4:
                            print("\n" + "-" * 50)
                            print("COMPARAÇÃO DOS TEMPOS DE EXECUÇÃO")
                            print("-" * 50)
                
                            if tempo_bubble_ex is not None:
                                print(f"Bubble Sort: {tempo_bubble_ex:.6f} segundos")
                            else:
                                print("Bubble Sort: Ainda não executado")
                
                            if tempo_insertion_ex is not None:
                                print(f"Insertion Sort: {tempo_insertion_ex:.6f} segundos")
                            else:
                                print("Insertion Sort: Ainda não executado")
                
                            if tempo_quick_ex is not None:
                                print(f"Quick Sort: {tempo_quick_ex:.6f} segundos")
                            else:
                                print("Quick Sort: Ainda não executado")
                
                            print("\n")