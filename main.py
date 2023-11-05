import BubbleSort, BubbleSortMelhorado, QuickSort, QuickSortMelhorado, InsertionSort
import ShellSort, SelectionSort, HeapSort, MergeSort
import time
import matplotlib.pyplot as plt
import pandas as pd
import random
import sys

sys.setrecursionlimit(10**5)

def random_vector(num):
    return [random.randint(1, num) for _ in range(num)]

def ordered_vector(num):
    return list(range(1, num + 1))

def inversely_ordered_vector(num):
    return list(range(num, -1, -1))

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

def plot_graph(df, algorithm, type):
    plt.figure(figsize=(12, 8))
    plt.title(type + " - Algoritmo de Ordenação - " + algorithm)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo de Execução (s)")
    plt.grid(True)
    plt.plot(df["Tamanho do Vetor"], df[algorithm], label=algorithm, linewidth=3)
    plt.legend()
    plt.savefig(type + "_" + algorithm + ".png")
    plt.close()




def main():
    sorting_algorithms = {
        "Bubble Sort": BubbleSort.bubble_sort,
        "Bubble Sort Melhorado": BubbleSortMelhorado.bubble_sort,
        "Quick Sort": QuickSort.quick_sort,
        "Quick Sort Melhorado": QuickSortMelhorado.quick_sort,
        "Insertion Sort": InsertionSort.insertion_sort,
        "Shell Sort": ShellSort.shell_sort,
        "Selection Sort": SelectionSort.selection_sort,
        "Heap Sort": HeapSort.heap_sort,
        "Merge Sort": MergeSort.merge_sort,
    }

    vet_length = [1000, 5000, 10000, 15000, 20000, 25000]

    # Vetor aleatório
    results_random = {"Tamanho do Vetor": vet_length}
    for algo_name, algo_func in sorting_algorithms.items():
        algorithm_times = []
        for num in vet_length:
            arr = random_vector(num)
            time_taken = measure_time(algo_func, arr)
            algorithm_times.append(time_taken)
        results_random[algo_name] = algorithm_times
    dfRandom = pd.DataFrame(results_random)

    for algo_name, algo_func in sorting_algorithms.items():
        plot_graph(dfRandom, algo_name, "Vetor Aleatório")


    # Vetor ordenado
    results_ordered = {"Tamanho do Vetor": vet_length}
    for algo_name, algo_func in sorting_algorithms.items():
        algorithm_times = []
        for num in vet_length:
            arr = ordered_vector(num)
            time_taken = measure_time(algo_func, arr)
            algorithm_times.append(time_taken)
        results_ordered[algo_name] = algorithm_times
    dfOrdered = pd.DataFrame(results_ordered)

    for algo_name, algo_func in sorting_algorithms.items():
        plot_graph(dfOrdered, algo_name, "Vetor Ordenado")

    # Vetor inversamente ordenado
    results_inversely_ordered = {"Tamanho do Vetor": vet_length}
    for algo_name, algo_func in sorting_algorithms.items():
        algorithm_times = []
        for num in vet_length:
            arr = inversely_ordered_vector(num)
            time_taken = measure_time(algo_func, arr)
            algorithm_times.append(time_taken)
        results_inversely_ordered[algo_name] = algorithm_times
    dfInverselyOrdered = pd.DataFrame(results_inversely_ordered)
    for algo_name, algo_func in sorting_algorithms.items():
        plot_graph(dfInverselyOrdered, algo_name, "Vetor Inversamente Ordenado")

if __name__ == "__main__":
    main()
