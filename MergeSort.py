import random

def cria_vetor_randomico(num):
    lista = []
    for i in range(num):
        x = random.randint(1, 25000)
        lista.append(x)
    return lista

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

# Função para verificar se o vetor está ordenado
def esta_ordenado(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))