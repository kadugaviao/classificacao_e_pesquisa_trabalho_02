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

def counting_sort(arr):
    if not arr:
        return arr
    

    max_value = max(arr)
    n = len(arr)

    count = [0] * (max_value + 1)
    saida = [0] * n

    for num in arr:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        valor_atual = arr[i]
        posicao = count[valor_atual] - 1
        saida[posicao] = valor_atual

        count[valor_atual] -= 1

    return saida

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]

    print("Counting Sort com lista aleatória (1000 elementos):")
    for i in range(10):
        medir_tempo(counting_sort, r_arr)
        print("----------")

    print("\nCounting Sort com lista ordenada (1000 elementos):")
    for i in range(10):
        medir_tempo(counting_sort, ord_arr)
        print("----------")

