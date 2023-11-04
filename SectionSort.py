import random

def cria_vetor_randomico(num):
    lista = []
    for i in range(num):
        x = random.randint(1, 25000)
        lista.append(x)
    return lista

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Função para verificar se o vetor está ordenado
def esta_ordenado(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))