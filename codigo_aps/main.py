# Bibliotecas
import random
import time
import os
import json
import funcoes
import mapa_campos

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
            dados_ordenados = funcoes.bubble_sort(dados_aleatorios)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_bubble = tempo_execucao

            funcoes.visualizar(tamanho_vetor, tempo_execucao, dados_ordenados)

        # Execução e Medição de Tempo Insertion Sort
        case 2:
            inicio = time.perf_counter()
            dados_ordenados = funcoes.insertion_sort(dados_aleatorios)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_insertion = tempo_execucao

            funcoes.visualizar(tamanho_vetor, tempo_execucao, dados_ordenados)

        # Execução e Medição de Tempo Quick Sort
        case 3:
            inicio = time.perf_counter()
            dados_ordenados = funcoes.quick_sort(dados_aleatorios) 
            fim = time.perf_counter()
            tempo_execucao = fim - inicio 
            tempo_quick = tempo_execucao

            funcoes.visualizar(tamanho_vetor, tempo_execucao, dados_ordenados)

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

                # Variável para armazenar a escolha de Parâmetro
                chave_busca = None

                # Menu Contextual
                print('''Qual será o Contexto Escolhido?: 
1. Satélite
2. Arcade
3. Spotify
4. Retornar
''')
                # Necessário para Definir qual Parâmetro será utilizado na Ordenação
                try:
                    escolha = int(input())

                    if escolha == 4:
                        break

                    if 1 <= escolha <= 3:
                        opcoes_campos = mapa_campos.campos_contexto[escolha]

                        # Menu para Escolha do Parâmetro (Variável "chave_busca" recebe Valor)
                        while True:
                            print("\nEscolha o parâmetro de ordenação desejado:")
                            for num, (nome_exibicao, _) in opcoes_campos.items():
                                print(f"{num}. {nome_exibicao}")

                            try:
                                opt_campo = int(input("\n"))

                                if opt_campo in opcoes_campos:
                                    # Pega o Nome Real do Campo no JSON
                                    chave_busca = opcoes_campos[opt_campo][1]
                                    break
                                else:
                                    print("\nParâmetro inválido! Escolha uma das opções da lista.")
                            except ValueError:
                                print("\nErro: Digite apenas números inteiros!")

                    else:
                        print("\nOpção inválida! Escolha um número de 1 a 4.")
                        continue

                    # Seleção do Arquivo pelo Usuário e sua Leitura por with open... json.load(f) + Tratamento de Exceção
                    diretorio_dado = os.path.dirname(os.path.abspath(__file__))
                    pasta_desordenados = os.path.join(diretorio_dado, "..", "pasta_dados_desordenados")
                    
                    nome_arquivo = input("\nDigite o nome do arquivo JSON (ex: jogadores_arcade.json): ")
                    if not nome_arquivo.endswith(".json"):
                        nome_arquivo += ".json"
                    
                    caminho_arquivo = os.path.join(pasta_desordenados, nome_arquivo)

                    with open(caminho_arquivo, "r", encoding = "utf-8") as f:
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
                        # Execução e Medição de Tempo Bubble Sort para Arquivo Externo
                        case 1:
                            inicio = time.perf_counter()
                            # Aqui se mostra o uso de key = lambda, para Recursão da Função com o uso da Variável "chave_busca".
                            dados_ordenados = funcoes.bubble_sort(dados_externos, key = lambda x: x[chave_busca])

                            # Inverte a Lista para ordená-la de forma Decrescente caso o Dado seja do tipo Inteiro ou de Ponto Flutuante
                            if dados_ordenados and isinstance(dados_ordenados[0][chave_busca], (int, float)):
                                dados_ordenados.reverse()

                            fim = time.perf_counter()
                            tempo_execucao = fim - inicio
                            tempo_bubble_ex = tempo_execucao

                            funcoes.tracar_caminho(caminho_arquivo, dados_ordenados, tempo_execucao)

                        case 2:
                            inicio = time.perf_counter()
                            # Aqui se mostra o uso de key = lambda, para Recursão da Função com o uso da Variável "chave_busca".
                            dados_ordenados = funcoes.insertion_sort(dados_externos, key = lambda x: x[chave_busca])

                            # Inverte a Lista para ordená-la de forma Decrescente caso o Dado seja do tipo Inteiro ou de Ponto Flutuante
                            if dados_ordenados and isinstance(dados_ordenados[0][chave_busca], (int, float)):
                                dados_ordenados.reverse()

                            fim = time.perf_counter()
                            tempo_execucao = fim - inicio
                            tempo_insertion_ex = tempo_execucao

                            funcoes.tracar_caminho(caminho_arquivo, dados_ordenados, tempo_execucao)

                        case 3:
                            inicio = time.perf_counter()
                            # Aqui se mostra o uso de key = lambda, para Recursão da Função com o uso da Variável "chave_busca".
                            dados_ordenados = funcoes.quick_sort(dados_externos, key = lambda x: x[chave_busca])

                            # Inverte a Lista para ordená-la de forma Decrescente caso o Dado seja do tipo Inteiro ou de Ponto Flutuante
                            if dados_ordenados and isinstance(dados_ordenados[0][chave_busca], (int, float)):
                                dados_ordenados.reverse()

                            fim = time.perf_counter()
                            tempo_execucao = fim - inicio
                            tempo_quick_ex = tempo_execucao

                            funcoes.tracar_caminho(caminho_arquivo, dados_ordenados, tempo_execucao)

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