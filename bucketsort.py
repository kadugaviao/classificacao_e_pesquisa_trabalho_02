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

def insertion_sort_bucket(bucket):
    for i in range(1, len(bucket)):
        value = bucket[i]
        j = i - 1
        
        while j >= 0 and bucket[j] > value:
            bucket[j + 1] = bucket[j]
            j -= 1
        
        bucket[j + 1] = value

def bucket_sort(arr):
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr
    
    n = len(arr)
    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n + 1)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index > n:
            index = n
        buckets[index].append(num)

    for i in range(len(buckets)):
        insertion_sort_bucket(buckets[i])

    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

    return arr

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]

    print("Bucket Sort com lista aleatória (1000 elementos):")
    for i in range(10):
        medir_tempo(bucket_sort, r_arr)
        print("----------")

    print("\nBucket Sort com lista ordenada (1000 elementos):")
    for i in range(10):
        medir_tempo(bucket_sort, ord_arr)
        print("----------")
