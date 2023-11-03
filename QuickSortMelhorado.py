import random

def cria_vetor_randomico(num):
    lista = []
    for i in range(num):
        x = random.randint(1, 25000)
        lista.append(x)
    return lista

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Escolha o pivô (neste caso, o primeiro elemento)
    pivot = arr[0]

    # Divide o vetor em duas partições: elementos menores ou iguais ao pivô e elementos maiores que o pivô
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # Recursivamente ordena as partições
    sorted_lesser = quick_sort(lesser)
    sorted_greater = quick_sort(greater)

    # Concatena as partições ordenadas com o pivô no meio
    return sorted_lesser + [pivot] + sorted_greater

# Função para verificar se o vetor está ordenado
def esta_ordenado(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))