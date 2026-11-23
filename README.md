# Análise de Performance de Algoritmos de Ordenação
Aplicação desenvolvida em Python para estudar e comparar o desempenho de três algoritmos de ordenação: Bubble Sort, Insertion Sort e Quick Sort. 

O sistema processa dados gerados internamente ou carregados de arquivos JSON, mede o tempo gasto exclusivamente na ordenação e permite comparar os resultados pelo terminal.

O projeto foi desenvolvido como Atividade Prática Supervisionada (APS) do curso de Ciência da Computação.

## Objetivos
- Implementar três algoritmos clássicos de ordenação.
- Comparar seus tempos de execução.
- Avaliar o comportamento com diferentes volumes de dados.
- Trabalhar com dados aleatórios, ordenados e semiordenados.
- Processar registros externos em formato JSON.

## Funcionalidades
- Ordenação interna: geração de vetores com valores inteiros aleatórios.
- Ordenação de arquivos: leitura de conjuntos de dados JSON.
- Três algoritmos: execução de Bubble Sort, Insertion Sort e Quick Sort.
- Ordem configurável: classificação crescente ou decrescente.
- Campos configuráveis: seleção do atributo usado na ordenação dos registros.
- Medição de desempenho: cronometragem com `time.perf_counter()`.
- Comparação: exibição dos tempos registrados para cada algoritmo.
- Exportação: gravação dos registros ordenados em `pasta_dados_ordenados`.
- Dados de teste: scripts para gerar conjuntos fictícios e arquivos semiordenados.

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso |
| :--- | :--- | :--- | :--- |
| Bubble Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |   


**OBS:** A implementação de Bubble Sort não possui interrupção antecipada quando uma passagem não realiza trocas. Por isso, mantém complexidade O(n²), inclusive para entradas já ordenadas.

## Contextos de Dados
O sistema disponibiliza três conjuntos temáticos para testar ordenação por diferentes atributos:

| Contexto | Exemplos de Campos |
| :--- | :--- |
| Satélite | Local, hora, latitude e longitude |
| Arcade | Nome do jogador, pontuação, duração e resultado da partida |
| Spotify | Nome da música, artista, visualizações e data de lançamento |   

Os arquivos JSON de exemplo ficam em `pasta_dados_desordenados`, e o repositório inclui conjuntos com diferentes quantidades de registros.

## Tecnologias
- Python 3.10 ou superior — linguagem utilizada no desenvolvimento.
- JSON — armazenamento e leitura dos conjuntos de dados.
- Faker — geração de dados fictícios nos scripts auxiliares.
- Bibliotecas padrão: `random`, `time`, `os`, `json` e `unicodedata`.

## Como executar
### 1. Pré-requisitos
Instale Python 3.10 ou superior.

Para utilizar os scripts de geração de dados, instale também a dependência Faker: `pip install Faker`

**OBS:** O programa principal utiliza apenas bibliotecas padrão do Python.

### 2. Execução da aplicação principal
Na raiz do repositório, execute: `python codigo_aps/main.py`

No menu, escolha uma opção:

1. Bubble Sort
2. Insertion Sort
3. Quick Sort
4. Comparar tempos
5. Selecionar arquivo JSON externo
6. Gerar novos dados aleatórios
7. Sair

Para executar algoritmos sobre vetores internos, gere os dados primeiro pela opção 6. 
Para trabalhar com arquivos externos, selecione a opção 5 e informe um arquivo JSON existente em `pasta_dados_desordenados`.

### 3. Gerar conjuntos de dados

Os scripts auxiliares permitem criar novos arquivos fictícios:

```text
python scripts_de_geracao_de_dados_externos/imagem_satelite.py
python scripts_de_geracao_de_dados_externos/arcade_partidas.py
python scripts_de_geracao_de_dados_externos/spotify_musicas.py
```

Cada script solicita a quantidade de registros e salva o arquivo gerado em `pasta_dados_desordenados`.

### 4. Gerar dados semiordenados

Para criar um conjunto parcialmente ordenado, execute: `python scripts_de_geracao_de_dados_externos/gerar_semi_ordenados.py`

O script solicita contexto, arquivo-base, campo de ordenação, percentual ordenado e direção da ordenação.

## Estrutura do Projeto

```text
aps_quarto_semestre/
├── codigo_aps/
│   ├── funcoes.py
│   ├── main.py
│   └── mapa_campos.py
├── pasta_dados_desordenados/
├── pasta_dados_ordenados/
├── scripts_de_geracao_de_dados_externos/
│   ├── arcade_partidas.py
│   ├── gerar_semi_ordenados.py
│   ├── imagem_satelite.py
│   ├── mapa_campos.py
│   └── spotify_musicas.py
├── APS - 3o e 4o CC - ED.pdf
├── LICENSE
└── README.md
```

## Medição de Desempenho
O tempo é medido imediatamente antes e depois da chamada do algoritmo, usando `time.perf_counter()`. Assim, a medição considera a execução da ordenação, sem incluir leitura ou geração dos dados.

Para arquivos externos, o resultado ordenado é salvo em `pasta_dados_ordenados`. Caso já exista arquivo com mesmo nome, o programa acrescenta um contador para evitar sobrescrever o arquivo anterior.

## Equipe
Projeto desenvolvido por estudantes do Bacharelado em Ciência da Computação da Universidade Paulista (UNIP):

- Pedro Henrique Santos de Almeida
- Fellipe Rodrigues Alves Aerre
- Rafael Piña Kasbergen
- Thales Duarte de Oliveira

## Licença
Este projeto está sob licença MIT.
