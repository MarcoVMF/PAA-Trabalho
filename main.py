import BubbleSort, BubbleSortMelhorado, QuickSort, QuickSortMelhorado, InsertionSort
import ShellSort, SelectionSort, HeapSort, MergeSort
from datetime import datetime
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
    start = datetime.now()
    sort_func(arr)
    end = datetime.now()
    return (end - start).total_seconds()

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
    results = {"Tamanho do Vetor": vet_length}

    for algo_name, algo_func in sorting_algorithms.items():
        algorithm_times = []
        for num in vet_length:
            arr = random_vector(num)
            time_taken = measure_time(algo_func, arr)
            algorithm_times.append(time_taken)
        results[algo_name] = algorithm_times
    dfRandom = pd.DataFrame(results)
    dfRandom.to_csv("random.csv", index=False)


    for algo_name, algo_func in sorting_algorithms.items():
        algorithm_times = []
        for num in vet_length:
            arr = ordered_vector(num)
            time_taken = measure_time(algo_func, arr)
            algorithm_times.append(time_taken)
        results[algo_name] = algorithm_times
    dfOrdered = pd.DataFrame(results)
    dfOrdered.to_csv("ordered.csv", index=False)


    for algo_name, algo_func in sorting_algorithms.items():
        algorithm_times = []
        for num in vet_length:
            arr = inversely_ordered_vector(num)
            time_taken = measure_time(algo_func, arr)
            algorithm_times.append(time_taken)
        results[algo_name] = algorithm_times
    dfInverselyOrdered = pd.DataFrame(results)
    dfInverselyOrdered.to_csv("inversely_ordered.csv", index=False)


if __name__ == "__main__":
    main()
