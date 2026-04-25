from random import randint
from time import perf_counter

def medir_tempo(func, arr):
    inicio = perf_counter()
    
    resultado = func(arr.copy())

    fim = perf_counter()

    print(f"{func.__name__}: {fim - inicio:.8f} segundos")

    return resultado

def random_list(min, max, tam=10):
    return [randint(min, max) for _ in range(tam)]

def max_heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda
    
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        max_heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        max_heapify(arr, j, 0)
    
    return arr

def max_heapify_iterativo(arr, n, i):
    while True:
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n and arr[esquerda] > arr[maior]:
            maior = esquerda

        if direita < n and arr[direita] > arr[maior]:
            maior = direita

        if maior == i:
            break

        arr[i], arr[maior] = arr[maior], arr[i]
        i = maior

def heap_sort_otimizado(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify_iterativo(arr, n, i)

    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        max_heapify_iterativo(arr, j, 0)

    return arr

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]

    print("Heapsort com lista aleatória (1000 elementos):")
    for i in range(10):
        medir_tempo(heap_sort, r_arr)
        print("----------")

    print("\nHeapsort com lista ordenada (1000 elementos):")
    for i in range(10):
        medir_tempo(heap_sort, ord_arr)
        print("----------")
