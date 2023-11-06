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
    return list (range(1, num + 1))

def inversely_ordered_vector(num):
    return list(range(num, -1, -1))

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

def plot_graph(df, title, filename):
    plt.figure(figsize=(12, 8))
    plt.title(title)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo de Execução (s)")
    plt.grid(True)
    for algo_name in df.columns[1:]:
        plt.plot(df["Tamanho do Vetor"], df[algo_name], label=algo_name, linewidth=3)
    plt.legend()
    plt.savefig(filename)
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

    for algo_name, algo_func in sorting_algorithms.items():
        results = {"Tamanho do Vetor": vet_length}
        for type_name, generator_func in [("Vetor Aleatório", random_vector),
                                          ("Vetor Ordenado", ordered_vector),
                                          ("Vetor Inversamente Ordenado", inversely_ordered_vector)]:
            algorithm_times = []
            for num in vet_length:
                arr = generator_func(num)
                time_taken = measure_time(algo_func, arr)
                algorithm_times.append(time_taken)
            results[type_name] = algorithm_times
        df = pd.DataFrame(results)
        df.to_excel(f"{algo_name}.xlsx")
        plot_graph(df, f"Algoritmo de Ordenação - {algo_name}", f"{algo_name}.png")

if __name__ == "__main__":
    main()
