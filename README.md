![Python](https://img.shields.io/badge/language-Python-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)


# Thread-Project-C012

Este repositório contém implementações em Python de algoritmos de escalonamento de processos, especificamente **FCFS (First-Come, First-Served)** e **SJF (Shortest Job First)**. Além disso, inclui simulações que utilizam esses algoritmos em cenários modelados.

## Estrutura do Repositório

- **`FCFS.py`**: Implementação do algoritmo FCFS.
- **`SJF.py`**: Implementação do algoritmo SJF.
- **`car.py`**: Define a classe `Car`, utilizada nas simulações.
- **`race_fcfs.py`**: Simulação de corrida utilizando o algoritmo FCFS.
- **`race_sjf.py`**: Simulação de corrida utilizando o algoritmo SJF.
- **`requirements.txt`**: Lista de dependências necessárias para executar os scripts.

## Pré-requisitos

Certifique-se de que o Python 3.6 ou superior está instalado em sua máquina. As dependências podem ser instaladas utilizando o arquivo `requirements.txt`.

### Instalando as Dependências

Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Como Executar

Após instalar as dependências, você pode executar os scripts de simulação com os seguintes comandos:

### Simulação com FCFS

```bash
python race_fcfs.py
```

### Simulação com SJF

```bash
python race_sjf.py
```

## Descrição dos Algoritmos

- FCFS (First-Come, First-Served): Este algoritmo escalona os processos na ordem em que eles chegam.
- SJF (Shortest Job First): Este algoritmo prioriza os processos com menor tempo de execução.
