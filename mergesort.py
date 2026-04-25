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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    esquerda = merge_sort(arr[:mid])
    direita = merge_sort(arr[mid:])

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def merge_sort_otimizado(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    esquerda = merge_sort_otimizado(arr[:mid])
    direita = merge_sort_otimizado(arr[mid:])

    if esquerda[-1] <= direita[0]:
        return esquerda + direita
    
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]

    print("Mergesort com lista aleatória (1000 elementos):")
    for i in range(10):
        medir_tempo(merge_sort, r_arr)
        medir_tempo(merge_sort_otimizado, r_arr)
        print("----------")

    print("\nMergesort com lista ordenada (1000 elementos - otimização tem vantagem):")
    for i in range(10):
        medir_tempo(merge_sort, ord_arr)
        medir_tempo(merge_sort_otimizado, ord_arr)
        print("----------")