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

def counting_sort_radix(arr, pos):
    n = len(arr)

    saida = [0] * n
    count = [0] * 10

    for i in range(n):
        digit = (arr[i] // pos) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // pos) % 10
        saida[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = saida[i]

def radix_sort(arr):
    if not arr:
        return arr
    
    max_num = max(arr)

    pos = 1
    while max_num // pos > 0:
        counting_sort_radix(arr, pos)
        pos *= 10

    return arr

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]

    print("Radix Sort com lista aleatória (1000 elementos):")
    for i in range(10):
        medir_tempo(radix_sort, r_arr)
        print("----------")

    print("\nRadix Sort com lista ordenada (1000 elementos):")
    for i in range(10):
        medir_tempo(radix_sort, ord_arr)
        print("----------")
