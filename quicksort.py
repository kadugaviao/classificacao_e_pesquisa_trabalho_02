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

def quicksort(arr):
    if len(arr) <= 1:
        return arr
        
    pivo = arr[0]
    menores = [x for x in arr[1:] if x <= pivo]
    maiores = [x for x in arr[1:] if x > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)

def quicksort_otimizado(arr):
    if len(arr) <= 1:
        return arr
        
    index = randint(0, len(arr) - 1)
    pivo = arr.pop(index)
    menores = [x for x in arr if x <= pivo]
    maiores = [x for x in arr if x > pivo]

    return quicksort_otimizado(menores) + [pivo] + quicksort_otimizado(maiores)

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr_pequeno = [i for i in range(0, 100)] 
    ord_arr = [i for i in range(0, 1000)]

    print("Quicksort com lista aleatória (1000 elementos):")
    for i in range(10):
        medir_tempo(quicksort, r_arr)
        medir_tempo(quicksort_otimizado, r_arr)
        print("----------")

    print("\nQuicksort normal com lista ordenada (100 elementos - pior caso):")
    for i in range(10):
        medir_tempo(quicksort, ord_arr_pequeno)
        print("----------")
    
    print("\nQuicksort otimizado com lista ordenada (1000 elementos):")
    for i in range(10):
        medir_tempo(quicksort_otimizado, ord_arr)
        print("----------")
