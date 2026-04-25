import sys
from random import randint
from time import perf_counter

sys.setrecursionlimit(10000)

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


def imprimir_tabela(titulo, grupos, resultados, ordem_colunas):
    nomes_ordenados = [nome for grupo in grupos for nome in grupo]

    rankings = {}
    for _, chave in ordem_colunas:
        ordenados = sorted(nomes_ordenados, key=lambda n: resultados[n][chave])
        rankings[chave] = {nome: i + 1 for i, nome in enumerate(ordenados)}

    pior_por_cenario = {
        chave: resultados[max(nomes_ordenados, key=lambda n: resultados[n][chave])][chave]
        for _, chave in ordem_colunas
    }

    def formatar_celula(tempo, rank, total, chave):
        ms = tempo * 1000
        pior = pior_por_cenario[chave]
        pct = ((pior - tempo) / pior * 100) if pior else 0.0
        return f"{ms:.3f}ms  (#{rank}/{total}, {pct:+.1f}%)"

    total = len(nomes_ordenados)
    cabecalho = ["Algoritmo"] + [t for t, _ in ordem_colunas]

    linhas_por_nome = {}
    for nome in nomes_ordenados:
        linha = [nome]
        for _, chave in ordem_colunas:
            linha.append(formatar_celula(resultados[nome][chave], rankings[chave][nome], total, chave))
        linhas_por_nome[nome] = linha

    larguras = [len(c) for c in cabecalho]
    for nome in nomes_ordenados:
        for i, texto in enumerate(linhas_por_nome[nome]):
            larguras[i] = max(larguras[i], len(texto))

    def montar_linha(colunas):
        return " | ".join(colunas[i].ljust(larguras[i]) for i in range(len(colunas)))

    separador      = "-+-".join("-" * w for w in larguras)
    sep_grupo      = " +-".join("-" * w for w in larguras)

    print(f"\n{titulo}")
    print("=" * len(titulo))
    print(f"#rank/9: posicao na entrada (1=mais rapido); +%: ganho em relacao ao pior da coluna")
    print()
    print(montar_linha(cabecalho))
    print(separador)
    for g, grupo in enumerate(grupos):
        for nome in grupo:
            print(montar_linha(linhas_por_nome[nome]))
        if g < len(grupos) - 1:
            print(sep_grupo)


def medir_algoritmos(algoritmos, cenarios, ordem_colunas, repeticoes):
    resultados = {}
    for nome, func in algoritmos:
        resultados[nome] = {}
        for _, chave_cenario in ordem_colunas:
            tempo = medir_media(func, cenarios[chave_cenario], repeticoes)
            resultados[nome][chave_cenario] = tempo
    return resultados


def main():
    tamanho = 1000
    repeticoes = 20

    arr_aleatoria = random_list(0, 10000, tamanho)
    arr_ordenada = list(range(tamanho))
    arr_invertida = list(range(tamanho, 0, -1))

    cenarios = {
        "aleatoria": arr_aleatoria,
        "ordenada":  arr_ordenada,
        "invertida": arr_invertida,
    }

    ordem_colunas = [
        ("Aleatoria", "aleatoria"),
        ("Ordenada",  "ordenada"),
        ("Invertida", "invertida"),
    ]

    algs_trab2 = [
        ("Merge Sort",             merge_sort),
        ("Merge Sort Otimizado",   merge_sort_otimizado),
        ("Heap Sort",              heap_sort),
        ("Heap Sort Otimizado",    heap_sort_otimizado),
        ("Quick Sort",             quicksort),
        ("Quick Sort Otimizado",   quicksort_otimizado),
        ("Counting Sort",          counting_sort),
        ("Radix Sort",             radix_sort),
        ("Bucket Sort",            bucket_sort),
    ]

    res2 = medir_algoritmos(algs_trab2, cenarios, ordem_colunas, repeticoes)

    grupos = [
        ["Merge Sort", "Merge Sort Otimizado"],
        ["Heap Sort",  "Heap Sort Otimizado"],
        ["Quick Sort", "Quick Sort Otimizado"],
        ["Counting Sort", "Radix Sort", "Bucket Sort"],
    ]

    imprimir_tabela(
        "=== Trabalho 2: Merge / Heap / Quick / Counting / Radix / Bucket Sort ===",
        grupos, res2, ordem_colunas
    )


if __name__ == "__main__":
    main()

