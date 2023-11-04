import random

def cria_vetor_randomico(num):
    lista = []
    for i in range(num):
        x = random.randint(1, 25000)
        lista.append(x)
    return lista

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Função para verificar se o vetor está ordenado
def esta_ordenado(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
