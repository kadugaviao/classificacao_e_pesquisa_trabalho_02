# Tarefa

Expandir a tabela do trabalho anterior com 6 novas implementações: mergesort, heapsort e quicksort em suas versões básicas e otimizadas. Adicionalmente, os métodos lineares trabalhados em aula: CountingSort, RadixSort e BucketSort.

Junto ao tempo, entre parêntese, colocar a diferença de tempo relativa ao Bubble Sort base de cada entrada.

Os algoritmos estão implementados em:

- `mergesort.py` — merge sort básico e otimizado (early-return se já ordenado)
- `heapsort.py` — heap sort básico e otimizado (heapify iterativo)
- `quicksort.py` — quicksort básico (pivô fixo) e otimizado (pivô aleatório)
- `countingsort.py` — counting sort estável
- `radixsort.py` — radix sort base 10
- `bucketsort.py` — bucket sort com insertion sort interno

A tabela completa (todos os 17 algoritmos dos dois trabalhos) pode ser vista ao rodar o arquivo `tabela_de_tempo.py`, que importa todos os módulos e exibe o tempo e a porcentagem de diferença em relação ao Bubble Sort base.
