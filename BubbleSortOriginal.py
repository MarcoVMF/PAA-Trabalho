import random

def cria_vetor_randomico(num):
    lista = []
    for i in range(num):
        x = random.randint(1, 25000)
        lista.append(x)
    return lista

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]