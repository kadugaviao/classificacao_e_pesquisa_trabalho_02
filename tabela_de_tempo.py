import sys
from random import randint
from time import perf_counter

sys.setrecursionlimit(10000)

from bubble_sort import bubble_sort1, bubble_sort2
from insertion_sort import insertion_sort, insertion_sort_binary
from selection_sort import cocktail_selection_sort, selection_sort
from shellsort import shell_sort, shell_sort_otimizado

from mergesort import merge_sort, merge_sort_otimizado
from heapsort import heap_sort, heap_sort_otimizado
from quicksort import quicksort, quicksort_otimizado
from countingsort import counting_sort
from radixsort import radix_sort
from bucketsort import bucket_sort


def random_list(min, max, tamanho):
    return [randint(min, max) for _ in range(tamanho)]


def medir_tempo(func, arr):
    inicio = perf_counter()
    func(arr.copy())
    fim = perf_counter()
    return fim - inicio


def medir_media(func, arr, repeticoes):
    medir_tempo(func, arr)

    total = 0.0
    for _ in range(repeticoes):
        total += medir_tempo(func, arr)
    return total / repeticoes


def formatar_celula(tempo, tempo_base):
    if tempo_base == 0:
        diferenca = 0.0
    else:
        diferenca = ((tempo_base - tempo) / tempo_base) * 100
    return f"{tempo:.8f}s ({diferenca:+.2f}%)"


def imprimir_tabela(resultados, ordem_colunas, algoritmo_base):
    cabecalho = ["Algoritmo"] + [titulo for titulo, _ in ordem_colunas]

    linhas = []
    for nome_algoritmo in resultados:
        linha = [nome_algoritmo]
        for _, chave_cenario in ordem_colunas:
            tempo = resultados[nome_algoritmo][chave_cenario]
            tempo_base = resultados[algoritmo_base][chave_cenario]
            linha.append(formatar_celula(tempo, tempo_base))
        linhas.append(linha)

    larguras = [len(texto) for texto in cabecalho]
    for linha in linhas:
        for i, texto in enumerate(linha):
            larguras[i] = max(larguras[i], len(texto))

    def montar_linha(colunas):
        return " | ".join(colunas[i].ljust(larguras[i]) for i in range(len(colunas)))

    separador = "-+-".join("-" * largura for largura in larguras)

    print(f"Tabela de tempos (valor em segundos e % relativo ao {algoritmo_base}; negativo = pior)")
    print(montar_linha(cabecalho))
    print(separador)
    for linha in linhas:
        print(montar_linha(linha))


def main():
    tamanho = 1000
    repeticoes = 20

    arr_aleatoria = random_list(0, 10000, tamanho)
    arr_ordenada  = list(range(tamanho))
    arr_invertida = list(range(tamanho, 0, -1))

    algoritmos = [
        ("Bubble Sort",           bubble_sort1),
        ("Bubble Sort Otimizado", bubble_sort2),
        ("Selection Sort",        selection_sort),
        ("Selection Cocktail",    cocktail_selection_sort),
        ("Insertion Sort",        insertion_sort),
        ("Insertion Binario",     insertion_sort_binary),
        ("Shell Sort",            shell_sort),
        ("Shell Sort Otimizado",  shell_sort_otimizado),
        ("Merge Sort",            merge_sort),
        ("Merge Sort Otimizado",  merge_sort_otimizado),
        ("Heap Sort",             heap_sort),
        ("Heap Sort Otimizado",   heap_sort_otimizado),
        ("Quick Sort",            quicksort),
        ("Quick Sort Otimizado",  quicksort_otimizado),
        ("Counting Sort",         counting_sort),
        ("Radix Sort",            radix_sort),
        ("Bucket Sort",           bucket_sort),
    ]

    ordem_colunas = [
        ("Aleatoria", "aleatoria"),
        ("Ordenada",  "ordenada"),
        ("Invertida", "invertida"),
    ]

    algoritmo_base = "Bubble Sort"

    cenarios = {
        "aleatoria": arr_aleatoria,
        "ordenada":  arr_ordenada,
        "invertida": arr_invertida,
    }

    resultados = {}
    for nome, func in algoritmos:
        resultados[nome] = {}
        for _, chave in ordem_colunas:
            resultados[nome][chave] = medir_media(func, cenarios[chave], repeticoes)

    imprimir_tabela(resultados, ordem_colunas, algoritmo_base)


if __name__ == "__main__":
    main()
